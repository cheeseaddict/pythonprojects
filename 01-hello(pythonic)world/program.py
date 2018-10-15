def print_header():
	print("--------------------------------")
	print("			Hello World")
	print("--------------------------------")


def greet_user():
	user_name = input("Hey user what is your name? ")
	greeting = "Nice to meet you " + user_name
	print(greeting)


def main():
	print_header()
	greet_user()


main()