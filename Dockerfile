# Dockerfile

FROM python:3.8-buster

# install nginx
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# install wkhtmltopdf
RUN apt-get install wkhtmltopdf -y --no-install-recommends

# copy source and install dependencies
RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
RUN mkdir -p /opt/app/super_shop_system
#COPY requirements.txt start-server.sh /opt/app/
#COPY /home/$(whoami)/.cache/pip /opt/app/pip_cache/
ADD . /opt/app/super_shop_system
WORKDIR /opt/app/super_shop_system
RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache
RUN python manage.py migrate
RUN python manage.py collectstatic --no-input
RUN chown -R www-data:www-data /opt/app
RUN chmod 755 start-server.sh

# start server
EXPOSE 8000
STOPSIGNAL SIGTERM
CMD ["/opt/app/super_shop_system/start-server.sh"]