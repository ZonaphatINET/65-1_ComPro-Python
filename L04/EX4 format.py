print('I   ' + 'love  '  +  'python.')
print('I ' + '  love' +  '  python.')
print('I'  + 'love' +  'python.')


first = 'I'
second = 'love'
third = 'Python'
sentence = first + '   ' + second + '  ' + third + '.'
print(sentence)


print ( '_' * 20 )
supernice = ' Nice ' * 3
print (supernice)
print ( '-' * 20 )


print (' I  {}  Python.  '.format(' love '))
print(' {}   {}   {} '.format('I',  'love', 'Python.'))


print (' I {0} {1}. {1} {0}s me. ' .format('love','Python'))


first = 'I'
second = 'love'
thirf = 'Python'
print(' {}  {}  {} . '.format (first, second, third))


print(' {0:8} | {1:8} ' .format('Fruit' , 'Quantity'))
print(' {0:8} | {1:8} ' .format('Apple' , '3'))
print(' {0:8} | {1:8} ' .format('ORange' , '10'))


print(' {0:8} | {1:>8} ' .format('Fruit' , 'Quantity'))
print(' {0:8} | {1:>8} ' .format('Apple' , '3'))
print(' {0:8} | {1:>8} ' .format('ORange' , '10'))


print(' {0:8} | {1:8} ' .format('Fruit' , 'Quantity'))
print(' {0:8} | {1:8.2f} ' .format('Apple' , 2.33333))
print(' {0:8} | {1:8.2f} ' .format('ORange' , 10))