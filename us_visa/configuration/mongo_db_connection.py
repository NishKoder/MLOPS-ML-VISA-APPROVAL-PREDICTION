import sys

from us_visa.exception import USvisaException
from us_visa.logger import logging

import os
from us_visa.constants import DATABASE_NAME, MONGODB_URL_KEY
import pymongo
import certifi

from dotenv import load_dotenv

load_dotenv()

ca = certifi.where()


class MongoDBClient:
    """
    Class Name :   export_data_into_feature_store
    Description :   This method exports the dataframe from mongodb
                    feature store as dataframe

    Output      :   connection to mongodb database
    On Failure  :   raises an exception
    """
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(
                        f"Environment key: {MONGODB_URL_KEY} is not set."
                    )
                MongoDBClient.client = pymongo.MongoClient(
                    mongo_db_url,
                    tlsCAFile=ca
                )
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection successful")
        except Exception as e:
            raise USvisaException(e, sys)

    def get_database_collection(self, collection_name: str):
        """
        Get a specified collection from the MongoDB.

        Args:
            collection_name (str): The name of the collection to retrieve
                                   from the database.

        Returns:
            The requested collection object from the MongoDB.
        """
        return self.database[collection_name]

    def close_connection(self):
        """
        Closes the MongoDB connection.

        :return: None
        """
        self.client.close()
        logging.info("MongoDB connection closed")

    def __del__(self):
        self.close_connection()
        logging.info("MongoDB connection closed")
