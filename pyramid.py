n = int(input())

# printing pyramid
for i in range(n):
   for j in range(n-i-1):
      # print spaces
      print("", end=" ")
   for j in range(2*i+1):
      # print stars
      print("*", end="")
   print()

# printing downward pyramid
for i in range(n-1):
   for j in range(i+1):
      # print spaces
      print("", end=" ")
   for j in range(2*(n-i-1)-1):
      # print stars
      print("*", end="")
   print()