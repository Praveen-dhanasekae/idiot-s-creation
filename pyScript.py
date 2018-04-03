import pymysql
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',                             
                             db='Bank',
                             )

cursor= connection.cursor();

try
      sql = "SELECT * FROM table2 "
      cursor.execute(sql)
      for row in cursor
        if((row["Loan_ACC"]!= 0)&(row["Loan_Acc_low"]!= 0))
        row["Points"]=((.35)())+(()())+(()())
         
