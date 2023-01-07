subject = ['physics', 'chemistry', 1997, 2000 , 'biology'];

# this method is use for updating exiting list and only takes one arguement
subject.append("biology")
print("update list is", subject)

#this method use to count how many object occur in list
print("count for biology is", subject.count("biology"))
print("count for 2000 is ", subject.count(2000))

#this method is use add content to an exiting list
blist =["math" , "tech" ,2001];
subject.extend(blist)
print("extended list are ", subject)

#this method is use for d index position of an object
print("index for biology is", subject.index('biology'))
print("index for 1997 is", subject.index(1997))

#this method is use for inserting an object into a particular index
subject.insert(3, 2005)
print("final list is", subject)

#this method use to return removed object from a list
print("list1: ", subject.pop(3))
print("list2: ", subject.pop(5))

#this method is used for removing a given object from a list
subject.remove("biology");
print("list=", subject)
subject.remove("math");
print("list=", subject)

#this method is use to reverse object inside the list
subject.reverse();
print("subject=", subject)

#this method use to changes or arrange object in the list
answer= subject.sort
print("complete list:", answer)


