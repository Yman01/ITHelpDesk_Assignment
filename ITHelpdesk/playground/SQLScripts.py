# from SQLClientDetails import mydb


# mycursor = mydb.cursor()
# mycursor.execute("Use HelpDesk")
# mycursor.execute("CREATE Table Users(UserID int auto_increment primary Key,FirstName VARCHAR(20) not null,Lastname VARCHAR(20) not null,Email VARCHAR(40) not null,Password VARCHAR(20) not null);")

# SQLNewUser = "INSERT INTO Users (FirstName,LastName,Email,Password) VALUES(%s,%s,%s,%s)"
# ValNewUser = ("Yamen","Kasso", "Yamen@Kasso", "Yamenkasso")
# mycursor.execute(SQLNewUser,ValNewUser)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")