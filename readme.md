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