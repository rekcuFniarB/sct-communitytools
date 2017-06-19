from django.apps import AppConfig

class SphBlogConfig(AppConfig):
    name = 'sphene.sphblog'
    def ready(self):
        from sphene.community.sphutils import add_setting_defaults
        add_setting_defaults({
           'blog_post_paging': 10,
        })
