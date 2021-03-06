{"filter":false,"title":"settings.py","tooltip":"/blog/settings.py","undoManager":{"mark":18,"position":18,"stack":[[{"start":{"row":0,"column":0},"end":{"row":120,"column":0},"action":"remove","lines":["\"\"\"","Django settings for blog project.","","Generated by 'django-admin startproject' using Django 1.11.20.","","For more information on this file, see","https://docs.djangoproject.com/en/1.11/topics/settings/","","For the full list of settings and their values, see","https://docs.djangoproject.com/en/1.11/ref/settings/","\"\"\"","","import os","","# Build paths inside the project like this: os.path.join(BASE_DIR, ...)","BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))","","","# Quick-start development settings - unsuitable for production","# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/","","# SECURITY WARNING: keep the secret key used in production secret!","SECRET_KEY = 'z&ul7jx@5(9+!q$9s#jf5&*&c3i#e2s-@l=vb$8^f(xpc0@_3o'","","# SECURITY WARNING: don't run with debug turned on in production!","DEBUG = True","","ALLOWED_HOSTS = ['21b2b37a52d445e7bac0ff6fd2159d90.vfs.cloud9.us-east-1.amazonaws.com']","","","# Application definition","","INSTALLED_APPS = [","    'django.contrib.admin',","    'django.contrib.auth',","    'django.contrib.contenttypes',","    'django.contrib.sessions',","    'django.contrib.messages',","    'django.contrib.staticfiles',","]","","MIDDLEWARE = [","    'django.middleware.security.SecurityMiddleware',","    'django.contrib.sessions.middleware.SessionMiddleware',","    'django.middleware.common.CommonMiddleware',","    'django.middleware.csrf.CsrfViewMiddleware',","    'django.contrib.auth.middleware.AuthenticationMiddleware',","    'django.contrib.messages.middleware.MessageMiddleware',","    'django.middleware.clickjacking.XFrameOptionsMiddleware',","]","","ROOT_URLCONF = 'blog.urls'","","TEMPLATES = [","    {","        'BACKEND': 'django.template.backends.django.DjangoTemplates',","        'DIRS': [],","        'APP_DIRS': True,","        'OPTIONS': {","            'context_processors': [","                'django.template.context_processors.debug',","                'django.template.context_processors.request',","                'django.contrib.auth.context_processors.auth',","                'django.contrib.messages.context_processors.messages',","            ],","        },","    },","]","","WSGI_APPLICATION = 'blog.wsgi.application'","","","# Database","# https://docs.djangoproject.com/en/1.11/ref/settings/#databases","","DATABASES = {","    'default': {","        'ENGINE': 'django.db.backends.sqlite3',","        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","    }","}","","","# Password validation","# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators","","AUTH_PASSWORD_VALIDATORS = [","    {","        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',","    },","    {","        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',","    },","    {","        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',","    },","    {","        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',","    },","]","","","# Internationalization","# https://docs.djangoproject.com/en/1.11/topics/i18n/","","LANGUAGE_CODE = 'en-us'","","TIME_ZONE = 'UTC'","","USE_I18N = True","","USE_L10N = True","","USE_TZ = True","","","# Static files (CSS, JavaScript, Images)","# https://docs.djangoproject.com/en/1.11/howto/static-files/","","STATIC_URL = '/static/'",""],"id":1},{"start":{"row":0,"column":0},"end":{"row":122,"column":44},"action":"insert","lines":["\"\"\"","Django settings for blog project.","Generated by 'django-admin startproject' using Django 1.11.15.","For more information on this file, see","https://docs.djangoproject.com/en/1.11/topics/settings/","For the full list of settings and their values, see","https://docs.djangoproject.com/en/1.11/ref/settings/","\"\"\"","","import os","","# Build paths inside the project like this: os.path.join(BASE_DIR, ...)","BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))","","","# Quick-start development settings - unsuitable for production","# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/","","# SECURITY WARNING: keep the secret key used in production secret!","SECRET_KEY = 'y&1z#wl#)&vg^_z0&qf+rtzh9+v9zn1&%&xi8w$-njkzia6a7e'","","# SECURITY WARNING: don't run with debug turned on in production!","DEBUG = True","","ALLOWED_HOSTS = [os.environ.get(\"C9_HOSTNAME\"), '127.0.0.1']","","","# Application definition","","INSTALLED_APPS = [","    'django.contrib.admin',","    'django.contrib.auth',","    'django.contrib.contenttypes',","    'django.contrib.sessions',","    'django.contrib.messages',","    'django.contrib.staticfiles',","    'posts',","]","","MIDDLEWARE = [","    'django.middleware.security.SecurityMiddleware',","    'django.contrib.sessions.middleware.SessionMiddleware',","    'django.middleware.common.CommonMiddleware',","    'django.middleware.csrf.CsrfViewMiddleware',","    'django.contrib.auth.middleware.AuthenticationMiddleware',","    'django.contrib.messages.middleware.MessageMiddleware',","    'django.middleware.clickjacking.XFrameOptionsMiddleware',","]","","ROOT_URLCONF = 'blog.urls'","","TEMPLATES = [","    {","        'BACKEND': 'django.template.backends.django.DjangoTemplates',","        'DIRS': [os.path.join(BASE_DIR, 'templates')],","        'APP_DIRS': True,","        'OPTIONS': {","            'context_processors': [","                'django.template.context_processors.debug',","                'django.template.context_processors.request',","                'django.contrib.auth.context_processors.auth',","                'django.contrib.messages.context_processors.messages',","                'django.template.context_processors.media',","            ],","        },","    },","]","","WSGI_APPLICATION = 'blog.wsgi.application'","","","# Database","# https://docs.djangoproject.com/en/1.11/ref/settings/#databases","","DATABASES = {","    'default': {","        'ENGINE': 'django.db.backends.sqlite3',","        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","    }","}","","","# Password validation","# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators","","AUTH_PASSWORD_VALIDATORS = [","    {","        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',","    },","    {","        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',","    },","    {","        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',","    },","    {","        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',","    },","]","","","# Internationalization","# https://docs.djangoproject.com/en/1.11/topics/i18n/","","LANGUAGE_CODE = 'en-us'","","TIME_ZONE = 'UTC'","","USE_I18N = True","","USE_L10N = True","","USE_TZ = True","","","# Static files (CSS, JavaScript, Images)","# https://docs.djangoproject.com/en/1.11/howto/static-files/","","STATIC_URL = '/static/'","STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )","","MEDIA_URL = '/media/'","MEDIA_ROOT = os.path.join(BASE_DIR, 'media')"]}],[{"start":{"row":24,"column":17},"end":{"row":24,"column":59},"action":"remove","lines":["os.environ.get(\"C9_HOSTNAME\"), '127.0.0.1'"],"id":2},{"start":{"row":24,"column":17},"end":{"row":24,"column":86},"action":"insert","lines":["'21b2b37a52d445e7bac0ff6fd2159d90.vfs.cloud9.us-east-1.amazonaws.com'"]}],[{"start":{"row":35,"column":33},"end":{"row":36,"column":0},"action":"insert","lines":["",""],"id":3},{"start":{"row":36,"column":0},"end":{"row":36,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":36,"column":4},"end":{"row":36,"column":6},"action":"insert","lines":["''"],"id":4}],[{"start":{"row":36,"column":5},"end":{"row":36,"column":6},"action":"insert","lines":["d"],"id":5},{"start":{"row":36,"column":6},"end":{"row":36,"column":7},"action":"insert","lines":["j"]},{"start":{"row":36,"column":7},"end":{"row":36,"column":8},"action":"insert","lines":["a"]},{"start":{"row":36,"column":8},"end":{"row":36,"column":9},"action":"insert","lines":["n"]},{"start":{"row":36,"column":9},"end":{"row":36,"column":10},"action":"insert","lines":["g"]},{"start":{"row":36,"column":10},"end":{"row":36,"column":11},"action":"insert","lines":["o"]}],[{"start":{"row":36,"column":11},"end":{"row":36,"column":12},"action":"insert","lines":["_"],"id":6},{"start":{"row":36,"column":12},"end":{"row":36,"column":13},"action":"insert","lines":["f"]},{"start":{"row":36,"column":13},"end":{"row":36,"column":14},"action":"insert","lines":["o"]},{"start":{"row":36,"column":14},"end":{"row":36,"column":15},"action":"insert","lines":["r"]},{"start":{"row":36,"column":15},"end":{"row":36,"column":16},"action":"insert","lines":["m"]},{"start":{"row":36,"column":16},"end":{"row":36,"column":17},"action":"insert","lines":["s"]}],[{"start":{"row":36,"column":17},"end":{"row":36,"column":18},"action":"insert","lines":["_"],"id":7},{"start":{"row":36,"column":18},"end":{"row":36,"column":19},"action":"insert","lines":["b"]},{"start":{"row":36,"column":19},"end":{"row":36,"column":20},"action":"insert","lines":["o"]},{"start":{"row":36,"column":20},"end":{"row":36,"column":21},"action":"insert","lines":["o"]},{"start":{"row":36,"column":21},"end":{"row":36,"column":22},"action":"insert","lines":["t"]},{"start":{"row":36,"column":22},"end":{"row":36,"column":23},"action":"insert","lines":["s"]},{"start":{"row":36,"column":23},"end":{"row":36,"column":24},"action":"insert","lines":["t"]},{"start":{"row":36,"column":24},"end":{"row":36,"column":25},"action":"insert","lines":["r"]},{"start":{"row":36,"column":25},"end":{"row":36,"column":26},"action":"insert","lines":["a"]}],[{"start":{"row":36,"column":26},"end":{"row":36,"column":27},"action":"insert","lines":["p"],"id":8}],[{"start":{"row":36,"column":28},"end":{"row":36,"column":29},"action":"insert","lines":[","],"id":9}],[{"start":{"row":19,"column":13},"end":{"row":19,"column":65},"action":"remove","lines":["'y&1z#wl#)&vg^_z0&qf+rtzh9+v9zn1&%&xi8w$-njkzia6a7e'"],"id":12}],[{"start":{"row":0,"column":0},"end":{"row":123,"column":44},"action":"remove","lines":["\"\"\"","Django settings for blog project.","Generated by 'django-admin startproject' using Django 1.11.15.","For more information on this file, see","https://docs.djangoproject.com/en/1.11/topics/settings/","For the full list of settings and their values, see","https://docs.djangoproject.com/en/1.11/ref/settings/","\"\"\"","","import os","","# Build paths inside the project like this: os.path.join(BASE_DIR, ...)","BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))","","","# Quick-start development settings - unsuitable for production","# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/","","# SECURITY WARNING: keep the secret key used in production secret!","SECRET_KEY = ","","# SECURITY WARNING: don't run with debug turned on in production!","DEBUG = True","","ALLOWED_HOSTS = ['21b2b37a52d445e7bac0ff6fd2159d90.vfs.cloud9.us-east-1.amazonaws.com']","","","# Application definition","","INSTALLED_APPS = [","    'django.contrib.admin',","    'django.contrib.auth',","    'django.contrib.contenttypes',","    'django.contrib.sessions',","    'django.contrib.messages',","    'django.contrib.staticfiles',","    'django_forms_bootstrap',","    'posts',","]","","MIDDLEWARE = [","    'django.middleware.security.SecurityMiddleware',","    'django.contrib.sessions.middleware.SessionMiddleware',","    'django.middleware.common.CommonMiddleware',","    'django.middleware.csrf.CsrfViewMiddleware',","    'django.contrib.auth.middleware.AuthenticationMiddleware',","    'django.contrib.messages.middleware.MessageMiddleware',","    'django.middleware.clickjacking.XFrameOptionsMiddleware',","]","","ROOT_URLCONF = 'blog.urls'","","TEMPLATES = [","    {","        'BACKEND': 'django.template.backends.django.DjangoTemplates',","        'DIRS': [os.path.join(BASE_DIR, 'templates')],","        'APP_DIRS': True,","        'OPTIONS': {","            'context_processors': [","                'django.template.context_processors.debug',","                'django.template.context_processors.request',","                'django.contrib.auth.context_processors.auth',","                'django.contrib.messages.context_processors.messages',","                'django.template.context_processors.media',","            ],","        },","    },","]","","WSGI_APPLICATION = 'blog.wsgi.application'","","","# Database","# https://docs.djangoproject.com/en/1.11/ref/settings/#databases","","DATABASES = {","    'default': {","        'ENGINE': 'django.db.backends.sqlite3',","        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","    }","}","","","# Password validation","# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators","","AUTH_PASSWORD_VALIDATORS = [","    {","        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',","    },","    {","        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',","    },","    {","        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',","    },","    {","        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',","    },","]","","","# Internationalization","# https://docs.djangoproject.com/en/1.11/topics/i18n/","","LANGUAGE_CODE = 'en-us'","","TIME_ZONE = 'UTC'","","USE_I18N = True","","USE_L10N = True","","USE_TZ = True","","","# Static files (CSS, JavaScript, Images)","# https://docs.djangoproject.com/en/1.11/howto/static-files/","","STATIC_URL = '/static/'","STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )","","MEDIA_URL = '/media/'","MEDIA_ROOT = os.path.join(BASE_DIR, 'media')"],"id":13},{"start":{"row":0,"column":0},"end":{"row":131,"column":44},"action":"insert","lines":["\"\"\"","Django settings for blog project.","Generated by 'django-admin startproject' using Django 1.11.15.","For more information on this file, see","https://docs.djangoproject.com/en/1.11/topics/settings/","For the full list of settings and their values, see","https://docs.djangoproject.com/en/1.11/ref/settings/","\"\"\"","","import os","import dj_database_url","","if os.path.exists('env.py'):","    import env","","# Build paths inside the project like this: os.path.join(BASE_DIR, ...)","BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))","","","# Quick-start development settings - unsuitable for production","# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/","","# SECURITY WARNING: keep the secret key used in production secret!","SECRET_KEY = os.environ.get(\"SECRET_KEY\")","","# SECURITY WARNING: don't run with debug turned on in production!","DEBUG = True","","ALLOWED_HOSTS = [os.environ.get(\"C9_HOSTNAME\"), '127.0.0.1']","","","# Application definition","","INSTALLED_APPS = [","    'django.contrib.admin',","    'django.contrib.auth',","    'django.contrib.contenttypes',","    'django.contrib.sessions',","    'django.contrib.messages',","    'django.contrib.staticfiles',","    'django_forms_bootstrap',","    'posts',","]","","MIDDLEWARE = [","    'django.middleware.security.SecurityMiddleware',","    'django.contrib.sessions.middleware.SessionMiddleware',","    'django.middleware.common.CommonMiddleware',","    'django.middleware.csrf.CsrfViewMiddleware',","    'django.contrib.auth.middleware.AuthenticationMiddleware',","    'django.contrib.messages.middleware.MessageMiddleware',","    'django.middleware.clickjacking.XFrameOptionsMiddleware',","]","","ROOT_URLCONF = 'blog.urls'","","TEMPLATES = [","    {","        'BACKEND': 'django.template.backends.django.DjangoTemplates',","        'DIRS': [os.path.join(BASE_DIR, 'templates')],","        'APP_DIRS': True,","        'OPTIONS': {","            'context_processors': [","                'django.template.context_processors.debug',","                'django.template.context_processors.request',","                'django.contrib.auth.context_processors.auth',","                'django.contrib.messages.context_processors.messages',","                'django.template.context_processors.media',","            ],","        },","    },","]","","WSGI_APPLICATION = 'blog.wsgi.application'","","","# Database","# https://docs.djangoproject.com/en/1.11/ref/settings/#databases","","# DATABASES = {","#     'default': {","#         'ENGINE': 'django.db.backends.sqlite3',","#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","#     }","# }","","DATABASES = {","    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))","}","","","# Password validation","# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators","","AUTH_PASSWORD_VALIDATORS = [","    {","        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',","    },","    {","        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',","    },","    {","        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',","    },","    {","        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',","    },","]","","","# Internationalization","# https://docs.djangoproject.com/en/1.11/topics/i18n/","","LANGUAGE_CODE = 'en-us'","","TIME_ZONE = 'UTC'","","USE_I18N = True","","USE_L10N = True","","USE_TZ = True","","","# Static files (CSS, JavaScript, Images)","# https://docs.djangoproject.com/en/1.11/howto/static-files/","","STATIC_URL = '/static/'","STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )","","MEDIA_URL = '/media/'","MEDIA_ROOT = os.path.join(BASE_DIR, 'media')"]}],[{"start":{"row":28,"column":17},"end":{"row":28,"column":59},"action":"remove","lines":["os.environ.get(\"C9_HOSTNAME\"), '127.0.0.1'"],"id":14},{"start":{"row":28,"column":17},"end":{"row":28,"column":86},"action":"insert","lines":["'f4c2fc80d4c041518d69eb35a1451b26.vfs.cloud9.us-east-1.amazonaws.com'"]}],[{"start":{"row":28,"column":17},"end":{"row":28,"column":86},"action":"remove","lines":["'f4c2fc80d4c041518d69eb35a1451b26.vfs.cloud9.us-east-1.amazonaws.com'"],"id":15},{"start":{"row":28,"column":17},"end":{"row":28,"column":86},"action":"insert","lines":["'21b2b37a52d445e7bac0ff6fd2159d90.vfs.cloud9.us-east-1.amazonaws.com'"]}],[{"start":{"row":0,"column":0},"end":{"row":131,"column":44},"action":"remove","lines":["\"\"\"","Django settings for blog project.","Generated by 'django-admin startproject' using Django 1.11.15.","For more information on this file, see","https://docs.djangoproject.com/en/1.11/topics/settings/","For the full list of settings and their values, see","https://docs.djangoproject.com/en/1.11/ref/settings/","\"\"\"","","import os","import dj_database_url","","if os.path.exists('env.py'):","    import env","","# Build paths inside the project like this: os.path.join(BASE_DIR, ...)","BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))","","","# Quick-start development settings - unsuitable for production","# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/","","# SECURITY WARNING: keep the secret key used in production secret!","SECRET_KEY = os.environ.get(\"SECRET_KEY\")","","# SECURITY WARNING: don't run with debug turned on in production!","DEBUG = True","","ALLOWED_HOSTS = ['21b2b37a52d445e7bac0ff6fd2159d90.vfs.cloud9.us-east-1.amazonaws.com']","","","# Application definition","","INSTALLED_APPS = [","    'django.contrib.admin',","    'django.contrib.auth',","    'django.contrib.contenttypes',","    'django.contrib.sessions',","    'django.contrib.messages',","    'django.contrib.staticfiles',","    'django_forms_bootstrap',","    'posts',","]","","MIDDLEWARE = [","    'django.middleware.security.SecurityMiddleware',","    'django.contrib.sessions.middleware.SessionMiddleware',","    'django.middleware.common.CommonMiddleware',","    'django.middleware.csrf.CsrfViewMiddleware',","    'django.contrib.auth.middleware.AuthenticationMiddleware',","    'django.contrib.messages.middleware.MessageMiddleware',","    'django.middleware.clickjacking.XFrameOptionsMiddleware',","]","","ROOT_URLCONF = 'blog.urls'","","TEMPLATES = [","    {","        'BACKEND': 'django.template.backends.django.DjangoTemplates',","        'DIRS': [os.path.join(BASE_DIR, 'templates')],","        'APP_DIRS': True,","        'OPTIONS': {","            'context_processors': [","                'django.template.context_processors.debug',","                'django.template.context_processors.request',","                'django.contrib.auth.context_processors.auth',","                'django.contrib.messages.context_processors.messages',","                'django.template.context_processors.media',","            ],","        },","    },","]","","WSGI_APPLICATION = 'blog.wsgi.application'","","","# Database","# https://docs.djangoproject.com/en/1.11/ref/settings/#databases","","# DATABASES = {","#     'default': {","#         'ENGINE': 'django.db.backends.sqlite3',","#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","#     }","# }","","DATABASES = {","    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))","}","","","# Password validation","# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators","","AUTH_PASSWORD_VALIDATORS = [","    {","        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',","    },","    {","        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',","    },","    {","        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',","    },","    {","        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',","    },","]","","","# Internationalization","# https://docs.djangoproject.com/en/1.11/topics/i18n/","","LANGUAGE_CODE = 'en-us'","","TIME_ZONE = 'UTC'","","USE_I18N = True","","USE_L10N = True","","USE_TZ = True","","","# Static files (CSS, JavaScript, Images)","# https://docs.djangoproject.com/en/1.11/howto/static-files/","","STATIC_URL = '/static/'","STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )","","MEDIA_URL = '/media/'","MEDIA_ROOT = os.path.join(BASE_DIR, 'media')"],"id":16},{"start":{"row":0,"column":0},"end":{"row":135,"column":44},"action":"insert","lines":["\"\"\"","Django settings for blog project.","Generated by 'django-admin startproject' using Django 1.11.15.","For more information on this file, see","https://docs.djangoproject.com/en/1.11/topics/settings/","For the full list of settings and their values, see","https://docs.djangoproject.com/en/1.11/ref/settings/","\"\"\"","","import os","import dj_database_url","","if os.path.exists('env.py'):","    import env","","# Build paths inside the project like this: os.path.join(BASE_DIR, ...)","BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))","","","# Quick-start development settings - unsuitable for production","# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/","","# SECURITY WARNING: keep the secret key used in production secret!","SECRET_KEY = os.environ.get(\"SECRET_KEY\")","","# SECURITY WARNING: don't run with debug turned on in production!","DEBUG = True","","ALLOWED_HOSTS = [os.environ.get(\"C9_HOSTNAME\"), '127.0.0.1', 'blog-test-app.herokuapp.com']","","","# Application definition","","INSTALLED_APPS = [","    'django.contrib.admin',","    'django.contrib.auth',","    'django.contrib.contenttypes',","    'django.contrib.sessions',","    'django.contrib.messages',","    'django.contrib.staticfiles',","    'django_forms_bootstrap',","    'posts',","]","","MIDDLEWARE = [","    'django.middleware.security.SecurityMiddleware',","    'django.contrib.sessions.middleware.SessionMiddleware',","    'django.middleware.common.CommonMiddleware',","    'django.middleware.csrf.CsrfViewMiddleware',","    'django.contrib.auth.middleware.AuthenticationMiddleware',","    'django.contrib.messages.middleware.MessageMiddleware',","    'django.middleware.clickjacking.XFrameOptionsMiddleware',","    'whitenoise.middleware.WhiteNoiseMiddleware',","]","","ROOT_URLCONF = 'blog.urls'","","TEMPLATES = [","    {","        'BACKEND': 'django.template.backends.django.DjangoTemplates',","        'DIRS': [os.path.join(BASE_DIR, 'templates')],","        'APP_DIRS': True,","        'OPTIONS': {","            'context_processors': [","                'django.template.context_processors.debug',","                'django.template.context_processors.request',","                'django.contrib.auth.context_processors.auth',","                'django.contrib.messages.context_processors.messages',","                'django.template.context_processors.media',","            ],","        },","    },","]","","WSGI_APPLICATION = 'blog.wsgi.application'","","","# Database","# https://docs.djangoproject.com/en/1.11/ref/settings/#databases","","if \"DATABASE_URL\" in os.environ:","    DATABASES = {","        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))","    }","else:","    print(\"Postgres URL not found, using sqlite instead\")","    DATABASES = {","        'default': {","            'ENGINE': 'django.db.backends.sqlite3',","            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","        }","    }","","","# Password validation","# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators","","AUTH_PASSWORD_VALIDATORS = [","    {","        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',","    },","    {","        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',","    },","    {","        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',","    },","    {","        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',","    },","]","","","# Internationalization","# https://docs.djangoproject.com/en/1.11/topics/i18n/","","LANGUAGE_CODE = 'en-us'","","TIME_ZONE = 'UTC'","","USE_I18N = True","","USE_L10N = True","","USE_TZ = True","","","# Static files (CSS, JavaScript, Images)","# https://docs.djangoproject.com/en/1.11/howto/static-files/","","STATIC_URL = '/static/'","STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )","STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')","","MEDIA_URL = '/media/'","MEDIA_ROOT = os.path.join(BASE_DIR, 'media')"]}],[{"start":{"row":28,"column":17},"end":{"row":28,"column":46},"action":"remove","lines":["os.environ.get(\"C9_HOSTNAME\")"],"id":17},{"start":{"row":28,"column":17},"end":{"row":28,"column":86},"action":"insert","lines":["'f4c2fc80d4c041518d69eb35a1451b26.vfs.cloud9.us-east-1.amazonaws.com'"]}],[{"start":{"row":28,"column":102},"end":{"row":28,"column":115},"action":"remove","lines":["blog-test-app"],"id":18},{"start":{"row":28,"column":102},"end":{"row":28,"column":117},"action":"insert","lines":["blog-tastic-app"]}],[{"start":{"row":28,"column":101},"end":{"row":28,"column":132},"action":"remove","lines":["'blog-tastic-app.herokuapp.com'"],"id":21},{"start":{"row":28,"column":101},"end":{"row":28,"column":130},"action":"insert","lines":["blog-tastic-app.herokuapp.com"]}],[{"start":{"row":28,"column":130},"end":{"row":28,"column":131},"action":"insert","lines":["'"],"id":22}],[{"start":{"row":28,"column":101},"end":{"row":28,"column":102},"action":"insert","lines":["'"],"id":23}]]},"ace":{"folds":[],"scrolltop":600,"scrollleft":0,"selection":{"start":{"row":28,"column":102},"end":{"row":28,"column":102},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1563782463525,"hash":"a45a13e44143be933c0d1bb442b7fdd91aa414b4"}