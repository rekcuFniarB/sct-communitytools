This is a fork of [Sphene Community Tools](https://github.com/hpoul/sct-communitytools) ported to Django 1.11. Some functions may remain broken.

Sphene Community Tools (SCT) - http://sct.sphene.net
Copyright (C) by Herbert Poul (herbert.poul@gmail.com)

Sphene Community Tools are django applications to build communities and 
similiar websites designed to be easily pluggable into any django 
project to build.
It currently consists of a forum, wiki and blog application.

### Requirements

* [Django](http://www.djangoproject.com) 1.11
* Python 2.7
* [PyCrypto](http://sf.net/projects/pycrypto) - (e.g. debian package python-crypto)
* [Python Imaging Library (PIL)](http://www.pythonware.com/products/pil/) (Pillow)


### Installation

[Create a django project](https://docs.djangoproject.com/en/1.11/intro/tutorial01/#creating-a-project). [Create a superuser](https://docs.djangoproject.com/en/1.11/intro/tutorial02/#creating-an-admin-user).

Copy **sphene** directory to your python path: site-packages or django apps directory (e.g. *django_root/my_project/sphene*). Also instead of copying you can make a symlink.

Add sphene modules to `INSTALLED_APPS` in `settings.py`:

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        #'django.contrib.staticfiles',
        'django.contrib.sites',
        'django.contrib.flatpages',
        'sphene.community',
        'sphene.sphboard',
        'sphene.sphwiki',
        'sphene.sphblog',
    ]

Note: if you placed sphene directory in django apps directory then module names in `INSTALLED_APPS` should be preceeded with your project name, e.g. `my_project.sphene.sphwiki`.

Add sphene middlewares:

    MIDDLEWARE = [
        'sphene.community.middleware.ThreadLocals',
        'sphene.community.middleware.GroupMiddleware',
        'sphene.community.middleware.LastModified',
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        #'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    ]

Add sphene context processor:

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                    os.path.join(ROOT_PATH, 'templates'),
                ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.template.context_processors.static',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    ## navigation middleware for SCT
                    'sphene.community.context_processors.navigation',
                ],
                'libraries': {
                    }
            },
        },
    ]


Setup [django caching](https://docs.djangoproject.com/en/1.11/topics/cache/). You can leave it unset on development server.

Set `USE_TZ` variable to `False` otherwise filter by month querysets in sphblog will not work (it's a bug).

Add special sphene settings:

    SPH_SETTINGS = {
         ## disable e-mail notifications
          'noemailnotifications': True,
         ## require captcha for new registrations, need djaptcha installed
          #'community_register_require_captcha': True,  
         ## See http://code.djangoproject.com/ticket/4789
          'workaround_select_related_bug': True,
         ## Other options found in the code:
         # 'wiki_attachments_upload_to': '',
         # 'wiki_pdf_generation_command': '',
         # 'wiki_pdf_generation': False,
         # 'wiki_pdf_generation_cachedir': '/tmp/sct_pdf', #default
         # 'community_email_show_only_public': True,
         # 'community_avatar_upload_to': '',
         'community_avatar_default_height': 100,
         'community_avatar_default_width': 100,
         # 'community_avatar_default': '',
         # 'community_avatar_max_height': 100,
         # 'community_avatar_max_width': 100,
         # 'community_avatar_max_size': '',
         # 'community_email_anonymous_require_captcha_timeout': ,
         # 'community_email_anonymous_require_captcha':,
         # 'markdown_top_heading_level': 1,
         'markdown_number_headings': False,
         # 'community_register_require_captcha': False,
         # 'community_groupaware_template_dir': None,
         # 'community_groups_in_url': ,
         # 'board_allow_attachments': False,
         # 'board_wysiwyg_testing': False,
         # 'board_wysiwyg': False,
         # 'board_post_paging': , #int paginate_by
         'use_gravatar': True,
         
         group = {
             'id': 0,
             'name': 'main', # Group name
             'longname': 'Main Group',
             'baseurl': 'www.example.com/',
             #'default_theme_id': 'None',
             #'parent_id': 'None',
         }
    }

Run `manage.py migrate`.

See also [original README](README).

