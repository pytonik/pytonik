from pytonik.Web import App, Version

m = App()


def index():
    data = {
        'title': 'Welcome',
        'name': 'Pytonik',
        'version': Version().VERSION_TEXT,
        'reversion': Version().VERSION_TEXT[0:5],
    }

    return m.views('index', data)
