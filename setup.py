from setuptools import setup, find_namespace_packages

from pytonik import Version

with open("README.md", "r") as fd:
    longdescription = fd.read()


setup(
    name='pytonik',
    version=Version.VERSION_TEXT + Version.EDITION,
    description='Pytonik is a python framework built to enhance web development fast and easy, also help web developers to build more apps with less codes',
    url="https://pytonik.readthedocs.io/en/latest",
    author='pytonik',
    author_email='info@pytonik.com',
    maintainer='Emmanuel Essien , Uduak Essien , Claret Nnamocha ',
    maintainer_email='emmamartinscm@gmail.com , acushla4real@gmail.com , devclareo@gmail.com',
    include_package_data=True,
    packages=find_namespace_packages(include=['*', '']),
    long_description=longdescription,
    long_description_content_type='text/markdown',
    license=Version.LICENSE,
    keywords=Version.KEYWORDS,
    entry_points={
        'console_scripts': ['pytonik = pytonik.cmd.help:main', 'pytonik-install = pytonik.cmd.install:main', 'pytonik-start = pytonik.cmd.start:main', 'pytonik-docs = pytonik.cmd.doc:main',  'pytonik-server = pytonik.cmd.server:main']
    },
    install_requires=['Pillow', 'colorama',
                      'mysql-connector-python', 'psycopg2-binary', 'cx-Oracle'],
    zip_safe=False,
    classifiers=[
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Office/Business',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python'
    ],
    python_requires='>=2.7, >=2.7.*, >=3.*',
)
