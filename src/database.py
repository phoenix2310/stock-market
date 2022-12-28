import os
import MySQLdb

connection=None
def connect():
    global connection
    connection = MySQLdb.connect(
        host=os.getenv("HOST"),
        user=os.getenv("USERNAME"),
        passwd=os.getenv("PASSWORD"),
        db=os.getenv("DATABASE"),
        ssl_mode="VERIFY_IDENTITY",
        ssl={
            "ca": "/etc/ssl/certs/ca-certificates.crt"
        }
    )
