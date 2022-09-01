def main():
    try:
        hours = int(input('How many hours did you wrok? '))
        pay_reat = float(input('Enter your hourly pay rate: '))
        gross_pay = hours * pay_reat
        print('Gross pay: $',format(gross_pay,',.2f'), sep=' ')
    except ValueError as err:
        print(err)

main()