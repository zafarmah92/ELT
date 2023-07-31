import psycopg2
from dagster import get_dagster_logger, resource


class PostgresDB():
    def __init__(self):
        self.host = "host.docker.internal"
        self.port = 5432
        self.database = "postgres"
        self.user = "postgres"
        self.password = "secret"
        self.conn = psycopg2.connect(
            host=self.host,
            port=self.port,
            database=self.database,
            user=self.user,
            password=self.password
        )
        self.cursor = self.conn.cursor()
        #get_dagster_logger().info(self.cursor)
        self.create_schema()
        #self.create_table()    

    def create_schema(self):
        try:
            self.cursor.execute("CREATE SCHEMA IF NOT EXISTS airup;")
            self.conn.commit()
        except:
            pass 

    def create_table(self,table_schema):
        self.cursor.execute(table_schema)
        self.conn.commit()


    def insert_data(self, insert_statement):
        self.cursor.execute(insert_statement)
        self.conn.commit()
        
    def __del__(self):
        self.cursor.close()
        self.conn.close()

@resource(
    description="Database connection manager"
)
def db_resource(init_context):
    return PostgresDB()

