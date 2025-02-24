import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(host = 'localhost',
                                   database = 'carboninfo',
                                   user = 'root',
                                   password = '')
    print("Connection Established")

except Error as e:
    print("Error connecting to MySQL Datavase", e)

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    #print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
