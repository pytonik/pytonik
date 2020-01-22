File
====

File upload properties consist of **upload**, **delete**, **ext**, **rename**, **Image**. This process requires installation **PIL** module.
``pip install Pillow``



**import Module**

.. code-block:: python

    from pytonik.Core.File import File


**Callable**


.. code-block:: python

    file = File()


**How to :**

•	get file extension
•	check file extension
•	upload file
•	get file size
•	check file size
•	upload and resize IMAGE


**Get file extension**

.. code-block:: python

    ext = file.ext(filename)


**Check file extension**


.. code-block:: python

    list_ext = ['png', 'jpg', 'JPG', 'jpeg']
    ext = file.ext(filename)

    if ext in list_ext:
        print("This file is valid")
    else:
        print("This file is not valid")






**Upload file**

.. code-block:: python

    file.upload(thefile, directory, rename)



IMAGE
-----

**get file size**


.. code-block:: python

    size = file.Image(directory, thefile).size()



**Check file size**


.. code-block:: python

    custom_size = 1024 * 1024 * 2  * 2MB File Size


    size = file.Image(directory, thefile).size()

    if custom_size >= size:
        print("Pass File size test")
    else:
        print("File Size is greater than its custom size")



**Upload and resize**


.. code-block:: python

    image = file.Image(directory, thefile)

    dimension = {64: 64, 128: 128}

    for w, h in dimension.items():
        image.resize(w, h)



**upload, resize and remain IMAGE - python 2 below**


.. code-block:: python

    image = file.Image(directory, thefile)

    dimension = {64: 64, 128: 128}

    rename = "Enter the new name of the file"

    for w, h in dimension.iteritems():
        image.resize(w, h rename)



**upload, resize and remain IMAGE - python 3 above**


.. code-block:: python

    image = file.Image(directory, thefile)

    dimension = {64: 64, 128: 128}

    rename = "Enter the new name of the file"

    for w, h in dimension.items():
        image.resize(w, h rename)
