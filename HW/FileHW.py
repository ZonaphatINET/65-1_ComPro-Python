#
# Calculate Bonus Base on Number of WorkPoints
# 0-40 Use Rate_1 
# Points more than 40 Use Rate_2
# Rate Are define in DepartmentRate.txt file
# Totoal Points are in WorkPoints.txt file
# The formula is: Bonus = Points-40 * Rate_2 + 40 * Rate_1
'''print("Bonus Report")
print("================================================")
print("Name\t  SirName\tDept\t Bonus")
print("================================================")

def main():
    Employee_file = open("Employee.txt","r")
    for i in Employee_file:
        ids = Employee_file.readline()
        name = Employee_file.readline()
        sirname = Employee_file.readline()
        dept = Employee_file.readline()
        bonus = Employee_file.readline()

        print('%s\t%s\t%s\t%s\n'%(name.strip("\n"),sirname.strip("\n"),dept.strip("\n"),bonus.split("\n")))

    Employee_file.close()

main()

print("================================================")
print("Total Bonus")
print("================================================")'''

print('Bonus Report')
print('================================================')
print('Name       SirName    Dept              Bonus ')
print('================================================')

def main():

    emp_file = open('Employee.txt', 'r')
    point_file = open('WorkPoints.txt','r')
    dep_file = open('DepartmentRate.txt','r')

    employee1 = emp_file.read().split('\n')
    work_point1 = point_file.read().split()
    dep_rate1 = dep_file.read().split()

    index = 1
    index_point = 1
    listbonus = []
    sumtotal = 0

    while index < len(employee1):
        print(employee1[index].ljust(10),employee1[index+1].ljust(10),employee1[index+2].ljust(10),end=''.ljust(7))
        for w in work_point1:
            if w == employee1[index-1]:

                for d in dep_rate1:
                    if d == employee1[index+2]:
                        rate1 = int(dep_rate1[dep_rate1.index(d)+2])
                        rate2 = int(dep_rate1[dep_rate1.index(d)+1])
                listbonus.append((int(work_point1[index_point])-40)*rate1 + 40*rate2)
                print('{:,}'.format((int(work_point1[index_point])-40)*rate1 + 40*rate2)+".00 ")
                
        index += 4
        index_point += 2

    for sum in listbonus:
        sumtotal += sum

    emp_file.close()
    point_file.close()
    dep_file.close()

    print('================================================')
    print('Total Bonus'.ljust(37), '{:,}'.format(sumtotal)+".00")
    print('================================================')

main()