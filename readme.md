django Login API
----------------------------
Simple django Login rest API


Installing packages
----------------------------

pip install django-cors-headers
pip install asgiref
pip install Django
pip install django-cors-headers
pip install djangorestframework


Running API in local
----------------------------

python manage.py migrate

python manage.py runserver 


API URL
----------------------------
POST: http://localhost:8080/api/login

Sample request:

```
{
    "username": "Hexaware",
    "password": "hexawareuk"
}
```

ALLOW CROSS ORIGIN REQUESTS FROM UI:
------------------------------------

Configure the UI URL for accepting cross origin requests in the file:

Line no: 73:

```hexaapi/hexaapi/settings.py```


```
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",  # React app running on localhost
]
```

POSTMAN Test:
------------

![Screenshot](/postman-test.png)

![img.png](img.png)
