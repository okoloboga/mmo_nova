class Equipment():

    def __init__(self,
                 id: int,
                 item_type: str,
                 name: str, 
                 effect: str, 
                 health_max: int,
                 bio_cost: int,
                 health_current: str,
                 repair_weak: int,
                 repair_strong: int,
                 cost_repair_weak: str,
                 cost_repair_strong: int
                 ):
    self.id = id                                    # Item id, armor starts from 'a'
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


    def __str__(self):
        return f'{self.name} {self.health_current} {self.defense}


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
        if strength == 'weak':
            self.health_current += self.repair_weak
        elif strength == 'strong':
            self.health_current += self.repair_strong
    

    # Processing damage of Equipment
    def equipment_damage(self, damage: int):
        self.health_current -= damage


    # Dealing damage, if it weapon
    def deal_damage(self, distance: int) -> int:
        if self.item_type == 'w':

            damage_list = self.effect.split('/')

            balistic = damage_list[0]
            chemical = damage_list[1]
            electro = damage_list[2]

        else:
            return -1
    

    # Return code of currents item state for database
    # /a'type'[id]_[hp]%
    def item_code(self) -> str:
        return f'/a{self.item_type}{self.id}_{int((self.health_current / self.health_max) * 100)}%'

