class ItemEquipment():

    def __init__(self,
                 item_id: int,
                 item_type: str,
                 name: str, 
                 effect: str, 
                 health_max: int,
                 bio_cost: int,
                 health_current: str,
                 repair_weak: int,
                 repair_strong: int,
                 cost_repair_weak: str,
                 cost_repair_strong: int,
                 description: str
                 ):
        
        self.item_id = item_id                                    # Item id, armor starts from 'a'
        self.item_type = item_type                      # head='h', chest='c', foot='f', bag='b', weapon='w' 
        self.name = name                                # Letter string
        self.effect = effect                            # If armour - defense, if weapo - attack: balistic/chemical/electro
                                                        # Weapon by distance: b_b_b/c_c_c/e_e_e    
        self.health_max = health_max                    # hp
        self.bio_cost = bio_cost                        # bio
        self.health_current = health_current            # int
        self.repair_weak = repair_weak                  # hp
        self.repair_strong = repair_strong              # hp
        self.cost_repair_weak = cost_repair_weak        # bio/crystals
        self.cost_repair_strong = cost_repair_strong    # craft recipe
        self.description = description                  # description of item


    def __str__(self) -> str:
        
        return f'{self.name} {self.health_current} {self.defense}'


    # Getting precentage of damage and current cost and profit of repair
    def ask_repair(self) -> dict:
        
        hp_precentage = int(self.health_current / self.health_max)
        if hp_precentage <= 0.5:
            repair = {'profit': self.repair_weak,
                      'cost': self.cost_repair_weak}
        else:
            repair = {'profit': self.repair_strong,
                      'cost': self.cost_repair_strong}
        return repair

    
    # Processing of Equipment repair
    def repair(self, strength: str):
        
        if self.name != 'Отсутствует':
            if strength == 'weak':
                self.health_current += self.repair_weak
            elif strength == 'strong':
                self.health_current += self.repair_strong
        else:
            pass    

    # Processing damage of Equipment
    def equipment_damage(self, damage: int):
        
        self.health_current -= damage


    # Dealing damage, if it weapon. Distance: 0, 1, 2, Enemy resist: [0, 0.3, 0.65]
    def deal_damage(self, distance: int, enemy_resists: list) -> int:
        
        if self.item_type == 'w':

            damage_list = self.effect.split('/')

            balistic = damage_list[0].split('_')
            chemical = damage_list[1].split('_')
            electro = damage_list[2].split('_')

            return (balistic[distance]*enemy_resists[0] 
                    + chemical[distance]*enemy_resists[1] 
                    + electro[distance]*enemy_resists[2])
            
        else:
            return -1
    

    # Return code of currents item state for database
    # /'type'[id]_[hp]%
    def item_code(self) -> str:
        
        return f'/{self.item_type}{self.item_id}_{int((self.health_current / self.health_max) * 100)}%'

