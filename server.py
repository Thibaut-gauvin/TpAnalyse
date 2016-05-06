# -*- coding: utf-8 -*-

import sqlite3
from analyzer import Analyzer
from bottle import route, run, debug, error, request, TEMPLATE_PATH, jinja2_template as template

TEMPLATE_PATH.append("./views")


# Render Home page (Api Doc)
@route('/', method='GET')
def documentation():
    return template('home.html')


# Render list of all analyzes
@route('/analyzes', method='GET')
def show_analyzes():
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
        return template('showAnalyse.html', error='This analyzes does not exist !')
    else:
        return template('showAnalyse.html', results=results)


# Create new analyze
@route('/analyzes', method='POST')
def create_analyze():
    text = request.POST.get('text', '').strip()
    analyze = Analyzer(text)
    analyze = analyze.parse_text()
    analyzed = analyze.format_before_save()

    conn = sqlite3.connect('analyzes.db')
    c = conn.cursor()
    c.execute("INSERT INTO analyzes (analyzed_text, creation_date, words_occur, letters_count, letters_occur, most_used_words) VALUES(?,?,?,?,?,?)", (analyzed.text, analyzed.creation_date, analyzed.words_occur, analyzed.letters_count, analyzed.letters_occur, analyzed.most_used_words))
    conn.commit()
    c.close()

    return template('result.html', analyze=analyzed)


# Trow 404 error when page not found
@error(404)
def mistake404(code):
    return template('404.html')


# Run Server Dev
debug(True)
run(reloader=True)
