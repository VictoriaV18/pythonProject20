import re
def is_palindrome(string):
    if string is None:
        return False
    string = str(string)
    cleaned_str = re.sub(r'[^a-zA-Z0-9]', '', string.lower())
    return cleaned_str == cleaned_str[::-1]
print(is_palindrome("A man, a plan, a canal -- Panama"))
print(is_palindrome("Madam, I'm Adam!"))
print(is_palindrome('333'))
print(is_palindrome('None'))
print(is_palindrome("Abracadabra"))