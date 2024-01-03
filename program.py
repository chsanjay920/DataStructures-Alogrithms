print("towers of hanoi")

def hanoi(n,A,C,B):
	if n == 0:
		return
	hanoi(n-1,A,B,C)
	print("shift disk",n,"from ",A,"to",C)
	hanoi(n-1,B,C,A)

hanoi(4,'A','C','B')