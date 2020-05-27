#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

# USING FUNCTION-----------------------------------------------------------#
def compute():
	ans = 0
	x = 1  # Represents the current Fibonacci number being processed
	y = 2  # Represents the next Fibonacci number in the sequence
	while x <= 4000000:
		if x % 2 == 0:
			ans += x
		x, y = y, x + y
	print(ans)

#---------------------------------OR---------------------------------------#
#                       WITHOUT USING FUNCTION
ans = 0
x = 1  # Represents the current Fibonacci number being processed
y = 2  # Represents the next Fibonacci number in the sequence
while x <= 4000000:
	if x % 2 == 0:
		ans += x
	t=x+y
	x=y
	y=t
print(ans)
