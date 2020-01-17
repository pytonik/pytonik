Getting Started
===============

Pytonik framework supports python version from 2.7 to newer,
Pytonik can be download from  ``https://pypi.org/pytonik``  using terminal or command line promts
``pip install pytonik==1.9.7b1``  or   ``https://github.com/pytonik/pytonik``
The installation will automatically be extracted into ``site-packages``  in Python  directory.

Pytonik provides command line tool that helps in creating project folder structure with the use of ``pytonik-start``
command, it gives internationalization, ``English`` as default language and other supported languages are listed below '

.. code-block:: python

    'bg_BG': 'Bulgarian',
    'cs_CZ': 'Czech',
    'da_DK': 'Danish',
    'de_DE': 'German',
    'el_GR': 'Greek',
    'es_ES': 'Spanish',
    'et_EE': 'Estonian',
    'fi_FI': 'Finnish',
    'fr_FR': 'French',
    'hr_HR': 'Croatian',
    'hu_HU': 'Hungarian',
    'it_IT': 'Italian',
    'lt_LT': 'Lithuanian',
    'lv_LV': 'Latvian',
    'nl_NL': 'Dutch',
    'no_NO': 'Norwegian',
    'pl_PL': 'Polish',
    'pt_PT': 'Portuguese',
    'ro_RO': 'Romanian',
    'ru_RU': 'Russian',
    'sv_SE': 'Swedish',
    'tr_TR': 'Turkish',
    'zh_CN': 'Chinese',


.. note::

    if you receive an error while running the command, the error will stop you from using the command, to get the error fixed,
    you will be required to add ``export LC_ALL=en_US.UTF-8`` and ``export LANG=en_US.UTF-8`` to system path. This error are common on ``MAC OS``, ``Ubuntu`` and ``Linux``.
    if you keep experiencing this error, refer to **File Structure**.


Installations
-------------

Install python and make sure it’s running on your computer operating system environment or web server.


**Python** can be downloaded at  ``https://www.python.org/downloads``
If you are using a cloud open terminal type or paste  ``sudo apt-get install python3``
download environment and Pytonik requirement.

During installation process add to path but if missed out, then you will have to add it to environment
path once the installation is completed.

After installation process, open Terminal/Command promts and type in ``python`` or  ``which python``.

**Note:-**  ``which python`` command  might not work on windows environment,
to achieve this, it will need the help of  ``https://git-scm.com`` on windows 10 or newer,
install ubuntu  ``https://www.microsoft.com/en-us/p/ubuntu/9nblggh4msv6``
