# -*- coding: utf-8 -*-

import sqlite3
from analyzer import Analyzer
from graphic import Graphic
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

    return template('showAnalyses.html', results=results)


# Render given analyze (analyze id)
@route('/analyzes/<id:int>', method='GET')
def show_all_analyzes(id):
    conn = sqlite3.connect('analyzes.db')
    c = conn.cursor()
    c.execute("SELECT * FROM analyzes WHERE id LIKE ?", (str(id)))
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

    if len(text) == 0:
        return {'message': 'error, you must provide `text` parameter'}

    analyze = Analyzer(text)
    analyzed = analyze.parse_text()

    graphic_fabric = Graphic(analyzed.letters_occur, analyzed.most_used_words, analyzed.letters_count)
    graphic_fabric.graph_letter_occurrence()
    graphic_fabric.graph_words_occurrence()

    analyzed = analyze.format_before_save()

    conn = sqlite3.connect('analyzes.db')
    c = conn.cursor()
    c.execute("INSERT INTO analyzes (analyzed_text, creation_date, words_occur, letters_count, letters_occur, most_used_words, letter_occur_graph_name, words_occur_graph_name) VALUES(?,?,?,?,?,?,?,?)", (analyzed.text, analyzed.creation_date, analyzed.words_occur, analyzed.letters_count, analyzed.letters_occur, analyzed.most_used_words, graphic_fabric.letter_occur_graph_name, graphic_fabric.words_occur_graph_name))
    conn.commit()
    c.close()

    return analyzed.to_json()


# Delete given analyze (analyze id)
@route('/analyzes/<id:int>', method='DELETE')
def show_all_analyzes(id):
    conn = sqlite3.connect('analyzes.db')
    c = conn.cursor()
    c.execute("SELECT * FROM analyzes WHERE id LIKE ?", (str(id)))
    results = c.fetchall()
    c.close()

    if not results:
        return {'message': 'error, there is no analyzes !'}
    else:
        conn = sqlite3.connect('analyzes.db')
        c = conn.cursor()
        c.execute("DELETE FROM analyzes WHERE id LIKE ?", (str(id)))
        conn.commit()
        c.close()

        return {'message': 'Analyze delete successfully'}


# Trow 404 error when page not found
@error(404)
def mistake404(code):
    return template('404.html')


# Run Server Dev
debug(True)
run(reloader=True)
