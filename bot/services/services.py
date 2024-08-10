import logging

from fluentogram import TranslatorRunner
from .constants import PHYS, CHEM, ELEC

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
            item_health = int((item[2:].split('_'))[1][:-1])

            logger.info(f'[{item_type}, {item_id}, {item_health}]')       
            
            # Is first Weapon in results yet?
            if item_type == 'w':
                item_type = 'w1' if 'weapon1' not in result else 'w2'

            result[name_code[item_type]] = (item_id, item_health)

            ''' 
            example
            {
             'head': [14, 5],
             'chest': [15, 5],
             ...
             }
            '''       
        return result
    else:
        return None
        

# Transform effects information from database to detailed information
def effects_to_details(effect_str: str,
                       i18n: TranslatorRunner) -> str:

    logger.info(f'effects_to_details({effect_str})')
    
    if len(effect_str) == 1:
        # Bag
        result = f'{effect_str} {i18n.cells.of.bag()}'

    elif len(effect_str) >= 20:
        # Weapon
        effect_list = effect_str.split('/')
        # ['🔪0-35-45', '🧪0-0-0', '⚡️0-0-10']
        f = [(i[1:]).split('-') for i in effect_list] 
        # [[0, 35, 45], [0, 0, 0], [0, 0, 10]]
        f = [list(map(lambda x: int(x.replace(chr(65039), '')), j)) for j in f]
        result = f'{i18n.closedamage.describe()} {PHYS}{f[0][0]}/{CHEM}{f[1][0]}/{ELEC}{f[2][0]}={f[0][0]+f[1][0]+f[2][0]}\n\
{i18n.middledamage.describe()} {PHYS}{f[0][1]}/{CHEM}{f[1][1]}/{ELEC}{f[2][1]}={f[0][1]+f[1][1]+f[2][1]}\n\
{i18n.rangedamage.describe()} {PHYS}{f[0][2]}/{CHEM}{f[1][2]}/{ELEC}{f[2][2]}={f[0][2]+f[1][2]+f[2][2]}'
    else:
        # Armor
        effect_list = effect_str.split('/')
        logger.info(f'effect_list: {effect_list}')
        # ['🔪0', '🧪2', '⚡️2']
        f = [int(i.replace(chr(65039), '')[1]) for i in effect_list]
        # ['0', '2', '2']
        result = f'{PHYS}{f[0]}%-{i18n.physical.defense.describe()}\n\
{CHEM}{f[1]}%-{i18n.chemecal.defense.describe()}\n\
{ELEC}{f[2]}%-{i18n.electric.defense.describe()}'

    return result












