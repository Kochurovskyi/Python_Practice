import csv
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='y**u',                     # Changed!!!
    passwd='***',                  # Changed!!!
    database='mydatabase'
)
mycrs = mydb.cursor()
# Table creating and check...
mycrs.execute("CREATE TABLE myrun (id INT AUTO_INCREMENT PRIMARY KEY, "
              "RunDt VARCHAR(255), "
              "RunTt VARCHAR(255), "
              "RunDs VARCHAR(255),"
              "RunTm VARCHAR(255))")

# Data transfer from CSV to DB (Table 'myrun')
fl = open('run.csv')
rds = csv.DictReader(fl)
for record in rds:
    RunDt = record.get('Date')
    RunTt = record.get('Title')
    RunDs = record.get('Distance')
    RunTm = record.get('Time')
    sqlin = 'insert into myrun (RunDt, RunTt, RunDs, RunTm) values (%s, %s, %s, %s)'
    values = (RunDt, RunTt, RunDs, RunTm)
    mycrs.execute(sqlin, values)
mydb.commit()
print(mycrs.rowcount, "records inserted.")

# Let's check the tables
mycrs.execute('SHOW TABLES')
for x in mycrs:
    print(x)

# Let's check the readings
mycrs.execute("SELECT * FROM myrun")
myresult = mycrs.fetchall()
for x in myresult:
    print(x)

mydb.close()
