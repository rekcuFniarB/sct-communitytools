from django.conf.urls import url
from sphene.sphwiki import views
#from django.views.generic.simple import redirect_to
from django.views.generic.base import RedirectView
from django.conf import settings

defaultdict = { 'group': settings.SPH_SETTINGS['group']['name'],
                'groupName': settings.SPH_SETTINGS['group']['name']}

urlpatterns = [
                       #url(r'^$', redirect_to, {'url': 'show/Start/'}),
                       url(r'^$', RedirectView.as_view(url='show/Start/')),
              ]

snip = r'(?P<snipName>[\w/:\-.]+?)'

urlpatterns.extend([
                        url(r'^recentchanges/$', views.RecentChangesClass.as_view(), defaultdict, name='sphene-sphwiki-recentChanges'),
                        url(r'^show/'          + snip + r'/$', views.showSnip, defaultdict, name='sphene-sphwiki-showSnip'),
                        url(r'^pdf/'           + snip + r'/$', views.generatePDF, defaultdict, name='sphene-sphwiki-generatePDF'),
                        url(r'^edit/'          + snip + r'/$', views.editSnip, defaultdict, name='sphene-sphwiki-editSnip'),
                        url(r'^editversion/'+ snip + r'/(?P<versionId>\d+)/$', views.editSnip, defaultdict, name = 'sphwiki_editversion'),
                        url(r'^history/'       + snip + r'/$', views.ShowHistoryClass.as_view(), defaultdict, name='sphene-sphwiki-history'),
                        url(r'^diff/'          + snip + r'/(?P<changeId>\d+)/$', views.diff, defaultdict, name = 'sphene-sphwiki-diff'),
                        url(r'^attachments/edit/'   + snip + r'/(?P<attachmentId>\d+)/$', views.attachmentEdit, defaultdict),
                        url(r'^attachments/create/'   + snip + r'/$', views.attachmentCreate, defaultdict, name='sphene-sphwiki-attachmentCreate'),
                        url(r'^attachments/list/'   + snip + r'/$', views.attachment, defaultdict, name='sphene-sphwiki-attachment'),

                        url(r'^tag/(?P<tag_name>\w+)/$', views.ShowTagSnips.as_view(), defaultdict, name = 'sphwiki_show_tag_snips'),
                  ])
