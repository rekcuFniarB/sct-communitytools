# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import migrations, models

def create_initial_group(apps, schema_editor):
    Groups = apps.get_model('sphene', 'Group')
    if Groups.objects.count() == 0:
        ## If table is empty create initial group
        group = Groups()
        if hasattr(settings, 'SPH_SETTINGS') and 'group' in settings.SPH_SETTINGS:
            if 'name' in settings.SPH_SETTINGS['group'] and settings.SPH_SETTINGS['group']['name'] != '':
                group.name = settings.SPH_SETTINGS['group']['name']
            else:
                group.name = 'main'
            if 'longname' in settings.SPH_SETTINGS['group'] and settings.SPH_SETTINGS['group']['longname'] != '':
                group.longname = settings.SPH_SETTINGS['group']['longname']
            else:
                group.longname = 'Main Group'
            if 'baseurl' in settings.SPH_SETTINGS['group'] and settings.SPH_SETTINGS['group']['baseurl'] != '':
                group.baseurl = settings.SPH_SETTINGS['group']['baseurl']
            else:
                group.baseurl = 'http://example.com/'
        else:
            group.name = 'main'
            group.longname = 'Main Group'
            group.baseurl = 'http://example.com/'
        group.save()
            

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sphene', '0001_initial'),
    ]
    
    operations = [
        migrations.RunPython(create_initial_group),
    ]
