import psycopg2
DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "root"

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

cur = conn.cursor()            
# execute a statement        
print('PostgreSQL database version:')      
cur.execute('SELECT version()')     
# display the PostgreSQL database server version    
db_version = cur.fetchone()      
print(db_version)

conn.close()
