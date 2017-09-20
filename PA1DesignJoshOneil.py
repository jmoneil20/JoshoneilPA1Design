#Josh O'Neil
#CS 151
#September 20th, 2017
#External Sources: Calculus Textbook

print("Hello, I am going to help you determine the cost of replacing the siding on your house.")
Width = input("Enter the width of the wall you want to replace in feet: ")
Length = input("Enter the length of the wall you want to replace in feet: ")
Width = int(Width)
Length = int(Length)
TotalSA = Width*Length
print(TotalSA)
Cost = input("Enter the cost per square foot of the siding you want to use: ")
TotalSA= int(TotalSA)
Cost= float(Cost)
TotalCost = TotalSA*Cost
print("$",TotalCost)
