Configuration
=============

``Pytonik`` supports CGI and requires configuration to be able to run on Apache or any python
CGI enable environment.  The Configuration step support both local and cloud server.

Local Server
------------

Look into configuring``WAMP``,``XAMPP``,``LAMP``and``MAMP``,
if you are not using any of the listed local servers don’t worry, this process supports Apache,
both older and newer version, Although you might notice little difference between versions.

**Apache**

Locate httpd.conf in your local server open it with a text or code editor.

Find ``AddHandler cgi-script .cgi`` add .py  ``AddHandler cgi-script .cgi .py``.

Find ``Options None`` change to ``Options ExecCGI``
or find ``Options +Indexes`` change to ``Options ExecCGI``
or change to  ``Options +Indexes FollowSymLinks +ExecCGI``
or find ``AllowOverride None`` change to ``AllowOverride All``.

Find ``DirectoryIndex index.html`` add index.py ``DirectoryIndex index.html index.py``.

Find and uncomment '#' if only is comment with  ``#LoadModule rewrite_module modules/mod_rewrite.so``
 and  ``#LoadModule alias_module modules/mod_alias.so``.

When all the changes are made, save ``httpd.conf`` file, Restart Apache for changes to take effect.

Server is set and ready to run python CGI application which means you can deploy pytonik on it.
Restart server and done.


Cloud Server
------------


Some Cloud server requires CGI configuration while some have it already configured and enabled.
All depends on the company who’s offering the services.  Look into ``CGI`` configuration on ``CentOS``, ``Linux``, ``Ubuntu`` and terminal will be used for configuration process.

**CentOS**


Install apache ``sudo yum install httpd`` open the httpd.conf file ``sudo nana /etc/httpd/conf/httpd.conf``
now set for editing.

Find ``AddHandler cgi-script .cgi`` add .py  ``AddHandler cgi-script .cgi .py``.

Find ``DirectoryIndex index.html`` add index.py ``DirectoryIndex index.html index.py``

When all the changes are made, save httpd.conf file, changes takes effect.

Server is set and ready to run python CGI application which means you can deploy pytonik on it.
Restart server ``sudo systemctl restart httpd`` and done.


**Ubuntu/Linux**


Install apache ``sudo apt-get install apache2``

open the httpd.conf file``sudo nano /etc/httpd/conf/httpd.conf``
or ``gksu gedit /etc/httpd/conf/httpd.conf`` now set for editing.

Find ``AddHandler cgi-script .cgi``add .py  ``AddHandler cgi-script .cgi .py``.

Find``DirectoryIndex index.html``add index.py ``DirectoryIndex index.html index.py``

When all the changes are made, save httpd.conf file, changes takes effect.

Server is set and ready to run python CGI application which means you can deploy pytonik on it.
Restart server ``sudo systemctl restart httpd`` and done.
