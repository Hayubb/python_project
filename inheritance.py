import math
class Students:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        
    def getInfo(self):
        print(self.firstName + " "+ self.lastName)
        
# class Person(Students):
#     def __init__(self, fname,lname,age):
#         Students.__init__(self,fname,lname,age)
#         self.age=age
#     def mess(self):
#         print(self.firstName + " "+self.lastName + "is now" +self.age +"old")
   
# studentOne = Person("Ayub",18)

# studentOne.getInfo()
# studentOne.mess()



# class Parent:
#     def __init__(self,fname,lname):
#         self.name=fname
#         self.sur=lname
#     def getinfo(self):
#         return self.name+" "+self.sur
# can1=Parent("Ayub","Agiri")
# stu=can1.getinfo()
# print(stu)





class InfoData: #Parent Class
    def __init__(self,fname,lname):
        #print(fname,lname)
        self.name=fname
        self.sur=lname
    def getinfo(self):
        return self.name+" "+self.sur



class Statistics(InfoData): #Child class
    def __init__(self, val1,val2,val3,val4,val5,fname,lname):#Child class contructor
        self.val1 = val1
        self.val2 = val2
        self.val3 = val3
        self.val4 = val4
        self.val5 = val5
        self.fname = fname
        self.lname = lname
        InfoData.__init__(self,self.fname,self.lname)
#     def mean(self):
#        return (self.val1 + self.val2 + self.val3 + self.val4 + self.val5)/5
        
#     def range(self):
#         my_list = [self.val1, self.val2, self.val3, self.val4, self.val5]
#         return max(my_list) - min(my_list)
        
        
#     def getinfo(self):#method overridden
#        return InfoData.getinfo(self)
   
# firstChild = Statistics(4,5,6,5,10, "Ayub", "Agiri")
# childInfo = firstChild.getinfo()
# meanVal = firstChild.mean()
# rangeVal = firstChild.range()
# print("The student name is %s , the mean score is %f and range score is %d" %(childInfo, meanVal, rangeVal))




# numbers=[1,2,3,4,5]
# number=str(numbers)



# class Child(Parent):
#     def __init__(self, fname, lname):
#         Parent.__init__(self,fname, lname,number)
        
        
# "Giving this list [6,4,4,7,6,4,5,5,7,8] find the statistics mean,median and range, 
# pls note you are to declare extra method that will sort the list in your class and 
# call this method in other methods in your class"
class solve:
    def __init__(self,list_values):
        self.list_values=list_values
    def sorted_list(self):
        arrange=sorted(self.list_values)
        return arrange
    def mean(self):
        return sum(self.list_values)/ len(self.list_values)
    def median(self):
        nom = self.sorted_list()
        if len(nom) % 2 == 0:
            first_no_pos  = len(nom)/2
            second_no_pos = first_no_pos - 1
            # print(first_no_pos)
            # print(second_no_pos)
            return (nom[math.floor(first_no_pos)] + nom[math.floor(second_no_pos)])/2
        else:
            index_pos = len(nom)//2
            return nom[index_pos]
    def mode(self):
        num={}
        for x in self.list_values:
            # print(num)
            if x not in num:
                num[x]=0
            num[x]+=1
        # print(num)
        res=max(num.values())
        result=[]
        for d ,i in num.items():
            if i == res:
                result.append(d)
        return result
    def range(self):
        return max(self.list_values)-min(self.list_values)
        

        
        
my_list = [6,4,4,7,6,4,5,5,7,8]
cal1=solve(my_list)
order=cal1.sorted_list()
meanval=cal1.mean()
medianval=cal1.median()
rangeval=cal1.range()
modeval=cal1.mode()
print(modeval)
# print("the sorted statistical %s has the mean is %f ,the median is %f ,and the range is %d ,and mode is %d" %(order,meanval,medianval,rangeval,modeval))


        