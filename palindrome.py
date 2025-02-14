def palindrome_check(word):
    return word == word[::-1]

word=input("enter your palindrome: ")
if palindrome_check(word):
    print(f"{word} is a apalindrome")