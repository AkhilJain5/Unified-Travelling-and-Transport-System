import mysql.connector
import GraphicUser_InterFace.Login_page
import GraphicUser_InterFace.StartPageGUI

UTTSdb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='harsh',
    database='UTTS')

#login page starter
Login_page = GraphicUser_InterFace.Login_page.Login()
Login_page.mainloop()

#saving username and password
file = open('LocalDATA//password.txt', 'r')
password = file.read()
file.close()
file = open('LocalDATA//username.txt', 'r')
username = file.read()
file.close()

cur=UTTSdb.cursor()
s="SELECT * FROM users WHERE first_name = '{}' AND Password = '{}'".format(username,password)
cur.execute(s)
QueryCheckForPassword=cur.fetchall()

#If to check wether password right or wrong
#if(QueryCheckForPassword==""):

# Home_page = GraphicUser_InterFace.StartPageGUI.Main()
# Home_page.mainloop()


#print(UTTSdb.connection_id)
#print to check connection establishment
