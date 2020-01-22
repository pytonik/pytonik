SMTP
====

Send email to user with pytonik framework, this could be one part you really want to look at.
Pytonik provides module that handles sending of emails and file attachment to users. this module has two methods
``send`` and ``attach`` . Before your application can to send or receive email. SMTP settings has to be enabled,
to do so, we will work through and see how to configure our web application to send out email to users


SMTP Environment Setting- you might wonder where to get the setting below, you can get smtp settings
from your email providers or emailing server,  example **GMAIL**, **YAHOO**, **OUTLOOK** or Custom email host.

.. code-block:: python

    'SMTP':
    {
        'server':   'mail.server.com',
        'port':     26,
        'username': 'from@mail.com',
        'password': '231222',
    }




**Import Module**

.. code-block:: python

    from pytonik.Core.SMTP import SMTP


**Callable**
.. code-block:: python

    mail = SMTP()


**Example:** ``Variable`` and ``Strings``

.. code-block:: python

    subject = "My pytonik"
    content = "I love Pytonik framework"
    from = "from@mail.com"
    to = "to@mail.com”


**Example:** Sending Email to user

.. code-block:: python

    sent = mail.send(from, to, subject, content, header='html')


**Example:** Sending Email  with attachment to user

.. code-block:: python

    file = "my_attachment.pdf"
    attached = mail.attach(file).send(from, to, subject, content)


**Example:** Rename file attachment before sending email and  attachment to user

.. code-block:: python

    file = "my_attachment.pdf"
    rename = "rename file"
    attached = mail.attach(file, rename).send(from, to, subject, content)

