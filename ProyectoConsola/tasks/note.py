import users.connection as connection

connect = connection.connect()
database = connect[0]
cursor = connect[1]


class Note:

    def __init__(self, user_id, title="", description=""):
        self.user_id = user_id
        self.title = title
        self.description = description

    def save(self):
        sql = "INSERT INTO notes (user_id, title, description) VALUES (%s, %s, %s)"
        cursor.execute(sql, (self.user_id, self.title, self.description))
        database.commit()
        return [cursor.rowcount, self]

    def list_notes(self):
        sql = f"SELECT * FROM notes WHERE user_id = {self.user_id}"
        cursor.execute(sql)
        return cursor.fetchall()

    def delete(self):
        sql = f"DELETE FROM notes WHERE user_id = {self.user_id} AND title LIKE '{self.title}'"
        cursor.execute(sql)
        database.commit()
        return [cursor.rowcount, self]
