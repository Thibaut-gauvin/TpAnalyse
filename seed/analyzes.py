import sqlite3
con = sqlite3.connect('analyzes.db')
con.execute("CREATE TABLE analyzes (id INTEGER PRIMARY KEY, analyzed_text longtext NOT NULL, creation_date DATETIME, words_occur int, letters_nb int, letters_nb_occur longtext, most_famous_words longtext)")

con.execute("INSERT INTO analyzes (analyzed_text,creation_date,words_occur,letters_nb,letters_nb_occur,most_famous_words) VALUES ('Read A byte of python to get a good introduction into Python','2016-05-05 17:20:50',12,60,'{ a:2, b:1 }','{ read:1, get:2 }')")
con.commit()
