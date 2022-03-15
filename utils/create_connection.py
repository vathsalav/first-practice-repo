import os

from psycopg import connect, OperationalError

from custom_exception.connection_problem import ConnectionProblem


def create_connection():
    try:
        conn = connect(
            host=os.environ.get("HOST"),
            dbname=os.environ.get("DB"),
            user=os.environ.get("USER"),
            password=os.environ.get("PASSWORD"),
            port=os.environ.get("PORT")
        )
        return conn
    except OperationalError as e:
        raise ConnectionProblem("Could not connect to the database")


connection = create_connection()

print(connection)
