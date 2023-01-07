# def gretings ():
#     return "hello somebody now"
# res = gretings()
# print(res)
#write a function dat accept 3 parameter print respectfully
# nd return d S.I as d ansa for folwing:a=800,5%,2hrs
#b=500,2%,4hrs.
# def simple_int (p,r,t):
#     return p * r * t / 100
# a=simple_int(800,5,2)
# b=simple_int(500,2,4)
# print("the S.I for 800,5%,2hrs is ", a)
# print("the S.I for 500,2%,4hrs is ",b)
# x=input ("enter your principal:")
# y=input ("enter your rate:")
# z=input ("enter your time:")
# def int_covert (con):
#     return int(con)
# a=int_covert(x)
# b=int_covert(y)
# c=int_covert(z)
# output = simple_int(a,b,c)
# print(output)
 
#write a func dat return d root of d quadratic equation:2x^2+6x-9
import math
def quadratic_for (a,b,c): 
    d= (b**2)-(4*a*c)
    value=math.sqrt(d)
    x1 = x2 = 0
    if d > 0:
        x1 = (-b+value)/(2*a)
        x2 = (-b-value)/(2*a)
  
    return "the root of equation for 2x^2+6x+9 is x1 = ",x1,"and x2 = ",x2 
answer=quadratic_for(1,14,-8)
print(answer)
    
# def get_formatted_name(first_name, last_name, middle_name=''):
# #  Return a full name, neatly formatted.
#  if middle_name:
#     full_name = first_name + ' ' + middle_name + ' ' + last_name
#  else:
#     full_name = first_name + ' ' + last_name
#  return full_name.title()
# musician = get_formatted_name("Ayub","Agiri")
# print(musician)
# musician = get_formatted_name("Ayub","Agiri")
# print(musician)

    

    
    


    
    
