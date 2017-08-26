from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class db:

    engine = None
    session = None

    def __init__(self):
        self.engine = self.create_engine()

    def create_engine(self):
        #return create_engine('sqlite:///:memory:', echo=True)
        return create_engine('mssql+pyodbc://user:pass@server_name')

    def create_session(self):
        self.session = sessionmaker(bind=self.engine)

    def test_db(self):
        """Test the database connection by reading something from the database"""
        db_conn.engine.connect()
        db_conn.engine.execute('use staging')
        r = db_conn.engine.execute('SELECT * FROM sys.tables')
        for row in r:
            print(row)

if __name__ == '__main__':
    db_conn = db()
    db_conn.create_session()
