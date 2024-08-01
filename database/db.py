import pymysql
db_host = 'db-veterinaria.c3mi660au4wg.us-east-2.rds.amazonaws.com'
db_user = 'abner'
db_password = 'Aerosmith1510'
db_database = 'db_veterinaria'
db_table = 'users'

def connectionSQL():
    """Establishes a connection to the MySQL database."""
    try:
        connection_sql = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_database
        )
        print("Successful connection to database")
        return connection_sql
    except pymysql.MySQLError as err:
        print("Error connecting to the database")
        print(err)
        return None

def add_user(Id, Nombre, Apellido, Cumpleaños):
    """Adds a user to the database."""
    connection_sql = connectionSQL()
    if connection_sql is None:
        print("No connection to the database. User not added.")
        return False

    try:
        # Use parameterized queries to prevent SQL injection
        instruction_sql = f"INSERT INTO {db_table} (Id, Nombre, Apellido, Cumpleaños) VALUES (%s, %s, %s, %s)"
        with connection_sql.cursor() as cursor:
            cursor.execute(instruction_sql, (Id, Nombre, Apellido, Cumpleaños))
            connection_sql.commit()
            print("User added")
            return True
    except pymysql.MySQLError as err:
        print("Error creating the user")
        print(err)
        return False
    finally:
        connection_sql.close()  # Always close the connection

def consult_user(id):

    connection_sql = connectionSQL()
    if connection_sql is None:
        print("No connection to the database. User not added.")
        return False

    try:
        # Use parameterized queries to prevent SQL injection
        instruction_sql = "SELECT * FROM users WHERE Id = " + id
        with connection_sql.cursor() as cursor:
            cursor.execute(instruction_sql)
            result_data = cursor.fetchall
            print(result_data)
            connection_sql.commit()
            return True
    except pymysql.MySQLError as err:
        print("Error creating the user")
        print(err)
        return False
    finally:
        connection_sql.close()  # Always close the connection