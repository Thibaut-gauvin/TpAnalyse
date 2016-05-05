# -*- coding: utf-8 -*-
import sqlite3
from bottle import route, run, debug, error, TEMPLATE_PATH, jinja2_template as template
TEMPLATE_PATH.append("./views")


# Render Home page (Api Doc)
@route('/', method='GET')
def documentation():
    return template('home.html')


# Render list of all analyzes
@route('/analyzes', method='GET')
def test():
    conn = sqlite3.connect('analyzes.db')
    c = conn.cursor()
    c.execute("SELECT * FROM analyzes")
    results = c.fetchall()
    c.close()

    if not results:
        return 'There is no analyzes !'
    else:
        return template('showAnalyses.html', results=results)


# Render given analyze (analyze id)
@route('/analyzes/<id>', method='GET')
def show_all_analyzes(id):
    conn = sqlite3.connect('analyzes.db')
    c = conn.cursor()
    c.execute("SELECT * FROM analyzes WHERE id = ?", (id))
    results = c.fetchall()
    c.close()

    if not results:
        return 'This analyzes does not exist !'
    else:
        return template('showAnalyse.html', results=results)


# Trow 404 error when page not found
@error(404)
def mistake404(code):
    return template('404.html')


# Run Server Dev
debug(True)
run(reloader=True)
