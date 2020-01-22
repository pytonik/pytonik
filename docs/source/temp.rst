Template Engine
===============


Pytonik provides flexible templating engine, making use of ``blocks``, ``Variables`` , ``Loops``, ``conditionals statement`` , ``operators`` , ``iteration`` and ``scopes``.


.. code-block:: python

    from pytonik.App import App
    app = App()

    items = [
            dict(name="dog", age=5),
            dict(name="cat", age=2),
            dict(name="snake", age=26),

        ]

    data = {
        'items': items,
        'my_var':  "Welcome to Pytonik",
        'my_var_2': "Nothing",
        'status': "active",
        'num': 1,

        }


    app.views('index', data)



Variables
---------

.. code-block:: python

    <div>{{my_var}}</div>


 
**Block**


Type of block if, each and call.

Loops
-----

**loop** with dictionary or json

.. code-block:: python

    {% each items %}
        <div>{{it.name}}  {{it.age}}</div>
    {% endeach %}


loop with ``list``

.. code-block:: python

    {% each [1,2,3] %}
        <div>{{it}}</div>
    {% endeach %}



Loop items has iteration with a scope, to access attributes which is a parent context or outer variable use ``..``


.. code-block:: python

    {% each items %}
        <div>{{..status}}</div><div>{{it.name}}  {{it.age}}</div>
    {% endeach %}




Conditionals
------------

Supported operators are: ``>``, ``>=``, ``<``, ``<=``, ``==``, ``!=``. You can also use conditionals with things that evaluate to truth.
``if`` conditional statement

.. code-block:: python

    {% if num %}
        {{my_var}}
    {% endif %}


if conditional statement with **else**

.. code-block:: python

    {% if num %}
        {{my_var}}
    {% else %}
        {{my_var_2}}

    {% endif %}



if conditional statement with operator


.. code-block:: python

    {% if num == 0 %}

        {{my_var}}

    {% endif %}





Callable
--------

call block, get or passed positional or keyword arguments or parameter.
url is class and path is method


.. code-block:: python

    {% call url 'path' %}


url is class and url is method while ``path=''`` is keyword arguments or parameter

.. code-block:: python

    {% call url 'url' path='' %}


