from django.conf import settings
from sphene.community.models import Group, Navigation, CommunityUserProfileField, PermissionFlag, Role
    
def init_data(sender, verbosity, **kwargs):
    sender_models = sender.get_models()
    
    sphsettings = {}
    if hasattr(settings, 'SPH_SETTINGS'):
        sphsettings = settings.SPH_SETTINGS
    sphsettings_group = sphsettings.get('group', {})
    group_name = sphsettings_group.get('name', 'main')
    group_longname = sphsettings_group.get('longname')
    group_baseurl = sphsettings_group.get('baseurl', 'www.example.com')
    
    if Group in sender_models:
        group, created = Group.objects.get_or_create( name = group_name,
                                                      longname = group_longname,
                                                      baseurl = group_baseurl )
    
    if Navigation in sender_models:
        nav = Navigation.objects.get_or_create( group = group,
                          label = 'Home',
                          href = '/wiki/show/Start/',
                          urltype = 0,
                          sortorder = 10,
                          navigationType = 0,
                        )

        nav = Navigation.objects.get_or_create( group = group,
                          label = 'Board',
                          href = '/board/show/0/',
                          urltype = 0,
                          sortorder = 20,
                          navigationType = 0,
                        )

    if CommunityUserProfileField in sender_models:
        CommunityUserProfileField.objects.get_or_create( name = 'ICQ UIN',
                                                         regex = '\d+',
                                                         sortorder = 100, )
        CommunityUserProfileField.objects.get_or_create( name = 'Jabber Id',
                                                         regex = '.+@.+',
                                                         sortorder = 200, )
        CommunityUserProfileField.objects.get_or_create( name = 'Website URL',
                                                         regex = 'http://.*',
                                                         sortorder = 300,
                                                        renderstring = '<a href="%(value)s">%(value)s</a>', )


def create_permission_flags(sender, verbosity, **kwargs):
    """
    Creates permission flags by looking at the Meta class of all models.

    These Meta classes can have a 'sph_permission_flags' attribute containing
    a dictionary with 'flagname': 'some verbose userfriendly description.'

    Permission flags are not necessarily bound to a given model. It just needs
    to be assigned to one so it can be found, but it can be used in any
    context.
    """
    sender_models = sender.get_models()
    
    #for myapp in DjangoApps.get_app_configs():
        #app_models = DjangoApps.get_app_config(myapp).models
        #if not app_models:
            #continue

        #for klass in app_models:
            #if hasattr(klass, 'sph_permission_flags'):
                #sph_permission_flags = klass.sph_permission_flags

                ## permission flags can either be a dictionary with keys beeing
                ## flag names, values beeing the description
                ## or lists in the form: ( ( 'flagname', 'description' ), ... )
                #if isinstance(sph_permission_flags, dict):
                    #sph_permission_flags = sph_permission_flags.iteritems()

                #for (flag, description) in sph_permission_flags:
                    #flag, created = PermissionFlag.objects.get_or_create(name = flag)
                    #if created and verbosity >= 2:
                        #print "Added sph permission flag '%s'" % flag.name


    for klass in sender_models:
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

    if Role in sender_models:
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


from django.db.models.signals import post_migrate
post_migrate.connect(init_data)
post_migrate.connect(create_permission_flags)
