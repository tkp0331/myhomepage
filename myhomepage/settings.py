from .settings_common import *
import os

DEBUG = False  # NOTE: 本番環境では必ずFalse

# 許可するホスト名のリスト
ALLOWED_HOSTS = [os.environ.get("ALLOWED_HOSTS")]

# 静的ファイルを配置する場所
STATIC_ROOT = "/usr/share/nginx/html/static"
MEDIA_ROOT = "/usr/share/nginx/html/media"

STATIC_URL = '/static/'

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,

    "loggers": {

        # Djangoが利用するロガー
        "django": {
            "handlers": ["file"],
            'level': 'INFO',  # INFO以上の深刻度のログだけを扱う
        },

        # homepageアプリケーションが利用するロガー
        "homepage": {
            "handlers": ["file"],
            "level": "INFO",  # INFO以上の深刻度のログだけを扱う
        },
    },

    # ハンドラの設定
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": os.path.join(BASE_DIR, "logs/django.log"),
            "formatter": "formatter1",
            "when": "D",  # ログローテーションの間隔の単位を指定
            "interval": 1,  # 何単位分でファイルを切り替えるか指定
            "backupCount": 7,  # 保存しておくログファイル数を指定
        },
    },

    # フォーマッタの設定
    "formatters": {
        "formatter1": {
            "format": "\t".join([
                "%(asctime)s",
                "[%(levelname)s]",
                "%(pathname)s(Line:%(lineno)d)",
                "%(message)s"
            ])
        }
    }
}
