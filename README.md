## Rodolfo De Nadai

This is my system for my personal website.

If you want to see this project in use... go to http://www.rdenadai.com.br

You may use this project as you wish, but please, remove any information that may refer to me.

### Requirements:

Please, see the requirements.txt for dependencies.

This project uses Amazon S3 to record some information (like images), so change the settings.py.

Since this is a open source project the django SECRET_KEY is with some default key, 
please set your own. You can build from: http://www.miniwebtool.com/django-secret-key-generator/ 

### Running

You may run this project locally by executing the docker-compose command.

```bash
$> docker-compose up --build -d
```

In case you want to debug, please, change the environment MODE to development (see entrypoint.sh for info).

### Sitemap:

```bash
$> python manage.py shell
$> from django.contrib.sites.models import Site
$> new_site = Site.objects.create(domain='foo.com', name='foo.com')
$> print(new_site.id)
```




Thanks