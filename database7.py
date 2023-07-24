.import sqlite3
import hashlib
from datetime import datetime

def con():
    conn =  sqlite3.connect('dtbs.db')
    return conn

def create_user():
    con2 = con()
    kur = con2.cursor()

    kur.execute("""
    create table if not exists user(
        `id` int not null  primary key,
        `first_name` varchar(50),
        `last_name` varchar (50),
        `email` varchar (50),
        `user_nomer` varchar (50),
        `pasword` varchar (150),
        `is_active` boolean default false,
        `registered_date_time` datetime
        )
    """)
    con2.commit()
    con2.close()

create_user()

def insert_user(data:dict):
    con2 = con()
    kur = con2.cursor()
    sha256 = hashlib.sha256()
    sha256.update(data['passwrod'].encode('utf-8'))
    hashed_password = sha256.hexdigest()
    query = """
        insert into user (
        `first_name`,
        `last_name`,
        `email`,
        `user_nomer`,
        `pasword`,
        `registered_date_time`
        )
        values ( ?, ?, ?, ?, ?,?)
        """
    values = (date['first_name'], data['last_name'], data['email'], data['user_name'], hashed_password, data[datetime.now()] )
    kur.execute(query, values)
    con2.commit()
    con2.close()




