from django.conf.urls import url
from sphene.sphwiki import views


urlpatterns = [
                       url(r'^$', 'django.views.generic.simple.redirect_to', {'url': 'show/Start/'}),
              ]

snip = r'(?P<snipName>[\w/:\-.]+?)'

urlpatterns.extend([
                        url(r'^recentchanges/$', views.recentChanges),
                        url(r'^show/'          + snip + r'/$', views.showSnip),
                        url(r'^pdf/'           + snip + r'/$', views.generatePDF),
                        url(r'^edit/'          + snip + r'/$', views.editSnip),
                        url(r'^editversion/'+ snip + r'/(?P<versionId>\d+)/$', views.editSnip, name = 'sphwiki_editversion'),
                        url(r'^history/'       + snip + r'/$', views.history),
                        url(r'^diff/'          + snip + r'/(?P<changeId>\d+)/$', views.diff),
                        url(r'^attachments/edit/'   + snip + r'/(?P<attachmentId>\d+)/$', views.attachmentEdit),
                        url(r'^attachments/create/'   + snip + r'/$', views.attachmentCreate),
                        url(r'^attachments/list/'   + snip + r'/$', views.attachment),

                        url(r'^tag/(?P<tag_name>\w+)/$', views.show_tag_snip, name = 'sphwiki_show_tag_snips'),
                  ])
