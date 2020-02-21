File Structure
==============

``Pytonik`` is a web framework that supports model view controller MVC, web development are made easier and
faster using the file structure below, it gives full access to ``controller``, ``model``, ``languages``, ``public``,  ``views`` , ``environment``.
Create folder in your web directory as follows:-  Type in ``pytonik-start`` on Terminal/command or you 'Link to download on github <https://github.com/pytonik/Folder-Structure>'


.. code-block:: python

    |─MyPytonikApp                            (application folder)
        |─ controller
            |─ IndexController.py
        |─ lang
            |─ en.py
        |─ model
            |─ Mymodel.py
        |─ public
            |─ Index.py
            |─ assets
            |─ uploads
            |- .htaccess
        |─ views
            |─ 404.html
            |─ homepage.html
        |- .env
        |- .htaccess





**Htacess:**

It’s a configuration file that support pytonik application to run on Apache Server,
this file is configured to set index and redirects application Uniform Resource Locator(URL) to public folder.

**Controller:**


It handles direct regulation of activities within the application, all component,
functions and interfacing depends on it.

**Lang:**


It handles internationalization translation of word or sentence within the application
and structured it conventionally.

**Model:**


It handles structuring each piece of function in the application, components and can be used by the controller or
called directly in view files

**Public:**


It handles asset files such as CSS, JS, images, uploads and access are set to audience

**Views:**

The result display sent from controller where the end user can see.


**Note:-** app.log file will be automatically created once pytonik is identified by the application project,
the file keeps track of errors and other useful information for bugs fixings.
