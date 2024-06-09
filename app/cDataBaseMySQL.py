import pymysql


##########################
#          Data Base     #
##########################


class MySQLDatabase:
    def __init__(self, host, port, user, password, db, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor, timeout=10):
        self.connection_params = {
            'host': host,
            'port': port,
            'user': user,
            'password': password,
            'db': db,
            'charset': charset,
            'cursorclass': cursorclass,
            'connect_timeout': timeout,
            'read_timeout': timeout,
            'write_timeout': timeout
        }
        self.connection = None

    def connect(self):
        self.connection = pymysql.connect(**self.connection_params)

    def close(self):
        if self.connection:
            self.connection.close()

    def create_table(self, table_name):
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                columns = ", ".join([f"col{i} VARCHAR(255)" for i in range(1, 51)])
                create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY AUTO_INCREMENT, {columns})"
                cursor.execute(create_table_query)
                self.connection.commit()
                print(f"Table '{table_name}' with 50 VARCHAR(255) columns created successfully")
        except pymysql.MySQLError as e:
            print(f"Error: {e}")
        finally:
            self.close()

    def insert_records(self, table_name, values):
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                placeholders = ", ".join(["%s"] * 51)
                insert_query = f"INSERT INTO {table_name} (id, {', '.join([f'col{i}' for i in range(1, 51)])}) VALUES ({placeholders})"
                cursor.executemany(insert_query, values)
                self.connection.commit()
                print(f"Records inserted successfully into '{table_name}'")
        except pymysql.MySQLError as e:
            print(f"Error: {e}")
        finally:
            self.close()

    def fetch_table_names(self):
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = %s", (self.connection_params['db'],))
                tables = cursor.fetchall()
                print("Tables in the database:")
                for table in tables:
                    print(table['TABLE_NAME'])
        except pymysql.MySQLError as e:
            print(f"Error: {e}")
        finally:
            self.close()

    def fetch_column_names(self, table_name):
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                cursor.execute("""
                    SELECT COLUMN_NAME
                    FROM information_schema.columns
                    WHERE table_schema = %s AND table_name = %s
                """, (self.connection_params['db'], table_name))
                columns = cursor.fetchall()
                print(f"Columns in table '{table_name}':")
                for column in columns:
                    print(column['COLUMN_NAME'])
        except pymysql.MySQLError as e:
            print(f"Error: {e}")
        finally:
            self.close()

    def show_records(self, table_name):
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM {table_name}")
                records = cursor.fetchall()
                print(f"Records in table '{table_name}':")
                for record in records:
                    print(record)
        except pymysql.MySQLError as e:
            print(f"Error: {e}")
        finally:
            self.close()

    def rename_table(self, old_table_name, new_table_name):
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                rename_table_query = f"RENAME TABLE {old_table_name} TO {new_table_name}"
                cursor.execute(rename_table_query)
                self.connection.commit()
                print(f"Table renamed from '{old_table_name}' to '{new_table_name}' successfully")
        except pymysql.MySQLError as e:
            print(f"Error: {e}")
        finally:
            self.close()

    def update_record(self, table_name, record_id, update_data):
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                set_clause = ", ".join([f"{key} = %s" for key in update_data.keys()])
                update_query = f"UPDATE {table_name} SET {set_clause} WHERE id = %s"
                cursor.execute(update_query, (*update_data.values(), record_id))
                self.connection.commit()
                print(f"Record with id {record_id} in table '{table_name}' updated successfully")
        except pymysql.MySQLError as e:
            print(f"Error: {e}")
        finally:
            self.close()


