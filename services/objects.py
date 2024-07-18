from .classes import Equipment


# Armor
helmet_cosmo = Equipment(id=0, 
                         item_type='h', 
                         name='Шлем космонавта',
                         effect='5/35/45',
                         health_max=5000,
                         bio_cost=5000,
                         health_current=5000,
                         repair_weak=100,
                         repair_strong=1000,
                         cost_repair_weak='pass',
                         cost_repair_strong=100)


helmet_stranger = Equipment(id=1,
                            item_type='h', 
                            name='Шлем странника',
                            effect='10/10/10',
                            health_max=1000,
                            bio_cost=500,
                            health_current=1000,
                            repair_weak=200,
                            repair_strong=50,
                            cost_repair_weak='pass',
                            cost_repair_strong=25)


helmet_forces = Equipment(id=2, 
                          item_type='h', 
                          name='Усиленный Шлем',
                          effect='15/10/10',
                          health_max=1200,
                          bio_cost=600,
                          health_current=1200,
                          repair_weak=200,
                          repair_strong=50,
                          cost_repair_weak='pass',
                          cost_repair_strong=25)


chest_cosmo = Equipment(id=3, 
                        item_type='c', 
                        name='Костюм космонавта',
                        effect='10/30/35',
                        health_max=5500,
                        bio_cost=5000,
                        health_current=5500,
                        repair_weak=100,
                        repair_strong=1000,
                        cost_repair_weak='50/4',
                        cost_repair_strong='100')


chest_stranger = Equipment(id=4, 
                           item_type='c', 
                           name='Костюм странника',
                           effect='15/10/5',
                           health_max=1100,
                           bio_cost=550,
                           health_current=1100,
                           repair_weak=200,
                           repair_strong=50,
                           cost_repair_weak='pass',
                           cost_repair_strong=25)

chest_forces = Equipment(id=5, 
                         item_type='c', 
                         name='Усиленный костюм',
                         effect='20/15/10',
                         health_max=1400,
                         bio_cost=700,
                         health_current=1400,
                         repair_weak=200,
                         repair_strong=50,
                         cost_repair_weak='pass',
                         cost_repair_strong=25)

foot_cosmo = Equipment(id=6, 
                       item_type='f', 
                       name='Ботинки космонавта',
                       effect='5/30/35',
                       health_max=4000,
                       bio_cost=4000,
                       health_current=4000,
                       repair_weak=100,
                       repair_strong=1000,
                       cost_repair_weak='50/4',
                       cost_repair_strong='100')


foot_stranger = Equipment(id=7, 
                          item_type='f', 
                          name='Ботинки странника',
                          effect='5/5/5',
                          health_max=800,
                          bio_cost=400,
                          health_current=800,
                          repair_weak=200,
                          repair_strong=50,
                          cost_repair_weak='pass',
                          cost_repair_strong=25)

foot_forces = Equipment(id=8, 
                        item_type='f', 
                        name='Усиленные ботинки',
                        effect='10/10/5',
                        health_max=900,
                        bio_cost=450,
                        health_current=900,
                        repair_weak=200,
                        repair_strong=50,
                        cost_repair_weak='pass',
                        cost_repair_strong=25)

# Weapon
g_17 = Equipment(id=9, 
                 item_type='w', 
                 name='G-17',
                 effect='0_35_45/0_0_0/0_0_10',
                 health_max=5000,
                 bio_cost=5000,
                 health_current=5000,
                 repair_weak=100,
                 repair_strong=1000,
                 cost_repair_weak='50/4',
                 cost_repair_strong='100')


spear_sharpened = Equipment(id=10, 
                            item_type='w', 
                            name='Заточенное копье',
                            effect='0_0_30/0_0_35/0_0_5',
                            health_max=5000,
                            bio_cost=5000,
                            health_current=5000,
                            repair_weak=100,
                            repair_strong=1000,
                            cost_repair_weak='50/4',
                            cost_repair_strong='100')
