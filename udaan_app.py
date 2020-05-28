"""This program allows the user to select the place they wish to visit.
The chosen place is passed to the class Planner."""

from udaan import Planner

list_of_places = {1: "goa",
                  2: "coorg",
                  3: "gokarna"}

print(" - - - - - -WELCOME TO UDAAN - - - - - - \n")
while True:
    user_input = False
    print("We are currently planning trips to:\n1) Goa\n2) Coorg\n3) Gokarna")
    user_input = int(input("Choose the place you wish to visit  "))

    if user_input not in list_of_places.keys():
        print("Invalid entry. Please select a place from the above list")

    else:
        place = list_of_places.get(user_input).lower()
        planner_object = Planner()
        planner_object.days_enquiry(place)
        planner_object.hotel_type_enquiry()
        planner_object.total_cost(place)
        planner_object.extra(place)
        planner_object.gui(place)
        break
