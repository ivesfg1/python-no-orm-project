from database.db import cursor, connection


def create_tables():

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Note (
            title VARCHAR(250) NOT NULL
        );
        """
    )
    connection.commit()
