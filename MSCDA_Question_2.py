##### Question 2
##### Write a program to calculate the profit/loss of N products based on their purchase costs, selling prices
##### , and monthly sales.

n = int(input('Enter the number of products: ')) # Record number of products input
print('')

def ArrayList(n):
    # define function to create lists recording product names, no of purchases, no of sales, purchase cost, selling prices
    prod_name = []
    no_of_purchase = []
    no_of_sale = []
    cost_per_item = []
    selp_per_item = []
    for i in range(n):
        prod_name = prod_name + [str(input('Enter the name of the product: '))]
        no_of_purchase = no_of_purchase + [int(input('Enter the number of ' + prod_name[i] + ' purchased: '))]
        no_of_sale = no_of_sale + [int(input('Enter the number of ' + prod_name[i] + ' sold: '))]
        cost_per_item = cost_per_item + [float(input('Enter the cost of each ' + prod_name[i] + ': $'))]
        selp_per_item = selp_per_item + [float(input('Enter the selling price of each ' + prod_name[i] + ': $'))]
        print('')

    return prod_name, no_of_purchase, no_of_sale, cost_per_item, selp_per_item


def ProductPnLPercent(no_of_purchase, no_of_sale, cost_per_item, selp_per_item):
    # define function to calculate product/loss percentage for each product
    n = len(no_of_purchase)
    prd_prof_loss_percent = []

    for i in range(n):
        prd_prof_loss = no_of_sale[i]*selp_per_item[i] - no_of_purchase[i]*cost_per_item[i]
        prd_prof_loss_percent = prd_prof_loss_percent + [round(prd_prof_loss/(no_of_purchase[i]*cost_per_item[i])*100, 2)]

    return prd_prof_loss_percent


def SortOrder(prd_prof_loss_percent):
    # define function to generate order index sorting profit/loss percentage values in descending
    n = len(prd_prof_loss_percent)

    val = prd_prof_loss_percent.copy()
    order = list(range(len(prd_prof_loss_percent)))

    for i in range(n):
        for j in range(n-1):
            if val[j] < val[j+1]:
                val[j], val[j+1] = val[j+1], val[j]
                order[j], order[j+1] = order[j+1], order[j]

    return order


def NewArraySorted(ar, desc_order):
    # define function to re-order values in given array following an order index
    # (which can be generated by SortOrder function)
    ar_sorted = []
    for i in desc_order:
        ar_sorted = ar_sorted + [ar[i]]

    return ar_sorted


def NetProfitLoss(no_of_purchase, no_of_sale, cost_per_item, selp_per_item):
    # define function to calculate total sale, total purchase cost, net profit/loss percentage for the whole product list
    n = len(no_of_purchase)

    tot_sale = 0
    tot_cost = 0
    for i in range(n):
        tot_sale = tot_sale + no_of_sale[i]*selp_per_item[i]
        tot_cost = tot_cost + no_of_purchase[i]*cost_per_item[i]

    tot_prof_loss = round((tot_sale - tot_cost)/tot_cost*100, 2)
    tot_sale = round(tot_sale, 2)
    tot_cost = round(tot_cost, 2)

    return tot_sale, tot_cost, tot_prof_loss


def Label(prof_loss_percent):
    # define function to label each product as 'Profit', 'Break-even' or 'Loss'
    if prof_loss_percent > 0:
        label = 'Profit'
    if prof_loss_percent == 0:
        label = 'Break-even'
    if prof_loss_percent < 0:
        label = 'Loss'

    return label


def PrintTable(n):
    # define function to print tabular format recording transaction indicators.
    prod_name, no_of_purchase, no_of_sale, cost_per_item, selp_per_item = ArrayList(n) #store products' information in lists

    prd_prof_loss_percent = ProductPnLPercent(no_of_purchase, no_of_sale, cost_per_item, selp_per_item) #generate list of profit/loss percentage for each product

    desc_order = SortOrder(prd_prof_loss_percent) #generate descending order index by sorting profit/loss percentage

    prod_name = NewArraySorted(prod_name, desc_order) #re-order values in product names list
    no_of_purchase = NewArraySorted(no_of_purchase, desc_order) #re-order values in no of purchase list
    no_of_sale = NewArraySorted(no_of_sale, desc_order) #re-order values in no of sale list
    cost_per_item = NewArraySorted(cost_per_item, desc_order) #re-order values in purchase cost list
    selp_per_item = NewArraySorted(selp_per_item, desc_order) #re-order values in selling price list
    prd_prof_loss_percent = NewArraySorted(prd_prof_loss_percent, desc_order) #re-order values in profit/loss percentage list

    tot_sale, tot_cost, tot_prof_loss = NetProfitLoss(no_of_purchase, no_of_sale, cost_per_item, selp_per_item) #generate total sale, total cost, net profit/loss percentage for the whole product list

    #structure table format and print values
    col1 = '  '
    col2 = '    Name    '
    col3 = ' #Purchases '
    col4 = '  #Sales  '
    col5 = '   Cost   '
    col6 = ' Selling Price '
    col7 = ' Total Purchase '
    col8 = ' Total Sales '
    col9 = '  P/L%  '
    col10 = ' Profit/Loss/Break-even '

    print(col1 + ' ' + col2 + '|' + col3 + '|' + col4 + '|' + col5 + '|' + col6 + '|' + col7 + '|' +col8 + '|' + col9 + '|' + col10 + '|')
    print('-'*134)
    for i in range(n):
        string = str(i+1) + ' '*(len(col1) - len(str(i+1))) + ' ' \
                 + ' ' + prod_name[i] + ' '*(len(col2) - len(prod_name[i]) - 1) + ' ' \
                 + '  ' + str(no_of_purchase[i]) + ' '*(len(col3) - len(str(no_of_purchase[i])) - 2) + ' ' \
                 + '   ' + str(no_of_sale[i]) + ' '*(len(col4) - len(str(no_of_sale[i])) - 3) + ' ' \
                 + ' $' + str(cost_per_item[i]) + ' '*(len(col5) - len(str(cost_per_item[i])) - 2) + ' ' \
                 + ' $' + str(selp_per_item[i]) + ' '*(len(col6) - len(str(selp_per_item[i])) - 2) + ' ' \
                 + ' $' + str(no_of_purchase[i]*cost_per_item[i]) + ' '*(len(col7) - len(str(no_of_purchase[i]*cost_per_item[i])) - 2) + ' ' \
                 + ' $' + str(no_of_sale[i]*selp_per_item[i]) + ' '*(len(col8) - len(str(no_of_sale[i]*selp_per_item[i])) - 2) + ' ' \
                 + ' ' + str(prd_prof_loss_percent[i]) + '%' + ' '*(len(col9) - len(str(prd_prof_loss_percent[i])) - 2) + ' ' \
                 + '   ' + Label(prd_prof_loss_percent[i])

        print(string)
    print('-'*134)
    string = 'Net Profit/Loss' + ' '*(len(col1) + len(col2) + len(col3) + len(col4) + len(col5) + len(col6) + 5 - len('Net Profit/Loss')) + ' ' \
             + ' $' + str(tot_cost) + ' '*(len(col7) - len(str(tot_cost)) - 2) + ' ' \
             + ' $' + str(tot_sale) + ' '*(len(col8) - len(str(tot_sale)) - 2) + ' ' \
             + ' ' + str(tot_prof_loss) + '%' + ' '*(len(col9) - len(str(tot_prof_loss)) - 2) + ' ' \
             + '   ' + Label(tot_prof_loss)
    print(string)

#execute function PrintTable() with input n
PrintTable(n)
