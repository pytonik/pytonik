Configuration
=============

``Pytonik`` supports Common Gateway Interface **(CGI)** and requires configuration to be able to run on Apache or any python
**CGI** enable environment.  The Configuration step support both local and cloud server.

Local Server
------------

Look into configuring ``WAMP`` , ``XAMPP`` , ``LAMP`` and ``MAMP``,
if you are not using any of the listed local servers don’t worry, this process supports **Apache**,
both older and newer version, Although you might notice little difference between versions.

.. note::

	If you keep encountering problems during setup or local machine is unable to run Common Gateway Interface **CGI** We reference **pytonik** video tutorials.
	
	 
**Apache**

Locate **httpd.conf** in your local server open it with a text or code editor.

Find ``AddHandler cgi-script .cgi`` add .py  ``AddHandler cgi-script .cgi .py``.

Find ``Options None`` change to ``Options ExecCGI``
or find ``Options +Indexes`` change to ``Options ExecCGI``
or change to  ``Options +Indexes FollowSymLinks +ExecCGI``
or find ``AllowOverride None`` change to ``AllowOverride All``.

Find ``DirectoryIndex index.html`` add index.py ``DirectoryIndex index.html index.py``.

Find and uncomment ``#`` if only is comment with  ``#LoadModule rewrite_module modules/mod_rewrite.so``
and  ``#LoadModule alias_module modules/mod_alias.so``.

When all the changes are made, save ``httpd.conf`` file, Restart Apache for changes to take effect.

Server is set and ready to run python CGI application which means you can deploy pytonik on it.
Restart server and done.


**Virtual Host (vhosts)**

Setting up a virtual host is very important espicially when using a local server.
virtual host grant you access to own custom domain names within a local environment, instead of ``localhost/mypytonik`` it uses ``mypytonik.test`` as the domain name. This features is very important especially when deploying application. Softwares Like ``MAMP`` and  ``WAMP`` provides **GUI** (graphic user interface) where you can add custom domain names, so you might not have to worry about how to set up **vhosts**, some other software's do not have such features. If you are using ``XAMPP`` then you will need to confirgure vhost in ``httpd-vhosts.conf`` file, While ``LAMP`` uses Terminal for most of its configurations but takes the same proccess. Check the configuration below. 

Locate **httpd-vhosts.conf** File

.. code-block:: python

	<VirtualHost *:80>
		DocumentRoot "c:/xampp/htdocs"
		ServerName localhost
		<Directory "c:/xampp/htdocs">
		</Directory>
	</VirtualHost>

	<VirtualHost *:80>
		DocumentRoot "c:/xampp/htdocs/mypytonik"
		ServerName mypytonik.test
		<Directory "c:/xampp/htdocs/mypytonik">
		</Directory>
	</VirtualHost>



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

open the httpd.conf file ``sudo nano /etc/httpd/conf/httpd.conf``
or ``gksu gedit /etc/httpd/conf/httpd.conf`` now set for editing.

Find ``AddHandler cgi-script .cgi`` add .py  ``AddHandler cgi-script .cgi .py``.

Find ``DirectoryIndex index.html`` add index.py ``DirectoryIndex index.html index.py``

When all the changes are made, save httpd.conf file, changes takes effect.

Server is set and ready to run python CGI application which means you can deploy pytonik on it.
Restart server ``sudo systemctl restart httpd`` and done.
