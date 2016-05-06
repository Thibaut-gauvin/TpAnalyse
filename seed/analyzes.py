import sqlite3
con = sqlite3.connect('analyzes.db')
con.execute("CREATE TABLE analyzes (id INTEGER PRIMARY KEY, analyzed_text longtext NOT NULL, creation_date DATETIME, words_occur longtext, letters_count INTEGER, letters_occur longtext, most_used_words longtext)")
con.commit()
