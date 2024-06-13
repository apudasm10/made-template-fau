import os, requests, unittest, sqlalchemy, time
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

    def testNA(self):
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

    def testValueRange(self):
        if not os.path.exists(self.db_path):
            self.fail(f"Database file '{self.db_path}' does not exist.")

        try:
            # Connect to the database
            connection = self.engine.connect()
            tables_to_check = ["Capital Bikeshare"]

            for table in tables_to_check:
                df = pd.read_sql_table(table, connection)

                if 'temp' not in df.columns or 'hum' not in df.columns:
                    self.fail(f"Table '{table}' does not contain 'temp' and/or 'hum' columns.")

                temp_out_of_range = df['temp'].between(0, 1, inclusive='both') == False
                hum_out_of_range = df['hum'].between(0, 1, inclusive='both') == False

                if temp_out_of_range.any():
                    print(sum(temp_out_of_range))
                    self.fail(f"Table '{table}' has 'temp' values out of range [0, 1].")
                if hum_out_of_range.any():
                    self.fail(f"Table '{table}' has 'hum' values out of range [0, 1].")

        except sqlalchemy.exc.OperationalError:
            self.fail("Could not connect to the database.")
        finally:
            self.connection.close()

    def testCreateDatabase(self):
        temp_db_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'temp_data.sqlite')
        if os.path.exists(temp_db_path):
            os.remove(temp_db_path)

        pipeline = Pipeline(self.url1, self.url2, "temp_data")
        pipeline.run_pipeline()

        self.assertTrue(os.path.exists(temp_db_path), f"Database was not created by the pipeline.")

    def testDatabaseExist(self):
        pipeline = Pipeline(self.url1, self.url2, "bike_data")
        pipeline.run_pipeline()

        self.assertTrue(os.path.exists(self.db_path), f"Database does not exist.")

    # def testDatabaseEquality(self):
    #     temp_db_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'temp_data.sqlite')
    #     # pipeline = Pipeline(self.url1, self.url2, "temp_data")
    #     # pipeline.run_pipeline()
    #
    #     engine1 = sqlalchemy.create_engine(f'sqlite:///{self.db_path}')
    #     engine2 = sqlalchemy.create_engine(f'sqlite:///{temp_db_path}')
    #
    #     inspector = sqlalchemy.inspect(engine1)
    #     tables = inspector.get_table_names()
    #
    #     for table_name in tables:
    #         # Fetch all rows from table in database 1
    #         with engine1.connect() as connection1:
    #             result1 = connection1.execute(sqlalchemy.text(f"SELECT * FROM {table_name}"))
    #             rows1 = result1.fetchall()
    #
    #         # Fetch all rows from table in database 2
    #         with engine2.connect() as connection2:
    #             result2 = connection2.execute(sqlalchemy.text(f"SELECT * FROM {table_name}"))
    #             rows2 = result2.fetchall()
    #
    #         # Assert that rows in both databases are identical
    #         self.assertEqual(rows1, rows2, f"Data in table '{table_name}' is not identical")


if __name__ == "__main__":
    print("Running Tests: ")
    unittest.main()
