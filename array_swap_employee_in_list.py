people = ["Johny", "Marry", "Francis" ] # to 3 developers in a company
# index      0,       1,       2,
print("Before: ", people)

# TRIANGLE ----- se utilizeaza ALG triunghiului 
# HW2 ----- add code user ---> place_A 

temp_1 = int(input("     First index - to remplace: "))
temp_2 = int(input("     Second index - to remplace: "))

if (temp_1 >= 0 and temp_1 < len(people)) and (temp_2 >= 0 and temp_2  < len(people)):
    pass
    #print("Temp = ", temp)
    temp = people[temp_1]
    people[temp_1] = people[temp_2]
    people[temp_2] = temp
    # people[0] = people[1] # Marry -> Johny
    # people[1] = temp      # Johny -> Marry
    print("After:  ", people)
    #for i in range(len(people)):
    #    print(i+1, people[i])
else:
    print ("Index is not valable")
