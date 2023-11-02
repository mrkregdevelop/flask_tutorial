def create_table() -> None:
    import sqlite3
    con = sqlite3.connect('example.db')
    cur = con.cursor()

    sql = """
        CREATE TABLE IF NOT EXISTS Emails (
        EmailId INTEGER PRIMARY KEY,
        EmailValue varchar(255)
        );
        """
    cur.execute(sql)

    con.commit()
    con.close()
