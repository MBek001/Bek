# CRUD create read update delete
# agarda kritilgan database bor bolsa ashibka cqaradi buning uchun { if not exists qoyish kifoya }

# import sqlite3
#
# conn = sqlite3.connect('databs.db')
#
# cur = conn.cursor()
# # cur.execute("""
# #     create table if not exists `user`(
# #         `first_name` varchar(50),
# #         `last_name` varchar(50),
# #         `phone` varchar(13),
# #         `birth_day` date,
# #        `is_active` boolean default false,
# #         `size_of_shoes` int
# #     )
# # """)
# conn.commit()
#
# # cur.execute("""
# #     insert into `user`(`first_name`, `last_name`, `phone`, `birth_day`, `is_active`, `size_of_shoes`)
# #     values
# #     ('Muhammadaziz', 'Ravshanov', '+998888888888', '2005-04-30', false, 42),
# #     ('Imom', 'Qurbonov', '+998938182001', '2001-02-21', false, 43),
# #     ('Manguberdi', 'Abdullayev', '+998939832020', '2001-06-20', false, 44)
# # """)
# # conn.commit()
# cur.execute("""
#     select * from user
# """)
# rows = cur.fetchall()
# for row in rows:
#     print(row)
#
# conn.close()

"""
UPDATE
""""

import sqlite3

def conn():
    return sqlite3.connect('databs.db')

def insert ( data: dict, table: str):
    con = conn()
    cur=con.cursor()
    cur.execute(f"""
        insert into {table}(first_name, last_name, phone, birth_day, is_active, size_of_shoes  )
        values 
        ( {data[first_name ]}, {data[last_name]}, {data[phone]},  {data[bitrh_day]}, {data[is_active]}, {data[size_of_shoes] )
    
    """)






