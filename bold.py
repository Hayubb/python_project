


set = [8,9,7,10,12,3,4,8,7,9,10,8]
#Mean
mean = sum(set)/len(set)
print("the mean of the set is ", round(mean))

#Mode
x = max(set)
print("the max no in d set is", x)
print(" so...d mode is ", set.count(x))

#Median
y= sorted(set)
print(y) 
median = len(y) // 2
print("d median is",median)

#Range
range = max(set) - min(set)
print("d range is ", range)


#for set in range(5,50,5):
   # list(range(set))
   # print(set)
    
    #my_list = list(range(10))
    #print(my_list)
#number 1
set= list(range(5,50,5))
print(set)
#number 2
my_frnd =["Ayo","Ibrahim","Abdulazeez","Sodiq","Habeb"]
my_frnd.append("Alex")
print("wen added is", my_frnd)
my_frnd.insert(2,"Ronn")
print("position is", my_frnd)
#number 3
number = [1,2,3,4,5,6,7]
a=number[0]**(1/2)
print(a)
b=number[1]**(1/2)
print(b)
c= number[2]**(1/2)
print(c)
d= number[3]**(1/2)
print(d)
e = number[4]**(1/2)
print(e)
f= number[5]**(1/2)
print(f)
i= number[6]**(1/2)
print(i)
new_list=[a , b, c, d, e, f, i]
print(new_list)

even = min(number)
count = max(number)
while (even < count):
    even += 1
    if (even % 2 == 0):
        print(even)
             
        

    


