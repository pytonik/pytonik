Session
=======


``pytonik`` provide sessions to store data and recall them when needed. Session has property to ``set``, ``get``
and destroy data with in pytonik web framework.

**Import Module**

.. code-block:: python

    from pytonik.Session import Session



**Attributes of Request are :**

•	set
•	get
•	destroy


**set** initiate data storage over http with keyword argument, ``set(key, value="", duration, url, path)``

.. code-block:: python

    Session.set('key', 'value', 'duration')


get retrieve data storage http with keyword argument.

.. code-block:: python

    Session.get('key')

destroy all session over http

.. code-block:: python

    Session.destroy()

destroy session associated with a keyword

.. code-block:: python

    Session.destroy('name')

