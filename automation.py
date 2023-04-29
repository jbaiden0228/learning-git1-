import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
mycursor = mydb.cursor()
sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")
def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")
  class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))
