gera um dump do banco de dados
```shell script
python manage.py dumpdata <model> #admin catalog
```

esse mesmo dump pode ser usado para carregar os dados
```shell script
python manage.py loaddata core.json
```
------
Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table

------
- from django.urls import reverse --> retorna a url baseada no name 
- from django.urls import reverse_lazy --> igual ao reverse, mas usado quando as urls ainda nao foram carregadas


auth
admin/teste