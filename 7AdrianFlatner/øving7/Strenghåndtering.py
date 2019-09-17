def check_equal(str1, str2):

    for n in str1 and str2:

        if str1 == str2:
            return True
        else:
            return False


str1 = "Hei"
str2 = "Hei"
str3 = "abba"

ans = check_equal(str1, str2)
print(ans)

#[::-1]
def reversed_word(str):
    new_string = ""
    index = len(str)
    while index:
        index -= 1
        new_string += str[index]
    return new_string

ans2 = reversed_word(str1)
print(ans2)

def check_palindrome(str):

    if str == reversed_word(str):
        return True
    else:
        return False

ans3 = check_palindrome(str3)
print(ans3)

str4 = "pepperkake"
str5 = "per"

#print(str4.find(str5))

def contains_string(str1,str2):

    if str2 in str1:
        return str1.index(str2)
    else:
        return -1


ans4 = contains_string(str4,str5)
print(ans4)

