# Work - McDoBot
# Author: Elyne
# 6 October

# It asks if you want fries with your meal
want_fries = input("Do you want fries with your meal?")

if want_fries.lower().strip("!.,?") == "yes":
    print("Got it! Adding fries to your meal! Would you like anything else?")
elif want_fries.lower().strip("!.") == "no":
    print("Alright, no fries then. What else would you like?")
else:
    print("Sorry, I don't understand...")

# It should accept  Yes/yes  or  No/no
# as inputs, and reply appropriately depending on the answer.
# If the user inputs anything else.
# it should repeat back their answer and
# say that it does not understand.
