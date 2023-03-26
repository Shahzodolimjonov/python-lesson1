from sqlite3 import connect

conn = connect('database.db')
cur = conn.cursor()

sql = '''
CREATE TABLE contacts (
  contact_id INTEGER PRIMARY KEY,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE,
  phone TEXT NOT NULL UNIQUE
);
'''

sql1 = '''
INSERT INTO contacts (first_name,last_name ,email,phone,manzil)
VALUES( 'Shahzod',  'Olimjonov','shahzod@gmail.com','+994333403434','kogont.');
'''
sql3 = '''
select * from contacts
'''
sql2 = '''
UPDATE contacts
SET first_name = 'shohzod', last_name = 'Alimjanov', email = 'asdsdsdhg@gmail.com', phone='+821934476639162'
WHERE contact_id=4'''
sql4 = '''
delete from contacts where contact_id=3
'''
sql5='''
ALTER TABLE contacts
add manzil text;
'''

try:
    cur.execute(sql1)
    for i in cur.fetchall():
        print(i)
except Exception as e:
    print(e)
conn.commit()



# conn = connect('data.db')
# cur = conn.cursor()

# sql = '''
# CREATE TABLE contacs (
#   contac_id INTEGER PRIMARY KEY,
#   first_name TEXT NOT NULL,
#   last_name TEXT NOT NULL,
#   email TEXT NOT NULL UNIQUE,
#   phone TEXT NOT NULL UNIQUE
# );
# '''

# sql1 = '''
# INSERT INTO contacts (first_name,last_name ,email,phone)
# VALUES( 'vali',  'aliyev','va23983@gmail.com','+99433230874301');
# '''

# try:
#     cur.execute(sql1)
#     for i in cur.fetchall():
#         print(i)
# except Exception as e:
#     print(e)
# conn.commit()

# conn = connect('MB.db')
# cur = conn.cursor()

# sql = '''
# CREATE TABLE firms (
#   firm_id INTEGER PRIMARY KEY,
#   firm_name TEXT NOT NULL,
#   last_name TEXT NOT NULL,
#   city TEXT NOT NULL,
#   phone TEXT NOT NULL UNIQUE
# );
# '''
# sql1 = '''
# insert into firms(firm_name,last_name,city,phone)
# values('samsung','VALI','UZB',+9989023232);
# '''
# sql2 = '''
# select * from firms
# '''
# sql3 = '''
# UPDATE firms
# SET firm_name='Apple', last_name='jek', city='germaniya', phone=+99835487347
# WHERE firm_id=3;
# '''
# sql4 = '''
# ALTER TABLE firms
# DROP COLUMN firm_name;
# '''
# sql5 = '''
# CREATE TABLE table_name (
#     last_name datatype constraint,
#     city datatype constraint,
# );
# '''
# try:
#     cur.execute(sql3)
#     for i in cur.fetchall():
#         print(i)
# except Exception as e:
#     print(e)
# conn.commit()

# conn = connect('CAR.db')
# cur = conn.cursor()

# sql = '''
# CREATE TABLE cars (
#   car_id INTEGER PRIMARY KEY,
#   car_name TEXT NOT NULL,
#   last_name TEXT NOT NULL,
#   city TEXT NOT NULL,
#   narxi TEXT NOT NULL UNIQUE
# );
# '''


# try:
#     cur.execute(sql)
#     for i in cur.fetchall():
#         print(i)
# except Exception as e:
#     print(e)
# conn.commit()