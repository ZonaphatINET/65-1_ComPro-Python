def digitalClock (i):
    T1 = 0
    T2 = 0
    T3 = 0
    time = 60
    sets = 60
    for h in range(0,i):
        if h == time:
            T2 += 1
            time += 60
        elif T2 == sets:
            T1 + 1


print(digitalClock())