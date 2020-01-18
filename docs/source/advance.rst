Advance
=======

We have lot of features to look into if we really want to achieve more using **pytonik**, I will choose to be a web
developer and I want to be very good in web development, but before I can become more better,
I need to know how to go about using all the modules provided by **pytonik**.
Knowing how to used will not make me better but limited. I think I need to improved and break my limit but now
how can I break my limit. The best way to do so, is to know how to create my own custom  ``model`` and ``controller``.
Great, I believe I can now start developing scalable web application.


Model
-----

Model, is breaking application into parts, in which each part as it model and can as well relate to another part.
Let say we have a model that is called ``Users``, and  ``Result``, these models are closely related, each model
cannot do without other. We will like to talk more about how to work with model but making a real
live example will explain better.  Model are created and saved into ``model`` folder. We will need to import Model and
inherit Model properties into our newly created model. below example will explained better.


**Example:** Users.py

.. code-block:: python

	from pytonik.Model import Model

	class Users(Model):

		def __getattr__(self, item):
			return item

		def __init__(self):
			return None

		def get(self, userid=""):
			returns "user"

		def list(self):
			return "all user"

		def delete(self, id=""):
			if id is not "":
				return "delete user with id"
			else:
				return "delete  all user"



 

**Example 1.0:** Result.py

.. code-block:: python

	from pytonik.Model import Model

	class Result(Model):

		def __getattr__(self, item):
			return item

		def __init__(self):
			return None

		def get(self, userid=""):
			return "user result"

		def list(self):
			return "all result"

		def deletebyuser(self, userid="", id=""):
			if userid is not "" and id is not "":
				return "delete user result that as id"
			else:
				return "delete user result"

		def delete(self, id=""):
			if id is not "":
				return "delete  result with id"
			else:
				return "delete  all result"



I will like to know more, at this stage I found the example very interesting, now that I have learnt how to create model,
feel I am still missing out, because I need to learn how to implement database query. ``Pytonik`` has an hand build **schema**
that will handle all database features. In our case we will use **Schema** ``method`` and ``attribute``, this module was design to enhance database structuring.
Since we are using Model Module we should be comfortable using database properties without ``calling`` or
``importing`` another module. if you have not learn more about **pytonik** ``Schema``,
I prefer you should to read more about how to use it because you will need it in the future if not now.


**Example 1.1:** Result.py

.. code-block:: python


    from pytonik.Model import Model

    class Result(Model):

       def __getattr__(self, item):
            return item

       def __init__(self):
            self.result = self.table('result')
            return None

       def get(self, userid=""):
           query= self.result.where('users_id','=',userid).select().get()
           return query.rowCount, query.result

       def list(self):
           query= self.result.select().get()
           return query.rowCount, query.result


       def deletbyuser(self, userid="", id=""):
            if userid is not " and id is not “”:
                query = self.result.where('users_id','=',userid).and ('result_id' '=', id).delete()
                return query
            else:
                query = self.result.where('users_id','=',userid).delete()
                return query

      def delete(self, id=""):
            if id is not "":
                query = self.result.where('result_id','=',id).delete()
                return query
            else:
                query = self.result.delete()
                return query




Controller
----------

**Controller**  is the heart of the application, it is the most important part of application and can function without
the help of model, but the ``model`` cannot function without ``controller``. The controller handles the result and send action in and out
of the application. Controller controls and send data to the browser using the help of  ``view``  which is a method in ``App`` module.
All controller files are stored in ``controller`` folder and are saved/stored in Capitalized form example ``UsersController.py``.
if file is saved ``userscontroller.py`` or ``Userscontroller.py`` are not accepted and will definitely lead to exception.

**Example:** UsersController.py

The illustration shows how to create controller and implement ``views`` module, which is one of the property of ``App`` module,
as you can see we are sending data ``user.html`` which is stored in our ``views`` folder in our **project directory**.

.. code-block:: python

    from pytonik.App import App
    
    mvc = App()
    
    def index():
    
    data = {
    'title': "pytonik MVC",
    'label': "List Pytonik Users”
    
    }
    mvc.views('user', data)



**Example:** user.html

Here we can see that we are  can display variable in ``user.html`` sent from ``UsersController.py``

.. code-block:: python

    <html>
    
    <head>
    <title>{{title}}</title>
    </head>
    
    <body>
    
        <h1>{{label}}</h1>
    
    </body>
    
    </html>





**How to load ``model`` in ``controller``**

**Example 1.0:** load model ``Users.py`` into controller ``UsersController.py``

once ``Users`` model load into ``UsersController`` it gives Controller access to all the methods and attribute in Users model.
we can call each of the method defined in ``Users``

.. code-block:: python

    from pytonik.App import App
    from pytonik.Model import Model

    mvc = App()
    users = Model.Load('Users')

    def index():

    data = {
    'title': "pytonik MVC",
    'label': "List Pytonik Users”

    }
    mvc.views('user', data)


.. note::

    if we keep importing module each time we want to make use of them,
    then we will write a huge lines of codes which is not what we want.
    pytonik has a module called ``Web``,
    it gives access to bunch of modules, so we will not have to be importing module into our controller.
    below example will explain.


**Example 1.1:** load model ``Users.py`` into controller ``UsersController.py`` .
``load`` is a method in ``Model`` module

.. code-block:: python

    from pytonik import Web

    mvc = Web.App()
    users = Web.Load('Users')

    def index():

    data = {
    'title': "pytonik MVC",
    'label': "List Pytonik Users”

    }
    mvc.views('user', data)

.. note::

    ``App`` Module has three important methods ``header`` is called when displaying strings or characters, ``redirect``  from initial page to the preferred page. ``referer`` from initial to the previous page.
    
 ``header`` method has ``type`` argument with default value ``text/html``.

Example:

.. code-block:: python

    from pytonik import Web
    mvc = Web.App()

    def index():

        mvc.header()
        
        print("i love pytonik")
        

``redirect`` method has ``location`` argument with default value ``/``. 

Example 1.0:

.. code-block:: python

    from pytonik import Web
    mvc = Web.App()

    def index():
        mvc.redirect('/login')
                
Example 1.1: Using ``url`` function together with ``redirect`` method

.. code-block:: python

    from pytonik import Web
    mvc = Web.App()

    def index():
        
        mvc.redirect(Web.url('/login'))
                                
                                
                                
``referer`` method has ``location`` argument with default value ``/``.

Example 1.0:

.. code-block:: python

    from pytonik import Web
    mvc = Web.App()

    def index():
        mvc.referer()
                                
.. note::

    Cases where referer page does not exist, set an alternative location ``referer('home')``. Let say previous page is not found, web have to provide the page. This means where are directing to **home** page

Example 1.1: Using ``url`` function together with ``referer`` method

.. code-block:: python

    from pytonik import Web
    mvc = Web.App()
    
    def index():
            
        mvc.referer(Web.url('/home'))
                                    
             