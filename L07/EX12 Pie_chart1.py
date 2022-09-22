import matplotlib.pyplot as plt

def main():
    sales = [100, 400, 300, 600]

    slice_labels = ['1st qtr','2st qtr','3st qtr','4st qtr']

    plt.pie(sales, labels=slice_labels)

    plt.title('Sales by Quarter')

    plt.show()

main()