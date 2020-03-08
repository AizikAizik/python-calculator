from tkinter import *

class calculator:
    def __init__(self, master):
        self.master = master
        master.title("Python Basic calc")
        
        #create screen widget
        self.screen = Text(master, state = 'disabled', width = 30, height = 3, background = 'grey', foreground = 'white')
        
        #position screen in the window
        self.screen.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5)
        self.screen.configure(state = 'normal')
        
        #initialize screen value as empty
        self.equation = ''
        
        #create buttons using method createButton
        b_1 = self.createButton(7)
        b_2 = self.createButton(8)
        b_3 = self.createButton(9)
        b_4 = self.createButton(u"\u232B", None)
        b_5 = self.createButton(4)
        b_6 = self.createButton(5)
        b_7 = self.createButton(6)
        b_8 = self.createButton(u"\u00F7")
        b_9 = self.createButton(1)
        b_10 = self.createButton(2)
        b_11 = self.createButton(3)
        b_12 = self.createButton('*')
        b_13 = self.createButton('.')
        b_14 = self.createButton(0)
        b_15 = self.createButton('+')
        b_16 = self.createButton('-')
        b_17 = self.createButton('=', None, 34)
        
        #store buttons in a list
        buttons = [b_1,b_2,b_3,b_4,b_5,b_6,b_7,b_8,b_9,b_10,b_11,b_12,b_13,b_14,b_15,b_16,b_17]
        
        #initialize counter
        count = 0
        
        #arrange buttons using a grid manager
        for row in range(1,5):
            for column in range(4):
                buttons[count].grid(row = row, column = column)
                count += 1
            
        #arrange the last button '=' at the bottom
        buttons[16].grid(row = 5, column = 0, columnspan = 4)
    
    #This function creates a button and takes one compulsory arguement, the value that should be on the button
    def createButton(self, val, write = True, width = 7):
        return Button(self.master, text = val, command = lambda: self.click(val, write), width = width)
    
    # this handles the on click event of a button
    def click(self, text, write):
        if write == None:
            # evaluate code when there is an equation to be evaluated
            if text == '=' and self.equation:
                #replace the unicode value division value with python division symbol
                self.equation = re.sub(u"\u00f7", '/', self.equation)
                print(self.equation)
                answer = str(eval(self.equation))
                self.clear_screen()
                self.insert_screen(answer, newline = True)
            elif text == u"\u232B":
                self.clear_screen()
        else:
                self.insert_screen(text)
    
    #to clear the screen
    def clear_screen(self):
        #set equation to empty before deleting the screen
        self.equation = ''
        self.screen.configure(state ='normal')
        self.screen.delete('1.0', END)
    
    # inserting values into the screen
    def insert_screen(self, value, newline = False):
        self.screen.configure(state = 'normal')
        self.screen.insert(END, value)
        #record every value inserted in screen
        self.equation += str(value)
        self.screen.configure(state = 'disabled')
 
    
root = Tk()
my_gui = calculator(root)
root.mainloop()