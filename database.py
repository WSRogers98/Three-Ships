# import sqlite3 module
import sqlite3
import random

def initDB():
    # create DB
    con = sqlite3.connect("mythics.db")
    cur = con.cursor()
    # init values
    cur.executescript("""
        create table IF NOT EXISTS mythics(
            name VARCHAR(255) PRIMARY KEY NOT NULL,
            type VARCHAR(255) NOT NULL,
            attack INT NOT NULL,
            defense INT NOT NULL,
            wins int,
            losses int
        );
    replace into mythics values ( 'Baba Yaga', 'Slavic', 50, 50,NULL ,NULL );
    replace into mythics values ( 'Achilles', 'Greek', 25, 75,NULL ,NULL);
    replace into mythics values ( 'Thor', 'Norse', 75, 25,NULL ,NULL);
    replace into mythics values ( 'Nagual', 'Mesoamerrican', 40, 60,NULL ,NULL);
        """)
    cur.executescript("""
            create table IF NOT EXISTS matchHistory(
                home VARCHAR(255) NOT NULL,
                away VARCHAR(255) NOT NULL,
                Winner VARCHAR(255) NOT NULL
            );
            """)
    # print data TEMP
    cur.execute("SELECT * from mythics")
    print(cur.fetchall())


def create(n, t, a, d):
    # connect to db
    con = sqlite3.connect("mythics.db")
    cur = con.cursor()

    #create new
    query = "INSERT OR REPLACE INTO mythics (name, type, attack, defense) VALUES (?, ?, ?, ?)"
    cur.execute(query, (n, t, a, d))
    cur.execute("SELECT * from mythics")
    print(cur.fetchall())

    # commit and close
    con.commit()
    cur.close()
    con.close()

def update(n, t, a, d,):
    # connect to db
    con = sqlite3.connect("mythics.db")
    cur = con.cursor()

    #update column
    query = "UPDATE mythics SET type = '{}',attack='{}',defense='{}' WHERE name = '{}'".format(t, a, d, n)
    cur.execute(query)

    cur.execute("SELECT * from mythics")
    print(cur.fetchall())
    # commit and close
    con.commit()
    cur.close()
    con.close()

def delete(id):
    # connect to db
    con = sqlite3.connect("mythics.db")
    cur = con.cursor()

    #delete row
    query="DELETE FROM mythics WHERE name = '{}'".format(id)
    cur.execute(query)

    cur.execute("SELECT * from mythics")
    print(cur.fetchall())

    # commit and close
    con.commit()
    cur.close()
    con.close()

def getTable():
    # connect to db
    con = sqlite3.connect("mythics.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM mythics")

    rows = cur.fetchall()
    columns = [description[0] for description in cur.description]
    return(rows, columns)

def getHistory():
    # connect to db
    con = sqlite3.connect("mythics.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM matchHistory")

    rows = cur.fetchall()
    columns = [description[0] for description in cur.description]
    return (rows, columns)

def getCharacters():
    con = sqlite3.connect("mythics.db")
    cur = con.cursor()
    cur.execute("SELECT name FROM mythics")
    print(cur.execute("SELECT name FROM mythics"))
    characters = cur.fetchall()
    return characters

def playMatch(home,away):
    # connect to db
    con = sqlite3.connect("mythics.db")
    cur = con.cursor()
    i = random.randint(0, 1)
    home = home.replace(',', '').replace(')', '').replace('(', '').replace("'", '')
    away = away.replace(',', '').replace(')', '').replace('(', '').replace("'", '')
    print(home)
    print(away)
    if i == 0:
        #home wins
        query = "UPDATE mythics SET wins = COALESCE(wins, 0)+1   WHERE name = ?"
        cur.execute(query,(home,))
        query = "UPDATE mythics SET losses = COALESCE(losses, 0)+1  WHERE name = ?"
        cur.execute(query,(away,))
        query = "INSERT INTO matchHistory (home, away, winner) VALUES (?, ?, ?)"
        cur.execute(query, (home, away, home))
    else:
        #away wins
        query = "UPDATE mythics SET wins = COALESCE(wins, 0) + 1 WHERE name = ?"
        cur.execute(query, (away,))
        query = "UPDATE mythics SET losses = COALESCE(losses, 0)+1 WHERE name = ?"
        cur.execute(query, (home,))
        query = "INSERT INTO matchHistory (home, away, winner) VALUES (?, ?, ?)"
        cur.execute(query, (home, away, away))

    cur.execute("SELECT * from mythics")
    print(cur.fetchall())
    # commit and close
    con.commit()
    cur.close()
    con.close()