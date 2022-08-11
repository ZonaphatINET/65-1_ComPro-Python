print('----------------')
print('KPH\tMPH')
print('----------------')
for number in range(50 ,130, 10) :
    kph = number + 10
    mph = kph * 0.6214
    print(kph, '\t%.1f' %mph)
print('----------------')