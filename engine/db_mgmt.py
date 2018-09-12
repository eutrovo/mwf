import psycopg2

class Mgmt:
    def __init__(self, database):
        try:
            self.connector = psycopg2.connect(
                host="localhost",database=database,
                user="postgres", password="postgres"
                )
            self.cursor = self.connector.cursor()
        except (Exception, psycopg2.DatabaseError) as error:
            raise error


    def create(self, table, cols, values):
        '''
        table must be string, cols and values must be tuples
        '''
        self.cursor.execute(f'''INSERT INTO {table} {cols}
                                VALUES {values};''')

    def read(self, cols, table, col = '', filter = ''):
        '''
        table must be string, cols must be tuple
        '''
        query = f'''SELECT {cols}
                    FROM {table}'''
        if col and filter:
            query += f" WITH {col} AS {filter};"
        else:
            query += ";"
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def update(self, table, cols_values_dict, filter):
        kv_items = ""
        for k,v in cols_values_dict.items():
            kv_items += f" {k} = {v},"
        kv_items = kv_items[:-1]
        self.cusor.execute(f'''UPDATE {table}
            SET {kv_items}
            WHERE {filter};''')

    def delete(self, table, filter):
        self.cursor.execute(f"DELETE FROM {table} WHERE {filter}")

    def commit(self):
        self.connector.commit

    def close(self):
        self.connector.close()
        self.cursor.close()
