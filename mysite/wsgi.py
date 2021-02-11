"""
WSGI config for mysite project.

これは、WSGI呼び出し可能なものを ``application``というモジュールレベルの変数として公開しています。

For more information on this file, see
https://docs.djangoproject.com/ja/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()
