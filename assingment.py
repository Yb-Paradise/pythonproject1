# A program to check whether a year is a leap year or not
year = 2023
if year % 4 == 0:
    print(year, "is a leap year")
else:
    print(year,"is now a leap year")
# a program to check whether a letter is a consonant or a vowel
letter="b"
letter=letter.lower()
if letter in ["a","e","i","o","u"]:
    print(letter,"is a vowel")
elif letter.isalpha():
    print(letter,"is a consonant")
else:
    print("Error")