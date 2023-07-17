# flask-api-template
Flask API Template with Swagger Documentation

```
├── README.md
├── apis
│   ├── __init__.py // API Blueprint
│   └── user
│       ├── __init__.py // User API Collection Blueprint(Registered Under API Blueprint)
│       └── get_user_info.py
├── app.py
├── auth.py // API Auth(API-KEY)
└── docs
    ├── __init__.py // Doc Blueprint
    └── user
        ├── __init__.py // User API Namespace(Registered Under Doc Blueprint)
        └── get_user_info.py
```

