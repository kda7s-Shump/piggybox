"""
ASGI config for mysite project.

これはASGI呼び出し可能なものを ``application``というモジュールレベルの変数として公開しています。

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_asgi_application()
