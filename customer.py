class Products:
    '''used only to display products according to the choice of customer'''
    def __init__(self,j):
        self.j=j
    def display_products(self):
        if self.j==1:
            self.file='washing_products.txt'
        elif self.j==2:
            self.file ='grocery.txt'
        elif self.j==3:
            self.file='cosmetics.txt'
        elif self.j == 4:
            self.file='gadgets_1.txt'
        else:
            print('correct no!!')
        with open(self.file,'r') as f:
                k=f.read()
                g=k.split('\n')
                g.pop()
                for i in range(len(g)):
                   l=g[i].split(',')
                   print(i+1,'name of product:',l[1],'\n''price:',l[2]+'rs','\n''product id:',l[0])


#inheritance
class Shopping_cart(Products):
    '''user will select the products which he/she wants to buy'''
    def add_to_cart(self):
        #Assosiation
        super().display_products()
        self.b=[]
        self.q=[]
        print('===========')
        while True:
            print(color.RED +'note: if you done shopping enter negative quantity to move towards bill or leave blank!!'+color.END)
            #exception handling
            try:
               buy=input('enter product id of the items which you want to buy:')
               quantity=int(input('enter the quantity of this product(integers only):'))
               if quantity < 0:
                   raise Exception
            except:
                break
            self.b.append(buy)
            self.q.append(quantity)
        self.price=0
        self.total=[]
        with open(self.file, 'r') as f:
            k = f.read()
            g = k.split('\n')
            for i in range(len(g)):
                l=g[i].split(',')
                self.total.append(l)
        for i in range(len(self.b)):
            for j in range(len(self.total)):
                if self.b[i]==self.total[j][0]:
                    #adding price to total bill of customer
                    self.price+=int(self.total[j][2])*int(self.q[i])
                    #quantity subtract after adding to user cart so admin may know if its too less
                    self.total[j][3]=str(int(self.total[j][3])-int(self.q[i]))
                    #after changes as the customer buys the product sending data to file
                    Shopping_cart.work(self)
                    self.work()
    def work(self):
        '''storing data to file after subtracting the quantity'''
        with open(self.file, 'w') as foo:
            for i in range(len(self.total)-1):
                foo.write(self.total[i][0]+','+self.total[i][1]+','+self.total[i][2]+','+self.total[i][3]+'\n')

#inheritance
class Bill(Shopping_cart):
    '''producing bill'''
    def __init__(self,j):
        super().__init__(j)

    #method overloading
    def display_product(self):
        #calling add to cart function from here
        super().add_to_cart()
        print('\n\n')
        print('BILL' +color.BOLD)
        print('your ordered list is as under:' +color.END)
        #printing ordered list
        for i in range(len(self.b)):
            for j in range(len(self.total)):
                if self.b[i] == self.total[j][0]:
                    print(color.BLUE +'='*10)
                    print('product id:',self.total[j][0],'\n','name of product',
                          self.total[j][1],'\n','price',self.total[j][2],'\n',
                          'no of items you ordered:',self.q[i])
        print('\n')
        print('*'*10)
        print(color.RED+'total price=',self.price, color.END)
        print('*'*10)

        Bill.card_validator(self)

    def card_validator(self):
        #4598454334520987 use this  as valid card no

       card_no = int(input("enter a 16 digit  card number without using -"+color.RED+'note(for trial you can use:4598454334520987):').strip())
       credit_no = str(card_no)
       if len(credit_no) != 16:
          print("your card length is not 16")
       else:
          validatelist = []
          for i in credit_no:
             validatelist.append(int(i))
          for i in range(0, len(credit_no), 2):
             validatelist[i] = validatelist[i] * 2
             if validatelist[i] >= 10:
                validatelist[i] = validatelist[i] - 9
          if sum(validatelist) % 10 == 0:
             print('This is a valid credit card number!'+color.END)
             date().check_expiry()
          else:
             print('This is not valid credit card! \n please try again!')
class date:
    def __init__(self):
        '''year should be in 4 digits'''

        self.year_of_expiry = int(input('enter expiry year of your card'))
        self.month = int(input("enter month of your card expiry"))


    def check_expiry(self):
        import datetime
        x = datetime.datetime.now()
        y = str(x)
        y = y.split('-')
        if int(y[0]) < self.year_of_expiry:
            print("you are able to continue shopping!\n have a nice day")
        elif int(y[0]) > self.year_of_expiry:
            print("your card is expired")
        else:
            if int(y[1]) <= self.month:
                print("you are able to continue shopping!\n have a nice day")
            else:
                print("your card is expired! \n have a nice day(:")

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
