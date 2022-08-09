inchr = input("Input one character: ")
if inchr >= 'A' and inchr <= 'Z' :
    print("You in put Upper Case Letter ", inchr)
elif inchr >= 'a' and inchr <= 'z' :
    print("You in put Lower Case Letter ", inchr)
elif inchr >= '0' and inchr <= '9' :
    print("You in put Number ", inchr)
else :
    print("It's not a letter or number.", inchr)