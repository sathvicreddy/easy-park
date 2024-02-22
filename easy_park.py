print ("-----------------------------")
print ("EASY PARK")
print("------------------------------")
import mysql.connector as c
con=c.connect(host="localhost",user="root",password= "593427",database="easy_park",auth_plugin="mysql_native_password")
cur=con.cursor()
#cur.execute("create database easy_park")
#cur.execute("create table tuck_shop(adno int,sname varchar(15),grade varchar(10),bill int) ")
#cur.execute("create table maintance room_no int,beds int,clock int,light int,ac int,cupboard int)")
#con.commit()
import random
global number
global number2
global slotcode
number2=random.randint(100000,999999)
number=random.randint(1000,9999)


def login():
    global user_name
    user_name=input("user name")
    b=input("enter password")
    q="select user_name,password from user where user_name='{}'".format(user_name)
    cur.execute(q)
    d=cur.fetchall()
    if user_name in d[0] and b in d[0]:
        print("successfully loggined")
    else:
        print("wront user name or password")
        login()
def signin():
    x=input("first name: ")
    a=input("user name      : ")
    b=input("password       : ")
    c=int(input("phone number   : "))
    d=input("e mai       : ")
    q="select user_name from user"
    cur.execute(q)
    s=cur.fetchall()
    if a in s[0]:
        print("user aldready exist on:",a)
    else:
        y="insert into user values('{}','{}','{}',{},'{}')".format(x,a,b,c,d)
        cur.execute(y)
        con.commit()
        z="create table {}(city char(20),area varchar(25),address varchar(50),slotnumber varchar(10),OTP int(5),verify char(15),time varchar(10),slot_order_id int(10))".format(a)
        cur.execute(z)
        con.commit()

def security_login():
    global agent_id
    x=input("user aldrady signin y/n")
    if x in "Nn":
        agent=input("agent name")
        y="create table {}(city char(20),area char(20),slot_number varchar(10),OTP int(10),status varchar(10))".format(agent)
        cur.execute(y)
        con.commit()
    agent_id=input("enter agent username")
    b=input("enter password")
    q="select agent_id,password from agent_user where agent_id='{}'".format(agent_id)
    cur.execute(q)
    d=cur.fetchall()
    if agent_id in d[0] and b in d[0]:
        print("successfully loggined")
    else:
        print("wront user name or password")
        login()


def locality():
    b="select * from locality"
    cur.execute(b)
    c=cur.fetchall()
    for i in c:
        print(i)
    global local
    print("select locality")
    local=input("enter area")
    a=input("enter the locality code")
def wheel2():
    b="select * from slots where vehicle_type='two_wheel'and area='{}'".format(local)
    cur.execute(b)
    c=cur.fetchall()
    for i in c:
        print(i)
    slotcode=input("enter the selected slot code")
    a="insert into {}(city ,area,address,slotnumber) select city,area,address,slot_number  from slots".format(user_name)
    cur.execute(a)
    con.commit()
    x="update {} set slot_order_id={} where slotnumber='{}'".format(user_name,number2,slotcode)
    cur.execute(x)
    con.commit()
    print("slot successfully booked")
    d="update {} set OTP={} where slot_order_id={}".format(user_name,number,number2)
    cur.execute(d)
    con.commit()
def wheel3():
    b="select * from slots where vehicle_type='three_wheel' and area='{}'".format(local)
    cur.execute(b)
    c=cur.fetchall()
    for i in c:
        print(i)
    slotcode=input("enter the selected slot code")
    a="insert into {}(city ,area,address,slotnumber) select city,area,address,slot_number  from slots)".format(user_name)
    cur.execute(a)
    con.commit()
    x="update {} set slot_order_id={} where slotnumber='{}'".format(user_name,number2,slotcode)
    cur.execute(x)
    con.commit()
    print("slot successfully booked")
    d="update {} set OTP={} where slot_order_id={}".format(user_name,number,number2)
    cur.execute(d)
    con.commit()
def wheel4():
    b="select * from slots where vehicle_type='four_wheel'and area='{}'".format(local)
    cur.execute(b)
    c=cur.fetchall()
    for i in c:
        print(i)
    slotcode=input("enter the selected slot code")
    a="insert into {}(city ,area,address,slotnumber) select city,area,address,slot_number  from slots)".format(user_name)
    cur.execute(a)
    con.commit()
    x="update {} set slot_order_id={} where slotnumber='{}'".format(user_name,number2,slotcode)
    cur.execute(x)
    con.commit()
    print("slot successfully booked")
    d="update {} set OTP={} where slot_order_id={}".format(user_name,number,number2)
    cur.execute(d)
    con.commit()
def history():
    print("order history")
    x="select * from {}".format(user_name)
    cur.execute(x)
    c=cur.fetchall()
    for i in c:
        print(i)
    
def profile():
    x="select * from user where user_name='{}'".format(user_name)
    cur.execute(x)
    b=cur.fetchall()
    print("name     : ",b[0][0])
    print("user name: ",b[0][1])
    print("password : ",b[0][2])
    print("phone    : ",b[0][3])
    print("address  : ",b[0][4])
#def agent_profile():
    


while True:
    print("1.......user login")
    print("2.......admin")
    j=int(input("select the vale"))
    if j==1:
        while True :
            print ("1.......login")
            print("2........sign in")
            print("3.........exit")
            a=int(input("selected value"))
            if a==1:
                login()
                while True:
                    locality()
                    print("1.......book a slot")
                    print("2.......history")
                    print("3.......profile")
                    print("4.......back")
                    z=int(input("enter the selected number"))
                    if z==1: 
                        while True:
                            print("vechile type")
                            print("1......2whealer")
                            print("2......3whealer")
                            print("3......4whealer")
                            c=int(input("enter the choise"))
                            if c==1:
                                wheel2()
                                break
                            elif c==2:
                                wheel3()
                                break
                            elif c==3:
                                wheel4()
                                break
                            elif c==4:
                                login()
                    elif z==2:
                        history()
                    elif z==3:
                        profile()
                    elif z==4: 
                        break
                    else:
                        print("invalid code")
            elif a==2:
                signin()
            elif a==3:
                break
            else:
                print("invalid code")
    elif j==2:
        while True :
            print ("1.......login")
            print("2.........exit")
            a=int(input("selected value"))
            if a==1:
                login()
                while True:
                    print("1.......slot updation")
                    print("2.......slot check otp")
                    print("3.......history")
                    print("4.......profile")
                    print("5.......logout")
                    z=int(input("enter the selected number"))
                    if z==1:
                        slot_update()
                    elif z==2:
                        verify()
                    elif z==2:
                        agent_history()
                    elif z==3:
                        agent_profile()
                    elif z==4:
                        login()
                    else:
                        print("invalid code")
            elif a==3:
                break
            else:
                print("invalid code")





 
