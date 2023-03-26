from psycopg2 import connect

Database='python_03'
User='postgres'
Password='shahzod0604'
Host='localhost'

conn=connect(
    database=Database, user=User, password=Password, host=Host, port='5432'
)

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
INSERT INTO contacts (contact_id,first_name,last_name,email,phone, manzil)
VALUES( 4, 'Vali4', 'Aliyev4', 'alivalis@gmail.com', '+9943383033344301', 'buxoro');
'''

sql2 = '''
update contacts
set first_name='Jonik', last_name='Jumayev', email='sdfss@gmail.com', phone=+99894043345, manzil='fargona'
where contact_id=3
'''
sql3 = '''
alter table contacts
add manzil text;
'''
sql4 = '''
select order_id, ship_city, order_date from orders
order by order_id
limit 10
'''

try:
    conn.autocommit = True
    cur.execute(sql2)
except Exception as e:
    print(e)
conn.commit()