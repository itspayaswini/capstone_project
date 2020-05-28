import pyautogui as pg
from tabulate import tabulate
import time


class Planner:
	"""Parent/Base class"""
	def __init__(self):
		self.cost_per_night = {"coorg": 2000, "gokarna": 2500, "goa": 2500}
		self.hotel_cost = {1: 1500, 2: 2500, 3: 5000}

	def days_enquiry(self, place):
    	
		print(f"Cost per day for {place} is Rs {self.cost_per_night.get(place)}.This cost includes food and the travel charges.")
		self.night_count = int(input("Enter the number of nights you wish to stay  "))
		self.package_cost = self.cost_per_night.get(place)*self.night_count

	def hotel_type_enquiry(self):
	#Allows the user to choose the type of hotel they wish to stay in

		while True:
            self.hotel_type = False
            print("Please select the type of hotel you wish to stay in:\n\
				1)1-star\n\
				2)2-star\n\
				3)3-star\n ")
            self.hotel_type = int(input())
            if self.hotel_type not in [1, 2, 3]:
                print("Enter valid choice")
            else:
                break

	def total_cost(self, place):
    	"""Computes the total cost of the trip."""

        self.cost_of_stay = self.hotel_cost.get
        (self.hotel_type) * self.night_count
        self.bill = self.cost_of_stay + self.package_cost
        table = [["Place", place], ["Number of nights", self.night_count],
                 ["Food and Transportation", self.package_cost],
                 ["Hotel Type", str(self.hotel_type) + " star"],
                 ["Total Cost of the Trip per person\n(Cost exclusive of GST)",
                  "Rs " + str(self.bill)]]
        print(tabulate(table, tablefmt="fancy_grid"))

    def extra(self, place):
    	"""Any extra feautures can be added here"""

        print(f"Here are some of the things you can do in {place}")

    def gui(self, place):
    	"""Displays some of must visit places on google chrome using pyautogui"""

        time.sleep(5)
        if place == "coorg":
            pg.press('win')
            pg.typewrite('chrome', .5)
            pg.PAUSE = 2
            pg.press('enter')
            pg.typewrite(
                'https://www.tripsavvy.com/places-to-visit-in-coorg-1539466', 0.1)
            pg.PAUSE = 2
            pg.press('enter')
        elif place == "gokarna":
            pg.press('win')
            pg.typewrite('chrome', .5)
            pg.PAUSE = 2
            pg.press('enter')
            pg.typewrite(
                'https://traveltriangle.com/blog/things-to-do-in-gokarna/', 0.1)
            pg.PAUSE = 2
            pg.press('enter')
        elif place == "goa":
            pg.press('win')
            pg.typewrite('chrome', .5)
            pg.PAUSE = 2
            pg.press('enter')
            pg.typewrite(
                'http://www.transindiatravels.com/goa/tourist-places-to-visit-in-goa/', 0.1)
            pg.PAUSE = 2
            pg.press('enter')
