from django.conf import settings
import os

def init_data(sender, verbosity, **kwargs):
    from sphene.community.models import Group, Navigation, CommunityUserProfileField
    from sphene.sphboard.models import Category, ThreadInformation
    os.environ['sph_init_data'] = 'true'
    sphsettings = {}
    if hasattr(settings, 'SPH_SETTINGS'):
        sphsettings = settings.SPH_SETTINGS
    sphsettings_group = sphsettings.get('group', {})
    group_name = sphsettings_group.get('name', 'main')
    group_longname = sphsettings_group.get('longname')
    group_baseurl = sphsettings_group.get('baseurl', 'www.example.com')
    
    sender_models = sender.get_models()
    
    if Category in sender_models:
        group, created = Group.objects.get_or_create( name = group_name,
                                                      longname = group_longname,
                                                      baseurl = group_baseurl )

        category, created = Category.objects.get_or_create( name = 'Example Category',
                                                   group = group,
                                                   description = 'This is just an example Category. You can modify categories in the django admin interface.',
                             )

    if ThreadInformation in sender_models:
        # Synchronize ThreadInformation with all posts ..
        # (Required for backward compatibility)
        synchronize_threadinformation(verbosity)


def synchronize_threadinformation(verbosity = -1):
    """ Will synchronize the 'ThreadInformation' objects. """
    from sphene.sphboard.models import Category, ThreadInformation, Post, THREAD_TYPE_DEFAULT

    # First find all threads ...
    if verbosity >= 2:
        print "Synchronizing ThreadInformation ..."
    all_threads = Post.objects.filter( thread__isnull = True )

    for thread in all_threads:
        # Find corresponding ThreadInformation
        try:
            thread_info = ThreadInformation.objects.type_default().filter( root_post = thread ).get()
        except ThreadInformation.DoesNotExist:
            thread_info = ThreadInformation( root_post = thread,
                                             category = thread.category,
                                             thread_type = THREAD_TYPE_DEFAULT )

        thread_info.update_cache()
        thread_info.save()



from django.db.models.signals import post_migrate
post_migrate.connect(init_data)
