from flask import Flask
from flask_flatpages import FlatPages
from flask_frozen import Freezer

app = Flask(__name__)


app.config.from_pyfile('settings.py')
pages = FlatPages(app)
freezer = Freezer(app)

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

