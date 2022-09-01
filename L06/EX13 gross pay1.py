def main():
    hours = int(input('How many hours did you work? '))
    pay_rate = float(input('Enter your hoyrly pay rate: '))
    gross_pay = hours * pay_rate
    print('Gross pay: $',format(gross_pay,',.2f'), sep='')

main()
