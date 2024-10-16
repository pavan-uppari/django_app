# django_app
Building a Backend API for a Simple Inventory Management System using Django Rest Framework.

## Getting Started

1. Create a virtual environment
```shell
python -m venv env
```
2. Active virtual environment
```shell
source env/bin/activate
```
3. Install dependencies
```shell
pip install -r requirements.txt
```
4. Start server
```shell
python3 -m django runserver
```
5. Also start redis in your machine
```shell
redis-server
```

## Supported Endpoints

1. POST item/ - Create item with name and description
2. GET item/{item_id}/ - Get an item with a given item id
3. PUT item/{item_id}/ - Update an item with a given item id
4. DELETE item/{item_id}/ - Delete an item with a given item id
5. POST api/token/ - get access token and refresh token with django superuser username and password
6. POST api/token/refresh/ - get access token from refresh token

## Other Constraints
Item name cannot be duplicate
