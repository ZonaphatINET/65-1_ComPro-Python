time_wrok = float (input('Enter the number of hours worke: '))
pay_rate = float (input('Enter the hourly pay reat: '))
if time_wrok <= 40:
    gross_pay = time_wrok * pay_rate
    print('The gross pay is $%.2f'(gross_pay))
else :
    over_time = time_wrok - 40
    gross_pay = (time_wrok * pay_rate)+(over_time * ((pay_rate  / 100) * 150))
    print('The gross pay is $%.2f'(gross_pay))