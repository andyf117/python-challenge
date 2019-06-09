import pandas as pd





dataframe_ = pd.read_csv('budget_data.csv')
list_x = dataframe_['Date'].tolist()



#The total number of months included in the dataset
months_ = dataframe_['Date'].tolist()
length_months_ = len(months_)
print("The total number of months: " + str(length_months_) )


# The net total amount of "Profit/Losses" over the entire period
net_list = dataframe_['Profit/Losses'].tolist()

net_total = 0

length_net_list = len(net_list)

for i in range(0, length_net_list):
    net_total+=net_list[i]
    
net_string = str(net_total)
print("\n\nThe net total amount of Profit/Losses over the entire period is: " + net_string)

#The average of the changes in "Profit/Losses" over the entire period
average = net_total/len(net_list)
average_string = str(average)
print("The average of the changes in Profit/Losses over the entire period: " + average_string)

max_ = max(net_list)
print("Greatest Increase in Profits: " + str(max_))

min_ = min(net_list)
print("Greatest Decrease in Profits: " + str(min_))
