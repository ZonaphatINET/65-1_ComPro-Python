first_score = float (input('first_score : '))
second_score = float (input('second_score : '))
third_score = float (input('third_score : '))
average_score = float((first_score + second_score + third_score) / 3)
print('Average Score :%.2f'%(average_score))
if average_score > 95:
    print('Congratulate!!!')