from django.conf.urls import url
from sphene.sphwiki import views
#from django.views.generic.simple import redirect_to
from django.views.generic.base import RedirectView

urlpatterns = [
                       #url(r'^$', redirect_to, {'url': 'show/Start/'}),
                       url(r'^$', RedirectView.as_view(url='show/Start/')),
              ]

snip = r'(?P<snipName>[\w/:\-.]+?)'

urlpatterns.extend([
                        url(r'^recentchanges/$', views.RecentChangesClass.as_view(), name='sphene-sphwiki-recentChanges'),
                        url(r'^show/'          + snip + r'/$', views.showSnip, name='sphene-sphwiki-showSnip'),
                        url(r'^pdf/'           + snip + r'/$', views.generatePDF, name='sphene-sphwiki-generatePDF'),
                        url(r'^edit/'          + snip + r'/$', views.editSnip, name='sphene-sphwiki-editSnip'),
                        url(r'^editversion/'+ snip + r'/(?P<versionId>\d+)/$', views.editSnip, name = 'sphwiki_editversion'),
                        url(r'^history/'       + snip + r'/$', views.ShowHistoryClass.as_view(), name='sphene-sphwiki-history'),
                        url(r'^diff/'          + snip + r'/(?P<changeId>\d+)/$', views.diff, name = 'sphene-sphwiki-diff'),
                        url(r'^attachments/edit/'   + snip + r'/(?P<attachmentId>\d+)/$', views.attachmentEdit),
                        url(r'^attachments/create/'   + snip + r'/$', views.attachmentCreate, name='sphene-sphwiki-attachmentCreate'),
                        url(r'^attachments/list/'   + snip + r'/$', views.attachment, name='sphene-sphwiki-attachment'),

                        url(r'^tag/(?P<tag_name>\w+)/$', views.show_tag_snips, name = 'sphwiki_show_tag_snips'),
                  ])
