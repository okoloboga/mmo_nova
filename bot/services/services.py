import logging

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format='%(filename)s:%(lineno)d #%(levelname)-8s '
           '[%(asctime)s] - %(name)s - %(message)s')


# Tramsform user equipment data from Database to dict
# Itemcode example: '/h14_5% /c15_5% /f16_5% /w11_30%'
def item_code_reader(item_code: str) -> dict | None:
    
    result: dict = {} # for transformed data
    name_code = {
                 'h': 'head',
                 'c': 'chest',
                 'f': 'foot',
                 'b': 'bag',
                 'w1': 'weapon1',
                 'w2': 'weapon2'
                 }
        
    item_code_list = item_code.split()
    logger.info(f'item_code_list: {item_code_list}')

    # result example
    # ['/h14_5%', '/c15_5%', '/f16_5%', '/w11_30%']
    if len(item_code) != 0:
        for item in item_code_list:
            
            item_type = item[1]
            item_id = int((item[2:].split('_'))[0])
            item_health = round((int((item[2:].split('_'))[1][:-1]) / 100), 2)

            logger.info(f'[{item_type}, {item_id}, {item_health}]')       
            
            # Is first Weapon in results yet?
            if item_type == 'w':
                item_type = 'w1' if 'weapon1' not in result else 'w2'

            result[name_code[item_type]] = (item_id, item_health)

            ''' 
            example
            {
             'head': [2, 0.7],
             'chest': [5, 0.5],
             ...
             }
            '''       
        return result
    else:
        return None
        

