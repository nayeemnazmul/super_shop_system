# Demo App

### How to run (1)
1. install docker
2. clone this repo
3. change directory to cloned repo
4. run in terminal - `docker build -t super_shop_system .`
   
you should see --

``` commandline
Step 1/18 : FROM python:3.8-buster
..................................
..................................
..................................
Successfully tagged super_shop_system:latest
```

5. 
```commandline
    docker run -it -p 8000:8000 \
     -e DJANGO_SUPERUSER_USERNAME=admin \
     -e DJANGO_SUPERUSER_PASSWORD=admin \
     -e DJANGO_SUPERUSER_EMAIL=admin@test.com \
     super_shop_system
```

you should see --

```commandline
Superuser created successfully.
[2021-06-22 13:28:59 +0000] [10] [INFO] Starting gunicorn 20.1.0
[2021-06-22 13:28:59 +0000] [10] [INFO] Listening at: http://0.0.0.0:8010 (10)
[2021-06-22 13:28:59 +0000] [10] [INFO] Using worker: sync
[2021-06-22 13:28:59 +0000] [17] [INFO] Booting worker with pid: 17
[2021-06-22 13:28:59 +0000] [18] [INFO] Booting worker with pid: 18
[2021-06-22 13:28:59 +0000] [19] [INFO] Booting worker with pid: 19
```

6. After you run this command, you should be able to visit `http://localhost:8000`
   and `http://localhost:8000/admin` in your browser to access the application.


### How to run (2nd way)
1. clone this repo
2. change directory to cloned repo
3. make virtual environment from python 3.8 and activate it
4. run in terminal - `pip install -r requirements.txt`
5. `python manage.py migrate`
6. `python manage.py collectstatic --no-input`
7. `python manage.py runserver`

you should see --

```commandline
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
June 22, 2021 - 20:00:00
Django version 3.2.4, using settings 'super_shop_system.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### Demo Screenshots

#### Products
![Product List](https://i.imgur.com/XkIXQvx.png "Product list")
#### Orders
![Order List](https://i.imgur.com/HlfVqpV.png "Order List")
#### Cart
![Cart](https://i.imgur.com/dwGKp79.png "Cart")
#### PDF Invoice with QRCode
![PDF Invoice with QRCode](https://i.imgur.com/dA9KfEy.png "PDF Invoice with QRCode")
