from customer import Bill,color,Products
class Register:
    '''register yourself to buy products'''
    def work(self):
        #return name,email and password
        name = input('enter your name:')
        email = input('enter your email:')
        password = input('enter your password:')
        return name,email,password
    def sign_up(self):
        name = input('enter your name:')
        email= input('enter your email:')
        password= input('enter your password:')
        conf_pass=input('enter confirm password:')
        if password == conf_pass:
            print('password confirm')
            z=True
        else:
            print('enter password again!\n'+color.RED+'cannot sign up'+color.END)
        details=[name,email,password]
        with open('login.txt','r') as f:
            r = f.readlines()
            f.seek(0)
            k = f.read()
            g = k.split('\n')
            g.pop()
            for i in range(len(r)-1):
                l=g[i].split(',')
                if l[1]==details[1]:
                    print(color.RED,'Cannot signup; enter your correct email as the '
                            'account have already created with this email!'+color.END)
                    con = False
                    self.sign_up()
                else:
                    con=True
            if con==True:
                with open('login.txt','a+') as f:
                    f.write(name+','+email+','+password+'\n')
                print('you have signup successfully')

    def log_in(self):
        print('='*10)
        print('log in')
        count=0
        user = list(a.work())
        with open('login.txt','r') as f:
            k=f.read()
            g=k.split('\n')
            for i in g:
                l=i.split(',')
                for j in range(0,1):
                    if l[j]==user[j] and l[j+1]==user[j+1] and l[j+2]==user[j+2]:
                        print('login successfully')
                        count+=1
                        global v
                        v= True
                        with open('customer_record.txt','a+') as f:
                            for i in user:
                              f.write(i+',')
        if count==0:
            print('enter correct login details!')
            a.log_in()



v=False

a=Register()
y=input(color.UNDERLINE+"\nDo you want to signup then type yes\nOR if you have account already then type no"+color.END)
if y=='yes':
   a.sign_up()
ask=input(color.DARKCYAN+'if you want to login press y\n or just want to see products press n:'+color.END)
if ask=='y':
   c=a.log_in()
if ask=='n':
    k = int(input('enter which types of products you want to see 1st?\n'
                  'press 1 for washing products\npress 2 for glocery\npress 3 for cosmetics\npress 4 for gadgets'))
    Products(k).display_products()
#check if you have login correctly then it will continue
if v==True:
    print(color.PURPLE+'**welcome to shopping cart**'+color.END)
    k = int(input('enter which types of products you want to see 1st?\n'
                  'press 1 for washing products\npress 2 for glocery\npress 3 for cosmetics\npress 4 for gadgets'))
    g = Bill(k)
    g.display_product()


