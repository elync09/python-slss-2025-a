# Work - Math problems
# Author: Elyne
# 14 November

# Solving math problems

# Question 1
def main():
    current_age = int(input("How old are you?"))
    # Difference between this year and 2049
    age_in_2049 = current_age + 31
    # Results
    print(f"You will be {age_in_2049} in 2049")
main()


# Question 2
def main():
    """5 judges give a
    score, results will be printed"""

    # Get judges to vote
    print("Please give a score from 0-10, half scores are allowed")
    score1 = float(input("Judge 1: "))
    score2 = float(input("Judge 2: "))
    score3 = float(input("Judge 3: "))
    score4 = float(input("Judge 4: "))
    score5 = float(input("Judge 5: "))

    # Calculate average source
    average_score = (score1 + score2 + score3 + score4 + score5) / 5

    # Announce final score
    print(f"Your Olympic score is: {average_score}")

main()

def main():
    """Ask customer if they
    want burger and fries
    then adds 14% of tax"""
    # Ask customer if they want a burger
    want_burger = input("Would you like a burger for $5? (Yes/No): ")

    if want_burger.lower().strip("!.,?") == "yes":
        burger_price = 5
        print("Got it! Adding a burger to your order!")
    else:
        burger_price = 0
        print("Alright, no burgers then.")

    # Ask customer if they want fries
    want_fries = input("Would you like some fries for $3? (Yes/No): ")

    if want_fries.lower().strip("!.,?") == "yes":
        fries_price = 3
        print("Sure, let me add that to your order!")
    else:
        fries_price = 0
        print("I see, no fries then!")

    # Calculate total before tax
    subtotal = burger_price + fries_price

    # Add the 14% tax
    tax = subtotal * 0.14

    # Final cost
    total_price = subtotal + tax

    print(f"Your total including tax will be: {total_price}")
main()
