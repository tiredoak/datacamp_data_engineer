import sys

def reverse(string):
	print(string[::-1])

if __name__ == "__main__":
	input = sys.argv[1]
	reverse(input)