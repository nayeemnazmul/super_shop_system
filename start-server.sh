#!/usr/bin/env bash
# start-server.sh
#if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
#    (cd super_shop_system; python manage.py createsuperuser --no-input)
#fi
(gunicorn super_shop_system.wsgi:application --user www-data --bind 0.0.0.0:8010 --workers 3) &
nginx -g "daemon off;"