from django.conf.urls import url

from sphene.sphblog.feeds import LatestBlogPosts

from sphene.sphblog import views as sphblog_views

from django.conf import settings

defaultdict = { 'group': settings.SPH_SETTINGS['group']['name'],
                'groupName': settings.SPH_SETTINGS['group']['name']}

#feeds = {
#    'latestposts': LatestBlogPosts,
#}

urlpatterns = [
        url(r'^feeds/latestposts/$', LatestBlogPosts(),
                            #{ 
                              #'noGroup': True,
                              #},
                              defaultdict,
                            name = 'sphblog-feeds'),
        url(r'^feeds/latestposts/(?P<category_id>\d+)/$', LatestBlogPosts(),
                            #{ 
                              #'noGroup': True,
                              #},
                            defaultdict,
                            name = 'sphblog-feeds'),

                       url(r'^$', sphblog_views.blogindex, defaultdict, name='sphblog_index'),
                       url(r'^postthread/$', sphblog_views.postthread, defaultdict, name = 'sphblog_postthread'),
                       url(r'^tag/(?P<tag_name>\w+)/(?:page/(?P<page>\d+)/)?$', sphblog_views.show_tag_posts, defaultdict, name = 'sphblog_show_tag_posts'),

                       # Indexes for year and month based archive
                       url(r'^archive/(?P<year>\d{4})/$', sphblog_views.blogindex, defaultdict, name='sphblog_archive_year'),
                       url(r'^archive/(?P<year>\d{4})/(?P<month>\d{1,2})/$', sphblog_views.blogindex, defaultdict, name='sphblog_archive_month'),
                       # Paged archives
                       url(r'^archive/(?P<year>\d{4})/page/(?P<page>\d+)/$', sphblog_views.blogindex, defaultdict, name='sphblog_archive_year_paged'),
                       url(r'^archive/(?P<year>\d{4})/(?P<month>\d{1,2})/page/(?P<page>\d+)/$', sphblog_views.blogindex, defaultdict, name='sphblog_archive_month_paged'),

                       url(r'^page/(?P<page>\d+)/$', sphblog_views.blogindex, defaultdict, name='sphblog_paged_index'),

                       url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<slug>.*)/$', sphblog_views.show_thread_redirect, defaultdict),
                       url(r'^(?P<category_id>\d+)/$', sphblog_views.blogindex_redirect, defaultdict, name='sphblog_category_index'),
                       url(r'^(?P<category_slug>[\w\-]+)/$', sphblog_views.blogindex, defaultdict, name='sphblog_category_index_slug'),
                       url(r'^(?P<category_slug>[\w\-]+?)/(?P<slug>[\w\-]+)/$', sphblog_views.show_thread, defaultdict, name='sphblog_show_thread'),
                ]

