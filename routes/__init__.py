import os
from flask import Flask, g, session, request, abort, render_template, url_for
from common.db import initDb, closeDb
from common.config import SESSION_KEY

app = Flask(__name__,
        template_folder='../templates',
        static_folder='../static')
app.secret_key = SESSION_KEY

@app.before_request
def init():
    g.conn, g.session = initDb()
    print 'Database connects.'

def after_request(req):
    pass

@app.teardown_request
def teardown(e):
    if hasattr(g, 'conn') and hasattr(g, 'session'):
        print 'Datebase disconnects.'
        closeDb()

@app.route('/initDatabase')
def initializeDatabase():
    if not app.debug:
        abort(404)

    from initDb import initDatabase
    initDatabase()
    return 'Init Database.'

import routes.business
import routes.customer
