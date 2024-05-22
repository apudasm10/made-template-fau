# Follow your project plan to build an automated data pipeline for your project
#     Write a script (for example in Python or Jayvee) that pulls the data sets you chose from the internet, transforms it and fixes errors, and finally stores your data in the /data directory
#         Place the script in the /project directory (any file name is fine)
#         Add a /project/pipeline.sh that starts your pipeline as you would do from the command line as entry point:
#             E.g. if you run your script on your command line using `python3 /project/pipeline.py`, create a /project/pipeline.sh with the content: 
#                     #!/bin/bash
#                     python3 /project/pipeline.py
#     The output of the script should be: datasets in your /data directory (e.g., as SQLite databases) 
#         Do NOT check in your data sets, just your script
#         You can use .gitignore to avoid checking in files on git
#         This data set will be the base for your data report in future project work
# Update the issues and project plan if necessary


import numpy as np
import pandas as pd
import requests, os
from zipfile import ZipFile
from sqlalchemy import create_engine


class Pipeline:
    def __init__(self, url, save_file_name):
        self.url = url
        self.save_file_name = save_file_name
        self.data = None
        path = 'sqlite:///data//' + save_file_name + '.sqlite'
        self.engine = create_engine(path, echo=False)
        self.files_to_delete = []

    def get_data(self):
        response = requests.get(self.url)

        if response.status_code == 200:
            filename = "downloaded_data.zip"
            self.files_to_delete.append(filename)

            # Write the downloaded content to the file
            with open(filename, 'wb') as f:
                f.write(response.content)
            
            # Extract the CSV file from the zip
            with ZipFile(filename, 'r') as zip_ref:
                csv_filename = zip_ref.namelist()[2]  # Get the file with hourly data
                zip_ref.extract(csv_filename)  # Extract the first file
                self.files_to_delete.append(csv_filename)
            
            # Load the extracted CSV file into a pandas DataFrame
            df = pd.read_csv(csv_filename)
            self.data = df

            for pa in self.files_to_delete: # Removing downloaded and extracted data
                os.remove(pa)
            
        else:
            print(f"Download failed. Status code: {response.status_code}")

    def transform_data(self):
        self.data.drop(self.data.columns[0], axis=1, inplace=True) # Deleting instant as it is just an index
        self.data.dropna(thresh=3) # Deleting a row if it has more 3 or more NA values
        self.data.bfill() # Filling the remaining NA values backward (Imputation)

    def save_data(self):
        self.data.to_sql(self.save_file_name, self.engine, if_exists='replace', index=False)

    def run_pipeline(self):
        self.get_data()
        print("Got the Data!")
        self.transform_data()
        print("Data Transformed!")
        self.save_data()
        print("Data Saved!")



if __name__ == '__main__':
    pipe = Pipeline("https://archive.ics.uci.edu/static/public/275/bike+sharing+dataset.zip", "bike_data")
    pipe.run_pipeline()
