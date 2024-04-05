class Stack():

    def __init__(self):
        self.stack = []
        self.last_pop = None
        self.addition = None
        self.subtraction = None
        
        # TODO:
        # self.multiplication = None
        # self.division = None
        # self.exponent = None
        
        self.pop_tracker = None
        self.add_tracker = None
        self.sub_tracker = None

        # TODO:
        # self.mult.tracker = None
        # self.div.tracker = None
        # self.exponent.tracker = None


        
        # TODO:
        # self.multiplication = None
        # self.division = None
        # self.exponent = None
        
        self.spop_tracker = None
        self.sadd_tracker = None
        self.ssub_tracker = None

        # TODO:
        # self.mult.tracker = None
        # self.div.tracker = None
        # self.exponent.tracker = None
        
        
    @classmethod
    def create_stack(cls):
        return cls()
    



    #---- STACK LOOSELY FUNCTIONS ----#
    def PUSH(self, value):
        self.stack.append(value)


    def POP(self):
        if self.stack:
            self.last_pop = self.stack.pop()
            self.pop_tracker = 1
        else:
            self.pop_tracker = 0
            print("<!!> Stack is empty. Cannot perform POP operation.")



    def ADD(self):
        if len(self.stack) >= 2:
            last_element = self.stack[-1]
            second_last_element = self.stack[-2]
            self.addition = last_element + second_last_element
            self.add_tracker = 1
        else:
            print("<!!> Not enough elements to perform ADD")
            self.add_tracker = 0


    def SUB(self):
        if len(self.stack) >= 2:
            last_element = self.stack[-1]
            second_last_element = self.stack[-2]
            self.subtraction = last_element - second_last_element
            self.sub_tracker = 1
        else:
            print("<!!> Not enough elements to perform ADD")
            self.sub_tracker = 0




    #---- STACK STRICT FUNCIONS ----#
    def SPOP(self):
        if self.stack:
            self.last_pop = self.stack.pop()
            self.spop_tracker = 1
        else:
            self.spop_tracker = 0
            raise ValueError("<!!> Stack is empty. Cannot perform POP operation.")



    def SADD(self):
        if len(self.stack) >= 2:
            last_element = self.stack[-1]
            second_last_element = self.stack[-2]
            self.addition = last_element + second_last_element
            self.sadd_tracker = 1
        else:
            self.sadd_tracker = 0
            raise ValueError("<!!> Not enough elements to perform SADD")
        

    def SSUB(self):
        if len(self.stack) >= 2:
            last_element = self.stack[-1]
            second_last_element = self.stack[-2]
            self.subtraction = last_element - second_last_element
            self.ssub_tracker = 1
        else:
            self.ssub_tracker = 0
            raise ValueError("<!!> Not enough elements to perform SSUB")




    
    #---- DISPLAY STUFF ----#
    def DISPLAY(self):
        print(self.stack)


    def DISPLAY_POP(self):
        if self.last_pop is not None and self.pop_tracker != 0:
            print(self.last_pop)
        if self.pop_tracker == 0 and self.last_pop != None:
            print(f"Last stored pop value : {self.last_pop}")
        if self.last_pop == None:
            print(self.last_pop)

            
    def DISPLAY_ADD(self):
        if self.addition is not None and self.add_tracker != 0:
            print(self.addition)
        if self.add_tracker == 0 and self.addition != None:
            print(f"Last stored ADD value : {self.addition}")
        if self.addition == None:
            print(self.addition)


    def DISPLAY_SUB(self):
        # If self.stack has more than or equal to 2 values
        if self.subtraction is not None and self.sub_tracker != 0:
            print(self.subtraction)
        # If self.stack has less than 2 elements and self.SUB() was performed
        # and self.subtraction had one value other than None
        if self.sub_tracker == 0 and self.subtraction != None:
            print(f"Last stored SUB value : {self.subtraction}")
        # If self.SUB() was never performed
        if self.subtraction == None:
            print(self.subtraction)


    def DISPLAY_SPOP(self):
        if self.last_pop is not None and self.pop_tracker != 0:
            print(self.last_pop)
        # if self.spop_tracker == 0 and self.last_pop != None:
        #     print(f"Last stored pop value : {self.last_pop}")
        if self.last_pop == None:
            print(self.last_pop)
            
            
    def DISPLAY_SADD(self):
        if self.addition is not None and self.add_tracker != 0:
            print(self.addition)
        # if self.sadd_tracker == 0 and self.addition != None:
        #     print(f"Last stored ADD value : {self.addition}")
        if self.addition == None:
            print(self.addition)


    def DISPLAY_SSUB(self):
        if self.subtraction is not None:
            print(self.subtraction)
        # if self.ssub_tracker == 0 and self.subtraction != None:
        #     print(f"Last stored SUB value : {self.subtraction}")
        if self.subtraction == None:
            print(self.subtraction)



# TODO : MAKE a StrictStack class to implement stricter functionalities to make code cleaner

# Example usage:
st = Stack.create_stack()

st.PUSH(3)
st.PUSH(4)
st.SSUB()
st.SPOP()
st.SSUB()
st.DISPLAY_SUB()
