
class main:
    '''user enters as an admin for entering as admin and enters as a customer for entering as a customer'''
    @staticmethod
    def ask():
        # ask whether to enter as admin or customer
        option = input('Do you want to enter as admin or customer\ntype c for customer and a for admin:')
        if option == 'c':
            from register import Register
        elif option == 'a':
            from admin_1 import admin
        else:
            print('please write correct option')
            main.ask()

m=main
m.ask()

