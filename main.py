import random
class Level25:
    def freak_accident(self, prob):
        r = random.random()
        if r < prob:
            random.randint(0, num_options)
            #call freak accident associated with num

    def budgeting(self, num, points, budgeting_mistakes):
        if num == 1:
            display_text = ("You cracked your phone screen! Do you (1) buy the newest phone for $1000 "
                            "or (2) go with last year's model for $500 and save the rest?")

            i = input(display_text)
            if i == "1":
                display_text = ("That might not have been the best choice :("
                                "when it comes to budgeting, it's important to know the difference between"
                                "items that are wants and items that are needs! -5 points")

                points -= 5
                budgeting_mistakes += 1

            elif i == "2":
                display_text = "good choice! that was good budgeting. +5 point!"
                points += 5

            else:
                display_text = ("not a valid choice")

        if num == 2:
            display_text = ("Your car is in the shop so you can't take it to work for the week. "
                               "Do you (1) take the subway for $2.90 every day or (2)  take an Uber for $30 every day")
            i = input(display_text)
            if i == "1":
                display_text = ("That might not have been the best financial choice :("
                                "Taking public transportation is a great way to cut down on spending! -5 points")

                points -= 5
                budgeting_mistakes += 1

            elif i == "2":
                display_text = "good choice! that was great budgeting. +5 point!"
                points += 5

            else:
                display_text = ("not a valid choice")
        
        if num == 3:
            display_text = ("")
    
    def loans(self, loan_amount, interest_rates):
        display_text =  ""
        #figure out based on interest rates and repayment plan
    
    def taxes(self):
        
