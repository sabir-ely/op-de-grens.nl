import sqlite3
from datetime import datetime

with sqlite3.connect("blog.db", detect_types=sqlite3.PARSE_DECLTYPES) as conn:

    c = conn.cursor()

    #Create description table
    c.executescript("""
        create table Description
        (
            id      integer primary key,
            content text
        );
        insert into Description values (1,  "");

        create table Article
        (
            id           integer primary key autoincrement,
            title        text,
            content      text,
            date_created timestamp,
            public       boolean
        );
    """)

    conn.commit()
