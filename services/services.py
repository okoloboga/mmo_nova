# Tramsform user equipment data from Database to dict
def item_code_reader(item_code: str) -> dict:
    
    result: dict  # for transformed data
    temp: list  # for processing
    name_code = {
                 'h': 'head',
                 'c': 'chest',
                 'f': 'foot',
                 'b': 'bag',
                 'w': 'weapon'
                 }
    
    
    item_code_list = item_code.split()
    
    for item in item_code_list:
        
        # example: ['h', 3, 0.45]
        temp.append([item[1], 
                    int((item[2:].split('_'))[1]), 
                    round(((item[2:].split('_'))[2][:-1] / 100), 2)])
        
        ''' 
        
        example
        {
         'head': [2, 0.7],
         'chest': [5, 0.5],
         ...
         }
         
        '''
        result[name_code[temp[0]]] = (temp[1], temp[2])
        
    return result
         
    

