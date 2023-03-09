import random
from classes import *
from collections import *
from dilmovies import *

def admin_menu_util(self, admin):
    while (True):
        print("Welcome to Admin Menu\n")
        print("1. Add theater")
        print("2. Add screen")
        print("3. Add show")
        print("4. Partner theatres Information")
        print("0. Exit Admin Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            theatre_name = input("Enter theater name: ")
            location = input("Enter theater location: ")
            theater = Theater(theatre_name, location)
            self.add_theater(theater)
        
        elif choice == "2":
            theater_name = input("Enter theater name: ")

            if theater_name in self.theaters:
                theater:Theater = self.theaters[theater_name]
                screen_name = input("Enter screen name: ")
                screen = Screen(screen_name)
                theater.add_screen(screen)
            else:
                print("Theater not found!")
        
        elif choice == "3":
            theater_name = input("Enter theater name: ")
            if theater_name in self.theaters:
                theater = self.theaters[theater_name]
                screen_name = input("Enter screen name: ")
                if screen_name in theater.screens:
                    screen:Screen = theater.screens[screen_name]
                    movie_name = input("Enter movie name: ")
                    start = input("Enter start time: ")
                    end = input("Enter end time: ")
                    time = (start, end)
                    show = Show(movie_name, time)
                    screen.add_show(show)
                else:
                    print("Screen not found!")
            else:
                print("Theater not found!")

        elif choice == "4":

            print("Our partner theatres are: \n")
            for theater in self.theaters:
                print(self.theaters[theater].name)
            print("\n")
                
            theater_name = input("Enter theater name: ")
            if theater_name in self.theaters:
                theater = self.theaters[theater_name]
                theater.info()
            else:
                print("Theater not found!")
        
        elif choice == "0":
            break

def user_menu_util(self, user):
    while (True):
        print("Welcome to User Menu\n")
        print("1. Search movie and Book ticket")
        print("2. My bookings")
        print("3. Cancel ticket")
        print("0. Exit User Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            movie_name = input("Enter movie name: ")
            print("Available theatres are: ")
            print("---------------------------------")

            for theater_name in self.theaters:
                theater = self.theaters[theater_name]
                
                for screen_name in theater.screens:
                    screen = theater.screens[screen_name]
                    
                    for show_time in screen.shows:
                        show = screen.shows[show_time]
                        if show.movie_name == movie_name:
                            print("Theater: ", theater.name)
                            print("Screen: ", screen.name)
                            print("Movie: ", show.movie_name)
                            print("Start time: ", show.time[0])
                            print("End time: ", show.time[1])
                            # print("Available seats: ", show.available_seats())
                            # print("Seats: ", show.seats)
                            print("---------------------------------")

                           
            book_choice = input("Do you want to book a ticket? (y/n): ")
            if book_choice == "y":
                theater_name = input("Enter theater name: ")
                if theater_name in self.theaters:
                    theater = self.theaters[theater_name]
                    screen_name = input("Enter screen name: ")
                    if screen_name in theater.screens:
                        screen = theater.screens[screen_name]
                        if movie_name in screen.movies:
                            start_time = int(input("Enter start time: "))
                            end_time = int(input("Enter end time: "))
                            time = (start_time, end_time)
                            if time in screen.shows:
                                show = screen.shows[time]
                                if show.available_seats() > 0:
                                    needed_seats = list(input("Enter seats separated by comma (A1,A2 ...) ").split(","))

                                    for seat in needed_seats:
                                        if seat in show.seats:
                                            if show.seats[seat] == None:
                                                show.seats[seat] = user.username
                                                print("Seat booked!")
                                                booking_id = random.randint(1000, 9999)
                                                booking = Booking(booking_id,user.username, theater.name, screen.name,  show.timeshow.movie_name, seat)
                                                user.bookings[booking_id] = booking
                                            else:
                                                print("Seat already booked!")
                                                break
                                        else:
                                            print("Seat not found!")
                                else:
                                    print("Sorry, no seats available!")
                            else:
                                print("Show not found!")
                            
                        else:
                            print("Show not found!")
                    else:
                        print("Screen not found!")


                            

        elif choice == "2":
            for booking_id in user.bookings:
                print(user.bookings[booking_id])
        elif choice == "3":
            booking_id = int(input("Enter booking id: "))
            if booking_id in user.bookings:
                booking = user.bookings[booking_id]
                theater = self.theaters[booking.theatre]
                screen = theater.screens[booking.screen]
                show = screen.shows[booking.show_time]
                show.seats[booking.seat] = None
                del user.bookings[booking_id]
                print("Ticket cancelled!")
            else:
                print("Booking not found!")
                         
        elif choice == "0":
            break
