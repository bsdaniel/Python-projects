import os



def main():
    f = input('Please enter a file name: ')
    while not os.path.isfile(f):
        print('{} doesnt exits!'.format(f))
        f = input('Please enter a file name: ')
    f = open(f)
    skip_first = True

    my_list = []
    counties = f.readlines()
    for line in counties: 
        if skip_first == True:
            skip_first = False
            continue
        bab = line.split()
            
        name = line[193:238].strip()
        percent = float(bab[11])
        count = int(bab[8])
        income = int(bab[20])
    
        county={'name':name, 'percent':percent, 'count':count,'income':income}
        my_list.append(county)

                  
    my_sorted_list = sorted(my_list, key=lambda x: x['percent'])
    #print(my_sorted_list)

    print_highest_data(my_sorted_list)
    print_lowest_data(my_sorted_list)
    search_counties(my_sorted_list)

    f.close()



    
def search_counties(my_sorted_list):
    search = input('Search: ').lower()
    
    while search not in ['q','quit']:
        for county in my_sorted_list:
            name = county['name'].lower()
            if search.lower() in name:
                print_county(county)

        search = input('Search: ').lower()
    


def print_highest_data(counties):
    print_county(counties[-1])
    

def print_lowest_data(counties):
    print_county(counties[0])


def print_county(county):

    print('Name: %s'% county['name'])
    print('Percentage: %.2f%%' % county['percent'])
    print('Children in Poverty: {:,}'.format(county['count']))
    print('Household Income: ${:,}'.format(county['income']))
    print()
    



if __name__ == '__main__':
    main()












