######################
# Database functions #
######################

import sqlite3
from data.util.paths import database_path


def createDatabase():
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS users (user_id int primary key, user_name varchar(20), user_language varchar(20), user_post varchar(20))')
    connection.commit()
    cursor.close()
    connection.close()
