# pytonik

[![Build Status](https://img.shields.io/pypi/v/pytonik)](https://pypi.python.org/pypi/pytonik)
[![Downloads](https://img.shields.io/pypi/dm/pytonik)](https://pypi.python.org/pypi/pytonik/)
[![Wheel](https://img.shields.io/pypi/wheel/pytonik.svg)](https://pypi.python.org/pypi/pytonik)
[![Python Version](https://img.shields.io/pypi/pyversions/pytonik)](https://pypi.python.org/pypi/pytonik)
[![License](https://img.shields.io/pypi/l/pytonik)](https://pypi.python.org/pypi/pytonik)
[![donate](https://img.shields.io/badge/donate-KoFi-blue.svg)](https://ko-fi.com/pytonik)

<p align="center">
  <img width="150" height="150" src="https://avatars3.githubusercontent.com/u/57829979?s=460&v=4">
</p>

Pytonik is a MVC(Model View Controller) framework built to enhance web development, it’s quick to set up. With Pytonik, you build more apps with less code. It runs on multiple operating systems including WINDOWS, MACOS, and LINUX.

[![Made with python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://pypi.python.org/pypi/pytonik)

## How to setup
If you are on a local machine, you will need to install a web server, either WAMP, XAMPP, LAMP or MAMP, depending on your particular environment.
After installing the server, enable CGI on your **httpd.conf** file as follows:

**Remove:-** Options Indexes FollowSymLinks and **Add:** Options Indexes FollowSymLinks ExecCGI

**Add:-** AddHandler cgi-script .cgi .py

```
<Directory "/var/www/cgi-bin">
    AllowOverride None
    Options ExecCGI
    Order allow, deny
    Allow from all
</Directory>
```


## How to Install

We strongly recommend that you to install this package using the Command Line.

```

$ pip install pytonik

```

In your application, you have to set the folder structure properly to be able to start your Pytonik application.

Below is a sample folder structure for a Pytonik application:

```

|─MyPytonikApp                            (application folder)
    |─ controller
        |─ IndexController.py
    |─ lang
        |─ en.py
    |─ model
    |─ public  
        |─ assets
        |- .htaccess
        |- index.py
    |─ views
        |─ 404.html
        |─ homepage.html
    |─ includes
        |─ header.html
    .env
    .htaccess


```

You can download the sample folder structure here [Folder-Structure](https://github.com/pytonik/Folder-Structure)

### How to get started

Once the folder structure is in place, create a file with name **.htaccess** in the root folder, open it and enter the following code block;

``` HTML
<IfModule mod_rewrite.c>
    RewriteEngine on
    RewriteRule ^$ public/
    RewriteRule (.*) public/$1 [NC,L]
    AddHandler cgi-script .cgi .py
    Options +ExecCGI
</IfModule>
````

Now, create a file with name **.env** in the root folder. To learn more about the **.env** file, please refer to [pytonik-env](https://github.com/pytonik/.env).

Inside the **.env** file, enter the following code block;

``` JSON
{
    "route": {
        "default": ""
    },
    "dbConnect": {
        "host": "localhost",
        "database": "pytonik-database",
        "password": "database-password",
        "username": "database-username",
        "port": "database-port",
        "driver": "MYSQLi"
    },
    "languages": {
       "en": "en",
       "fr": "fr",
       "ef": "ef",
    },
    "SMTP": {
        "server": "test@server.com",
        "port": 25,
        "username": "test@example.com",
        "password": "testpassword"
    },
    "default_action": "index",
    "default_controller": "index",
    "default_route": "index",
    "default_language": "en"
}

```

Create a folder with name **public** in the root of your application (if you haven't already), and inside the folder, create a file with name **index.py**.

Open the new **index.py** file and enter the following code segment.

``` Python
#!/usr/local/bin/python

try:
    from pytonik import Web
except Exception as err:
    exit(err)

App = Web.App()
App.runs()
```

Inside **public** folder, create another file with name **.htaccess**, open it and enter the following code block.

``` HTML
<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteRule ^(.*)$ index.py/$1 [L]
</IfModule>
```

Inside **controller** folder, create a file with name **IndexController.py** (if you haven't already), this will serve as the default controller.

Inside **views** folder, create a file with name **homepage.html**. **views** folder is were all html template will reside.

Open **public/index.py** and enter the following code segment.

``` Python
from pytonik import Web
m = Web.App()
def index():
    data = {
        "title": "Home",
  
    }
    m.header()
    m.views('homepage', data)
```

Wooooow! The setup is complete. Congrats!.

You can accomplish any task with Pytonik.

Note: All Python files (.py extension) should have their permissions set to **755**.

## Learn more about Pytonik

Learn more about using  MYSQL [Helper](https://github.com/pytonik/pytonik_mysql_helper).

Learn more about using attribute tags and types [Template Engine](https://github.com/pytonik/pytonik_template_engine).

Learn more about using [Forms](https://github.com/pytonik/pytonik_form/).

Learn more about using [Session](https://github.com/pytonik/pytonik_sessions/).

Learn more about uploading [Files](https://github.com/pytonik/pytonik_file_upload).

Download sample application folder to quickly get up and running with Pytonik [SampleFolder](https://github.com/betacodings/SampleFolder).

## Contact

**Name:**  Pytonik MVC

**Email:** dev@pytonik.com
