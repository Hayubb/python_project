glossary = {
   "maximum":"returns the largest number",
   "minimum":"reutuns the smallest number",
   "append":"use for updatind list",
    "insert":"use for placind an object in an index",
   "round":"round up a number to n digit"
}
for x, y in glossary.items():
  print("\nkeyword:",x)
  print("meaninig:",y)
  print("\nthe meaning of",x,"is define as",y)
for name in glossary.keys ():
   print(name)
    
#message = input("enter your name: ")
#print("Hello",message)

#code = "\n enter a message and i will repeat it for you"
#code += "\n (to stop message enter 'stop' and it stop): "
#message = ""
#active = True
#while active:
 #   message=input(code)
  #  if message == 'stop':
   #     active = False
    #else:
     #   print(message)
    
    
# food = ["Rice","Beans","Yam","Spag","Oat"]
# finished_food = []
# while "Rice" in food:
#     food.remove("Rice")
#     print("sorry,we run out of Rice")
# while food:
#     foods = food.pop()
#     print("i'ave made your food",foods)
#     finished_food.append(foods)
# print("\n food that was made:")
# for finished_foods in finished_food:
#     print(finished_foods)    


#def T_shirt(size=("large","medium"),message = "i love python"):
 # '''make t-shirt for free'''
  #print(message,"has been printed on size",size,"t-shirt\n")
#T_shirt("\nlarge")
#T_shirt("\nsmall","good vibe")
#T_shirt("\nmeduim")

def city_state(state,city):
  print(state+","+city)
city_state("lagos","ikeja")
  

