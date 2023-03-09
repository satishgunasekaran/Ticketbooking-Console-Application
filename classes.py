from collections import *
class User:
    def __init__(self, username, password, role="user"):
        self.username = username
        self.password = password
        self.bookings = {}
        self.role = role

class Theater:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.screens = {}
    
    def add_screen(self, screen):
        if screen.name in self.screens:
            print("Screen already exists!")
        else:
            self.screens[screen.name] = screen
            print(f"Screen {screen.name} added successfully! to theatre {self.name}")
    
    def info(self):
        print(f"\n{self.name} Theatre screens: ")
        print("----------------------------")
        for screen in self.screens.values():
            print(f"{screen.name} shows: ")
            for show in screen.shows.values():
                print(f"{show.time[0]} - {show.time[1]} : {show.movie_name}")
            print("----------------------------")

        print("-----------------------------\n")
        
class Screen:
    def __init__(self, name):
        self.name = name
        self.shows = {}
        self.movies = defaultdict(lambda:[])
    
    def add_show(self, show):
        if show.time in self.shows:
            print("Show already exists!")
        else:
            self.shows[show.time] = show
            self.movies[show.movie_name].append(show)
            print(f"Show {show.movie_name} added successfully! to screen {self.name}")

class Show:
    def __init__(self, movie_name, time):
        self.movie_name = movie_name
        self.time = time
        self.seats = {"A1":None, "A2":None, "A3":None ,"A4":None, "A5":None, "A6":None, "A7":None, "A8":None, "A9":None, "A10":None, "A11": None, "A12": None}
    
    def available_seats(self):
        count = 0
        # print 3 seats in a row
        
        for i in range(1, 13):
            if self.seats[f"A{i}"] is None:
                count += 1
                print(f"A{i}", end=" ")
            else:
                print("XX", end=" ")
            if i % 3 == 0:
                print()

        return count

   

class Booking:
    def __init__(self,booking_id, username, theatre, screen ,show_time,movie_name,seat):
        self.booking_id = booking_id
        self.username = username
        self.show_time = show_time
        self.movie_name = movie_name
        self.seat = seat
        self.theatre = theatre
        self.screen = screen

    def __str__(self):
        return f"\n-----------------------------\nBooking ID: {self.booking_id}\nUser: {self.username}\nMovie: {self.movie_name}\nTheatre: {self.theatre}\nScreen: {self.screen}\nShow Time: {self.show_time}\nSeat: {self.seat}"
