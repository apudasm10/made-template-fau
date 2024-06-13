import os, requests, unittest, sqlalchemy
import pandas as pd
from pipeline import Pipeline


class PipelineUnitTest(unittest.TestCase):
    def setUp(self):
        self.url1 = "https://archive.ics.uci.edu/static/public/275/bike+sharing+dataset.zip"
        self.url2 = "https://archive.ics.uci.edu/static/public/560/seoul+bike+sharing+demand.zip"
        self.pipe = Pipeline(self.url1, self.url2, "bike_data")
        self.db_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'bike_data.sqlite')
        self.engine = sqlalchemy.create_engine(f'sqlite:///{self.db_path}')
        self.connection = self.engine.connect()

    def testDownload(self):
        response1 = requests.get(self.url1)
        self.assertTrue(response1.status_code == 200, msg=f'{self.url1} not accessible.')
        response2 = requests.get(self.url2)
        self.assertTrue(response2.status_code == 200, msg=f'{self.url2} not accessible.')

    def testTableExist(self):
        if not os.path.exists(self.db_path):
            self.fail(f"Database file '{self.db_path}' does not exist.")

        self.inspector = sqlalchemy.inspect(self.engine)

        try:
            tables = self.inspector.get_table_names()
            self.assertIn("Capital Bikeshare", tables,
                          "Table 'Capital Bikeshare' does not exist in the database.")
            self.assertIn("Seoul Bikeshare", tables,
                          "Table 'Seoul Bikeshare' does not exist in the database.")
        except sqlalchemy.exc.OperationalError:
            self.fail("Could not connect to the database.")
        finally:
            self.connection.close()

    def test_tables_have_row_with_three_or_more_na(self):
        if not os.path.exists(self.db_path):
            self.fail(f"Database file '{self.db_path}' does not exist.")

        try:
            tables_to_check = ["Capital Bikeshare", "Seoul Bikeshare"]

            for table in tables_to_check:
                df = pd.read_sql_table(table, self.connection)
                if (df.isna().sum(axis=1) <= 3).any():
                    self.assertTrue(True)
                else:
                    self.fail(f"Table '{table}' have row with 3 or more NA values.")
        except sqlalchemy.exc.OperationalError:
            self.fail("Could not connect to the database.")
        finally:
            self.connection.close()


if __name__ == "__main__":
    print("Running Tests: ")
    unittest.main()
