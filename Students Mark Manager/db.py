import sqlite3


class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS Students(
            roll_no text,
            name text,
            english text,
            maths text,
            physics text,
            chemistry text,
            computer text

        )
        """
        self.cur.execute(sql)
        self.con.commit()

    def insert(self, roll_no, name, english, maths, physics, chemistry, computer):
        self.cur.execute(
            "insert into Students values (?,?,?,?,?,?,?)",
            (roll_no, name, english, maths, physics, chemistry, computer),
        )
        self.con.commit()

    def fetch(self):
        self.cur.execute("SELECT * from Students")
        rows = self.cur.fetchall()

        return rows

    def remove(self, roll_no):
        self.cur.execute("delete from Students where roll_no=?", (roll_no,))
        self.con.commit()

    def update(self, roll_no, name, english, maths, physics, chemistry, computer):
        self.cur.execute(
            "update Students set name=?, english=?, maths=?, physics=?, chemistry=?, computer=? where roll_no=?",
            (name, english, maths, physics, chemistry, computer, roll_no),
        )
        self.con.commit()
