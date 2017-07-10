import os
import unittest
import testing.postgresql
from init_db import init_data
from drop_table import drop_table
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.postgresql = testing.postgresql.Postgresql()
        dsn = self.postgresql.dsn()
        uri = 'postgresql://{}@{}:{}/{}'
        TEST_DB_URI = uri.format(dsn['user'], dsn['host'], dsn['port'],
                                 dsn['database'])

        import flaskr
        flaskr.app.config['DATABASE_URI'] = TEST_DB_URI
        flaskr.app.testing = True
        self.app = flaskr.app.test_client()
        engine = create_engine(TEST_DB_URI)
        Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        self.session = Session()
        with flaskr.app.app_context():
            init_data([], self.session)



    def tearDown(self):
        drop_table(self.session)
        self.session.close()
        self.postgresql.stop()
        self.postgresql = None

    def test_download_file(self):
        r = self.app.get("/download/test_download")
        print("debug here", r.data)


if __name__ == '__main__':
    unittest.main()
