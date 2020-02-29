How to contribute to Pytonik
==========================

Thank you for considering contributing to Pytonik!

Support questions
-----------------

Please, don't use the issue tracker for this. Use one of the following
resources for questions about your own code:

* The ``#get-help`` channel on our Discord chat: https://discordapp.com/invite/36kGE5

	* The IRC channel ``#pytonik`` on FreeNode is linked to Discord, but
		Discord is preferred.

* Join Community : https://gitter.im/pytonik-mvc/community

* The mailing list dev@pytonik.com for long term discussion or larger issues.
* Ask on `Stack Overflow``. Search with Google first using:
	``site:stackoverflow.com pytonik {search term, exception message, etc.} ``


Reporting issues
----------------

- Describe what you expected to happen.
- If possible, include a `minimal reproducible example`_ to help us
	identify the issue. This also helps check that the issue is not with
	your own code.
- Describe what actually happened. Include the full traceback if there was an
	exception.
- List your Python, pytonik, and versions. If possible, check if this
	issue is already fixed in the repository.

.. _minimal reproducible example: https://stackoverflow.com/help/minimal-reproducible-example

Submitting patches
------------------

- Use ``Black``_ to autoformat your code. This should be done for you as a
	git ``pre-commit``_ hook, which gets installed when you run ``pip install -e .[dev]``.
	You may also wish to use Black's ``Editor integration``_.
- Include tests if your patch is supposed to solve a bug, and explain
	clearly under which circumstances the bug happens. Make sure the test fails
	without your patch.
- Include a string like "Fixes #123" in your commit message
	(where 123 is the issue you fixed).
	See `Closing issues using keywords
	<https://help.github.com/articles/creating-a-pull-request/>`.

First time setup
----------------

- Download and install the `latest version of git`_.
- Configure git with your `username`_ and `email`_::
```
git config --global user.name 'your name'
git config --global user.email 'your email'
```
- Make sure you have a ``GitHub account``.
- Fork pytonik to your GitHub account by clicking the `Fork`_ button.

- `Clone`_ your GitHub fork locally

`` 
git clone https://github.com/{username}/pytonik
cd pytonik 
``

- Add the main repository as a remote to update later

`` 
git remote add pallets https://github.com/pytonik/pytonik
git fetch pytonik
``

- Create a virtualenv::
``
python3 -m venv env
. env/bin/activate
# or "env\Scripts\activate" on Windows
``

- Install pytonik in editable mode with development dependencies

`` pip install -e ".[dev]" ``

- Install the ``pre-commit framework ``.
- Install the pre-commit hooks

`` 
pre-commit install --install-hooks
``

New to Github
------------

**GitHub account:** https://github.com/join
**latest version of git:** https://git-scm.com/downloads
**username:** https://help.github.com/en/articles/setting-your-username-in-git
**email:** https://help.github.com/en/articles/setting-your-commit-email-address-in-git
**Fork:** https://github.com/pallets/pytonik/fork
**Clone:** https://help.github.com/en/articles/fork-a-repo#step-2-create-a-local-clone-of-your-fork
**pre-commit framework:** https://pre-commit.com/#install

Start coding
------------

-   Create a branch to identify the issue you would like to work on. If you're submitting a bug or documentation fix, branch off of the latest ".x" branch::

`` 
git checkout -b your-branch-name origin/1.9.x ``

If you're submitting a feature addition or change, branch off of the
"master" branch
`` 
git checkout -b your-branch-name origin/master
``

- Using your favorite editor, make your changes, `` committing as you go ``.
- Include tests that cover any code changes you make. Make sure the test fails without your patch. `` Run the tests <contributing-testsuite> ``.
- Push your commits to GitHub and ``create a pull request`` by using

`` git push --set-upstream origin your-branch-name ``


Running the tests
-----------------

Run the basic test suite with::

``pytest``

This only runs the tests for the current environment. Whether this is relevant
depends on which part of pytonik you're working on. Travis-CI will run the full
suite when you submit your pull request.

The full test suite takes a long time to run because it tests multiple
combinations of Python and dependencies. You need to have Python 2.7, 3.4,
3.5, 3.6, 3.7, 3.8 and PyPy 2.7 installed to run all of the environments. Then run::

Building the docs
-----------------

Build the docs in the ``docs`` directory using Sphinx::

``
cd docs
pip install -r requirements.txt
make html
``

Open ``_build/html/index.html`` in your browser to view the docs.

Read more about `Sphinx <https://www.sphinx-doc.org/en/master/>`_.
