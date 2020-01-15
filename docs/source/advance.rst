Advance
=======

We have lot of features to look into if we really want to achieve more using pytonik, I will choose to be a web
developer and I want to be very good web development, but before I can become more better,
I need to know how to go about using all the modules provided by pytonik.
Knowing how to used will not still make me better. I think I need to improved and break my limit but now
how can I break my limit. The best way out is to know how to create my own custom  model and controller and
how to play around them. Great, I believe I can now start developing scalable web application.

Model
-----

Model is breaking application into parts, in which each part as it model and can as well relate to another part.
Let say we have a model that is called ``Users``, and  ``Result``, these tables are closely related, one each model
cannot do without each other. We will like to talk more about how to work with model but making a real
live example will explain better.  Model are created and saved into ``model`` folder. We will inherit Model module


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

		def deletbyuser(self, userid="", id=""):
			if userid is not "" and id is not "":
				return "delete user result that as id"
			else:
				return "delete user result"

		def delete(self, id=""):
			if id is not "":
				return "delete  result with id"
			else:
				return "delete  all result"



I will like to know more because at this stage I found this interesting, now that I have learnt how to create model,
feel I am still missing out, because I need to learn how to implement database query. Pytonik has hand build methods
that will handle all database features. In our case we will use Schema database attribute build to support only pytonik
developer. Since we are using Model Module we should be comfortable using database properties without calling or
importing another module. if you have not learn more about pytonik Database Schema but I will rather call it eloquence,
I prefer you should to read more about how to used it because you will so much need it in the future if not now.


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

Controller is the heart of the application, it is the most important part of application and can function without
the help of model, but the model cannot function without controller. It handle the result and send action in and out
of the application. Controller controls and send data to the browser using the help of view method.
All controller files are stored in``controller``folder and are saved in sentence case example ``UsersController.py``.
if file is saved ``userscontroller.py`` or ``Userscontroller.py`` are not accepted and will definitely lead to exception.

**Example:** UsersController.py

This illustrate how to create controller and implement views module, which is one of the property of App module,
as you can see we are sending data ``user.html`` which is stored in our ``views`` folder in our application directory

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

Here we can see that we are  can display variable in``user.html`` sent from ``UsersController.py``

.. code-block:: python

    <html>
    
    <head>
    <title>{{title}}</title>
    </head>
    
    <body>
    
        <h1>{{label}}</h1>
    
    </body>
    
    </html>





