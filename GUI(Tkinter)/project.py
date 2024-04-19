import mysql.connector as sql
def main():
    fit=sql.connect(database="giridhar",user='root',password='giri')
    
    print('connected')
    print('')
    print('')
    print('WELCOME TO RAHI FITNESS CENTER')
    print('')
    print('')
    print('TO LoOGIN PRESS')
    print('')
    print('')
    print('TO CREATE YOUR NEW ACCOUNT PRESS')
    print('')
    print('')
    print('TO EXIT PRESS')
    print('')

    c=int(input('enter your choice'))
    if (c==1):
        print('')
        print('to login please enter your user id and password')
        print('')
        uname=input('enter your user id')
        print('')
        pwd=input('enter your password')
        print('')
        name=input('enter your name')
        print('')
        c1=fit.cursor()
        c1.execute('select *from user_rigister')
        data=c1.fetchall()
        count=c1.rowcount

        for row in data:
            if (user_id in row) and (password in row):
                print('')
                print('SUCCESSFULLY LOGIN!!!!!!')
                print('Welcome to name', 'fitness center')
                print('')
                print('')
                print('to see castumer details press:1')
                print('')
                print('to update costumer details press:2')
                print('')
                print('to see item in jim press:3')
                print('')
                print('to update new items press:4')
                print('')
                c2=int(input('enter your choice'))
                if (c2==1):
                    c1=fit.cursor()
                    c1.execute('selcet * from cutmer')
                    data=c1.fetchall()
                    count=c1.rowcount
                    print('total costumer is',count)
                    for row in data:
                        print(row)
            elif (c2==2):
                print('')
                print('to update costumer details please enter the following details')
                print('')
                v_costumer_id=int(input('integer costumer id(in integer) :'))
                print('')
                v_costumer_addres=input('enter address of costumer')
                print('')
                v_date_of_joined=input('custumer joined data')
                print('')
                v_amt_paid=int(input('paid amount'))
                print('')
                c1=fit.cursor()
                update_dtails="insert into costumer values("+ str(v_costumer_id) +",'"+ (v_costumer_name) +"','"+(v_costumer_address) +"','"(v_date_of_joined)+"',"+ str(v_amt_paid) +")"
                c1.execute(update_details)
                fit.commit()
                print('costumer details succesufully updated')
            elif(c2==3):
                print('FOLLOWING ITEMD RECTHERE IN', name,'JIM')
                c1=fit.cursor()
                c1.excuted('select * from jim_items')
                data=c1.fetchall()
                count=c1.rowcount
                print('total jim item is', count)
                for row in data:
                    print(row)
            elif(c2==4):
                print('to update new items enter the following details')
                v_object_id=int(input('enter the object code(in integer)'))
                v_object_name+input('enter the name of jit items')
                v_date_of_purchase=input('enter the date og repair')
                v_total_people_using=int(input('total persons'))
                c1=fit.cussor()
                updates2=("insert into jim_items values('"+ str(v_object_id)+ "','"+ (v_object_name) +"','"+(v_date_of_purchase) +"','"+ (v_repairing_date)+"','" ,str(v_total_people_using) +"')")
                c1.excute(updates2)
                fit.commit()
                print('item updated')
          

            else:
                ('something went to worng')
       
    elif(c==2):
       print('')
       print('to create your account please enter your user id and password')
       print('')
       c1=fit.cursor()
       v_user_id=int(input("create your user id (in integer)"))
       print(" ")
       v_password=int(input("create your password(in integer)"))
       print(" ")
       v_name=input("your full name")
       print(" ")
       c1=fit.cursor()
       update=("insert into user1_fitness values("+str(v_user_id) +",'"+ str(v_password) + (v_name) +"')")
       c1.execute(update)
       fit.commit()
       print("account created")
    elif (c==3):
       print("vist again")
       print(" ")
       print("thank you")
    else:
       ("somthing went wrong")
        
                 
main()     
           
          


