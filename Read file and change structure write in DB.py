import mysql.connector
mysql=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="DATABASENAME"
)

mycursor=mysql.cursor()
emp = open("DLB_TICKETS_SR_13_6200.txt", "r+")#txt file name and text file and python file should be n same directory


for employee in emp.readlines():
    x = employee.split(",")
    s = x[2]+","+x[3]+","+x[4];
    sql = "insert into table_name(colums) values (%s,%s,%s)"#table name
    val=(x[0],x[1],s)
    print(sql)
    print(val)
    mycursor.execute(sql, val)





mysql.commit()
emp.close()

