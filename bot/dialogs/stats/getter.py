import logging

from aiogram_dialog import DialogManager
from aiogram.types import User
from fluentogram import TranslatorRunner
from sqlalchemy.ext.asyncio import AsyncSession

from services import get_user, item_code_reader, get_equipment, effects_to_details

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format='%(filename)s:%(lineno)d #%(levelname)-8s '
           '[%(asctime)s] - %(name)s - %(message)s')


# Getting User data from Database
async def character_stats_getter(dialog_manager: DialogManager,
                                 session: AsyncSession,
                                 i18n: TranslatorRunner,
                                 event_from_user: User,
                                 **kwargs) -> dict:
    user_id = event_from_user.id
    logger.info(f'User {user_id} getting info about character')
    user = await get_user(session, user_id)
    dialog_manager.current_context().dialog_data['equipment'] = user.equipment

    return {'characters_stats': i18n.characters.stats(first_name=user.first_name,
                                                      health=user.health,
                                                      bioresource=user.bioresource,
                                                      crystals=user.crystals),
            'button_armor': i18n.button.armor(),
            'button_weapon': i18n.button.weapon(),
            'button_back': i18n.button.back()}


# Getting list of armor of User
async def character_armor_getter(dialog_manager: DialogManager,
                                 session: AsyncSession,
                                 i18n: TranslatorRunner,
                                 event_from_user: User,
                                 **kwargs) -> dict:
    user_id = event_from_user.id
    logger.info(f'User {user_id} getting armor of character')
    armor_list: list = [] # For result of Character Armor
    equipment = str(dialog_manager.current_context().dialog_data['equipment'])
    items = item_code_reader(equipment)

    logger.info(f'Need to get items: {items}')
    
    if 'head' in items:
        head = await get_equipment(session, 
                                   item_id = items['head'][0],
                                   health_current = items['head'][1])
        armor_list.append(f'🪖-{head.name} - {items['head'][1]}% {head.effect}')
    else:
        armor_list.append(f'🪖-{i18n.empty()} - 🔪0/🧪0/⚡️0')

    if 'chest' in items:
        chest = await get_equipment(session, 
                                    item_id = items['chest'][0],
                                    health_current = items['chest'][1])
        armor_list.append(f'🦺-{chest.name} - {items['chest'][1]}% {chest.effect}')
    else:
        armor_list.append(f'🦺-{i18n.empty()} - 🔪0/🧪0/⚡️0')
 
    if 'foot' in items:
        foot = await get_equipment(session, 
                                   item_id = items['foot'][0],
                                   health_current = items['foot'][1])
        armor_list.append(f'👞-{foot.name} - {items['foot'][1]}% {foot.effect}')
    else:
        armor_list.append(f'👞-{i18n.empty()} - 🔪0/🧪0/⚡️0')

    if 'bag' in items:
        bag = await get_equipment(session, 
                                  item_id = items['bag'][0],
                                  health_current = items['bag'][1])
        armor_list.append(f'🎒-{bag.name} - {items['bag'][1]}% {bag.effect}')
    else:
        armor_list.append(f'🎒-{i18n.empty()} - 2')
 
    return {'characters_armor': i18n.characters.armor(),
            'armor_list': armor_list,
            'button_back': i18n.button.back()}


# Getting list of weapon of User
async def character_weapon_getter(dialog_manager: DialogManager,
                                  session: AsyncSession,
                                  i18n: TranslatorRunner,
                                  event_from_user: User,
                                  **kwargs) -> dict:
    user_id = event_from_user.id
    logger.info(f'User {user_id} getting weapon of character')
    weapon_list: list = [] # For result of Character weapon
    equipment = dialog_manager.current_context().dialog_data['equipment']
    items = item_code_reader(equipment)

    logger.info(f'Need to get items: {items}')
    
    if 'weapon1' in items:
        weapon1 = await get_equipment(session, 
                                      item_id = items['weapon1'][0],
                                      health_current = items['weapon1'][1])
        weapon_list.append(f'⚔1-{weapon1.name} - {items['weapon1'][1]}% {weapon1.effect}')
    else:
        weapon_list.append(f'⚔1-{i18n.empty()} - 🔪0-0-5/🧪0-0-0/⚡️0-0-2')

    if 'weapon2' in items:
        weapon2 = await get_equipment(session, 
                                      item_id = items['weapon2'][0],
                                      health_current = items['weapon2'][1])
        weapon_list.append(f'⚔2-{weapon2.name} - {items['weapon2'][1]}% {weapon2.effect}')
    else:
        weapon_list.append(f'⚔2-{i18n.empty()} - 🔪0-0-5/🧪0-0-0/⚡️0-0-2') 
    
    logger.info(f'Total list to return: {weapon_list}')
 
    return {'characters_weapon': i18n.characters.weapon(),
            'weapon_list': weapon_list,
            'button_back': i18n.button.back()}


# Getting data of selected equipment
async def equipment_details_getter(dialog_manager: DialogManager,
                                   session: AsyncSession,
                                   i18n: TranslatorRunner,
                                   event_from_user: User,
                                   **kwargs) -> dict:
    user_id = event_from_user.id
    item = dialog_manager.current_context().dialog_data['selected_item']
    eqipment = dialog_manager.current_context().dialog_data['equipment']
    logger.info(f'User {user_id} get information about his {item}')
    items = item_code_reader(eqipment)

    # What item is it? Get it by emoji
    item_type_map = {'🪖': 'head',
                     '🦺': 'chest',
                     '👞': 'foot',
                     '🎒': 'bag',
                     '1': 'weapon1',
                     '2': 'weapon2'}
    item = items[item_type_map[item]]  # Here we have list [id, item_health]
    logger.info(f'ID and Current health of selected item is {item}')
    selected_item = await get_equipment(session,
                                        item_id = item[0],
                                        health_current = item[1])

    effects = effects_to_details(selected_item.effect, i18n)

    return {'equipment_details': i18n.equipment.details(name=selected_item.name,
                                                        description=selected_item.description,
                                                        current_health=item[1],
                                                        effects=effects            
                                                        ),
            'button_unequip': i18n.button.unequip(),
            'button_back': i18n.button.back()}
