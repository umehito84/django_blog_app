# 本番環境用設定
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('6rzyzoy+uduw71+gswzs2@7@$wx4jumg3x7riz=wod@^#(%pe+')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['', '.']