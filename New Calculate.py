def add(P, Q):
    return P+Q
def subtract(P, Q):
    return P-Q
def multiply (P, Q):
    return P*Q
def divide (P, Q):
    return P/Q

print ("Please select the operation from the 4 answers!")
print ("a. Add")
print ("b. Subtract")
print ("c. Multiply")
print ("d. Divide")

choice = input("Please enter choice (a/ b/ c/ d): ")

num_1 = int (input ("Please enter your 1st Number.: "))
num_2 = int (input ("Please enter your 2nd Number and see your result.: "))

if choice == 'a':
    print (num_1, " + ", num_2, " = ", add(num_1, num_2))

elif choice == 'b':
    print (num_1, " - ", num_2, " = ", subtract(num_1, num_2))

elif choice == 'c':
    print (num_1, " * ", num_2, " = ", multiply(num_1, num_2))

elif choice == 'c':
    print (num_1, " / ", num_2, " = ", divide(num_1, num_2))

else:
    print ("This is a invalid input for errors!")