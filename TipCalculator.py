from tkinter import Tk,Radiobutton,Button,Label,StringVar,IntVar,Entry

class TipCalculator():
    def __init__(self):
        window = Tk()
        window.title("Tip Calculator App")
        window.configure(background = "blue")
        window.geometry("470x270")
        window.resizable(width=True,height=True)

        self.meal_cost = StringVar()
        self.tip_percent = IntVar()
        self.tip = StringVar()
        self.total_cost = StringVar()

        tip_percents = Label(window,text="Tip Percentages",bg="purple",fg="white",width=15)
        tip_percents.grid(column=0,row=0,padx=30,pady=30)

        bill_amount = Label(window,text = "Bill Amount",bg="black",fg="white",width=15)
        bill_amount.grid(column=1,row=0,padx=15,pady=30)

        bill_amount_entry = Entry(window,textvariable = self.meal_cost,width=14)
        bill_amount_entry.grid(column=2,row=0,padx=15)


        five_percent_tip = Radiobutton(window,text="5%  ",variable = self.tip_percent,value=5)
        five_percent_tip.grid(row=2,column=0,padx=15)
        ten_percent_tip = Radiobutton(window,text="10%",variable = self.tip_percent,value=10)
        ten_percent_tip.grid(row=3,column=0,padx=15)
        fifteen_percent_tip = Radiobutton(window,text="15%",variable = self.tip_percent,value=15)
        fifteen_percent_tip.grid(row=4,column=0,padx=15)
        twenty_percent_tip = Radiobutton(window,text="20%",variable = self.tip_percent,value=20)
        twenty_percent_tip.grid(row=5,column=0,padx=15)
        twentyfive_percent_tip = Radiobutton(window,text="25%",variable = self.tip_percent,value=25)
        twentyfive_percent_tip.grid(row=6,column=0,padx=15)
        thirty_percent_tip = Radiobutton(window,text="30%",variable=self.tip_percent,value=30)
        thirty_percent_tip.grid(row=7,column=0,padx=15)
        
        
        tip_amount = Label(window,text="Tip Amount",bg="green",fg="white",width=15)
        tip_amount.grid(column=1,row=2,padx=15)
        tip_amount_entry = Entry(window,textvariable=self.tip,width=14)
        tip_amount_entry.grid(column=2,row=2)


        bill_total = Label(window,text="Bill Total",bg="orange",fg="white",width=15)
        bill_total.grid(column=1,row=5)
        bill_total_entry = Entry(window,textvariable=self.total_cost ,width=14)
        bill_total_entry.grid(row=5,column=2)

        calculate_button = Button(window,text="Calculate",bg="green",fg="white",command=self.calculate)
        calculate_button.grid(row=7,column=1)
        clear_button = Button(window,text="Clear",bg="darkblue",fg="white",command=self.clear)
        clear_button.grid(row=7,column=2)
        
        window.mainloop()
        
    def calculate(self):
        pre_tip = float(self.meal_cost.get())
        percentage = self.tip_percent.get()  / 100
        tip_amount_entry = pre_tip * percentage
        self.tip.set(tip_amount_entry)

        final_bill = pre_tip + tip_amount_entry
        self.total_cost.set(final_bill)

    def clear(self):
        self.meal_cost.set("")
        self.total_cost.set("")
        self.tip.set("")
        


TipCalculator()
