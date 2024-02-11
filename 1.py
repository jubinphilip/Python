import math

n=int(input("Enter number1 :"))

m=int(input("Enter number2 :"))

def top2():
	print("\n")
	for i in range(math.ceil(m/2)):
		print("\___/",end='   ')
			
	print("\n",end='/')
	for j in range(int(m/2)):
		print("   ",end='\___/')
	print("\033[F",end="")
for i in range(n-1):
	top2()
	if(i==n-2):
		print("\n")
