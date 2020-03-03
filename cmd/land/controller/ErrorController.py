from pytonik.Web import App, Version

m = App()


def index():
    m.header()

    print("do work here")


def page400():
    data = {
        'title': '400 NOT Found!',
        'name': 'Pytonik',
        'version': Version().VERSION_TEXT

    }
    m.views('400', data)


def page404():
    data = {
        'title': '404 NOT Found!',
        'name': 'Pytonik',
        'version': Version().VERSION_TEXT
    }
    m.views('405', data)


def page405():
    data = {
        'title': '405 NOT Found!',
        'name': 'Pytonik',
        'version': Version().VERSION_TEXT
    }
    m.views('405', data)

