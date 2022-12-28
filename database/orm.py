from database.db import cursor, connection

# docs: https://www.psycopg.org/psycopg3/docs/basic/params.html


class Note:

    table_name = "Note"
    table_fields = ("title",)

    @classmethod
    def all(cls):
        query = f"SELECT * FROM {cls.table_name}"
        cursor.execute(query)
        results = cursor.fetchall()
        return results

    @classmethod
    def get(cls, search_field, search_value):

        query = f"SELECT * FROM {cls.table_name} WHERE {search_field}=%s"
        cursor.execute(query, (search_value,))

        instance = cursor.fetchone()

        if instance is None:
            raise ValueError("Instancia não existe no banco")

        return instance

    @classmethod
    def insert(cls, *args, **kwargs):

        query = f"INSERT INTO {cls.table_name} VALUES (%s)"

        # if kwargs:
        #     cursor.execute(query, tuple(kwargs.values()))
        #     connection.commit()
        #     return

        cursor.execute(query, args)
        connection.commit()

    # @classmethod
    # def update(cls, search_field, search_value, *args):

    #     """
    #     UPDATE Note
    #     SET title = 'Novo valor',
    #         outro_campo = 'Novo valor'
    #     WHERE search_field = search_value;
    #     """

    #     instance = cls.get(search_field, search_value)

    #     query = f"""
    #     UPDATE {cls.table_name}
    #     {set_new_fields_string}
    #     WHERE {search_field}='{search_value}'
    #     """
    #     # cursor.execute(query, args)
    #     cursor.execute(query)
    #     connection.commit()

    @classmethod
    def delete(cls, search_field, search_value):
        cls.get(search_field, search_value)
        query = f"DELETE FROM {cls.table_name} WHERE {search_field}='{search_value}'"
        cursor.execute(query)
        connection.commit()

    @classmethod
    def clear(cls):
        query = f"DELETE FROM {cls.table_name}"
        cursor.execute(query)
        connection.commit()
