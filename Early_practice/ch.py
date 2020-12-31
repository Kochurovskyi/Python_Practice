import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='y**u',  # Changed!!!
    passwd='***',  # Changed!!!
    database='mydatabase'
)
mycrs = mydb.cursor()
mycrs.execute("SELECT * FROM myrun")
mydata = mycrs.fetchall()

run_src = 'Marathon'
print('We are searching...', run_src)
print('_________________')
print('We found...')

lst_U = []  # The list of findings (ids)
for i in mydata:
    RunNm = i[0]
    RunTt = i[2]
    for j in range(len(RunTt) - 1):
        if RunTt[j:j + len(run_src)].lower() == run_src.lower() and not RunTt in lst_U:
            lst_U.append(RunNm)  # Adding the DB id to the lst_U if we find something

# Printing out
pr_f = 'Date of Running: {}, Location: {}, Distance: {}km, --> Result(Time): {}'  # Output format
for i in lst_U:
    query = ("select * from myrun where id='%s'" % int(i))
    mycrs.execute(query)
    result = mycrs.fetchone()
    print(pr_f.format(result[1], result[2], result[3], result[4]))
if len(lst_U) == 0:
    print('Nothing')
mydb.close()

