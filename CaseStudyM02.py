# Name: Brennan Morrisey
# File name: CaseStudyM02
# Tests if a students gpa meets a certain threshold
#

#declare global vars
fname = " "
lname =  " "
gpa = 0


lname = input("What is your last name? or enter ZZZ to quit ")
while lname != "ZZZ":
    
    fname = input("Enter your first name ")
    gpa = input("Enter your GPA ")
    if float(gpa) >= 3.5:
        print("You've made the dean's list ")
    elif float(gpa) >= 3.25 :
        print("You've made the honor role ")
    else:
        print("You have not made the Dean's list or honor role ")
    lname = input("What is your last name? or enter ZZZ to quit ")
