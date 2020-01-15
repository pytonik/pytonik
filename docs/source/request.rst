Request
=======


Pytonik Request library contains form methods and attributes which comprises of ``POST`` , ``GET`` and ``PARAM``,
it outline how to use form to perform task such as Login, Registering, Posting, Updating, Requesting, Sending actions.


**Import Module**

.. code-block:: python

    from pytonik.Request import Request


**Attribute of Request are :-**

•	method
•	get
•	post
•	file
•	param


method Return ``` POST ``` and ``` GET ```


.. code-block:: python

    Request.method


get returns the value of ``GET`` request by obtaining the value using key attribute.

.. code-block:: python

    Request.get('name')

post returns the value of ``POST`` request by obtaining the value using key attribute.
.. code-block:: python

    Request.post('name')

get param returns the value of GET request by accessing the key attributes to obtain the value from either a
custom http query string ``https://test.com/id/2/name/dog/age/3``  or http request query
string ```https://test.com/?id=2&name=dog&age=3 ``` . which get attribute cannot perform such tasks

.. code-block:: python

    Request.param('id')

    Request.param('name')

    Request.param('age')



file returns POST request by accessing the key attributes to obtain the value for sent request from file fields.
Request.file('picture')

**Example:** using post attribute which will return POST
Demonstration form with html code

.. code-block:: python

    <form method="post" enctype="multipart/form-data">
    <input type="text"  name="id" value="" >
    <input type="text" name="name" value="" >
    <input type="text"  name="age" value="" >
    <input type="file"  name="picture" value="" >
    <button type="submit"  name="submit">Submit</button>
    </form>



Form actions is handle using the help of operators together with conditional statement to make it easy to check if fields are empty or not :- where ```is```    is the same as ```==``` and ```is not``` is the same as ``` !=```.
Notice that the form method is set to ``POST``

.. code-block:: python

    if Request.method == "POST":

        id = Request.post('id')
        name = Request.post('name')
        age = Request.post('age')

        picture = Request.file('picture')
        if id == "":
            print("ID is empty")
        elif name == "":
            print("NAME is empty")

        elif age == "":
            print("AGE is empty")

        elif file == "":
            print("PICTURE is empty")
        else:
            print("SUBMITTED successfully")


