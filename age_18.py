import random


class Level18:
    def __init__(self, level):
        self.level = level

    def college_choice(self, points):
        print("You have the choice between Syracuse and Cornell. Syracuse is offering\n"
              "to give you half off for tuition, while Cornell is full price.")
        x = input("Which college will you chose to attend? ")
        while x not in ["S", "C", "Syracuse", "Cornell"]:
            print("Invalid answer. Try again.")
        if x in ["S", "Syracuse"]:
            print("This option is a very financially beneficial decision. +10 points")
            points += 10
        else:
            print("This option is not the most financially beneficial decision, but\n"
                  "there are a lot of other factors when it comes to picking colleges.\n"
                  "It just matters how you plan to pay for college without getting into\n"
                  "too much debt. -10 points")
            points -= 10

        return points

    

    def bank_loan(self, points):
            print("To pay for your college, you would need an education loan \
              Bank A offers a loan of $50,000 at the fixed interest rate of 6.37% to be payed over the span of 6 years \
            Bank B offers a loan of $60,000 at the fixed interest rate of 4.2% to be payed over the span of 6 years"
              )

            user_choice = input("which bank's loan would be more beneficial? Hint: look at interest rates -> ")
            while user_choice not in "A" or "B" or "Bank A" or "Bank B":
                print("Invalid. go again")
                print(user_choice)
            if user_choice == "A" or user_choice == "Bank A":
                print("Good Job!")
                points += 10
            else:
                print("Unfortunately the total repayment amount is higher for Loan B")
                points -= 10
            print("First convert the interest rate percentage to decimal. Then, find the total interest paid by multiplying \
              the loan amount with the interest rate and \
              repayment period of 5 years \
              Finally, find the total repayment by adding the loan amount and the total interest paid")

            return points

        # Loan A is better in terms of minimizing the total repayment amount

    def bank_account(self, points):
        print("You just started a job and now you are earning money.")
        x = input("Would you like to open a bank account?")
        while x not in ["yes", "Yes", "y", "Y", "YES", "no", "No", "n", "N", "NO"]:
            print("Invalid response. Try again.")
            x = input()
        if x in ["yes", "Yes", "y", "Y", "YES"]:
            print("Correct! Opening a bank account allows you to keep your maney safe, the money is protected\n" 
                  "from error and fraud, and make online purchases with ease.")
            points += 10
        else:
            print("That's not best choice. Opening a bank account allows you to keep your maney safe, the money\n" 
            "is protected from error and fraud, and make online purchases with ease.")
            points -= 10

        return points
    
    def budgeting(self, points):
            display_text = ("You cracked your phone screen! Do you (1) buy the newest phone for $1000 "
                            "or (2) go with last year's model for $500 and save the rest?")

            i = input(display_text)
            print(i)
            while i not in ["1","2"]:
                print(i)
            if i == "1":
                display_text = ("That might not have been the best choice :("
                                "when it comes to budgeting, it's important to know the difference between"
                                "items that are wants and items that are needs! -5 points")

                print(display_text)
                points -= 5
            elif i == "2":
                display_text = "good choice! that was good budgeting. +5 point!"
                points += 5
                print(display_text)


            display_text2 = ("Your car is in the shop so you can't take it to work today. "
                            "Do you (1) take the subway for $2.90 or (2) take an Uber for $30")
            y = input(display_text2)
            print(y)
            while y not in ["1","2"]:
                print(y)
            if y == "1":
                display_text2 = "good choice! that was good budgeting. +5 point!"
                points += 5
                print(display_text2)


            else:
                display_text2 = ("That might not have been the best choice :("
                                "when it comes to budgeting, it's important to know the difference between"
                                "items that are wants and items that are needs! -5 points")
                points -= 5
                print(display_text2)

            return points


    def credit(self, points):
        # question 1
        x = input("Do you want to apply for a credit card?")
        while x not in ["yes", "Yes", "y", "Y", "YES", "no", "No", "n", "N", "NO"]:
            print("Invalid response. Try again.")
            x = input()
        if x in ["yes", "Yes", "y", "Y", "YES"]:
            print("Yes! Building your credit can create oppertunities for getting low-interest\n"
                  "on mortgages, personal loans/credit cards, and end up paying less money during\n" 
                  "the term of your loan and have more of savings. The younger you start, the more\n"
                  "benifical it will be.")
            points += 5
        else:
            print("This is not the best choice. Building your credit can create oppertunities for\n"
                  "getting low-interest on mortgages, personal loans/credit cards, and end up paying\n"
                  "less money during the term of your loan and have more of savings. If you have more\n"
                  "money for savings, you can use it to invest in your future.")
            points -= 5
        # question 2
        print("Your credit card payments are due.")
        x = input("Do you pay them?")
        while x not in ["yes", "Yes", "y", "Y", "YES", "no", "No", "n", "N", "NO"]:
            print("Invalid response. Try again.")
            x = input()
        if x in ["yes", "Yes", "y", "Y", "YES"]:
            print("Great job! Having a bad credit score will affect you by having trouble taking out\n"
                  "a credit card, car loan, or a mortgage. The other consequenses is causing higher interest\n"
                  "rates and fewer loan options. Paying your credit is important!")
            points += 10
        else:
            print("This is a bad choice. Having a bad credit score will affect you by having trouble\n"
                  "taking out a credit card, car loan, or a mortgage. The other consequenses is causing\n"
                  "higher interest rates and fewer loan options. Paying your credit is important!")
            points -= 10
        # question 3
        x = input("What will the minimum payment on a $500 credit card if the minimum payment\n"
                  "percentage is 2%?")
        if x in ["10", "$10", "ten", "ten dollars"]:
            print("Yes correct! Good job! Make sure to always pay the minimun spending amount on your\n"
                  "credit card because if you don't, you could be charged a late fee and risk having your\n"
                  "card suspended. Also, you can miss out on credit card rewards.")
            points += 5
        else:
            print("The correct answer is $10. Make sure to always pay the minimun spending amount on your\n"
                  "credit card because if you don't, you could be charged a late fee and risk having your\n"
                  "card suspended. Also, you can miss out on credit card rewards.")
            points -= 5

        return points

# if __name__ == '__age 18__':
#     MyApp().run()
