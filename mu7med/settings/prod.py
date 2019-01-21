from .base import *
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = False
ADMINS = (
    ('Mohamed Youssef', 'mu7med.youssef@gmail.com'),
)
ALLOWED_HOSTS = ['mu7med.herokuapp.com']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
