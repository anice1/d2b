#!/usr/bin/python3
"""
 Here is where you can register all sql services you'd like to run during
 automation. 
 These sql files are loaded into the Kernel. Now create something great!

"""

from typing import List
from handlers.log_handler import LogHandler
from handlers.service_handler import Service
from handlers.db_connect_handler import DatabaseConn


logger = LogHandler(log_file="logs/analytics.log")

conn = DatabaseConn(connector="pg")
conn = conn.connect()
conn.autocommit = True


class AnalyticsServiceProvider(Service):

    # name of analytics in sql e.g. "product_analysis.sql"
    def __init__(self, service_list: List[str] = None) -> None:

        # name of files in data/raw to upload.
        self.service_list = service_list

    def execute_service(self):
        # Read the sql file
        print("Running Analysis...")
        for f in self.service_list:
            try:
                # instantiate class
                print(f"Running Query... {f}\t")
                cur = conn.cursor()
                cur.execute(open(f, "r").read())
                print("Successful! \n")
            except Exception as e:
                print(": ", e)
                logger.logger.error(e)
        conn.close()
        print("------" * 20)
        print("Analysis Completed \n")
