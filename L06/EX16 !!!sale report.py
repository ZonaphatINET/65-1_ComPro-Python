from multiprocessing.sharedctypes import Value


def main():
    total = 0.0

    try:
        infile = open('sales_data.txt','r')
        for line in infile:
            amount = float(line)
            total += amount

        infile.close()
        print(format(total, ',.2f'))
#Error filename
    except IOError:
        print('An error occured trying in the file.')
#Error data non numeric only
    except ValueError:
        print('Non-numeric data found in the file')
#Error ??? 
    except:
        print('An error occured.')

main()