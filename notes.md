generates a database dump
```shell script
python manage.py dumpdata <model> #admin catalog
```

load the database dump
```shell script
python manage.py loaddata core.json
```
------
Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table

------
- from django.urls import reverse --> get url by the name
- from django.urls import reverse_lazy --> same as reverse (usually used when the urls have not yet been loaded)

auth
admin/teste