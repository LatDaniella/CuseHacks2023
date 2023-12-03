import random
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path

class Level18:
    def __init__(self, level):
        self.level = level

    def start_screen(self, points):
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/gianna/Documents/untitled folder 4/build/assets/frame0")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)


        window = Tk()

        window.geometry("333x600")
        window.configure(bg = "#FFFFFF")


        canvas = Canvas(
            window,
            bg = "#FFFFFF",
            height = 600,
            width = 333,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            166.0,
            333.0,
            image=image_image_1
        )

        canvas.create_rectangle(
            0.0,
            430.0,
            333.0,
            600.0,
            fill="#D9D9D9",
            outline="")

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: window.destroy(),
            relief="flat"
        )
        button_1.place(
            x=50.0,
            y=486.0,
            width=224.0,
            height=47.0
        )

        canvas.create_text(
            33.0,
            44.0,
            anchor="nw",
            text="Money Madness",
            fill="#5CD685",
            font=("MontserratRoman ExtraBold", 24 * -1)
        )
        window.resizable(False, False)
        window.mainloop()

        window.destroy()
        return points




    def college_choice(self, points):

        x = 0
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/gianna/Documents/untitled folder 2/build/assets/frame0")

        window = Tk()

        window.geometry("335x600")
        window.configure(bg = "#FFFFFF")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        def o1(num):

            canvas = Canvas(
                window,
                bg = "#FFFFFF",
                height = 600,
                width = 335,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
            )

            canvas.place(x = 0, y = 0)
            button_image_next = PhotoImage(
            file=relative_to_assets("button_next.png"))
            button_next = Button(
                image=button_image_next,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.bank_loan(points),
                relief="flat"
            )
            button_next.place(
                x=48.0,
                y=474.0,
                width=83.0,
                height=81.0
            )

            if num == 1:
                canvas.create_text(
                59.0,
                47.0,
                anchor="nw",
                text="This option is a very financially beneficial decision. +10 points",
                fill="#000000",
                font=("MontserratRoman ExtraBold", 18 * -1),
                justify= "left",
                width = 250
                )
                points += 10
                
            else:
                canvas.create_text(
                59.0,
                47.0,
                anchor="nw",
                text=("This option is not the most financially beneficial decision, but here are a lot of other factors when it comes to picking colleges."
                    " It just matters how you plan to pay for college without getting into "
                    "too much debt. -10 points"),
                fill="#000000",
                font=("MontserratRoman ExtraBold", 18 * -1),
                justify="left",
                width = 250
                )
                points -= 10

            window.resizable(False, False)
            window.mainloop()
            return points

        canvas = Canvas(
            window,
            bg = "#FFFFFF",
            height = 600,
            width = 335,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            0.0,
            430.0,
            335.0,
            600.0,
            fill="#D9D9D9",
            outline="")

        canvas.create_rectangle(
            0.0,
            234.0,
            335.0,
            430.0,
            fill="#FFFFFF",
            outline="")

        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            167.0,
            332.0,
            image=image_image_1
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: o1(1),
            relief="flat"
        )
        button_1.place(
            x=48.0,
            y=474.0,
            width=83.0,
            height=81.0
        )
    
        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: o1(2),
            relief="flat",
        )
        button_2.place(
            x=192.0,
            y=474.0,
            width=83.0,
            height=81.0
        )

        canvas.create_text(
            59.0,
            47.0,
            anchor="nw",
            text="You have the choice between Syracuse and Cornell. Syracuse is offering\n"
              "to give you half off for tuition, while Cornell is full price.\n"
                "Which college will you chose to attend? 1. Syracuse 2. Cornell",
            fill="#000000",
            font=("MontserratRoman ExtraBold", 18 * -1),
            justify= "left",
            width = 250
        )


        window.resizable(False, False)
        window.mainloop()

        window.destroy()

        return points

    
    

    def bank_loan(self, points):
            
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/gianna/Documents/untitled folder 2/build/assets/frame2")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)


        def o1(num):
            canvas = Canvas(
                window,
                bg = "#FFFFFF",
                height = 600,
                width = 335,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
            )

            canvas.place(x = 0, y = 0)
            canvas.place(x = 0, y = 0)
            button_image_next = PhotoImage(
            file=relative_to_assets("button_next.png"))
            button_next = Button(
                image=button_image_next,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.bank_account(points),
                relief="flat"
            )
            button_next.place(
                x=48.0,
                y=474.0,
                width=83.0,
                height=81.0
            )

            if num == 1:
                canvas.create_text(
                59.0,
                47.0,
                anchor="nw",
                text="Good Job! +10 points",
                fill="#000000",
                font=("MontserratRoman ExtraBold", 18 * -1),
                justify= "left",
                width = 250
                )

            else:
                canvas.create_text(
                59.0,
                47.0,
                anchor="nw",
                text="Unfortunately the total repayment amount is higher for Loan 2",
                fill="#000000",
                font=("MontserratRoman ExtraBold", 18 * -1),
                justify= "left",
                width = 250
                )
                points -= 10

        window = Tk()

        window.geometry("335x600")
        window.configure(bg = "#FFFFFF")


        canvas = Canvas(
            window,
            bg = "#FFFFFF",
            height = 600,
            width = 335,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            0.0,
            430.0,
            335.0,
            600.0,
            fill="#D9D9D9",
            outline="")

        canvas.create_text(
            59.0,
            47.0,
            anchor="nw",
            text=("To pay for your college, you would need an education loan"
            "Bank 1 offers a loan of $50,000 at the fixed interest rate of 6.37% to be payed over the span of 6 years"
            "Bank 2 offers a loan of $60,000 at the fixed interest rate of 4.2% to be payed over the span of 6 years"
            "which bank's loan would be more beneficial? Hint: look at interest rates."
            
            ),
            fill="#000000",
            font=("MontserratRoman ExtraBold", 18 * -1)
        )

        canvas.create_rectangle(
            209.0,
            13.0,
            309.0,
            113.0,
            fill="#000000",
            outline="")

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: o1(1),
            relief="flat"
        )
        button_1.place(
            x=193.0,
            y=474.0,
            width=83.0,
            height=81.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: o1(2),
            relief="flat"
        )
        button_2.place(
            x=59.0,
            y=474.0,
            width=83.0,
            height=81.0
        )

        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            169.0,
            356.0,
            image=image_image_1
        )
        window.resizable(False, False)
        window.mainloop()

        canvas = Canvas(
            window,
            bg = "#FFFFFF",
            height = 600,
            width = 335,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_text(
                59.0,
                47.0,
                anchor="nw",
                text="First convert the interest rate percentage to decimal. Then, find the total interest paid by multiplying"
                    "the loan amount with the interest rate and"
                    "repayment period of 5 years"
                    "Finally, find the total repayment by adding the loan amount and the total interest paid",
                fill="#000000",
                font=("MontserratRoman ExtraBold", 18 * -1),
                justify= "left",
                width = 250
            )

        return points

        # Loan A is better in terms of minimizing the total repayment amount



    def bank_account(self, points):
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/gianna/Documents/untitled folder 2/build/assets/frame5")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        def o1(num):
            canvas = Canvas(
                window,
                bg = "#FFFFFF",
                height = 600,
                width = 335,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
            )

            canvas.place(x = 0, y = 0)
            button_image_next = PhotoImage(
            file=relative_to_assets("button_next.png"))
            button_next = Button(
                image=button_image_next,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.budgeting(points),
                relief="flat"
            )
            button_next.place(
                x=48.0,
                y=474.0,
                width=83.0,
                height=81.0
            )

            canvas.place(x = 0, y = 0)
            if num == 2:
                canvas.create_text(
                59.0,
                47.0,
                anchor="nw",
                text="Correct! Opening a bank account allows you to keep your maney safe, the money is protected\n" 
                  "from error and fraud, and make online purchases with ease.",
                fill="#000000",
                font=("MontserratRoman ExtraBold", 18 * -1),
                justify= "left",
                width = 250
                )
                points += 10
            
            else:
                canvas.create_text(
                59.0,
                47.0,
                anchor="nw",
                text="That's not best choice. Opening a bank account allows you to keep your maney safe, the money\n" 
                "is protected from error and fraud, and make online purchases with ease.",
                fill="#000000",
                font=("MontserratRoman ExtraBold", 18 * -1),
                justify= "left",
                width = 250
                )
                points -= 10



        window = Tk()

        window.geometry("335x600")
        window.configure(bg = "#FFFFFF")


        canvas = Canvas(
            window,
            bg = "#FFFFFF",
            height = 600,
            width = 335,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_text(
            59.0,
            47.0,
            anchor="nw",
            text="You just started a job and now you are earning money. Would you like to open a bank account? 1. No 2. Yes",
            fill="#000000",
            font=("MontserratRoman ExtraBold", 18 * -1)
        )

        canvas.create_rectangle(
            0.0,
            427.0,
            335.0,
            600.0,
            fill="#D9D9D9",
            outline="")

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_1.place(
            x=209.0,
            y=474.0,
            width=83.0,
            height=81.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
            x=42.0,
            y=474.0,
            width=83.0,
            height=81.0
        )

        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            167.0,
            341.0,
            image=image_image_1
        )
        window.resizable(False, False)
        window.mainloop()

        return points
    
    def budgeting(self, points):

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/gianna/Documents/untitled folder 2/build/assets/frame8")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        def o1(num):
            canvas = Canvas(
                window,
                bg = "#FFFFFF",
                height = 600,
                width = 335,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
            )

            canvas.place(x = 0, y = 0)
            canvas.place(x = 0, y = 0)
            button_image_next = PhotoImage(
            file=relative_to_assets("button_next.png"))
            button_next = Button(
                image=button_image_next,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.credit(points),
                relief="flat"
            )
            button_next.place(
                x=48.0,
                y=474.0,
                width=83.0,
                height=81.0
            )
            if num == 1:
                canvas.create_text(
                59.0,
                47.0,
                anchor="nw",
                text="good choice! that was good budgeting. +5 point!",
                fill="#000000",
                font=("MontserratRoman ExtraBold", 18 * -1),
                justify= "left",
                width = 250
                )
                points += 5
            
            else:
                canvas.create_text(
                59.0,
                47.0,
                anchor="nw",
                text="That might not have been the best financial choice, but there are many factors to deciding your transportation! -3 points",
                fill="#000000",
                font=("MontserratRoman ExtraBold", 18 * -1),
                justify= "left",
                width = 250
                )
                points -= 3


        window = Tk()

        window.geometry("335x600")
        window.configure(bg = "#FFFFFF")


        canvas = Canvas(
            window,
            bg = "#FFFFFF",
            height = 600,
            width = 335,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            0.0,
            430.0,
            335.0,
            600.0,
            fill="#D9D9D9",
            outline="")

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: o1(1),
            relief="flat"
        )
        button_1.place(
            x=209.0,
            y=474.0,
            width=83.0,
            height=81.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: o1(2),
            relief="flat"
        )
        button_2.place(
            x=42.0,
            y=474.0,
            width=83.0,
            height=81.0
        )

        canvas.create_text(
            59.0,
            45.0,
            anchor="nw",
            text="Your car is in the shop so you can't take it to work today. "
                "Do you (1) take the subway for $2.90 or (2) take an Uber for $30",
            fill="#000000",
            font=("MontserratRoman ExtraBold", 18 * -1)
        )

        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            227.0,
            330.0,
            image=image_image_1
        )
        window.resizable(False, False)
        window.mainloop()


        return points


    def credit(self, points):

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/gianna/Documents/untitled folder 2/build/assets/frame6")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        def o1(num):
            canvas = Canvas(
                window,
                bg = "#FFFFFF",
                height = 600,
                width = 335,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
            )

            canvas.place(x = 0, y = 0)
            if num == 2:
                canvas.create_text(
                59.0,
                47.0,
                anchor="nw",
                text="Yes! Building your credit can create oppertunities for getting low-interest"
                  "on mortgages, personal loans/credit cards, and end up paying less money during\n" 
                  "the term of your loan and have more of savings. The younger you start, the more\n"
                  "benifical it will be.",
                fill="#000000",
                font=("MontserratRoman ExtraBold", 18 * -1),
                justify= "left",
                width = 250
                )
                points += 5
            
            else:
                canvas.create_text(
                59.0,
                47.0,
                anchor="nw",
                text="This is not the best choice. Building your credit can create oppertunities for"
                  "getting low-interest on mortgages, personal loans/credit cards, and end up paying"
                  "less money during the term of your loan and have more of savings. If you have more"
                  "money for savings, you can use it to invest in your future.",
                fill="#000000",
                font=("MontserratRoman ExtraBold", 18 * -1),
                justify= "left",
                width = 250
                )
                points -= 5


        window = Tk()

        window.geometry("335x600")
        window.configure(bg = "#FFFFFF")


        canvas = Canvas(
            window,
            bg = "#FFFFFF",
            height = 600,
            width = 335,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.place(x = 0, y = 0)
        button_image_next = PhotoImage(
        file=relative_to_assets("button_next.png"))
        button_next = Button(
            image=button_image_next,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print(points),
            relief="flat"
        )
        button_next.place(
            x=48.0,
            y=474.0,
            width=83.0,
            height=81.0
        )

        canvas.create_rectangle(
            0.0,
            430.0,
            335.0,
            600.0,
            fill="#D9D9D9",
            outline="")

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: o1(1),
            relief="flat"
        )
        button_1.place(
            x=42.0,
            y=474.0,
            width=83.0,
            height=81.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: o1(2),
            relief="flat"
        )
        button_2.place(
            x=209.0,
            y=474.0,
            width=83.0,
            height=81.0
        )

        canvas.create_text(
                59.0,
                47.0,
                anchor="nw",
                text="Do you want to apply for a credit card? 1. No 2. Yes",
                fill="#000000",
                font=("MontserratRoman ExtraBold", 18 * -1),
                justify= "left",
                width = 250
                )
        
        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            167.0,
            358.0,
            image=image_image_1
        )

        canvas.create_text(
            86.0,
            42.0,
            anchor="nw",
            text="Credit",
            fill="#000000",
            font=("MontserratRoman ExtraBold", 18 * -1)
        )
        window.resizable(False, False)
        window.mainloop()

        # question 1
        window.destroy()

        # question 2

        def o2(num):
            canvas = Canvas(
                window,
                bg = "#FFFFFF",
                height = 600,
                width = 335,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
            )

            canvas.place(x = 0, y = 0)
            if num == 2:
                canvas.create_text(
                59.0,
                47.0,
                anchor="nw",
                text="Great job! Having a bad credit score will affect you by having trouble taking out"
                  "a credit card, car loan, or a mortgage. The other consequenses is causing higher interest"
                  "rates and fewer loan options. Paying your credit is important!",
                fill="#000000",
                font=("MontserratRoman ExtraBold", 18 * -1),
                justify= "left",
                width = 250
                )
                points += 10
            
            else:
                canvas.create_text(
                59.0,
                47.0,
                anchor="nw",
                text="This is a bad choice. Having a bad credit score will affect you by having trouble"
                  "taking out a credit card, car loan, or a mortgage. The other consequenses is causing"
                  "higher interest rates and fewer loan options. Paying your credit is important!",
                fill="#000000",
                font=("MontserratRoman ExtraBold", 18 * -1),
                justify= "left",
                width = 250
                )
                points -= 10


        window = Tk()

        window.geometry("335x600")
        window.configure(bg = "#FFFFFF")


        canvas = Canvas(
            window,
            bg = "#FFFFFF",
            height = 600,
            width = 335,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            0.0,
            430.0,
            335.0,
            600.0,
            fill="#D9D9D9",
            outline="")

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: o2(1),
            relief="flat"
        )
        button_1.place(
            x=42.0,
            y=474.0,
            width=83.0,
            height=81.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: o2(2),
            relief="flat"
        )
        button_2.place(
            x=209.0,
            y=474.0,
            width=83.0,
            height=81.0
        )

        canvas.create_text(
                59.0,
                47.0,
                anchor="nw",
                text="Your credit card payments are due. Do you pay them? 1. No 2. Yes",
                fill="#000000",
                font=("MontserratRoman ExtraBold", 18 * -1),
                justify= "left",
                width = 250
                )
        
        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            167.0,
            358.0,
            image=image_image_1
        )

        canvas.create_text(
            86.0,
            42.0,
            anchor="nw",
            text="Credit",
            fill="#000000",
            font=("MontserratRoman ExtraBold", 18 * -1)
        )
        window.resizable(False, False)
        window.mainloop()

        """
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
"""
        return points

# if __name__ == '__age 18__':
#     MyApp().run()
