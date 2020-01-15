Validations
===========

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


Method ``email`` validates only alphabet and character ``.`` , ``_`` , ``-`` and ``@``, returns bool  ``True`` or ``False`` render support to email address ``my_email@gmail.com``, ``email@gmail.com`` , ``my.email@gmail.com``,  `` my_email@gmail.com``

**Example**


.. code-block:: python

    email_validations = valid.email('my_email@gmail.com')



Method `` fullname `` validates full name input field returns ``True`` or ``False`` :  `` firstname lastname prefix firstname lastname ``


**Example**

.. code-block:: python

    fullname_validations = valid.fullname("prefix firstname lastname")



Method `` extension `` check and validate list of prefix  if exist in or as an occurrence in the list, returns  `` True`` or `` False ``

**Example**

.. code-block:: python

    get_extension = valid.extension('filename.jpg', ['png', 'jpg'])



Method  `` length `` check and valid the starting length of a string and expected end,  where minimum ``min`` is  integer and maximum ``max``   integer (‘I love', min, max) `` returns  `` True`` or `` False ``

**Example**

.. code-block:: python

    length_validation = valid.length('i love python', 4, 18)



 
