import pandas as pd
import os
from time import sleep
from random import randint

def read_items(file_name):
    laptop = pd.read_excel(file_name, sheet_name='Laptop')
    mobile = pd.read_excel(file_name, sheet_name='Mobile')
    soap = pd.read_excel(file_name, sheet_name='Soap')
    duck = pd.read_excel(file_name, sheet_name='Rubber Duck')
    return laptop, mobile, soap, duck

def join_products():
    amazon_items = read_items('Amazon_20_RPA.xlsx');
    flipkart_items = read_items('Flipkart_20_RPA.xlsx');
    
    items = []
    for i in range(len(amazon_items)):
        items.append(pd.concat([amazon_items[i], flipkart_items[i]], ignore_index=True))
    
    for item in items:    
        item.sort_values(by=['Price'], ascending=True)
        
    item_obj = {
        'laptop': items[0],
        'mobile': items[1],
        'soap': items[2],
        'rubber duck': items[3]
    }

    # sleep(randint(23, 37))
    return item_obj

productItems = join_products()
# print(productItems['laptop'])

if __name__ == '__main__':
    pass
    

    
    