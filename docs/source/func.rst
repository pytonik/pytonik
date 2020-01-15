Functions
=========



Iteration
---------
Pytonik iteration module handles iteration, enumerate dictionary and Json.

**Import Module**

.. code-block:: python

    from pytonik.Functions.iteration import iteration

**Callable**

.. code-block:: python

    iter = iteration()

**Example**  Country

.. code-block:: python

    country = [{ 'country_name': 'Afghanistan'}, {'country_name': 'Aland Islands'}, { 'country_name': 'Albania'}']


**Example**  Table Result

   +---------------+
   | List Country  |
   +===============+
   | Afghanistan   |
   +---------------+
   | Aland Islands |
   +---------------+
   | Albania       |
   +---------------+
   | Nigeria       |
   +---------------+

**Example**   Country with iteration

.. code-block:: python

    country = [{ 'country_name': 'Afghanistan'}, {'country_name': 'Aland Islands'}, { 'country_name': 'Albania'}']

    iter.iteri(country, 'id')


**Example**  Iteration Table Result

   +----+-----------------+
   | id | List Country    |
   +====+=================+
   |  1 | Afghanistan     |
   +----+-----------------+
   |  2 | Aland Islands   |
   +----+-----------------+
   |  3 | Albania         |
   +----+-----------------+
   |  4 | Nigeria         |
   +----+-----------------+



CURL
----

Pytonik curl is an in-built module support sending or initiating actions within or outside pytonik framework.
It enables access to API’s and return respond back to the application, in form of JSON, HTML, RAW data etc.
In this case the use of curl module is to POST, GET,  HEAD, PUT information in internal or from external API’s URL
using attributes like ``status``, ``reason``,  and ``result``.  Whereby ``status`` handles response codes
example **200**, **404**, **500**, etc. which the ```reason``` of this status could be OK, Not Found, Internal server Error, etc.
Get excepted information from ``result``

**Import Module**

.. code-block:: python

    from pytonik.Functions.curl import curl


**Callable**

.. code-block:: python

    cl = curl()


**Curl Local Variable**

.. code-block:: python

    URL #accept url link
    HTTPHEADER #httpheader  application/x-www-form-urlencoded etc.
    CONTENTHEADER #accept text/plain, html/plain etc.
    TIMEOUT #accept
    POSTFIELDS #accept dictionary formate {name: example, next: testing}
    POST #accept folder or url part / or /mypath
    GET	#accept folder or url part / or /mypath
    HEAD #accept folder or url part / or /mypath
    PUT #accept folder or url part / or /mypath
    PORT #accept url port 8080


GET retrieves information from api’s server

.. code-block:: python

    url = "https://example.com"
    cl = curl()
    cl.set(cl.URL, url)
    cl.set(cl.GET, '/users/{username}'.format(username='testme'))
    cl.finish()
    print(cl.status, cl.reason, cl.result())



HEAD check api’s and returns response  ``status`` and ``reason``

.. code-block:: python

    url = "https://example.com"
    cl = curl()
    cl.set(cl.URL, url)
    cl.set(cl.HEAD, '/users')
    cl.finish()
    print(cl.status, cl.reason)




POST:-  sent data/information to api using parameters or arguments
and returns response ``status`` , ``reason``, and  ``result``

.. code-block:: python

    url = "https://example.com"
    cl = curl()

    cl.set(cl.URL, url)
    cl.set(cl.CONTENTHEADER, 'application/x-www-form-urlencoded')
    cl.set(cl.ACCEPTHEADER, 'text/plain')
    cl.set(cl.POST, '/add/users')
    cl.set(cl.POSTFIELDS, {'username':'testme', 'password':'test' })
    cl.finish()
    print(cl.status, cl.reason, cl.result('utf-8'))



Now
----

Now module handle time, date functions and accuracy, you might know what time and date are because
it happens every date, pytonik provides the best way to handle time date and format with additional
future like readable time and date. now module contains methods that support ``ago``,  ``time``, ``date``, ``datetime``,
``create``, ``timestamp``,  ``past``, ``future``, ``subtract`` Now module is usable on both pytonik template
engine, controller and model

**Import module**

.. code-block:: python

    from pytonik.Functions.now import now


**callable**

.. code-block:: python

    nowdatetime = now()




Ago: covert datetime to readable format ``1 year 20 minutes ago`` accept string and format as argument
``%Y-%m-%d %H:%M:%S``

Example 1 : returns ``32 minutes ago.``


.. code-block:: python

    nowdatetime.ago("2020-01-09 08:32:18")



Date: return correct date, let say todays date ``2020-01-09`` accept ``format`` as argument, default ``format``
is set to ``%Y-%m-%d``

Example 1 : returns ``12:30:59```


.. code-block:: python

    nowdatetime.date()


Time: return correct time, let say my present ``12:30:59`` accept format as argument, default format is set to ``` %H:%M:%S```

**Example 1:** returns ``12:30:59``

.. code-block:: python

    nowdatetime.time()






Date: return correct date, let say todays date ``2020-01-09 08:18:03`` accept format as argument,
default format is set to ``%Y-%m-%d %H:%M:%S``


**Example :** returns ``2020-01-09 08:18:03``

.. code-block:: python

    nowdatetime.datetime()


Create: This method helps to create new datetime from an existing datetime. In other words changing a previous datetime format to a new datetime format.
Let say our present  ``2020-01-09 08:18:03`` and format ``%Y-%m-%d %H:%M:%S`` we want to change it to
``01-09-2020 08:18`` and the formation for this will be  ``%Y-%m-%d %H:%M``.

**Example** : returns ``01-09-2020 08:18``

.. code-block:: python

    nowdatetime.create("2020-01-09 08:18:03", oldformat="%Y-%m-%d %H:%M:%S", newformat="%Y-%m-%d %H:%M ")


Timestamp: return correct unix time and with the same method covert timestamp to date and time. Let say it returns
``1578576738`` and we want to convert it to datetime. We will need to use the same
``timestamp`` method and it returns ``2020-01-09 08:32:18``

Example 1: returns ``1578576738``

.. code-block:: python

    nowdatetime.timestamp()


Example 2: returns ``2020-01-09 08:32:18``

.. code-block:: python

    nowdatetime.timestamp('1578576738')



Past: returns previous minutes, hours, days, weeks, seconds, let say we want to go back to 27 days from today date and time.. now in our calendar todays date and time is  ```2020-01-09 08:32:18 ```

Example : returns ``2019-12-13 08:58:15.983552``

.. code-block:: python

    nowdatetime.past(days=20)



**Past:** returns previous ``minutes``, ``hours``, ``days``, ``weeks``, ``seconds``,
let say we want to look into 27 days from today date and time.. now in our calendar todays date and time is
``2020-01-09 08:32:18``

**Example:** returns ``2020-02-05 09:02:08.269823``

.. code-block:: python

    nowdatetime.future(days=20)




Subtract: subtracting or minus a date time from another from date time..
this process comment both date time to provide their format respectively. Argument are
```date1```, ```format1``` and  ```date2``` ```format2```

Example : returns ``27``

.. code-block:: python

    nowdatetime.subtract(date1='2020-01-09 08:32:18', format1='%Y-%m-%d %H:%M:%S',  date2='2019-12-13 08:58:15.983552', format2='%Y-%m-%d %H:%M:%S.%f')





Extend / Include
----------------


Pytonik has a wonderful module that handles both including and extending of external file or paging ``include``

and ``extend`` module helps to structure and  manage file architecture. Cases where you have a file named header
and all your content or code are saved in it and you want to use it in other file or page of your web application,
``include`` module handles that purpose but you can ``extend`` or ``include``. At this stage you might be wondering
what’s difference between the both properties, actually no difference.

This modules are mostly used when working with pytonik Template Engine or html pages

Sample: we are including and extending a file named ``header.html`` where ``home`` is the parent folder in our ``views``
folder and ``inc`` is a sub folder, using dot ``.`` sign to separate both folders and file. The last dot signifies
last or end of the folder and next is the file. Exception is thrown if your file path or folder cannot be located,
this might result in page not found or error path.



**Example:** Include
.. code-block:: python

        {% call include 'home.inc.header'  %}


**Example:** Extend

.. code-block:: python

        {% call extend 'home.inc.header'  %}



Let make callable outside template engine

.. code-block:: python

    from pytonik.Functions.extend import extend
    extending = extend()


.. code-block:: python

    extending.extend(path="home.inc.header")



Validations
-----------

Pytonik provide bundles of validity functions that help to validate and trim syntax, string and characters.
This Callable class are user when developing application that involves or supporter accuracy in data supply.


**Import Module**

.. code-block:: python

    from pytonik.Functions.validation import validation


**Callable**

.. code-block:: python

    valid = validation()

Method ``ip`` validates only digits and character that contains ``.`` returns bool  ``True`` or ``False``  render support IP Address ``http://domainname.com``, ``https://domainname.com`` , ``ftp://domainname.com`` , ``www.domainname.com``

**Example**

.. code-block:: python

    url_validations = valid.url('ftp://domainname.com')


Method ``ip`` validates only digits and character that contains ``.`` returns bool  ``True`` or ``False``  render support IP Address ``0.0.0.0`` ``123.123.12.1``


**Example**

.. code-block:: python

   ipaddress_validation = valid.ip('123.123.12.1')




Method ``phone`` validates only digits and character contains ``-`` and ``+``, returns bool  ``True`` or ``False``  render support to phone number: ``+1-000-000-000``, ``10000000000`` ,  ``0000000000``,  ``0000-000-0000``, ``00000000000`` ,  ``+1000000000``


**Example**

.. code-block:: python

    phone_validations = valid.phone("+234-800-000-6000")


Method ``count``  return total count of a string

**Example**

.. code-block:: python

    count = valid.count('i love python')


Method ``email`` validates only alphabet and character ``.`` , ``_`` , ``-`` and ``@``, returns bool
``True`` or ``False`` render support to email address
``my_email@gmail.com``, ``email@gmail.com`` , ``my.email@gmail.com``,  `` my_email@gmail.com``

**Example**


.. code-block:: python

    email_validations = valid.email('my_email@gmail.com')



Method ``fullname`` validates full name input field returns ``True`` or ``False`` :
``firstname lastname prefix firstname lastname``


**Example**

.. code-block:: python

    fullname_validations = valid.fullname("prefix firstname lastname")



Method ``extension`` check and validate list of prefix  if exist in or as an occurrence in the list, returns
``True`` or ``False``

**Example**

.. code-block:: python

    get_extension = valid.extension('filename.jpg', ['png', 'jpg'])



Method  ``length`` check and valid the starting length of a string and expected end,  where minimum
``min`` is  integer and maximum ``max``   ``integer (‘I love', min, max)`` returns    ``True`` or ``False``

**Example**

.. code-block:: python

    length_validation = valid.length('i love python', 4, 18)



 


Pagination
----------

Pytonik provides pagination module that helps to navigate through pages and tables,
it has favorites of methods that meetup expectations ``number``,  ``alphabet`` , ``alphabet_first_last`` ,  ``next_previous``, ``first_last``
Each of the method has same argument and parameter ``total``, ``page``, ``url``, ``css``.


**Import Module**

.. code-block:: python

    from pytonik.Functions.pagination import  pagination

**Callable**

.. code-block:: python

    pagin = pagination()


**Example:** Numbering Pagination

.. code-block:: python

    pagin.number(total=10, page = 1, url='/blog', css=['pagination’, 'page-item', 'page-link'])


**Example:** Alphabet Pagination

.. code-block:: python

    pagin.alphabet(total=10, page = 'A', url='/blog', css=['pagination', 'page-item', 'page-link'])




**Example:** Alphabet First Last Pagination

.. code-block:: python

    pagin.alphabet_first_last(total=10, page = 'A', url='/blog', css=['pagination’, 'page-item', 'page-link'])



**Example:** Next Previous Pagination

.. code-block:: python

    pagin.next_previous(total=10, page = 1, url='/blog', css=['pagination’, 'page-item', 'page-link'])



**Example:** First  Last Pagination

.. code-block:: python

    pagin.first_last(total=10, page = 1, url='/blog', css=['pagination’, 'page-item', 'page-link'])


