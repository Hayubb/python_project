


dict1 = {"ten":10,"twenty":20,"thirty":30}
dict2={"thirty":30,"fourty":40,"fifty":50}
#marge together
result1= dict1.copy()
for key,value in dict2.items():
    result1[key] = value
# print(result1)

# students={"sade":"80","sola":"70", "nike":"60", "tosin":"80", "Wale":"50"}
# #Find ow many students got above 60 scores and List them
# std_list=[]
# for student in students.values():
#     if int(student) > 60:
#         std_list.append(students.keys())
# print(std_list)
        
        
students={"sade":"80","sola":"70", "nike":"60", "tosin":"80", "Wale":"50"}
# Find ow many students got above 60 scores and List them
std_list=[]
for i in students:
    print(i)
    i_int = int(students[i])
    # print(i_int)
    # print(type(i_int))
    
    if i_int > 60:
        std_list.append(i)
# print(std_list)
        
dic= {'a': 10, 'b': 10, 'c': 40, 'd': 20, 'e': 70, 'f': 80, 'g': 40, 'h': 20}
# Find the frequency of key values
d ={}
for i in dic.values():
    # print(i)
    if i not in d:
        d[i]= 0
    d[i] += 1
           
        
        
# print(d)


str="i love coding with python"
# find hw many times each character appear and also minimum valuey
y={}
t=[]
for x in str:
    # print(x)
    if x not in y:
        y[x]=0
    y[x] += 1
print(y)
smallest = max(y.values())
print("The Largest = ",smallest)
for key , value in y.items():
        if value < smallest:
            smallest = value
print("The smallest is ",   y)
for key , value in y.items():
    if smallest == value:
        print("This is smallest " ,key)
        
        
        
    
  
        
        

        
        








