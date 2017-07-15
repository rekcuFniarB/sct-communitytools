from django.apps import AppConfig
from sphene.community import sphsettings
from django.conf import settings
import re

class SphBoardConfig(AppConfig):
    name = 'sphene.sphboard'
    label = 'sphboard'
    _SPHCONF = {}
    def ready(self):
        from sphene.contrib.libs.common.text.bbcode import HtmlEquivTag, SoftBrTag, Emoticon, ImgTag, ColorTag, MemberTag, EmailTag, UrlTag, QuoteTag

        ## All below code moved here from sphene.contrib.libs.common.text.bbcode due to "app not ready" error.
        
        self._SPHCONF['defaults'] = {
            'board_count_views': True,
            'board_heat_days': 30,
            'board_heat_post_threshold': 10,
            'board_heat_view_threshold': 100,
            'board_heat_calculator': 'sphene.sphboard.models.calculate_heat',
        
            # Defines if the 'Notify Me' checkbox should be selected by default.
            'board_default_notifyme': True,
    
            # How long a user is allowed to edit his post in seconds.
            # -1: forever,
            # 0: never
            'board_edit_timeout': -1, #30 * 60,
    
            # How long a user is allowed to hide his post in seconds.
            # -1: forever,
            # 0: never
            'board_hide_timeout': -1, #30 * 60,
    
            # Timeout for the rendered body in the cache
            # Default 6 hours
            'board_body_cache_timeout': 6 * 3600,
            'board_signature_cache_timeout': 6 * 3600,
            'board_authorinfo_cache_timeout': 6 * 3600,
    
            # See http://code.djangoproject.com/ticket/4789
            # When activating this setting, select_related() will not be used.
            'workaround_select_related_bug': False,
    
    
            'board_post_paging': 10,
    
            # Allow users to attach files to their posts ?
            'board_allow_attachments': True,
    
            # Pass the board and blog posts through the wiki camel case
            # markup. This will allow wiki links to be automatically placed
            # into the posts. It is better to turn this off and use the
            # sph extended BBCODE wiki label.
            'board_auto_wiki_link_enabled': True,
            # default location of emoticons
            'board_emoticons_root': settings.STATIC_URL + 'sphene/emoticons/',
            'board_emoticons_list': {
                '0:-)': 'angel.gif',
                'O:-)':'angel.gif',
                ':angel:':'angel.gif',
                ':)':'smile.gif',
                ':(':'sad.gif',
                ':D':'grin.gif',
                ':p':'tongue.gif',
                ';)':'wink.gif',
                ':-)':'smile.gif',
                ':-(': 'sad.gif',
                ':-D': 'grin.gif',
                ':-P': 'tongue.gif',
                ':-p': 'tongue.gif',
                ':-/': 'unsure.gif',
                ':-\\': 'unsure.gif',
                ';-)': 'wink.gif',
                ':-$': 'confused.gif',
                ':-S': 'confused.gif',
                'B-)': 'cool.gif',
                ':lol:': 'lol.gif',
                ':batman:': 'batman.gif',
                ':rolleyes:': 'rolleyes.gif',
                ':icymad:': 'bluemad.gif',
                ':mad:': 'mad.gif',
                ':crying:': 'crying.gif',
                ':eek:': 'eek.gif',
                ':eyebrow:': 'eyebrow.gif',
                ':grim:': 'grim_reaper.gif',
                ':idea:': 'idea.gif',
                ':rotfl:': 'rotfl.gif',
                ':shifty:': 'shifty.gif',
                ':sleep:': 'sleep.gif',
                ':thinking:': 'thinking.gif',
                ':wave:': 'wave.gif',
                ':bow:': 'bow.gif',
                ':sheep:':  'sheep.gif',
                ':santa:':  'santaclaus.gif',
                ':anvil:': 'anvil.gif',
                ':bandit:': 'bandit.gif',
                ':chop:': 'behead.gif',
                ':biggun:': 'biggun.gif',
                ':mouthful:': 'blowingup,gif',
                ':gun:': 'bluekillsred.gif',
                ':box:': 'boxing.gif',
                ':gallows:': 'hanged.gif',
                ':jedi:': 'lightsaber1.gif',
                ':bosh:': 'mallet1.gif',
                ':saw:': 'saw.gif',
                ':stupid:': 'youarestupid.gif',
            },

            # default tag used when rendering user signatures in posts
            'board_signature_tag':'<div class="signature">%(signature)s</div>',
        
            # default link in board posts
            'board_post_link':'<a href="%(url)s">%(text)s</a>',
    
            'board_attachments_upload_to': 'var/sphene/sphwiki/attachment/%Y/%m/%d',
    
            'board_slugify_links': True,
    
            # Display the reply form directly below a thread instead of just a 'Post Reply' link.
            'board_quick_reply': False,
        
            # Activates the experimental WYSIWYG editor -
            #   only if 'bbcode' is the only markup choice.
            # If you are using it, please provide feedback in the
            # forums at http://sct.spene.net !
            'board_wysiwyg': False,
            # This options let users test the wysiwyg editor by appending
            # ?wysiwyg=1 to the post URL. (I just added it so it can be seen on
            # sct.sphene.net and tested by users.)
            'board_wysiwyg_testing': False,
        }
        sphsettings.add_setting_defaults(self._SPHCONF['defaults'])
    
        styleincludes = sphsettings.get_sph_setting( 'community_styleincludes', [])
        styleincludes.append(settings.STATIC_URL + 'sphene/sphboard/styles/base.css')
        sphsettings.set_sph_setting( 'community_styleincludes', styleincludes )
        
        self._SPHCONF['BBTAGS'] = {}
        
        self._SPHCONF['BBTAGS']['_COLORS'] = ('aqua', 'black', 'blue', 'fuchsia', 'gray', 'green', 'lime', 'maroon', 
            'navy', 'olive', 'purple', 'red', 'silver', 'teal', 'white', 'yellow')
        self._SPHCONF['BBTAGS']['_COLOR_REGEXP'] = re.compile(r'#[0-9A-F]{6}')
        self._SPHCONF['BBTAGS']['_MEMBER_REGEXP'] = re.compile(r'^[\'"]?(?P<username>[0-9A-Za-z_]{1,30})[\'"]?(?:;(?P<post_id>[0-9]+))?$')
        self._SPHCONF['BBTAGS']['_BBTAG_REGEXP'] = re.compile(r'\[\[?\/?([A-Za-z\*]+)(:[a-f0-9]+)?(=[^\]]+)?\]?\]')

        # 'text' is a dummy entry for text nodes
        self._SPHCONF['BBTAGS']['_INLINE_TAGS'] = (
            'b', 'i', 'color', 'member', 'email', 'url', 
            'br', 'text', 'img', 'softbr', 'emoticon', 'u'
        )
        self._SPHCONF['BBTAGS']['_BLOCK_LEVEL_TAGS'] = ('p', 'quote', 'list', 'pre', 'code', 'div')
        self._SPHCONF['BBTAGS']['_FLOW_TAGS'] = self._SPHCONF['BBTAGS']['_INLINE_TAGS'] + self._SPHCONF['BBTAGS']['_BLOCK_LEVEL_TAGS']
        self._SPHCONF['BBTAGS']['_OTHER_TAGS'] = ('*',)

        self._SPHCONF['BBTAGS']['_ANCHOR_TAGS'] = ('member', 'email', 'url')

        # Rules, defined so that the output after translation will be 
        # XHTML compatible. Other rules are implicit in the parsing routines.
        # Note that some bbtags can adapt to their context in the rendering
        # phase in order to generate correct XHTML, so have slacker rules than normal
        # Also, some tags only exist to make parsing easier, and are
        # not intended for use by end user.
        self._SPHCONF['BBTAGS']['_TAGS'] = (
            #           name          allowed_children   implicit_tag
            # <br/>
            HtmlEquivTag('br',         (),             'div', 
                self_closing=True, discardable=True, html_equiv='br'),
            
            # <br/>, but can adapt during render
            SoftBrTag   ('softbr',     (),             'div', 
                self_closing=True, discardable=True),
            
            # <img/>,  but can adapt
            Emoticon    ('emoticon',   ('text',),      'div'),
            
            # <b>
            HtmlEquivTag('b',          self._SPHCONF['BBTAGS']['_INLINE_TAGS'],   'div',
                html_equiv='b'),
            
            # <u>
            HtmlEquivTag('u',          self._SPHCONF['BBTAGS']['_INLINE_TAGS'],   'div',
                html_equiv='u'),
            
            # <img/>
            ImgTag('img',          self._SPHCONF['BBTAGS']['_INLINE_TAGS'],   'div'),
            
            # <i>
            HtmlEquivTag('i',          self._SPHCONF['BBTAGS']['_INLINE_TAGS'],   'div',
                html_equiv='i'),
            
            # <span>
            ColorTag    ('color',      self._SPHCONF['BBTAGS']['_INLINE_TAGS'],   'div'),
            
            # <a>
            MemberTag   ('member',     ('text',),      'div' ),
            
            # <a>
            EmailTag    ('email',      ('text',),      'div'),
            
            # <a>
            UrlTag      ('url',        self._SPHCONF['BBTAGS']['_INLINE_TAGS'],      'div'),
            
            # <p>
            HtmlEquivTag('p',          self._SPHCONF['BBTAGS']['_INLINE_TAGS'],   None,
                html_equiv='p'),
            
            # <div>
            HtmlEquivTag('div',        self._SPHCONF['BBTAGS']['_INLINE_TAGS'],     None,
                html_equiv='div'),
            
            # <blockquote>
            QuoteTag    ('quote',      self._SPHCONF['BBTAGS']['_BLOCK_LEVEL_TAGS'] + ('softbr',), 'div'),
            
            # <ul>
            HtmlEquivTag('list',       ('*', 'softbr'), None,
                html_equiv='ul'),
            
            # <pre> (only img currently needed out of the prohibited elements)
            HtmlEquivTag('pre',        self._SPHCONF['BBTAGS']['_INLINE_TAGS'],   None, 
                prohibited_elements=('img', 'big', 'small', 'sub', 'sup', 'br'),
                html_equiv='pre'), 
            
            # <pre class="code">
            HtmlEquivTag('code',       self._SPHCONF['BBTAGS']['_INLINE_TAGS'], None, 
                prohibited_elements = ('img', 'big', 'small', 'sub', 'sup', 'br'),
                html_equiv='pre', attributes={'class':'code'}),
                
            # <li>
            HtmlEquivTag('*', self._SPHCONF['BBTAGS']['_FLOW_TAGS'], 'list',
                html_equiv='li')
        )
        

        # Make a dictionary
        self._SPHCONF['BBTAGS']['_TAGDICT'] = {}
        for t in self._SPHCONF['BBTAGS']['_TAGS']:
            if t.name != 'text':
                self._SPHCONF['BBTAGS']['_TAGDICT'][t.name] = t

        ## Make list of valid tags
        self._SPHCONF['BBTAGS']['_TAGNAMES'] = [t.name for t in self._SPHCONF['BBTAGS']['_TAGS']]
