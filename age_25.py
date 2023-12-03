import random


class Level25:
    def __init__(self, level):
        self.level = level

    home_insurance = False
    car_insurance = False
    health_insurance = False

    def insurance(self,points):
        # Health insurance
        x = input("will you buy health insurance" )
        print(x)
        while x not in ["yes", "Yes", "y", "Y", "YES", "no", "No", "n", "N", "NO"]:
            print("Invalid response. Try again.")
            x = input()
        if x in ["yes", "Yes", "y", "Y", "YES"]:
            print("Good option! It's always important to have health insurance considering the high hospital costs")
            health_insurance = True
            points += 10
        else:
            print("Bad option! While you may be a healthy person, it's always important to have health insurance considering the high hospital costs")
            health_insurance = False
            points -= 10
        # car insurance
        y = input("will you buy car insurance")
        print(y)
        while y not in ["yes", "Yes", "y", "Y", "YES", "no", "No", "n", "N", "NO"]:
            print("Invalid response. Try again.")
            x = input()
        if y in ["yes", "Yes", "y", "Y", "YES"]:
            print("Good option! It's always important to have car insurance. Accidents can happen any time!")
            car_insurance = True
            points += 10
        else:
            print("Bad option! While you may be a safe driver, other people can damage your car and fixing your car is expensive!")
            car_insurance = False
            points -= 10

        # home insurance
        z = input("will you buy house insurance")
        while z not in ["yes", "Yes", "y", "Y", "YES", "no", "No", "n", "N", "NO"]:
            print("Invalid response. Try again.")
            x = input()
        if z in ["yes", "Yes", "y", "Y", "YES"]:
            print("Good option! It's always important to have house insurance in case of emergencies such as natural disasters or theft")
            home_insurance = True
            points += 10
        else:
            print("Bad option! It would be a huge financial burden to fix the house in case of issues like natural disasters! ")
            home_insurance = False
            points -= 10
        return points

    def taxes(self, points):
        user_choice = input("April is here and your taxes are due soon, are you going to pay them now? Type Yes or No ")
        while user_choice not in ["Yes", "No"]:
            print(user_choice)
        if user_choice == "Yes":
            print("that's a good choice \n"
                  "income tax is the tax on money you earn from your jobs. They are often due annually. \
                  Failure to pay could result in penalties or interest charges, negatively affect your credit score, etc. ")
            points += 5
        elif user_choice == "No":
            print("wrong choice! \n"
                  "Income tax is the tax on money you earn from your jobs. \n" "They are often due annually. \n"
                  "Failure to pay could result in penalties or interest charges, negative effect on credit score, etc. ")
            points -= 5

        return points

    def freak_accident(self, prob=.6,):
        r = random.random()
        if r < prob:
            option = random.randint(1, 3)
            # call freak accident associated with num
            if option == 1:
                print("Oh No! You broke your leg while riding a bike!.")
                if health_insurance == False:
                    print("You didn't invest in health insurance! The damages costs $35,000.")
                else:
                    print("You invested in health insurance! The damages to your health have been covered.")
            elif option == 2:
                print("Oh No! Someone on the freeway slammed into the back of your car!")
                if car_insurance == False:
                    print("You didn't invest in car insurance! The damages costs $10,000.")
                else:
                    print("You invested in car insurance! The damages to your car have been covered.")
            else:
                print("Oh No! You left your stove on and your house burns down.")
                if home_insurance == False:
                    print("You didn't invest in home insurance! The damages costs $50,000.")
                else:
                    print("You invested in home insurance! The damages to your house have been covered.")

    def budgeting(self, num, points):
        if num == 1:
            display_text = ("You cracked your phone screen! Do you (1) buy the newest phone for $1000 "
                            "or (2) go with last year's model for $500 and save the rest? Choose 1 or 2")

            i = input(display_text)
            while i not in ["1", "2"]:
                print(i)
            if i == "1":
                display_text = ("That might not have been the best choice :("
                                " when it comes to budgeting, it's important to know the difference between"
                                "items that are wants and items that are needs! -5 points")
                print(display_text)

                points -= 5
            else:
                display_text = "good choice! that was good budgeting. +5 point!"
                print(display_text)
                points += 5


        if num == 2:
            display_text = ("Your car is in the shop so you can't take it to work today. "
                            "Do you (1) take the subway for $2.90 or (2)  take an Uber for $30? Choose 1 or 2 ")
            i = input(display_text)
            while i not in ["1", "2"]:
                print(i)
            if i == "2":
                display_text = ("That might not have been the best choice"
                                "when it comes to budgeting, it's important to know the difference between"
                                "items that are wants and items that are needs! -5 points")
                print(display_text)
                points -= 5
            else:
                display_text = "good choice! that was good budgeting. +5 point!"
                print(display_text)
                points += 5
        return points

    def emergency_fund(self, points):
        user_choice = input("you are saving 1000 per month, do you want to save some for emergency fund? yes or no?")
        while user_choice not in ["yes", "no"]:
            user_choice = input(
                "you are saving 1000 per month, do you want to save some for emergency fund? yes or no?")
        if user_choice == "yes":
            print("Good Job! It's always important to have some money saved in case an emergency occurs")
            points += 15
        else:
            print("While it may not seem important right now, it's always important to have some money saved in case\
                   an emergency occurs ")
            points -= 15
        return points

    def taxes(self, points):
        user_choice = input("April is here and your taxes are due soon, are you going to pay them now? Type Yes or No ")
        if user_choice == "Yes":
            print("that's a good choice \n"
                  "income tax is the tax on money you earn from your jobs. They are often due annually. \
                  Failure to pay could result in penalties or interest charges, negatively affect your credit score, etc. ")
            points += 5
        elif user_choice == "No":
            print("wrong choice! \n"
                  "Income tax is the tax on money you earn from your jobs. \n" "They are often due annually. \n"
                  "Failure to pay could result in penalties or interest charges, negative effect on credit score, etc. ")
            points -= 5

        else:
            user_choice = input(
                "April is here and your taxes are due soon, are you going to pay them now? Type Yes or No ")
            print(user_choice)

        return points


