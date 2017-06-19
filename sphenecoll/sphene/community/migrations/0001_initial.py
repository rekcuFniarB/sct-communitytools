# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 22:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationChangelog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=250)),
                ('model', models.CharField(max_length=250)),
                ('version', models.CharField(max_length=250)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'get_latest_by': 'applied',
                'verbose_name': 'Application change log',
                'verbose_name_plural': 'Application change logs',
            },
        ),
        migrations.CreateModel(
            name='CommunityUserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('displayname', models.CharField(max_length=250, verbose_name='Display name')),
                ('public_emailaddress', models.CharField(max_length=250, verbose_name='Public email address')),
                ('avatar', models.ImageField(blank=True, height_field=b'avatar_height', null=True, upload_to=b'var/sphene/sphwiki/attachment/%Y/%m/%d', verbose_name='Avatar', width_field=b'avatar_width')),
                ('avatar_height', models.IntegerField(blank=True, null=True, verbose_name='Avatar height')),
                ('avatar_width', models.IntegerField(blank=True, null=True, verbose_name='Avatar width')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Community user profile',
                'verbose_name_plural': 'Community user profiles',
            },
        ),
        migrations.CreateModel(
            name='CommunityUserProfileField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('help_text', models.CharField(blank=True, help_text=b'An optional help text displayed to the user.', max_length=250)),
                ('regex', models.CharField(blank=True, help_text=b'An optional regular expression to validate user input.', max_length=250)),
                ('renderstring', models.CharField(blank=True, help_text=b'An optional render string how the value should be displayed in the profile (e.g. &lt;a href="%(value)s"&gt;%(value)s&lt;/a&gt; - default: %(value)s', max_length=250)),
                ('sortorder', models.IntegerField()),
            ],
            options={
                'ordering': ['sortorder'],
                'verbose_name': 'Community user profile field',
                'verbose_name_plural': 'Community user profile fields',
            },
        ),
        migrations.CreateModel(
            name='CommunityUserProfileFieldValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=250)),
                ('profile_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.CommunityUserProfileField', verbose_name='Profile field')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.CommunityUserProfile', verbose_name='User profile')),
            ],
            options={
                'verbose_name': 'Community user profile field value',
                'verbose_name_plural': 'Community user profile field values',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('longname', models.CharField(max_length=250)),
                ('baseurl', models.CharField(help_text=b'The base URL under which this group will be available. Example: sct.sphene.net', max_length=250)),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
            },
        ),
        migrations.CreateModel(
            name='GroupMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userlevel', models.IntegerField(choices=[(0, 'Normal User'), (5, 'Administrator')])),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.Group', verbose_name='Group')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Group member',
                'verbose_name_plural': 'Group members',
            },
        ),
        migrations.CreateModel(
            name='GroupTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template_name', models.CharField(db_index=True, max_length=250)),
                ('source', models.TextField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.Group', verbose_name='Group')),
            ],
            options={
                'verbose_name': 'Group template',
                'verbose_name_plural': 'Group templates',
            },
        ),
        migrations.CreateModel(
            name='Navigation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=250)),
                ('href', models.CharField(max_length=250)),
                ('urltype', models.IntegerField(choices=[(0, b'Relative (e.g. /wiki/show/Start)'), (1, b'Absolute (e.g. http://sphene.net')], default=0)),
                ('sortorder', models.IntegerField(default=100)),
                ('navigationType', models.IntegerField(choices=[(0, b'Left Main Navigation'), (1, b'Top navigation')], default=0)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.Group', verbose_name='Group')),
            ],
            options={
                'ordering': ['sortorder'],
                'verbose_name': 'Navigation',
                'verbose_name_plural': 'Navigations',
            },
        ),
        migrations.CreateModel(
            name='PermissionFlag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Permission flag',
                'verbose_name_plural': 'Permission flags',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.Group', verbose_name='Group')),
                ('permission_flags', models.ManyToManyField(related_name='roles', to='community.PermissionFlag', verbose_name='Permission flags')),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.CreateModel(
            name='RoleGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.Group', verbose_name='Group')),
            ],
            options={
                'verbose_name': 'Role group',
                'verbose_name_plural': 'Role groups',
            },
        ),
        migrations.CreateModel(
            name='RoleGroupMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rolegroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.RoleGroup', verbose_name='Role group')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Role group member',
                'verbose_name_plural': 'Role group members',
            },
        ),
        migrations.CreateModel(
            name='RoleMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_limitations', models.BooleanField(verbose_name='Has limitations')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.Role', verbose_name='Role')),
                ('rolegroup', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='community.RoleGroup', verbose_name='Role group')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Role member',
                'verbose_name_plural': 'Role members',
            },
        ),
        migrations.CreateModel(
            name='RoleMemberLimitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(db_index=True)),
                ('object_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='Object type')),
                ('role_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.RoleMember', verbose_name='Role member')),
            ],
            options={
                'verbose_name': 'Role member limitation',
                'verbose_name_plural': 'Role member limitations',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.Group', verbose_name='Group')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='TaggedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(db_index=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sph_taggeditem_set', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'Tagged item',
                'verbose_name_plural': 'Tagged items',
            },
        ),
        migrations.CreateModel(
            name='TagLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=250)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='labels', to='community.Tag')),
            ],
            options={
                'verbose_name': 'Tag label',
                'verbose_name_plural': 'Tag labels',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('path', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Theme',
                'verbose_name_plural': 'Themes',
            },
        ),
        migrations.AddField(
            model_name='taggeditem',
            name='tag_label',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='community.TagLabel'),
        ),
        migrations.AddField(
            model_name='group',
            name='default_theme',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='community.Theme'),
        ),
        migrations.AddField(
            model_name='group',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='community.Group'),
        ),
        migrations.AlterUniqueTogether(
            name='taglabel',
            unique_together=set([('tag', 'label')]),
        ),
        migrations.AlterUniqueTogether(
            name='taggeditem',
            unique_together=set([('tag_label', 'content_type', 'object_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together=set([('group', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='rolememberlimitation',
            unique_together=set([('role_member', 'object_type', 'object_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='rolegroupmember',
            unique_together=set([('rolegroup', 'user')]),
        ),
        migrations.AlterUniqueTogether(
            name='rolegroup',
            unique_together=set([('group', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='role',
            unique_together=set([('name', 'group')]),
        ),
        migrations.AlterUniqueTogether(
            name='grouptemplate',
            unique_together=set([('group', 'template_name')]),
        ),
        migrations.AlterUniqueTogether(
            name='communityuserprofilefieldvalue',
            unique_together=set([('user_profile', 'profile_field')]),
        ),
    ]
