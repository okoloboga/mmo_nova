'''

  /$$$$$$   /$$$$$$  /$$$$$$/$$$$   /$$$$$$   /$$$$$$ 
 |____  $$ /$$__  $$| $$_  $$_  $$ /$$__  $$ /$$__  $$
  /$$$$$$$| $$  \__/| $$ \ $$ \ $$| $$  \ $$| $$  \__/
 /$$__  $$| $$      | $$ | $$ | $$| $$  | $$| $$      
|  $$$$$$$| $$      | $$ | $$ | $$|  $$$$$$/| $$      
 \_______/|__/      |__/ |__/ |__/ \______/ |__/     
 
 
  /$$                 /$$                           /$$    
| $$                | $$                          | $$    
| $$$$$$$   /$$$$$$ | $$ /$$$$$$/$$$$   /$$$$$$  /$$$$$$  
| $$__  $$ /$$__  $$| $$| $$_  $$_  $$ /$$__  $$|_  $$_/  
| $$  \ $$| $$$$$$$$| $$| $$ \ $$ \ $$| $$$$$$$$  | $$    
| $$  | $$| $$_____/| $$| $$ | $$ | $$| $$_____/  | $$ /$$
| $$  | $$|  $$$$$$$| $$| $$ | $$ | $$|  $$$$$$$  |  $$$$/
|__/  |__/ \_______/|__/|__/ |__/ |__/ \_______/   \___/  

'''

 
helmet_cosmo = {'item_id': 0,
                'item_type': 'h', 
                'name': 'Шлем космонавта',
                'effect': '5/35/45',
                'health_max': 5000,
                'bio_cost': 5000,
                'repair_weak': 100,
                'repair_strong': 1000,
                'cost_repair_weak': 'pass',
                'cost_repair_strong': 100,
                'description': ('Стандартный шлем космонавта.\n'
                                + 'Громоздкий, тяжелый и неудобный.')}


helmet_stranger = {'item_id': 1,
                   'item_type': 'h', 
                   'name': 'Шлем странника',
                   'effect': '10/10/10',
                   'health_max': 1000,
                   'bio_cost': 500,
                   'repair_weak': 200,
                   'repair_strong': 50,
                   'cost_repair_weak': 'pass',
                   'cost_repair_strong': 25,
                   'description': ('Легкая и простая защита головы.\n'
                                   + 'Можно сделать из того, что есть под рукой.')}


helmet_forces = {'item_id': 2, 
                 'item_type': 'h', 
                 'name': 'Усиленный Шлем',
                 'effect': '15/10/10',
                 'health_max': 1200,
                 'bio_cost': 600,
                 'repair_weak': 200,
                 'repair_strong': 50,
                 'cost_repair_weak': 'pass',
                 'cost_repair_strong': 25,
                 'description': ('Шлем странника.\n'
					   		     + 'Усиленный каркасом из костей и перетяннутый жилами.')}


'''
           /$$                             /$$    
          | $$                            | $$    
  /$$$$$$$| $$$$$$$   /$$$$$$   /$$$$$$$ /$$$$$$  
 /$$_____/| $$__  $$ /$$__  $$ /$$_____/|_  $$_/  
| $$      | $$  \ $$| $$$$$$$$|  $$$$$$   | $$    
| $$      | $$  | $$| $$_____/ \____  $$  | $$ /$$
|  $$$$$$$| $$  | $$|  $$$$$$$ /$$$$$$$/  |  $$$$/
 \_______/|__/  |__/ \_______/|_______/    \___/
'''


chest_cosmo = {'item_id': 3, 
               'item_type': 'c', 
               'name': 'Костюм космонавта',
               'effect': '10/30/35',
               'health_max': 5500,
               'bio_cost': 5000,
               'repair_weak': 100,
               'repair_strong': 1000,
               'cost_repair_weak': 'pass',
               'cost_repair_strong': 100,
               'description': ('Стандартный костюм космонавта.\n'
 							   + 'Жаркий, неудобный, большой и очень заметный.')}


chest_stranger = {'item_id': 4, 
                  'item_type': 'c', 
                  'name': 'Костюм странника',
                  'effect': '15/10/5',
                  'health_max': 1100,
                  'bio_cost': 550,
                  'repair_weak': 200,
                  'repair_strong': 50,
                  'cost_repair_weak': 'pass',
                  'cost_repair_strong': 25,
                  'description': ('Легкая и простая защита тела.\n'
							      + 'Можно сделать из того что есть под рукой.')}


chest_forces = {'item_id': 5, 
                'item_type': 'c', 
                'name': 'Усиленный костюм',
                'effect': '20/15/10',
                'health_max': 1400,
                'bio_cost': 700,
                'repair_weak': 200,
                'repair_strong': 50,
                'cost_repair_weak': 'pass',
                'cost_repair_strong': 25,
                'description': ('Костюм странника.\n'
							    + 'Усиленный каркасом из костей и перетяннутый жилами.')}


'''
  /$$$$$$                      /$$    
 /$$__  $$                    | $$    
| $$  \__//$$$$$$   /$$$$$$  /$$$$$$  
| $$$$   /$$__  $$ /$$__  $$|_  $$_/  
| $$_/  | $$  \ $$| $$  \ $$  | $$    
| $$    | $$  | $$| $$  | $$  | $$ /$$
| $$    |  $$$$$$/|  $$$$$$/  |  $$$$/
|__/     \______/  \______/    \___/ 
'''

foot_cosmo = {'item_id': 6, 
              'item_type': 'f', 
              'name': 'Ботинки космонавта',
              'effect': '5/30/35',
              'health_max': 4000,
              'bio_cost': 4000,
              'repair_weak': 100,
              'repair_strong': 1000,
              'cost_repair_weak': 'pass',
              'cost_repair_strong': 100,
              'description': ('Стандартный ботинки космонавта.\n'
					   	      + 'Тжелые и шумные.')}


foot_stranger = {'item_id': 7, 
                 'item_type': 'f', 
                 'name': 'Ботинки странника',
                 'effect': '5/5/5',
                 'health_max': 800,
                 'bio_cost': 400,
                 'repair_weak': 200,
                 'repair_strong': 50,
                 'cost_repair_weak': 'pass',
                 'cost_repair_strong': 25,
                 'description': ('Легкая и простая защита ног.\n'
							     + 'Можно сделать из того что есть под рукой. ')}


foot_forces = {'item_id': 8, 
               'item_type': 'f', 
               'name': 'Усиленные ботинки',
               'effect': '10/10/5',
               'health_max': 900,
               'bio_cost': 450,
               'repair_weak': 200,
               'repair_strong': 50,
               'cost_repair_weak': 'pass',
               'cost_repair_strong': 25,
               'description': ('Ботинки странника.\n'
				     		   + 'Усиленные каркасом из костей и перетяннутый жилами.')}


''' 
 /$$                          
| $$                          
| $$$$$$$   /$$$$$$   /$$$$$$ 
| $$__  $$ |____  $$ /$$__  $$
| $$  \ $$  /$$$$$$$| $$  \ $$
| $$  | $$ /$$__  $$| $$  | $$
| $$$$$$$/|  $$$$$$$|  $$$$$$$
|_______/  \_______/ \____  $$
                     /$$  \ $$
                    |  $$$$$$/
                     \______/
''' 

bag_leafy = {'item_id': 9,
             'item_type': 'b',
             'name': 'Рюкзак лиственный',
             'effect': '4',
             'health_max': 150,
             'bio_cost': 300,
             'repair_weak': 50,
             'repair_strong': 10,
             'cost_repair_weak': 'pass',
             'cost_repair_strong': 20,
             'description': ('Простой рюкзак сделанный из подручных средств')}

bag_leafy_creeper = {'item_id': 10,
                     'item_type': 'b',
                     'name': 'Рюкзак лиственный лианный',
                     'effect': '6',
                     'health_max': 180,
                     'bio_cost': 360,
                     'repair_weak': 50,
                     'repair_strong': 10,
                     'cost_repair_weak': 'pass',
                     'cost_repair_strong': 20,
                     'description': ('Рюкзак странника укрепленный костями и жилами')}

'''
                                                                 
                                                                
 /$$  /$$  /$$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$$ 
| $$ | $$ | $$ /$$__  $$ |____  $$ /$$__  $$ /$$__  $$| $$__  $$
| $$ | $$ | $$| $$$$$$$$  /$$$$$$$| $$  \ $$| $$  \ $$| $$  \ $$
| $$ | $$ | $$| $$_____/ /$$__  $$| $$  | $$| $$  | $$| $$  | $$
|  $$$$$/$$$$/|  $$$$$$$|  $$$$$$$| $$$$$$$/|  $$$$$$/| $$  | $$
 \_____/\___/  \_______/ \_______/| $$____/  \______/ |__/  |__/
                                  | $$                          
                                  | $$                          
                                  |__/ 
'''


g_17 = {'item_id': 11, 
        'item_type': 'w', 
        'name': 'G-17',
        'effect': '0_35_45/0_0_0/0_0_10',
        'health_max': 20,
        'bio_cost': 1000,
        'repair_weak': 10,
        'repair_strong': 1,
        'cost_repair_weak': 'pass',
        'cost_repair_strong': 50,
        'description': ('Земной пистолет преднаначен для среднего и ближнего боя')}


spear_sharpened = {'item_id': 12, 
                   'item_type': 'w', 
                   'name': 'Заточенное копье',
                   'effect': '0_0_30/0_0_35/0_0_5',
                   'health_max': 15,
                   'bio_cost': 350,
                   'repair_weak': 5,
                   'repair_strong': 1,
                   'cost_repair_weak': 'pass',
                   'cost_repair_strong': 30,
                   'description': ('Крепкая легкая палка с наконечником из заточенной кости\n'
			 					   + 'предназначен для ближнего боя')}

unarmed = {'item_id': 13,
           'item_type': 'w',
           'name': 'Отсутствует',
           'effect': '0_0_5/0_0_2/0_0_0',
           'health_max': 1,
           'bio_cost': 0,
           'repair_weak': 0,
           'repair_strong': 0,
           'cost_repair_weak': '',
           'cost_repair_strong': 0,
           'description': ('Ты собрался защищаться голыми рукми?')}


'''
             /$$                           /$$    
            | $$                          | $$    
  /$$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$  /$$$$$$  
 /$$_____/|_  $$_/   |____  $$ /$$__  $$|_  $$_/  
|  $$$$$$   | $$      /$$$$$$$| $$  \__/  | $$    
 \____  $$  | $$ /$$ /$$__  $$| $$        | $$ /$$
 /$$$$$$$/  |  $$$$/|  $$$$$$$| $$        |  $$$$/
|_______/    \___/   \_______/|__/         \___/  

'''

old_helmet_cosmo = {'item_id': 14, 
                    'item_type': 'h', 
                    'name': 'Шлем космонавта',
                    'effect': '0/2/2',
                    'health_max': 5000,
                    'bio_cost': 5000,
                    'repair_weak': 100,
                    'repair_strong': 1000,
                    'cost_repair_weak': 'pass',
                    'cost_repair_strong': 100,
                    'description': ('Стандартный шлем космонавта.\n'
                                    + 'Грамостки,тяжелый и неудобный.')}


old_chest_cosmo = {'item_id': 15, 
                   'item_type': 'c', 
                   'name': 'Костюм космонавта',
                   'effect': '1/2/2',
                   'health_max': 5500,
                   'bio_cost': 5000,
                   'repair_weak': 100,
                   'repair_strong': 1000,
                   'cost_repair_weak': '50/4',
                   'cost_repair_strong': 100,
                   'description': ('Стандартный костюм космонавта.\n'
                                   + 'Жаркий, неудобный, большой и очень заметный.')}


old_foot_cosmo = {'item_id': 16, 
                  'item_type': 'f', 
                  'name': 'Ботинки космонавта',
                  'effect': '0/2/2',
                  'health_max': 4000,
                  'bio_cost': 4000,
                  'repair_weak': 100,
        	      'repair_strong': 1000,
               	  'cost_repair_weak': '50/4',
                  'cost_repair_strong': 100,
                  'description': ('Стандартный ботинки космонавта.\n'
		    	         	      + 'Тжелые и шумные.')}


''' 
   /$$                 /$$               /$$
  | $$                | $$              | $$
 /$$$$$$    /$$$$$$  /$$$$$$    /$$$$$$ | $$
|_  $$_/   /$$__  $$|_  $$_/   |____  $$| $$
  | $$    | $$  \ $$  | $$      /$$$$$$$| $$
  | $$ /$$| $$  | $$  | $$ /$$ /$$__  $$| $$
  |  $$$$/|  $$$$$$/  |  $$$$/|  $$$$$$$| $$
   \___/   \______/    \___/   \_______/|__/
'''

items_data = {'helmet_cosmo': helmet_cosmo,
              'helmet_stranger': helmet_stranger,
              'helmet_forces': helmet_forces,
              'chest_cosmo': chest_cosmo,
              'chest_stranger': chest_stranger,
              'chest_forces': chest_forces,
              'foot_cosmo': foot_cosmo,
              'foot_stranger': foot_stranger,
              'foot_forces': foot_forces,
              'bag_leafy': bag_leafy,
              'bag_leafy_creeper': bag_leafy_creeper,
              'g_17': g_17,
              'spear_sharpened': spear_sharpened,
              'unarmed': unarmed,
              'old_helmet_cosmo': old_helmet_cosmo,
              'old_chest_cosmo': old_chest_cosmo,
              'old_foot_cosmo': old_foot_cosmo}