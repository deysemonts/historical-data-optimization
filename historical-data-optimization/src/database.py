from dotenv import load_dotenv
from os import getenv
import cx_Oracle as cx

load_dotenv()

ORACLE_URL = getenv("ORACLE_URL")
ORACLE_CLIENT = getenv("ORACLE_CLIENT")

def connect():
    if ORACLE_CLIENT:
        try:
            cx.init_oracle_client(lib_dir=ORACLE_CLIENT)
        except:
            pass

    return cx.connect(ORACLE_URL)
