# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 22:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone


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
            name='BlogCategoryConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enable_googleblogping', models.BooleanField(help_text=b'Enable ping to blogsearch.google.com ?')),
            ],
        ),
        migrations.CreateModel(
            name='BlogPostExtension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, b'Draft'), (2, b'Published'), (3, b'Hidden')])),
                ('slug', models.CharField(db_index=True, max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BoardUserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signature', models.TextField(default=b'', verbose_name='Signature')),
                ('markup', models.CharField(choices=[(b'bbcode', b'BBCode')], max_length=250, null=True, verbose_name='Markup')),
                ('default_notifyme_value', models.NullBooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
                'verbose_name': 'Board user profile',
                'verbose_name_plural': 'Board user profiles',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
                ('allowview', models.IntegerField(choices=[(-1, b'All Users'), (0, b'Loggedin Users'), (1, b'Members of the Group'), (2, b'Staff Members'), (3, b'Nobody')], default=-1)),
                ('allowthreads', models.IntegerField(choices=[(-1, b'All Users'), (0, b'Loggedin Users'), (1, b'Members of the Group'), (2, b'Staff Members'), (3, b'Nobody')], default=0)),
                ('allowreplies', models.IntegerField(choices=[(-1, b'All Users'), (0, b'Loggedin Users'), (1, b'Members of the Group'), (2, b'Staff Members'), (3, b'Nobody')], default=0)),
                ('sortorder', models.IntegerField(default=0)),
                ('slug', models.CharField(db_index=True, max_length=250, unique=True)),
                ('category_type', models.CharField(blank=True, db_index=True, max_length=250)),
            ],
            options={
                'ordering': ['sortorder'],
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='CategoryLastVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastvisit', models.DateTimeField(default=django.utils.timezone.now)),
                ('oldlastvisit', models.DateTimeField(null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sphene.Category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Category last visit',
                'verbose_name_plural': 'Category last visits',
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
                ('profile_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sphene.CommunityUserProfileField', verbose_name='Profile field')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sphene.CommunityUserProfile', verbose_name='User profile')),
            ],
            options={
                'verbose_name': 'Community user profile field value',
                'verbose_name_plural': 'Community user profile field values',
            },
        ),
        migrations.CreateModel(
            name='ExtendedCategoryConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_label', models.CharField(blank=True, max_length=250)),
                ('body_label', models.CharField(blank=True, max_length=250)),
                ('body_initial', models.TextField(blank=True)),
                ('body_help_text', models.TextField(blank=True)),
                ('post_new_thread_label', models.CharField(blank=True, max_length=250)),
                ('above_thread_list_block', models.TextField(blank=True, help_text=b'HTML which will be displayed above the thread list.')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sphene.Category', unique=True)),
            ],
            options={
                'verbose_name': 'Extended category config',
                'verbose_name_plural': 'Extended category configs',
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
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sphene.Group', verbose_name='Group')),
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
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sphene.Group', verbose_name='Group')),
            ],
            options={
                'verbose_name': 'Group template',
                'verbose_name_plural': 'Group templates',
            },
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sphene.Category')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sphene.Group')),
            ],
            options={
                'verbose_name': 'Monitor',
                'verbose_name_plural': 'Monitors',
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
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sphene.Group', verbose_name='Group')),
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
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
                ('choices_per_user', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Poll',
                'verbose_name_plural': 'Polls',
            },
        ),
        migrations.CreateModel(
            name='PollChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=250)),
                ('count', models.IntegerField()),
                ('sortorder', models.IntegerField(default=0)),
                ('poll', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='sphene.Poll')),
            ],
            options={
                'ordering': ['sortorder'],
                'verbose_name': 'Poll choice',
                'verbose_name_plural': 'Poll choices',
            },
        ),
        migrations.CreateModel(
            name='PollVoters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='sphene.PollChoice')),
                ('poll', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='sphene.Poll')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Poll voter',
                'verbose_name_plural': 'Poll voters',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0, editable=False)),
                ('subject', models.CharField(max_length=250)),
                ('body', models.TextField()),
                ('postdate', models.DateTimeField(auto_now_add=True)),
                ('markup', models.CharField(choices=[(b'bbcode', b'BBCode')], max_length=250, null=True)),
                ('is_hidden', models.IntegerField(db_index=True, default=0, editable=False)),
                ('author', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sphboard_post_author_set', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='sphene.Category')),
                ('thread', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='sphene.Post')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
            managers=[
                ('allobjects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='PostAnnotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created', models.DateTimeField()),
                ('hide_post', models.BooleanField()),
                ('markup', models.CharField(choices=[(b'bbcode', b'BBCode')], max_length=250, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='annotation', to='sphene.Post', unique=True)),
            ],
            options={
                'verbose_name': 'Post annotation',
                'verbose_name_plural': 'Post annotations',
            },
        ),
        migrations.CreateModel(
            name='PostAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileupload', models.FileField(blank=True, upload_to=b'var/sphene/sphwiki/attachment/%Y/%m/%d', verbose_name='File')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='sphene.Post')),
            ],
            options={
                'verbose_name': 'Post attachment',
                'verbose_name_plural': 'Post attachments',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sphene.Group', verbose_name='Group')),
                ('permission_flags', models.ManyToManyField(related_name='roles', to='sphene.PermissionFlag', verbose_name='Permission flags')),
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
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sphene.Group', verbose_name='Group')),
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
                ('rolegroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sphene.RoleGroup', verbose_name='Role group')),
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
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sphene.Role', verbose_name='Role')),
                ('rolegroup', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sphene.RoleGroup', verbose_name='Role group')),
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
                ('role_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sphene.RoleMember', verbose_name='Role member')),
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
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sphene.Group', verbose_name='Group')),
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
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='labels', to='sphene.Tag')),
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
        migrations.CreateModel(
            name='ThreadInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thread_type', models.IntegerField(choices=[(1, b'Default'), (2, b'Moved Thread')])),
                ('heat', models.IntegerField(db_index=True, default=0)),
                ('heat_calculated', models.DateTimeField(null=True)),
                ('sticky_value', models.IntegerField(db_index=True, default=0)),
                ('post_count', models.IntegerField(default=0)),
                ('view_count', models.IntegerField(default=0)),
                ('thread_latest_postdate', models.DateTimeField(db_index=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sphene.Category')),
                ('latest_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thread_latest_set', to='sphene.Post')),
                ('root_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sphene.Post')),
            ],
            options={
                'verbose_name': 'Thread information',
                'verbose_name_plural': 'Thread informations',
            },
        ),
        migrations.CreateModel(
            name='ThreadLastVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastvisit', models.DateTimeField(default=django.utils.timezone.now)),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sphene.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Thread last visit',
                'verbose_name_plural': 'Thread last visits',
            },
        ),
        migrations.CreateModel(
            name='UserPostCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_count', models.IntegerField(default=0)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sphene.Group')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User post count',
                'verbose_name_plural': 'User post counts',
            },
        ),
        migrations.CreateModel(
            name='WikiAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded', models.DateTimeField(editable=False)),
                ('fileupload', models.FileField(upload_to=b'var/sphene/sphwiki/attachment/%Y/%m/%d', verbose_name='fileupload')),
                ('description', models.TextField(blank=True, verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='WikiPreference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view', models.IntegerField(choices=[(-1, b'All Users'), (0, b'Loggedin Users'), (1, b'Members of the Group'), (2, b'Staff Members'), (3, b'Nobody')])),
                ('edit', models.IntegerField(choices=[(-1, b'All Users'), (0, b'Loggedin Users'), (1, b'Members of the Group'), (2, b'Staff Members'), (3, b'Nobody')])),
            ],
        ),
        migrations.CreateModel(
            name='WikiSnip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('title', models.CharField(blank=True, max_length=250, verbose_name='title')),
                ('body', models.TextField(verbose_name='body')),
                ('created', models.DateTimeField(editable=False)),
                ('changed', models.DateTimeField(editable=False)),
                ('creator', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wikisnip_created', to=settings.AUTH_USER_MODEL)),
                ('editor', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wikisnip_edited', to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sphene.Group')),
            ],
        ),
        migrations.CreateModel(
            name='WikiSnipChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edited', models.DateTimeField()),
                ('title', models.CharField(blank=True, max_length=250)),
                ('body', models.TextField()),
                ('message', models.TextField()),
                ('change_type', models.IntegerField()),
                ('editor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('snip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sphene.WikiSnip')),
            ],
        ),
        migrations.AddField(
            model_name='wikipreference',
            name='snip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sphene.WikiSnip'),
        ),
        migrations.AddField(
            model_name='wikiattachment',
            name='snip',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='sphene.WikiSnip'),
        ),
        migrations.AddField(
            model_name='wikiattachment',
            name='uploader',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='taggeditem',
            name='tag_label',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='sphene.TagLabel'),
        ),
        migrations.AddField(
            model_name='poll',
            name='post',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='sphene.Post'),
        ),
        migrations.AddField(
            model_name='monitor',
            name='thread',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sphene.Post'),
        ),
        migrations.AddField(
            model_name='monitor',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='group',
            name='default_theme',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sphene.Theme'),
        ),
        migrations.AddField(
            model_name='group',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sphene.Group'),
        ),
        migrations.AddField(
            model_name='category',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sphene.Group'),
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='sphene.Category'),
        ),
        migrations.AddField(
            model_name='blogpostextension',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sphene.Post', unique=True),
        ),
        migrations.AddField(
            model_name='blogcategoryconfig',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sphene.Category', unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='userpostcount',
            unique_together=set([('user', 'group')]),
        ),
        migrations.AlterUniqueTogether(
            name='threadlastvisit',
            unique_together=set([('user', 'thread')]),
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
        migrations.AlterUniqueTogether(
            name='categorylastvisit',
            unique_together=set([('user', 'category')]),
        ),
    ]