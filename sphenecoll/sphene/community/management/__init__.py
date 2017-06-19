from django.db.models import signals
from django.apps import apps as DjangoApps
from sphene.community import models
from django.conf import settings

def init_data(app, created_models, verbosity, **kwargs):
    from sphene.community.models import Group, Navigation, CommunityUserProfileField
    if Group in created_models:
        group, created = Group.objects.get_or_create( name = 'example',
                                                      longname = 'Example Group',
                                                      baseurl = 'www.example.com', )
        group.save()

        if Navigation in created_models:
            nav = Navigation( group = group,
                              label = 'Home',
                              href = '/wiki/show/Start/',
                              urltype = 0,
                              sortorder = 10,
                              navigationType = 0,
                              )
            nav.save()

            nav = Navigation( group = group,
                              label = 'Board',
                              href = '/board/show/0/',
                              urltype = 0,
                              sortorder = 20,
                              navigationType = 0,
                              )
            nav.save()

    if CommunityUserProfileField in created_models:
        CommunityUserProfileField( name = 'ICQ UIN',
                                   regex = '\d+',
                                   sortorder = 100, ).save()
        CommunityUserProfileField( name = 'Jabber Id',
                                   regex = '.+@.+',
                                   sortorder = 200, ).save()
        CommunityUserProfileField( name = 'Website URL',
                                   regex = 'http://.*',
                                   sortorder = 300,
                                   renderstring = '<a href="%(value)s">%(value)s</a>', ).save()


#from django.db import backend, connection, transaction
from sphene.community.models import PermissionFlag, Role, Group
from sphene.community.models import ApplicationChangelog

def create_permission_flags(app, created_models, verbosity, **kwargs):
    """
    Creates permission flags by looking at the Meta class of all models.

    These Meta classes can have a 'sph_permission_flags' attribute containing
    a dictionary with 'flagname': 'some verbose userfriendly description.'

    Permission flags are not necessarily bound to a given model. It just needs
    to be assigned to one so it can be found, but it can be used in any
    context.
    """

    for myapp in DjangoApps.get_app_configs():
        app_models = DjangoApps.get_app_config(myapp).models
        if not app_models:
            continue

        for klass in app_models:
            if hasattr(klass, 'sph_permission_flags'):
                sph_permission_flags = klass.sph_permission_flags

                # permission flags can either be a dictionary with keys beeing
                # flag names, values beeing the description
                # or lists in the form: ( ( 'flagname', 'description' ), ... )
                if isinstance(sph_permission_flags, dict):
                    sph_permission_flags = sph_permission_flags.iteritems()

                for (flag, description) in sph_permission_flags:
                    flag, created = PermissionFlag.objects.get_or_create(name = flag)
                    if created and verbosity >= 2:
                        print "Added sph permission flag '%s'" % flag.name

    if Role in created_models:
        # Create a 'Group Admin' role for all groups.
        rolename = 'Group Admin'
        permissionflag = PermissionFlag.objects.get(name = 'group_administrator')
        groups = Group.objects.all()
        for group in groups:
            role, created = Role.objects.get_or_create( name = rolename, group = group )
            if not created:
                continue

            role.save()
            role.permission_flags.add(permissionflag)
            role.save()

            if verbosity >= 2:
                print "Created new role '%s' for group '%s' and assigned permission '%s'" % (rolename, group.name, permissionflag.name)

# handle both post_syncdb and post_migrate (if south is used)
def syncdb_compat(app_label, handler=None, *args, **kwargs):
    if app_label=='community':
        app = DjangoApps.get_app_config(app_label)
        models = app.models
        handler(app=app, created_models=models, verbosity=1, **kwargs)

def syncdb_compat_init_data(app, *args, **kwargs):
    syncdb_compat(app, handler=init_data, *args, **kwargs)

def syncdb_compat_create_permission_flags(app, *args, **kwargs):
    syncdb_compat(app, handler=create_permission_flags, *args, **kwargs)

if 'south' in settings.INSTALLED_APPS:
    from south.signals import post_migrate
    post_migrate.connect(syncdb_compat_init_data, dispatch_uid="communitytools.sphenecoll.sphene.community.management")
    post_migrate.connect(syncdb_compat_create_permission_flags)
else:
    from django.db.models.signals import post_migrate
    post_migrate.connect(syncdb_compat_init_data, sender=models, dispatch_uid="communitytools.sphenecoll.sphene.community.management")
    post_migrate.connect(syncdb_compat_create_permission_flags, sender=models)
