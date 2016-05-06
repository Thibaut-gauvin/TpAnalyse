import sqlite3
con = sqlite3.connect('analyzes.db')
con.execute("CREATE TABLE analyzes (id INTEGER PRIMARY KEY ASC, analyzed_text longtext NOT NULL, creation_date DATETIME, words_occur longtext, letters_count INTEGER, letters_occur longtext, most_used_words longtext, letter_occur_graph_name longtext, words_occur_graph_name longtext)")
con.commit()
