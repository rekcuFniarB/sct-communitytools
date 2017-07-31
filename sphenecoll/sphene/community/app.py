from django.apps import AppConfig

class SphCommunityConfig(AppConfig):
    name = 'sphene.community'
    label = 'community'
    def ready(self):
        import sphene.community.avatar
