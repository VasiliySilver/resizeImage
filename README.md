# Resize Image Project
This app allows resize image with Django Project
![img.png](img.png)

## Installation:
> #### Local
1. git clone "https://github.com/VasiliySilver/resizeImage.git"
2. go to the project folder
3. run `sudo pip3 install -r requirements.txt`
4. run `python manage.py migrate`
5. then `python manage.py collectstatic`
6. then `python manage.py runserver`
7. for testing, create a superuser too.

> #### Remote
1. download docker
2. download docker-compose
3. once Docker and Docker Compose is installed, run the following command:
```
$ sudo docker-compose run web django-admin startproject composeexample 
```
4. Connect the database
> In this section, you set up the database connection for Django.
> 1. In this section, you set up the database connection for Django.
> 2. In your project directory, edit the `composeexample/settings.py` file.

> Replace the `DATABASES = ...` with the following:
```python
# settings.py
   
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}
```
5. Save and close the file.
6. Run the docker-compose up command from the top level directory for your project.
7. At this point, your Django app should be running at port 8000 on your Docker host. On Docker Desktop for Mac and Docker Desktop for Windows, go to http://localhost:8000 on a web browser to see the Django welcome page.
<br>

# Contact me:
- [Github](https://github.com/VasiliySilver)
- [Telegram](https://t.me/svaaugust)
- [Instagram](https://www.instagram.com/mr_is_nobody/)
- [Website](https://www.ogo-proger.ru)
