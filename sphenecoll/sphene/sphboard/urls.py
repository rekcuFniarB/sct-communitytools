from django.conf.urls import url

from sphene.sphboard.feeds import LatestThreads, LatestGlobalThreads

from sphene.sphboard import views as boardViews

urlpatterns = [
                       #url(r'^$', 'django.views.generic.simple.redirect_to', {'url': 'show/0/'}, name = 'sphboard-index'),
                       url(r'^feeds/latest/(?P<category_id>.+)/$',
                           LatestThreads(),
                           {},
                           'sphboard-feeds'),
                       url(r'^feeds/all/$',
                           LatestGlobalThreads(),
                           {},
                           'sphboard-global-feeds'),

                        url(r'^$', boardViews.showCategory, {'category_id': '0'}, name = 'sphboard-index'),
                        #url(r'^show/(?P<category_id>\d+)/(?P<slug>.+)/$', boardViews.showCategory, name = 'sphboard_show_category'),
                        url(r'^show/(?P<category_id>\d+)/(?P<slug>.+)/$', boardViews.ShowCategoryClass.as_view(), name = 'sphboard_show_category'),
                        url(r'^show/(?P<category_id>\d+)/$', boardViews.ShowCategoryClass.as_view(), name = 'sphboard_show_category_without_slug'),
                        url(r'^list_threads/(?P<category_id>\d+)/$', boardViews.listThreads),
                        url(r'^latest/(?P<category_id>\d+)/$', boardViews.showCategory, { 'showType': 'threads' }, name = 'sphboard_latest'),
                        url(r'^thread/(?P<thread_id>\d+)/(?P<slug>.+)/$', boardViews.showThread, name = 'sphboard_show_thread'),
                        url(r'^thread/(?P<thread_id>\d+)/$', boardViews.showThread, name = 'sphboard_show_thread_without_slug'),
                        url(r'^options/(?P<thread_id>\d+)/$', boardViews.options, name = 'sphboard_options'),
                        url(r'^move/(?P<thread_id>\d+)/$', boardViews.move, name = 'sphboard_move_thread'),
                        url(r'^post/(?P<category_id>\d+)/(?P<post_id>\d+)/$', boardViews.post),
                        url(r'^post/(?P<category_id>\d+)/$', boardViews.post, name = 'sphboard_post_thread'),
                        url(r'^reply/(?P<category_id>\d+)/(?P<thread_id>\d+)/$', boardViews.reply, name = 'sphboard_reply'),
                        url(r'^annotate/(?P<post_id>\d+)/$', boardViews.annotate),
                        url(r'^hide/(?P<post_id>\d+)/$', boardViews.hide),
                        url(r'^move_post_1/(?P<post_id>\d+)/$', boardViews.move_post_1, name='move_post_1'),
                        url(r'^move_post_2/(?P<post_id>\d+)/(?P<category_id>\d+)/$', boardViews.move_post_2, name='move_post_2'),
                        url(r'^move_post_3_cat/(?P<post_id>\d+)/(?P<category_id>\d+)/$', boardViews.move_post_3, name='move_post_3'),
                        url(r'^move_post_3_thr/(?P<post_id>\d+)/(?P<category_id>\d+)/(?P<thread_id>\d+)/$', boardViews.move_post_3, name='move_post_3'),
                        url(r'^delete_moved_info/(?P<pk>\d+)/$', boardViews.delete_moved_info, name='delete_moved_info'),
                        url(r'^vote/(?P<thread_id>\d+)/$', boardViews.vote),
                        url(r'^togglemonitor_(?P<monitortype>\w+)/(?P<object_id>\d+)/(?P<monitor_user_id>\d+)/$', boardViews.toggle_monitor, name = 'sphboard_toggle_user_monitor'),
                        url(r'^togglemonitor_(?P<monitortype>\w+)/(?P<object_id>\d+)/$', boardViews.toggle_monitor, name = 'sphboard_toggle_monitor'),
                        url(r'^catchup/(?P<category_id>\d+)/$', boardViews.catchup, name='sphboard_catchup'),
                        url(r'^poll/(?P<poll_id>\d+)/edit/$', boardViews.edit_poll, name = 'sphboard_edit_poll'),
                        url(r'^admin/(?P<user_id>\d+)/posts/$', boardViews.admin_user_posts, name = 'sphboard_admin_user_posts'),
                        url(r'^admin/(?P<user_id>\d+)/posts/(?P<post_id>\d+)/delete/$', boardViews.admin_post_delete, name = 'sphboard_admin_post_delete'),
                        url(r'^admin/(?P<user_id>\d+)/posts/delete/$', boardViews.admin_posts_delete, name = 'sphboard_admin_posts_delete'),
                  ]

