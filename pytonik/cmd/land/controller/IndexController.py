from pytonik.Web import App, Version

app = App()


def index():
    data = {
        'title': 'Welcome',
        'name': 'Pytonik',
        'version': Version().VERSION_TEXT,
        'reversion': Version().VERSION_TEXT[0:6],
    }

    return app.views('index', data)
