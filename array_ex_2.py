number = int(input("Enter the number: "))
odd_number_list =[]

def odd_number(n):
    for x in range(n):
        if x % 2 == 0:
            continue
        odd_number_list.append(x)            

odd_number(number)
print(odd_number_list)