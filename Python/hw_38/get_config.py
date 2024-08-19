from dotenv import load_dotenv

import os

load_dotenv()


def get_db_config():
    ICH_HOST = os.getenv("ICH_HOST")
    ICH_PASSWORD = os.getenv("ICH_PASSWORD")
    ICH_USER = os.getenv("ICH_USER")
    ICH_DATABASE = os.getenv("ICH_DATABASE")

    dbconfig = {
        'host': f"{ICH_HOST}",
        'user': f"{ICH_USER}",
        'password': f"{ICH_PASSWORD}",
        'database': f"{ICH_DATABASE}",
    }

    return dbconfig
