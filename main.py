print("Greetings")
x = int(input("How many terms? "))

y, z = 0, 1
count = 0

if x <= 0:
   print("Please enter a positive integer")

elif x == 1:
   print("Fibonacci sequence upto",x,":")
   print(y)

else:
   print("Fibonacci sequence:")
   while count < x:
       print(y)
       nth = y + z
       y = z
       z = nth
       count += 1