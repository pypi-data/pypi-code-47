import os


def chocobo_roast(num_guests, hotness_level):
    guests = ""
    if(num_guests > 1):
        guests = "Guests"
    else:
        guests = "Guest"
    print("{} {} and {} Level of hotness".format(num_guests, guests,hotness_level))



chocobo_roast(1, 10)