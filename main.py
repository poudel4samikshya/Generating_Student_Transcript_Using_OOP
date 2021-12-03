
#Using OOP concept to print the trancript
class Demographics:
    def __init__(self,ID,Age,Gender,In_state,*args,**kwargs):
        super(Demographics,self).__init__(*args,**kwargs)

        self.ID = ID
        self.Age = Age
        self.Gender = Gender
        self.In_state = In_state

# method to calculate tution_fees

        def tution_fees_percredit(self):
            num_credits = 3

            if(self.In_state == "yes" or self.In_state == "Yes"):

                self.fees = 560 * num_credits
            else:
                self.fees = 913 * num_credits
            return self.fees
        self.fees = tution_fees_percredit(self)


class Grade:
    def __init__(self,Math_score,Science_score,English_score,*args,**kwargs):
        super(Grade,self).__init__(*args,**kwargs)

        self.Math_score = Math_score
        self.Science_score = Science_score
        self.English_score = English_score


        self.average = ((self.Math_score + self.Science_score + self.English_score)/3)
#method to calculate grade
        def grade_calc(self) :
            if(self.average > 90 and  self.average <= 100):
                self.grade = "A"
            elif(self.average > 80 and self.average < 90):
                self.grade = "B"
            elif (self.average > 70 and self.average < 80):
                self.grade = "C"
            else:
                self.grade = "F"
            return self.grade

        self.grade = grade_calc(self)


#child class for Grade and Demographics
class final(Demographics,Grade):
    def __init__(self,*args,**kwargs):
        super(final,self).__init__(*args,**kwargs)

#printing transcript
        print()
        print("__________ STUDENT TRANSCRIPT ___________")
        print("_________________________________________")
        print()
        print("Student ID:              ",self.ID)
        print("Student Age:             ",self.Age,)
        print("Student Gender:          ",self.Gender)
        print("In-state/Out-of-state:   ",self.In_state)

        print()

        print("Math Score:              ", self.Math_score)
        print("Science Score:           ", self.Science_score)
        print("English Score:           ", self.English_score)
        print()
        print("Grade:                   ", self.grade)
        print("Tution Fees:             ", self.fees)
        print()

        print("__________________________________________")
        print("__________________________________________")

def student_info():
    ID = int(input("Plese enter your ID : "))
    Age = int(input("Plese enter your Age : "))
    Gender = str(input("Plese enter your Gender : "))
    In_state = str(input("Plese enter your yes for in_state otherwise no : "))

    Math_score = float(input("Please enter Math Score: "))
    Science_score = float(input("Please enter Scince Score: "))
    English_score = float(input("Please enter English Score: "))
    
# validation for negative and over 100 scores

    while((Math_score < 0 or Math_score > 100) or (Science_score < 0 or Science_score > 100) or (English_score < 0 or English_score > 100)):
        print("Plese enter Right set of your scores 'NO NEGATIVES' & 'NO OVER 100'")
        Math_score = float(input("Please enter Math Score: "))
        Science_score = float(input("Please enter Scince Score: "))
        English_score = float(input("Please enter English Score: "))
        
#calling child class final which will print the transcript
        
    transcript = final(ID,Age,Gender,In_state,Math_score,Science_score,English_score)
    
#calling student_info function to get student information

student_info()
