def my_list():
    my_list = [item for item in input("Enter your items: ").split()]
    print(my_list)
    count = 0
    for item in my_list:
        count += 1
    print(" The length of the list is: ", count)

my_list()










def lengthlist():
    My_list=[0,"A",3.5,10,100]
    print(My_list)
    count=0
    for item in My_list:
        count+=1
    print("The Length Of List Is :",count)

lengthlist()