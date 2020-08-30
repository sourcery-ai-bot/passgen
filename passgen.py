import secrets
import os
import time

filename = 'pass.txt'
base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!!!!@@@@####$$$$%&%&%&%&****'
print('you password cant be longer than ' + str(len(base) - 21) + '.')

class Password:
    def __init__(self, size, amount, path):
        self.size = size
        self.amount = amount
        self.list = []
        self.path = path

    def generate_list(self):
        password_list = []

        for j in range (self.amount):
            password = ""
            for _ in range (self.size):
                nextchar = base[secrets.randbelow(len(base))]
                while (nextchar in password):
                    nextchar = base[secrets.randbelow(len(base))]
                password += nextchar
            password_list.append(password)

        self.list = password_list

    def create_new_file(self):
        if os.path.exists(self.path):
            os.remove(self.path)
        
        self.file = open(self.path, 'w+')

    def print_toscreen(self):
        for j in self.list:
            print(j)

    def writetofile_andclose(self):
        for j in self.list:
            self.file.write(j + '\n')
        self.file.close()

def generate_new_password(filename):
    amount = int(input('how many passwords do you want to generate: '))
    size = int(input('insert the size of each password: '))

    if size > 0 and not size > 69 and amount > 0:
        p = Password(size, amount, filename)
        p.generate_list()
       
        output = input('I generated your passwords, do you want it to be written in a file?(y/n, default = y)')
        if output == 'n':
            p.print_toscreen()
        else:
            p.create_new_file()
            p.writetofile_andclose()

    else:
        print("I can't generate your password with the given numbers.")

while True:
    try:
        action = int(input('what do you want to do:\n'  +
                '1 - generate a new password list\n'     +
                '2 - change file name\n' +
                '3 - quit\n'))

        if action is 1:
            generate_new_password(filename)
            print('your passwords were printed.')
        elif action is 2:
            filename = input('insert your new file name(extension will automatically be .txt): ') + '.txt'
            os.system('cls')
            print('ok.')
        elif action is 3:
            os.system('cls')
            print('goodbye.')
            time.sleep(3)
            quit()
    except ValueError:
            print('you can only type numbers, the program will now close.')
            time.sleep(5)
            quit()



