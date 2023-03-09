
from dilmovies import *
dilmovies = DILMovies()

dilmovies.admins["admin"] = User("admin", "1234", "admin")
dilmovies.add_user("satish","1234")


# Miraj theater
miraj = Theater("Miraj", "Coimbatore")

screen1 = Screen("Screen 1")
screen2 = Screen("Screen 2")


show1 = Show("Vaathi",(10, 13))
show4 = Show("Vaathi",(14, 17))

show2 = Show("Master",(14, 17))
show3 = Show("Tenet",(10, 13))


screen1.shows[show1.time] = show1
screen1.shows[show4.time] = show4

screen2.shows[show2.time] = show2
screen2.shows[show3.time] = show3


screen1.movies[show1.movie_name].append(show1) 
screen2.movies[show2.movie_name].append(show2)
screen2.movies[show3.movie_name].append(show3)

miraj.add_screen(screen1)
miraj.add_screen(screen2)


dilmovies.add_theater(miraj)

# End of Miraj theater


def main():
    while (True):
        print("Welcome to DIL Movies\n")
        print("1. Login")
        print("2. Register")
        print("0. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            user = dilmovies.login()
            if user is not None:
                if user.role == "admin":
                    dilmovies.admin_menu(user)
                else:
                    dilmovies.user_menu(user)
            
        elif choice == "2":
            user = dilmovies.register()
            dilmovies.user_menu(user)

        elif choice == "0":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()



