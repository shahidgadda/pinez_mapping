"""
WSGI config for products project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys
import site

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "products.settings")
SITE_ROOT = os.path.dirname(os.path.dirname( __file__ ))

application = get_wsgi_application()

