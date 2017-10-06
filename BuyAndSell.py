#Buy and Sell and keeping track of the stocks and profit mechanism 
#dictionary of number of stocks that the user buy 

Stock ={}

def get_percentage(name,day):
    today = get_price(name,day)
    yesterday = get_price(name,day)
    percent = (today/yesterday)*100-1
    percent_string = str(percent) +"%"
    return percent_string 
    

def buy(name,day):
    quantity = request.args['buy']
    global Stock
    global money 
    global invested_money
    statement = ""
    today_price = get_price(name,day)
    cost = today_price*quantity
    if cost < money: 
        money = money - cost 
        invested_money = cost
        statement = "Transaction succeed"
    else:
        statement = "Too much money can't handle it"
    
    #add value to dictionary
    check = 0
    for keys in Stock: 
        if keys == name:
            Stock[name] = Stock[name]+quantity
            check = 1
    if check == 0:
        Stock[name] = quantity
    return statement

def sell(name,day):
    global Stock
    global money
    global invested_money
    quantity = request.args['sell']
    statement = " "
    for keys in Stock: 
        if keys == name:
            if Stock[name]>=quantity:
                Stock[name] -= quantity
                today_price = get_price(name,day)
                profit = today_price*quantity
                if invested_money < profit: 
                    invested_money = 0
                else: 
                    invested_money = invested_money - profit
                money = money + profit
                statement = "Sell complete"
            else:
                statemment ="Cannot sell"
    return statement

def total_money():
    return money+invested_money
def growth_money(day):
    global invested_money
    global Stock
    invested_money = 0
    for keys in Stock:
        current_value = get_price(keys,day)
        invested_money += Stock[keys]*current_value
    
    return invested_money
        