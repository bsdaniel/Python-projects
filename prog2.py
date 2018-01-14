#!/usr/bin/env python3

import csv


def get_data_list(FILE_NAME):
    data_list = []

    with open('table.csv','r') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=',')
        skip_first = True
        for row in file_reader:
            if skip_first == True:
                skip_first = False
                continue
        
            data_list.append(row)

            date = row [0]
            opencol = row [1]
            high = row [2]
            low = row [3]
            closecol = row [4]
            volume = row [5]
            Adj = row [6]
       

         

    return data_list


def get_monthly_averages(data_list):
    date_column = 0
    volume_column = 5
    close_column = 6



    tmp_dict = {}

    for data in data_list:

    	date = data[date_column]

    	volume = int(data[volume_column])

    	close = float(data[close_column])
    	date = date[5:7] + '-' + date[:4]
    	if date in tmp_dict:
    		tmp_dict[date]['sales'] += volume * close
    		tmp_dict[date]['volume'] += volume
    	else:
    		tmp_dict[date] = {

    			'sales': volume * close,

    			'volume': volume

    		} 
    monthly_average_list = []

    for date in tmp_dict.keys(): 

    	avg = tmp_dict[date]['sales'] / tmp_dict[date]['volume']

    	monthly_average_list.append((avg, date))

    monthly_average_list.sort()

    monthly_average_list.reverse()

    return monthly_average_list



def print_info(monthly_average_list):
    with open('monthly_averages.txt','a') as w:
        w.write('')
        w.write('Highest 6 months: \n')
        higher = (monthly_average_list[:6])
        for high in higher:
            w.write('%s: %.2f\n' % (high[1],high[0]))

            w.write('')
            

        w.write('Lowest 6 months: \n')
        lowest = (monthly_average_list[-6:])
        for low in lowest:
            w.write('%s: %.2f\n' % (low[1],low[0]))

def main():
        
    File = input('Please enter a stock file: ')

    data_list = get_data_list(File)

    month_average = get_monthly_averages(data_list)
    
    print_info(month_average)
if __name__ == '__main__':
    main()
