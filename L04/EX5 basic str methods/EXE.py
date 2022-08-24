type = str(input('Enter a strung: '))
if type.isalpha() and type.islower() :
    print('This is what I found about that string:')
    print('The string is alpahanumeric.')
    print('The string contains only alpahabetic')
    print('The letters in the string aer all lowercase')
elif type.isnumeric() :
    print('This is what I found about that string:')
    print('The string is alpahanumeric.')
    print('The string contains only digits.')
elif type.isalnum() and type.isupper() :
    print('This is what I found about that string:')
    print('The string is alpahanumeric.')
    print('The letters in the string are all uppercase.')
else :
    print('Errer!!')