''' 
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6
 1 0 1 1 0 1 1 1 0 1 1 1 1 0 1 1 1 1 1 0 1 1 1 1 1 1 0
 A n I R a C H M i N G K H w A N
  low   low     low       low         low           loww
'''

low = 1
sp = 3
print("Original Text: anirachmingkhwan")
text = 'anirachmingkhwan'
#text = str(input('Enter name : '))
print("Output Text: ",end='')
for name in range(len(text)):               #name แทนค่าที่ละตัวของ (len)text
    if name == low :                        #name เท่ากับค่า low
        print(text.lower()[name],end='')    #แสดง text เป็นตัวเล็ก ตามค่า name
        low += sp                           #low รวมกับ sp 1 + 3 = 4
        sp += 1                             #sp เพิ่ม 1 
    else :                                  #name ไม่เท่ากับ low 
        print(text.upper()[name],end='')    #แสดง text เป็นตัวใหญ่ ตามค่า name
