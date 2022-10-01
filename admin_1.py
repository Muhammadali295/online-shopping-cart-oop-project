from customer import Products,color
class admin:
    #Takes id and password from user
    def Enter_id_and_password(self):

        self.id= int(input('Enter id'))
        self.password = str(input('Enter Password'))
        if self.id == 4 and self.password == 'oop':
            admin.ask(self)
        else:
            print('Id and Password doesnot match, please try again')
            return admin.Enter_id_and_password(self)
    # ask whether to add product , delete product ,view product or view customer record



    #ask whether to do any more changes or not
    def ask(self):
        '''user views for the product for entering 1,adds the product for entering 2,
        views the customer record for entering 3 and deletes the product for entering 4 and display the stock of products for entering 5'''
        ask = int(input('Do you want to \n1)view product \n2)add product \n3)view customer record'
                        ' \n4)delete product\n5)display quantity\nEnter any number to continue'))
        if ask == 1:
            k = int(input('enter which types of products you want to see 1st?\n'
                          'press 1 for washing products\npress 2 for glocery\npress 3 for cosmetics\npress 4 for gadgets'))
            Products(k).display_products()
            admin.ask_more(self)
        elif ask == 2:
            admin.add_product(self)
        elif ask == 3:
            admin.customer_record(self)
        elif ask ==4:
            admin.delete_product(self)
        elif ask == 5:
            admin.display_stock(self)
        else:
            print('please enter appropriate number')

    # adds the desired product given by admin
    def add_product(self):
        '''adds the products of grocery for entering 1,adds the product of cosmetics for entering 2,
        adds the product of gadgets for entering 3,Exits for entering 4'''
        self.product_number =int(input('please enter number of product type to add product\n1)washing products\n2)grocery\n3)cosmetics\n4)gadgets'))
        if self.product_number== 1:
            self.product_amount = int(input('how many number of products do you want to enter'))
            for i in range(0,self.product_amount):
                self.product_id=int(input('product id:'))
                self.washing_name = str(input('please enter washing name:'))
                self.washing_price= int(input('please enter washing price per kg:'))
                self.quantity = int(input('please enter quantity of products which you are adding in stock:'))
                with open('washing_products.txt','a+') as o:
                    washing_list=f'{self.product_id},{self.washing_name},{self.washing_price},{self.quantity}'
                    o.write(str(washing_list)+'\n')
                    o.close()

            admin.ask_more(self)

        elif self.product_number== 2:
            self.product_amount = int(input('how many number of products do you want to enter'))
            for i in range(0, self.product_amount):
                self.product_id = int(input('product id:'))
                self.grocery_name = str(input('please enter grocery name'))
                self.grocery_price= int(input('please enter grocery price'))
                self.quantity = int(input('please enter quantity of products which you are adding in stock:'))

                with open('grocery.txt','a+') as f:
                    grocery_list=f'{self.product_id},{self.grocery_name},{self.grocery_price},{self.quantity}'
                    f.write(str(grocery_list)+'\n')
                    f.close()
            admin.ask_more(self)

        elif self.product_number== 3:
            self.product_amount = int(input('how many number of products do you want to enter'))
            for i in range(0, self.product_amount):
                self.product_id = int(input('product id:'))
                self.cosmetics_name= str(input('please enter cosmetics name'))
                self.cosmetics_price= int(input('please enter cosmetics price'))
                self.quantity = int(input('please enter quantity of products which you are adding in stock:'))
                with open('cosmetics.txt','a+') as f:
                    cosmetics_list=f'{self.product_id},{self.cosmetics_name},{self.cosmetics_price},{self.quantity}'
                    f.write(str(cosmetics_list)+'\n')
                    f.close()
            admin.ask_more(self)

        elif self.product_number== 4:
            self.product_amount = int(input('how many number of products do you want to enter'))
            for i in range(0, self.product_amount):
                self.product_id = int(input('product id:'))
                self.gadgets_name= str(input('please enter gadget name'))
                self.gadgets_price= int(input('please enter gadget price'))
                self.quantity = int(input('please enter quantity of products which you are adding in stock:'))
                with open('gadgets_1.txt','a+') as f:
                    gadgets_list=f'{self.product_id},{self.gadgets_name},{self.gadgets_price},{self.quantity}'
                    f.write(str(gadgets_list)+'\n')
                    f.close()
            admin.ask_more(self)
        else :
            print('please type appropriate number')
            admin.add_product(self)

    # ask whether to do any more changes or not
    def ask_more(self):
        self.changes = int(input('\nDo you want to do any more changes\ntype 1 for yes\nand 2 for no\nEnter any number to continue:'))
        if self.changes == 1:
            self.ask_1 = int(input('Do you want to \n1)view product \n2)add product \n3)view customer record \n'
                                   '4)delete product\n5)display quantity\nEnter any number to continue'))
            if self.ask_1 == 1:
                k = int(input('enter which types of products you want to see 1st?\n'
                      'press 1 for washing products\npress 2 for glocery\npress 3 for cosmetics\npress 4 for gadgets'))
                Products(k).display_products()
            elif self.ask_1 == 2:
                admin.add_product(self)
            elif self.ask_1 == 3:
                admin.customer_record(self)
            elif self.ask_1 == 4:
                admin.delete_product(self)
            elif self.ask_1 == 5:
                admin.display_stock(self)
            else:
                print('please enter appropriate number')
                admin.ask_more(self)
            #user views for the product for entering 1,adds the product for entering 2,
            # views the customer record for entering 3 and deletes the product for entering 4
        elif self.changes == 2:
            print('Have a nice day (:')
            #runs when user says no to any more changes

        else :
            print('please enter appropriate number')
            admin.ask_more(self)
            #runs when appropriate number is not given in the self.changes

    # deletes the product given by admin
    def file(self):
        self.j= int(input('enter which types of products you want to see 1st?\n'
                      'press 1 for washing products\npress 2 for glocery\npress 3 for cosmetics\npress 4 for gadgets'))
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
    def delete_product(self):
        admin.file(self)
        with open(self.file, 'r') as f:
            k = f.read()
            g = k.split('\n')
            g.pop()
            pr_id = []
            print(g)
            for i in range(len(g)):
                l = g[i].split(',')
                pr_id.append(l[0])
                print(i + 1, 'name of product:', l[1], '\n''price:', l[2] + 'rs', '\n''product id:', l[0])
        #print(l)
        #print(pr_id)
        id = []
        h = int(input('how many products do you want to remove:'))
        for i in range(0, h):
            id_ = input('enter product id:')
            id.append(id_)
            # with open(self.file, 'r') as f:
        for i in id:
            for j in range(len(pr_id)):
                if pr_id[j] == i:
                    g[j:(j + 1)] = ''

        with open(self.file, 'w') as f:
            for i in range(len(g)):
                f.write(g[i] + '\n')

        admin.ask_more(self)


    def customer_record(self):
        '''view the record of customers to admin'''
        with open('login.txt') as f:
            lines = f.read()
            l = lines.split('\n')
            l.pop()
            print('total no of customers are:', len(l))
        for i in range(len(l)):
            s = l[i].split(',')
            print('\t', 'customer', ':-', i + 1, '\nuser name:', s[0], '\nemail:', s[1], '\npassword:', s[2])
            print('============')

        admin.ask_more(self)

    def display_stock(self):
        '''view the stock of products available so admin can add it'''
        admin.file(self)
        with open(self.file,'r') as f:
            l=f.read()
            k=l.split('\n')
            k.pop()
            qan=[]
            for i in range(len(k)):
                z= k[i].split(',')
                print(i + 1, 'name of product:',z[1])
                qan.append(z[3])
                if int(z[3])< 50:
                    print('quantity:',color.RED + z[3] + color.END)
                else:
                    print('quantity',z[3])
            admin.ask_more(self)

a1 =admin()
a1.Enter_id_and_password()
