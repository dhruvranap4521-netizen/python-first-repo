a = int(input("Enter any year :"))

if ((a%4 == 0 and not(a%100 == 0)) or a%400 == 0):
        
    print("Year is leap  ")
else :
    print("Year is not leap")
