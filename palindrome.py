def check_palindrome(string):
    l = len(string)

    for i in range(l):
        if string[i] == string[l-i-1]:
            print(f"{string} is a palindrome.")
            break
        else:
            print(f"{string} is not a palindrome")
            break

user_string = input("Enter your string: ")
check_palindrome(user_string)
