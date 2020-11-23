from .settings_common import *
from .settings_secret import SECRET_KEY  # 賢くないが、上書きすればよい

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

LOGGING = {
    'version': 1,
    'disable_exsisting_loggers': False,

    'loggers': {
        # django用のロガー
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },

        # app「homepage」用のロガー
        'homepage': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },

    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # consoleへ出力するハンドラ
            'formatter': 'dev',
        },
    },

    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s',
            ])
        }
    }
}
