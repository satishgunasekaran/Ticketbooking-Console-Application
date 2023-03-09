from collections import *
from classes import *
from menus import user_menu_util, admin_menu_util

class DILMovies:
    def __init__(self):
        self.theaters = {}
        self.users = {}
        self.admins = {}

    def add_theater(self, theater):
        if theater.name in self.theaters:
            print("Theater already exists!")
        else:
            self.theaters[theater.name] = theater
            print(f"Theater {theater.name} added successfully!")
    
    def add_user(self, username, password):
        if username in self.users:
            print("User already exists!")
        else:
            user = User(username, password)
            self.users[username] = user
            print("User registered Successfully!")
        return user


    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username in self.admins and self.admins[username].password == password:
            print("Welcome admin!")
            return self.admins[username]
        elif username in self.users  and self.users[username].password  == password:
            print("Welcome user!")
            return self.users[username]
        else:
            print("Wrong username or password!")
            return None
    
    def register(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        self.users[username] = User(username, password)
        print("User registered!")
        return self.users[username]
    
    def admin_menu(self, admin):
        admin_menu_util(self, admin)

    

    def user_menu(self, user):
        user_menu_util(self, user)






   
