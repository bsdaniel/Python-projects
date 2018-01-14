
file_name = input('Sale file: ')
categories = {}
try:
    f = open(file_name)
    for line in f:
        fields = line.split(';')
        name, service, price, date, = fields
        try:
            price = float(price)
            cust_services = {'service': service, 'price': price}

            if service in categories:
                categories[service] = round((categories[service] + price),2)
            else:
                categories[service] = price
        except ValueError:
            print('The amount, %s, cannot be converted to a float!' % price)


    for key in categories.keys():
        print('%s: $%.2f'%(key,categories[key]))

    f.close()

except IOError:
    print("[Errno 2] No such file or directory: '%s'" % file_name)


    


    
