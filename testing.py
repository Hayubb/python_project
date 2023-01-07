count = 0
while (count < 9):
    print("the count is: ", count)
    count += 1
print("end of count")


var= 3
while (var < 3):
    num= input("enter your number: ")
    print("you entered" , num)
else:("you entered incorrect number")

for letter in "ayub" :
    print("each letter: ", letter)

animals=["goat","dog","ram","cow"]
for biology in animals :
    print("mammals: ", biology)
    
for num in range (10,30):
    for x in range (3,num):
        if num%x == 0:
            z = num/x
            print (num,x,z)
            break
    else:
        print(num,"is not a factor")
number= 5
while(number < 20):
    print(number ,"is lesser than 5")
    number += 1
else:
    print(number , "is not less than 5")

