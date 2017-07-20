from django.conf.urls import url
from sphene.community import views as communityViews
from django.conf import settings

#from sphene.contrib.libs.common.utils.utils import mergedict

defaultdict = { 'group': settings.SPH_SETTINGS['group']['name'],
                'groupName': settings.SPH_SETTINGS['group']['name']}

urlpatterns = [
                       url(r'captcha/(?P<token_id>\w+).jpg$', communityViews.captcha_image, defaultdict),
                       #url(r'accounts/login/$', 'django.contrib.auth.views.login', { 'noGroup': True,
                       #                                                           }),
                       #url(r'accounts/register/$', 'django.contrib.auth.views.logout', { 'noGroup': True,
                       #                                                               }),
                       url(r'accounts/login/$', communityViews.accounts_login, defaultdict),
                       url(r'accounts/logout/$', communityViews.accounts_logout, defaultdict),
                       url(r'accounts/forgot/$', communityViews.accounts_forgot, defaultdict),
                       url(r'profile/(?P<user_id>\d+)/$', communityViews.profile, defaultdict, name='sphene-community-profile'),
                       url(r'profile/edit/$', communityViews.profile_edit_mine, defaultdict),
                       url(r'profile/edit/(?P<user_id>\d+)/$', communityViews.profile_edit, defaultdict, name='sphene-community-profile-edit'),
                       url(r'profile/(?P<user_id>\d+)/reveal_address/$', communityViews.reveal_emailaddress, defaultdict, name = 'sph_reveal_emailaddress',),

                       url(r'admin/permission/role/list/$', communityViews.admin_permission_role_list, defaultdict, name = 'community_admin_permission_role_list'),
                       url(r'admin/permission/role/edit/(?P<role_id>\d+)/$', communityViews.admin_permission_role_edit, defaultdict),
                       url(r'admin/permission/role/create/$', communityViews.admin_permission_role_edit, defaultdict, name = 'admin_permission_role_create'),
                       url(r'admin/permission/role/member/(?P<role_id>\d+)/list/$', communityViews.admin_permission_role_member_list, defaultdict),
                       url(r'admin/permission/role/member/(?P<role_id>\d+)/add/$', communityViews.admin_permission_role_member_add, defaultdict),
                       url(r'admin/permission/role/member/(?P<role_id>\d+)/addgroup/$', communityViews.admin_permission_role_groupmember_add, defaultdict),

                       url(r'admin/permission/rolegroup/list/$', communityViews.admin_permission_rolegroup_list, defaultdict, name = 'community_admin_permission_rolegroup_list'),
                       url(r'admin/permission/rolegroup/edit/(?P<rolegroup_id>\d+)/$', communityViews.admin_permission_rolegroup_edit, defaultdict),

                       url(r'admin/users/$', communityViews.admin_users, defaultdict, name='sph_admin_users'),
                       url(r'admin/users/(?P<user_id>\d+)/switch/$', communityViews.admin_user_switch_active, defaultdict, name='sph_admin_user_switch_active'),

                       url(r'^accounts/register/$', communityViews.register, defaultdict, name = 'sph_register'),
                       url(r'^accounts/register/(?P<emailHash>[a-zA-Z\./\+0-9=]+)/(?P<email>[a-zA-Z%@\./\+0-9_-]+)/$', communityViews.register_hash, defaultdict, name = 'sph_register_hash'),
                       url(r'^tags/json/autocompletion/$', communityViews.tags_json_autocompletion, defaultdict, name = 'sph_tags_json_autocompletion'),
                ]
