# Homework-02 GPA Calculator
#
# Formular GPA = sum(GradeLevel * Grade Point) / Total Credit
# Grade Point: A = 4, B = 3, C = 2, D = 1, F = 0
# Credit: Math = 3, English = 2, Science = 3, History = 2, Art = 1
# Grade Level: A = 90, B = 80, C = 70, D = 60, F = 0

Credits = {"Computer Programming": 3, "Math": 3, "English": 3, "Physic": 3, "Dance": 1, "Electronic": 3}
Grade_Level = {"A": 80, "B": 70, "C": 60, "D": 50, "F": 0}
Grade_Point = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}

Students_Marks = {"John": {"Computer Programming": 80, "Math": 90, "English": 70, "Physic": 50, "Dance": 60, "Electronic": 80}, 
                   "Peter": {"Computer Programming": 85, "Math": 80, "English": 65, "Physic": 60, "Dance": 90, "Electronic": 95}, 
                   "Mary": {"Computer Programming": 45, "Math": 70, "English": 60, "Physic": 65, "Dance": 80, "Electronic": 70},
                   "Tom": {"Computer Programming": 80, "Math": 55, "English": 75, "Physic": 70, "Dance": 75, "Electronic": 80},
                   "Jane": {"Computer Programming": 90, "Math": 95, "English": 80, "Physic": 75, "Dance": 80, "Electronic": 85}}
'''
def grade():
    global Grade_Level
    global Grade_Point
    print("Students Grade & GPA")
    for k, v in Students_Marks.items():
        print(k,"\t  ","Computer Programming :",v.pop("Computer Programming"),"Math :",v.pop("Math"),"English :",
              v.pop("English"),"Physic :",v.pop("Physic"),"Dance :",v.pop("Dance"),"Electronic :",v.pop("Electronic"),"GPA :")

def main():
    grade()

main()
'''

'''
def grade_L(point: int()) -> str():
    for i in Grade_Level:
        if point >= Grade_Level[i]:
            return i

def grade_P(point: int()) -> int():
    for i in Grade_Point:
        if point >= Grade_Point[i]:
            return Grade_Point[i]

def main():
    for key in Students_Marks:
        print("{:10}".format(key), end=' ')
        sumG = 0
        sumC = 0
        for value in Students_Marks[key]:
            print(value, "{:5}".format(grade_L(Students_Marks[key][value])), end="")
            sumG += grade_P(Students_Marks[key][value]) * Credits[value]
            sumC += Credits[value]
        print("GPA: {:.2f}".format(sumG / sumC))
        #print(sumG)
        #print(sumC)
main()
'''
for i in Students_Marks: 
    print(i.ljust(10),end='')
        
    sum_grade = 0
    sum_credit = 0

    for value in Students_Marks["John"] :
        resultStr = ()
        resultInt = 0
        for grade,point in Grade_Level.items():
                if Students_Marks[i][value] >= point:                   
                    resultStr = grade
                    resultInt = Grade_Point[grade]                 
                    break
        for sub,credis_sub in Credits.items():
                if sub == value:              
                    credis = credis_sub                
                    break
        sum_grade = (sum_grade + resultInt * credis) 
        sum_credit = (sum_credit + credis)
        sum = (sum_grade/ sum_credit)       
        print(sub, ":",resultStr.ljust(5),end='')
        
    print('GPA: {:.2f}'.format(sum))