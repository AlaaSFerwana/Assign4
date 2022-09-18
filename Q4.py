Un_list= [int (item) for item in input("Enter your numbers: ").split()]
print(Un_list)
n_count=0
p_count=0
for item in Un_list:
   if item<0 :
       n_count+=1
   else :
        p_count += 1

print("The Number of the negative value is :", n_count)

print("The Number of the positive value is :", p_count)
total= sum(Un_list)
average= total/(len(Un_list))

print("Total = :",total)
print  ( "The Average is ",float(average))



