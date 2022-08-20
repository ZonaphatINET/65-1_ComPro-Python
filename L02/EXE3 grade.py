test_score = float(input('Enter your test score: '))
if test_score <= 60:
    print('Your grade is F.')
elif test_score <= 69:
    print('Your grade is D.')
elif test_score <= 79:
    print('Your grade is C.')
elif test_score <= 89:
    print('Your grade is B.')
else:
    print('Your grade is A.')