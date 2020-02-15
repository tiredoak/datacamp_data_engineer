
import sys

def hello(user_input):
	print(f"From a user: {user_input}")


if __name__ == "__main__":
	arg1 = sys.argv[1]
	hello(arg1)