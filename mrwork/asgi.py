"""
ASGI config for mrwork project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from mangum import Mangum
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mrwork.settings")

application = get_asgi_application()
handler = Mangum(application, lifespan="off")
