s = input('Enter a string ')
if s.lower() == s[::-1].lower():
    print("true")
else:
    print("False")