#Python Program for Code Evaluation for Greephire
#Power Ball lottery simulator
#Daniel Cavender
import random
def chooseRand(ls,num): # a function that finds a random loto number based on its number of times input
    hold = [pair for pair in ls if pair[1]==num] # create a list of all the pairs that match the number given
    return random.choice(hold) # return a random choice from that list


EmployeeNums = {} #a dictionary that holds the emloyee's name and loto number
choosen = {} #a dictionary that holds the number of times a certain number was chosen
flag = None
while flag != "yes":
    lotNums=[] # hold the Employee's loto nums
    fName = input("Enter your first name: ")
    lName = input("Enter your last name: ")
    Ename = fName+" "+lName
    for rnd in range(6):
        if lotNums == []: #base case for the first number
            num = (input("choose a number between 1 and 69: "))
            while int(num)<=0 or int(num) >=70: # ensures they choose a valid number
                num = (input("choose a number between 1 and 69: "))
        elif rnd == 5: # case for the last number
            num = (input("choose a number between 1 and 16 for the Powerball: "))
            while int(num)<=0 or int(num) >=17:
                num = (input("choose a number between 1 and 16 for the Powerball: "))
        else:
            num = (input("choose a number between 1 and 69, exluding "+" or ".join(lotNums)+" :"))
            while num in lotNums or (int(num)<=0 or int(num) >=70):
                num = (input("choose a number between 1 and 69, exluding "+" or ".join(lotNums)+" :"))
        lotNums.append(num)#add the number that they chose to their list
        if num in choosen:
            choosen[num] = choosen[num]+1 #adjust the stored value for that number
        else:
            choosen[num] = 1 # if it is not in the dictionary add it with a value of 1
    EmployeeNums[".".join(lotNums)] = Ename #after all the number are chosen make the list a string and store it in the
                                            #dictionary with the employee's name as the value this makes finding the winner faster
    flag = input("finished entering lottery numbers for all Employees? (yes/no) ")

for employee in EmployeeNums:
    lsEmployee = employee.split(".")
    print(EmployeeNums[employee]+ " " + " ".join(lsEmployee[0:len(lsEmployee)-1]) + " Powerball "+ lsEmployee[len(lsEmployee)-1])

stuff = []
for num in choosen:
    temp = (num,choosen[num]) # create a list of tuples
    stuff.append(temp)
stuff.sort(key = lambda x:x[1], reverse=True) # sort the list on the number of times that a number was chosen
print(stuff)
#used = [] # used to store all the numbers that have been used
final = [] # used to store the powerball numbers
for pair in stuff:
    if len(final)<6: # check to see if the number has been used and make sure that 6 numbers have not been chosen already
        print(pair)
        temp = chooseRand(stuff,pair[1])
        stuff.remove(pair)
        print(stuff)
        #used.append(pair[1])
        final.append(temp)

print(final)


print("Winning numbers: ", end="")
for num in range(len(final[:5])):
    print(final[num][0], end=" ")

print("Powerball "+final[5][0])
