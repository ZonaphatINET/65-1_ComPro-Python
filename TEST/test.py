TeamA = ['Somchai', 'Somkiet','Daycha','Yodchai','Petch','Sopa']
TeamB = ['Nares','Sopa','Nipa','Daycha','Pimon','Petch']
TeamC = ['Choojai', 'Sopa', 'Somkiet','Nares', 'Nipa','Daycha','Tawan']
TeamD = ['Sopa','Tawan', 'Pimon','Yodchai','Petch','Somjai']

Reward = [0,5000,7500,10000,15000]

def R1():

    print('REWARDS FOR SALE TEAM')
    print('----------------------')
    print('Name           Reward')
    print('----------------------')
    Member4 = []
    Member3 = []
    Member2 = []
    Member1 = []
    Total = 0


    TeamA1 = set(TeamA)
    TeamB1 = set(TeamB)
    TeamC1 = set(TeamC)
    TeamD1 = set(TeamD)

    MU = TeamA1 | TeamB1 | TeamC1 | TeamD1
    
    M4 = TeamA1 & TeamB1 & TeamC1 & TeamD1
    Member4.append(M4)
    
    M3_1 = TeamA1 & TeamB1 & TeamC1 
    M3_2 = TeamA1 & TeamB1 & TeamD1 
    M3 = (M3_1 | M3_2 ).difference(M4)
    Member3.append(M3)

    M2_1 = TeamA1 & TeamB1
    M2_2 = TeamA1 & TeamC1
    M2_3 = TeamA1 & TeamD1
    M2_4 = TeamB1 & TeamC1
    M2_5 = TeamB1 & TeamD1
    M2_6 =  TeamC1 & TeamD1
    M2 = (M2_1 | M2_2 | M2_3 | M2_4| M2_5| M2_6 ).difference(M4,M3)
    Member2.append(M2)

    M1 = MU.difference(M4,M3,M2)
    Member1.append(M1)


    for M4 in sorted(M4) :
        print(M4,' '*(13-len(M4)),format(Reward[4],','))
        Total += Reward[4]
    for M3 in sorted(M3) :
        print(M3,' '*(13-len(M3)),format(Reward[3],','))
        Total += Reward[3]
    for M2 in sorted(M2) :
        print(M2,' '*(14-len(M2)),format(Reward[2],','))
        Total += Reward[2]
    for M1 in sorted(M1) :
        print(M1,' '*(14-len(M1)),format(Reward[1],','))
        Total += Reward[1]
    print('----------------------')
    print('Total         ','{:,}'.format(Total))
    print('----------------------')


  



R1()