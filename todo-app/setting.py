

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todo.apps.TodoConfig', 
]


PDB_NAME = config.get('appdb', 'NAME')
PDB_USER = config.get('appdb', 'USER')
PDB_PASSWORD = config.get('appdb', 'PASSWORD')
PDB_HOST = config.get('appdb', 'HOST')


DATABASES = {

    'default': {
        'CONN_MAX_AGE': 500,
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': PDB_NAME,
        'USER': PDB_USER,
        'PASSWORD': PDB_PASSWORD,
        'HOST': PDB_HOST,
        'PORT': '5432',
    },
}