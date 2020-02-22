from setuptools import setup, find_namespace_packages

from pytonik import Version

with open("README.md", "r") as fd:
    longdescription = fd.read()



setup(
    name='pytonik',
    version = Version.VERSION_TEXT+Version.EDITION,
    description='Pytonik is a python framework built to enhance web development fast and easy, also help web developers to build more apps with less codes',
    url="https://pytonik.readthedocs.io",
    author='pytonik',
    author_email='info@pytonik.com',
    maintainer= 'Emmanuel Essien',
    maintainer_email='emmamartinscm@gmail.com',
    packages=find_namespace_packages(include=['*', '']),
    long_description = longdescription,
    long_description_content_type='text/markdown',
    license= Version.LICENSE,
    keywords = Version.KEYWORDS,
    entry_points = {
        'console_scripts' : ['pytonik-start = pytonik.cmd.start:main', 'pytonik-docs = pytonik.cmd.doc:main',  'pytonik-server = pytonik.cmd.server:main']
                    },
    install_requires=['Pillow', 'mysql-connector-python', 'psycopg2-binary', 'cx-Oracle'],
    zip_safe=False,                
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Environment :: Web Environment',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Python Software Foundation License',
        'Programming Language :: Python',
        'Topic :: Office/Business',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
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
