#
# This code was copied from
#  http://axiak.net/blog/2007/5/22/cached-inclusion-tag/
# Originally written by Michael C Axiak (obvioulsy)
#
# (As of time of this writing .. the site was not available.. i have to access
#  it through google cache :) )
#
#
from functools import partial

from django.core.cache import cache
from django import template
from django.template.base import Template
from django.template.library import TagHelperNode
from django.utils.functional import curry
from inspect import getargspec
from django.utils.itercompat import is_iterable
import re

__all__ = ['cache_inclusion_tag']


class TemplateSyntaxError(Exception):
    pass

# Regex for token keyword arguments
kwarg_re = re.compile(r"(?:(\w+)=)?(.+)")

def token_kwargs(bits, parser, support_legacy=False):
    """
    A utility method for parsing token keyword arguments.

    :param bits: A list containing remainder of the token (split by spaces)
        that is to be checked for arguments. Valid arguments will be removed
        from this list.

    :param support_legacy: If set to true ``True``, the legacy format
        ``1 as foo`` will be accepted. Otherwise, only the standard ``foo=1``
        format is allowed.

    :returns: A dictionary of the arguments retrieved from the ``bits`` token
        list.

    There is no requirement for all remaining token ``bits`` to be keyword
    arguments, so the dictionary will be returned as soon as an invalid
    argument format is reached.
    
    Copied from https://django.readthedocs.io/en/1.8.x/_modules/django/template/base.html
    """
    if not bits:
        return {}
    match = kwarg_re.match(bits[0])
    kwarg_format = match and match.group(1)
    if not kwarg_format:
        if not support_legacy:
            return {}
        if len(bits) < 3 or bits[1] != 'as':
            return {}

    kwargs = {}
    while bits:
        if kwarg_format:
            match = kwarg_re.match(bits[0])
            if not match or not match.group(1):
                return kwargs
            key, value = match.groups()
            del bits[:1]
        else:
            if len(bits) < 3 or bits[1] != 'as':
                return kwargs
            key, value = bits[2], bits[0]
            del bits[:3]
        kwargs[key] = parser.compile_filter(value)
        if bits and not kwarg_format:
            if bits[0] != 'and':
                return kwargs
            del bits[:1]
    return kwargs

def parse_bits(parser, bits, params, varargs, varkw, defaults,
               takes_context, name):
    """
    Parses bits for template tag helpers (simple_tag, include_tag and
    assignment_tag), in particular by detecting syntax errors and by
    extracting positional and keyword arguments.
    Copied from https://django.readthedocs.io/en/1.8.x/_modules/django/template/base.html
    """
    if takes_context:
        if params[0] == 'context':
            params = params[1:]
        else:
            raise TemplateSyntaxError(
                "'%s' is decorated with takes_context=True so it must "
                "have a first argument of 'context'" % name)
    args = []
    kwargs = {}
    unhandled_params = list(params)
    for bit in bits:
        # First we try to extract a potential kwarg from the bit
        kwarg = token_kwargs([bit], parser)
        if kwarg:
            # The kwarg was successfully extracted
            param, value = list(six.iteritems(kwarg))[0]
            if param not in params and varkw is None:
                # An unexpected keyword argument was supplied
                raise TemplateSyntaxError(
                    "'%s' received unexpected keyword argument '%s'" %
                    (name, param))
            elif param in kwargs:
                # The keyword argument has already been supplied once
                raise TemplateSyntaxError(
                    "'%s' received multiple values for keyword argument '%s'" %
                    (name, param))
            else:
                # All good, record the keyword argument
                kwargs[str(param)] = value
                if param in unhandled_params:
                    # If using the keyword syntax for a positional arg, then
                    # consume it.
                    unhandled_params.remove(param)
        else:
            if kwargs:
                raise TemplateSyntaxError(
                    "'%s' received some positional argument(s) after some "
                    "keyword argument(s)" % name)
            else:
                # Record the positional argument
                args.append(parser.compile_filter(bit))
                try:
                    # Consume from the list of expected positional arguments
                    unhandled_params.pop(0)
                except IndexError:
                    if varargs is None:
                        raise TemplateSyntaxError(
                            "'%s' received too many positional arguments" %
                            name)
    if defaults is not None:
        # Consider the last n params handled, where n is the
        # number of defaults.
        unhandled_params = unhandled_params[:-len(defaults)]
    if unhandled_params:
        # Some positional arguments were not supplied
        raise TemplateSyntaxError(
            "'%s' did not receive value(s) for the argument(s): %s" %
            (name, ", ".join("'%s'" % p for p in unhandled_params)))
    return args, kwargs

def generic_tag_compiler(parser, token, params, varargs, varkw, defaults,
                         name, takes_context, node_class):
    """
    Returns a template.Node subclass.
    Copied from https://django.readthedocs.io/en/1.8.x/_modules/django/template/base.html
    """
    bits = token.split_contents()[1:]
    args, kwargs = parse_bits(parser, bits, params, varargs, varkw,
                              defaults, takes_context, name)
    return node_class(takes_context, args, kwargs)

def cache_inclusion_tag(self, file_name, cache_key_func=None, cache_time=99999, context_class=template.Context,  takes_context=False, name=None):
    """
    This function will cache the rendering and output of a inclusion tag for cache_time seconds.

    To use, just do the following::

    from django import template
    from esp.web.util.template import cache_inclusion_tag
    
    register = template.Library()

    def cache_key_func(foo, bar, baz):
        # takes the same arguments as below
        return str(foo)

    @cache_inclusion_tag(register, 'path/to/template.html', cache_key_func=cache_key_func)
    def fun_tag(foo, bar, baz):
        return {'foo': foo}


    The tag will now be cached.
    """
    def dec(func):
        params, varargs, varkw, defaults = getargspec(func)

        class InclusionNode(TagHelperNode):
            def render(self, context):
                resolved_args, resolved_kwargs = self.get_resolved_arguments(context)

                if takes_context:
                    args = [context] + resolved_args
                else:
                    args = resolved_args

                if cache_key_func:
                    cache_key = cache_key_func(*args)
                else:
                    cache_key = None

                if cache_key != None:
                    retVal = cache.get(cache_key)
                    if retVal:
                        return retVal

                _dict = func(*resolved_args, **resolved_kwargs)

                if not getattr(self, 'nodelist', False):
                    from django.template.loader import get_template, select_template
                    if isinstance(file_name, Template):
                        t = file_name
                    elif not isinstance(file_name, basestring) and is_iterable(file_name):
                        t = select_template(file_name)
                    else:
                        t = get_template(file_name)
                    self.nodelist = t.nodelist
                new_context = context_class(_dict, **{
                    'autoescape': context.autoescape,
                    'current_app': context.current_app,
                    'use_l10n': context.use_l10n,
                    'use_tz': context.use_tz,
                })
                # Copy across the CSRF token, if present, because
                # inclusion tags are often used for forms, and we need
                # instructions for using CSRF protection to be as simple
                # as possible.
                csrf_token = context.get('csrf_token', None)
                if csrf_token is not None:
                    new_context['csrf_token'] = csrf_token

                retVal = self.nodelist.render(new_context)
                if cache_key != None:
                    cache.set(cache_key, retVal, cache_time)
                return retVal

        function_name = (name or
            getattr(func, '_decorated_function', func).__name__)
        compile_func = partial(generic_tag_compiler,
            params=params, varargs=varargs, varkw=varkw,
            defaults=defaults, name=function_name,
            takes_context=takes_context, node_class=InclusionNode)
        compile_func.__doc__ = func.__doc__
        self.tag(function_name, compile_func)
        return func

    return dec
