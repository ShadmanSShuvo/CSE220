# n = int(input('Input a number : '))
# print('Your number is :', n)
# if (n % 2 == 0):
#     print('Number is even')
# else :
#     print('Number is odd')
a,b,c = 1,2,3
print(a,b,c)
print(type(c))

myList = [1,2, 'akif', [7,8]]
print(myList[3][1],myList[2][3], sep = '\n') #normally sep na dile comma gula space hoye jay
print(str(myList[3][1])+ '\n'+ str(myList[2][3])) #python strongly typed language. int ar string er merging hobena, string e convert kore nite hobe
# myList[2][3] = 'p' cannot really modify string by indexing but I can see characters by indexing
myList[3][1] = 9 
print(myList[3][1])
myList[2] = [5,6] #different type jinish assign kora is fine
mytuple = (1,2, 'john', (4,5)) #can't modify tuples
print(mytuple[2][2])


#slicing 
newList = myList[1:3] #[including:excluding]
print(newList* 2) #prints it twice
print('Length of the newList is : ' + str(len(newList)))


#dictionary
#keys can be anytype but values must be object

dict = {'Abba' : [1,2,3], 3:'Abba'}
print(dict['Abba'])
print(dict[3])