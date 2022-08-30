import psycopg2
DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "root"
DB_PORT = '5432'


#establishing the connection
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Retrieving data
cursor.execute('SELECT * from "Employee"')

#Fetching 1st row from the table
result = cursor.fetchmany(1);
print(result)

#Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()

