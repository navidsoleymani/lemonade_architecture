# Lemonade Architecture

This architecture is based on a combination of standard architectures and conventions that have been used experimentally
over the years specifically for the use of Django, and can be a solution to reduce the hassle of using it in large
projects...

> [!NOTE]
> Next, an example will be added to the project so that definitions and conventions are also available as examples.

## Start Project

In Django projects, it is a good idea to place configuration files in a directory called "config" at the very beginning.

```

└── project
    └── config
        ├── __init__.py
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        ├── wsgi.py
        └── README.md
```

Next, the following files must be added to the root of the project.

```

└── project
    ├── dockerfile  
    ├── localepaths  
    ├── mediaroot  
    ├── staticfilesdirs  
    ├── config        
    ├── staticroot       
    ├── venv
    ├── views
    ├── CHANGELOG.md  
    ├── README.md     
    ├── requirements.txt  
    ├── manage.py    
    ├── dockercompose.yml  
    ├── SAMPLEENV.txt    
    ├── templates
    ├── sampleapp  
    ├── .env
    └── .gitignore
```

Based on the names of each of the directories and files above, we can understand the meanings and reasons for their
existence. Therefore, we will only talk about concepts that raise questions about their existence.

### App

There may be parts to each project, while each project represents a specific concept of a set of operations that
ultimately make up the entire project.

> [!IMPORTANT]  
> Note that each app in the project should be designed in such a way that it does not have any direct connection to
> other
> apps.

> [!NOTE]
> Communication between apps or apps with outside the app is done through interfaces and IDs in databases.

> [!NOTE]
> Every app should be designed in such a way that its absence does not affect the entire project.

Next, we will discuss the files that are inside each application.

```

└── project
    └── sampleapp
        ├── __init__.py  
        ├── imports  
        ├── interfaces  
        ├── migrations  
        ├── serializers  
        ├── utils
        ├── admin_repo
        ├── models_repo
        ├── apps.py  
        ├── admin.py  
        ├── models.py
        ├── definitions.py
        └── README.md
        
```

#### imports

Try to import settings or classes that may change during the project into this section, and also provide facilities to
easily change these settings from outside the app.

#### interfaces

In this directory, try to store any logic that you may need outside the app as classes in this section so that logic
from this section can be used in other apps in the app.

#### serializer

Try to create a serializer for all data inputs and outputs in the application.

#### utils

Try to place the tool you need in this section so that it can be used without having to leave the app.

#### admin_repo & models_repo

Try to use these directories in apps where you have a large number of tabs to make your source code more readable.

#### definitions

For greater readability and to try to prevent typos, try to consolidate in-app definitions into one file.

### views

This directory is actually a forum for building project endpoints and using and combining different interfaces in
different apps to create APIs.

Next, we will look at the structure of this directory.

```python
└── project
    └── views
        ├── __init__.py  
        ├── versions
        |   ├── __init__.py  
        |   ├── v1
        |   |   ├── __init__.py
        |   |   ├── apis_repo
        |   |   ├── urls_repo  
        |   |   ├── apis.py
        |   |   ├── urls.py
        |   |   └── README.md
        |   └── README.md
        ├── urls.py
        └── README.md
```

In this directory, we separate different versions of endpoints. Within each version directory, we list the APIs and
endpoints so that each can be easily accessed.

## Object Oriented

Let's try to use complete object-oriented design in the development process and do this optimally and completely.

## DB

In database designs, we should try to be as careful in the design as possible and observe indexing in introducing
database models.
Avoid using additional flags as much as possible.
Avoid using unnecessary relations.
Avoid defining additional logic in models as much as possible and create logic in the service or interface layer.

## Naming

Use standard naming rules and try to follow them throughout the code if you use any rules.

## PEP8

Use standard naming rules and try to follow them throughout the code if you use any rules.

## Endpoint

Let's try to follow standard methods when naming our endpoints.

## Response

Let's try to create a specific structure for our responses and adhere to this structure in all respects. Let's try to
publish the correct status codes.

## Apis

When creating APIs, try to validate requests and use the correct request methods.

## Cache

Let's try to use cache correctly from the very beginning.