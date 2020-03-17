Environment File
================

``Pytonik``  environment file contains properties with argument. It is the first step that needs to be taken
to setup file and make sure it is configured properly. It handles all ``pytonik`` application settings that
will be used to developed web application and the environment file is saved as ``.env``

``Pytonik`` framework cannot run or function without setting all necessary environment file argument requirement.

**.env Properties :**

•	route
•	dbConnect
•	languages
•	SMTP
•	error


route
-----

route set all default method for reused purposes, either to pass on parameters or revoking controller, below is the illustration.
We'll be using ``ContactController.py``  and ``BlogController.py`` for the demonstrations.

.. code-block:: python

    'route':
            {
            'edit': 'ContactController@edit',

           'blog': 'blogController@read:id:para',

            }




**How to defined route:**

Custom ``'edit': 'ContactController@edit'`` edit is function in ``ContactController.py`` Controller.

Checkout the result here, now we will be having:-  ``http://example.com/edit`` instead of ``http://example.com/contact/edit``


Pass parameter  ``'blog': 'blogController@read:id:para'`` Where ``id`` and ``para`` is an argument and ``read`` is a function in `` BlogController.py`` Controller.
Check the result out here, now we will be having:- ``http://example.com/blogs/1/tea`` instead of ``http://example.com/blog/read/id/1/para/tea``


dbConnect
---------

dbConnect sets all Database connection parameters. To configure pytonik to work with MYSQL database, parameters are required
to enable database to function probably.

**MYSQL**

.. code-block:: python

    'dbConnect':
             {
                  'host': 'localhost',

                  'database': 'pytonik-database',

                  'prefix': 'prefix_',

                  'password': 'database-password',

                  'username': 'database-username',

                  'port': 'database-port',

                  'driver': 'MYSQL'
             }



**Oracle**


.. code-block:: python

    'dbConnect':
             {
                  'host': 'localhost',

                  'database': 'pytonik-database',

                  'prefix': 'prefix_',

                  'password': 'database-password',

                  'username': 'database-username',

                  'port': 'database-port',

                  'driver': 'Oracle'
             }



**pyPgSQL**

.. code-block:: python

    'dbConnect':
             {
                  'host': 'localhost',

                  'database': 'pytonik-database',

                  'prefix': 'prefix_',

                  'password': 'database-password',

                  'username': 'database-username',

                  'port': 'database-port',

                  'driver': 'pyPgSQL'

             }




**SQLite**

.. code-block:: python

    'dbConnect':
             {
            'path': 'folderDB',

            'prefix': 'prefix_',

            'name': 'databasefile.db'

            'driver': 'SQLite'
             }

** Note: ** pytonik driver supports only ``SQLite``, `` MYSQL``, ``Oracle`` and ``PostgreSQL`` Database


Languages
---------

`` Pytonik `` supports internationalize, all languages files are store in lang folder,
to enable web application to run multiple language translations, environment file needs to be configured
with all necessary argument, below used English as ``en`` , French as ``fr`` and Russian as ``ru``.
The language file is saved as ``.py``

Example: ``en.py``,  ``fr.py`` , ``ru.py``

.. code-block:: python

    'languages':
    {
       'en': 'en',
       'fr': 'fr',
       'ru': 'ru',
    }


Note: Our web application will be using English as the default language which is en. defined as follow
``'default_languages':'en'``

SMTP
----

To enable application to send mails to or fro, pytonik framework requires `` SMTP `` setting as follows.

.. code-block:: python

    'SMTP':
    {
        'server':   'test@server.com',
        'port':     '25',
        'username': 'test@example.com',
        'password': 'testpassword',
    }


**Note:** Web application that requires sending of electronic mails, above setting is compulsory.

error
-----

pytonik provides support for error page handling to avoid showing of errors, programing bug or codes to the audience,
it handles error such as:- method not found / error in method **400**,  page not found **404** and controller not found **405**.


.. code-block:: python

    'error':
    {
        '400':   'custom/error400',
        '404':     'custom/error404',
        '405': 'custom/error405',
    }



Default
-------

We will look at how to define all default properties as such routes , controllers , actions and languages.
Below are examples and you can as well set yours differently.

.. code-block:: python

    'default_controllers' :'index',
    'default_actions': 'index',
    'default_routes' : 'index',
    'default_languages': 'en'


Why ``default_controllers`` are set to  ``index`` means that the application depends on IndexController, let say your index page is being pointed to IndexController.

Why ``default_actions`` are set to ``index`` means all default methods are set to index respective of the controller.

Why ``default_routes`` are set to ``index`` means application points to IndexController.

Why ``default_languages`` set to ``en`` means application is using  en.py language file by default for internationalization.




