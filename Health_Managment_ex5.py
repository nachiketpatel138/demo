# 1 total 3 client 
# 2 food log and retrive
# total 6 file

def getdate():
    import datetime
    return datetime.datetime.now()



def take(b):
    if b==1:
        ex_fo=input('Enter the 1 for Ex or 2 for Food : ')
        if ex_fo=='1':
            ex = input('Name of ex : ')
            with open('ex_nachiket.txt','a') as f:
                f.write(str(getdate()) +'  '+ ex+'\n')
                print('Sucess')
        else:
            food=input('Enter the food name : ')
            with open('food_nachiket.txt','a') as f:
                f.write(str(getdate())+''+ food,'\n')


def retrive(c):
    if c==1:
        ex_fo=input('Enter the 1 for Ex or 2 for Food : ')
        if ex_fo=='1':
            with open('ex_nachiket.txt') as f:
                read = f.read()
                print(read)
                
                
        else:
            with open('ex_nachiket.txt') as f:
                read = f.read()
                print(read)
            


print('Wel-Come To Helth Managment System')
a = int(input('press [1] for log \npress [2] for retrive \n'))
if a==1:
    b=int(input('[1] for [Nachiket] \n[2] for [pe2]\n3 for [raju]\n'))
    take(b)
elif a==2:
    c=int(input('Press 1 for Nachiket 2 for pe2 3 for raju'))
    retrive(c)
else:
    print("You not Enter the valid number ")