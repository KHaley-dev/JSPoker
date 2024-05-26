import os
from dotenv import load_dotenv
import logger
import mysql.connector

load_dotenv()
main_logger = logger.Logger("db")
dbk_logger = logger.Logger("db.get_env_value")

def get_env_value(value):
    try:
        return os.environ[value]
    except:
        dbk_logger.critical(f"Environmental varialbe \"{value}\" was not found. To fix this issue\n * Gather your database information: host, name, user, password, port\n * Add them to your .env file\n * Read JSPoker/api/README.md for more information")
        quit()

DB_HOST = get_env_value("DB_HOST")
DB_NAME = get_env_value("DB_NAME")
DB_USER = get_env_value("DB_USER")
DB_PASSWORD = get_env_value("DB_PASSWORD")
DB_PORT = get_env_value("DB_PORT")

# print(DB_HOST,DB_NAME,DB_USER,DB_PASSWORD,DB_PORT)
main_logger.info("Database information gathered")
db = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    passwd=DB_PASSWORD,
    database=DB_NAME
)
main_logger.info(f"Connected to database {DB_HOST}:{DB_NAME} (user: {DB_USER})")
cursor = db.cursor()

