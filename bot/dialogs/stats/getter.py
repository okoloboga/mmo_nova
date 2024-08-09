import logging

from aiogram_dialog import DialogManager
from aiogram.types import User
from fluentogram import TranslatorRunner
from sqlalchemy.ext.asyncio import AsyncSession

from services import get_user, item_code_reader, get_equipment

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
        armor_list.append('🪖-'+head.name)
        armor_list.append(f'{head.health_current} {head.effect}')   
    else:
        armor_list.append('🪖-'+i18n.empty())
        armor_list.append('🔪0/🧪0/⚡️0')

    if 'chest' in items:
        chest = await get_equipment(session, 
                                    item_id = items['chest'][0],
                                    health_current = items['chest'][1])
        armor_list.append('🦺-'+chest.name)
        armor_list.append(f'{chest.health_current} {chest.effect}')
    else:
        armor_list.append('🦺-'+i18n.empty())
        armor_list.append('🔪0/🧪0/⚡️0')
 
    if 'foot' in items:
        foot = await get_equipment(session, 
                                   item_id = items['foot'][0],
                                   health_current = items['foot'][1])
        armor_list.append('👞-'+foot.name)
        armor_list.append(f'{foot.health_current} {foot.effect}')
    else:
        armor_list.append('👞-'+i18n.empty())
        armor_list.append('🔪0/🧪0/⚡️0')

    if 'bag' in items:
        bag = await get_equipment(session, 
                                  tem_id = items['bag'][0],
                                  health_current = items['bag'][1])
        armor_list.append('🎒-'+bag.name)
        armor_list.append(f'{bag.health_currevnt} {bag.effect}')
    else:
        armor_list.append('🎒-'+i18n.empty())
        armor_list.append('2')
 
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
    equipment = str(dialog_manager.current_context().dialog_data['equipment'])
    items = item_code_reader(equipment)

    logger.info(f'Need to get items: {items}')
    
    if 'weapon1' in items:
        weapon1 = await get_equipment(session, 
                                      item_id = items['weapon1'][0],
                                      health_current = items['weapon1'][1])
        weapon_list.append('⚔1 '+weapon1.name)
        weapon_list.append(f'{weapon1.health_current} {weapon1.effect}')
    else:
        weapon_list.append('⚔1 '+i18n.empty())
        weapon_list.append('🔪0-0-5/🧪0-0-0/⚡️0-0-2')

    if 'weapon2' in items:
        weapon2 = await get_equipment(session, 
                                      item_id = items['weapon2'][0],
                                      health_current = items['weapon2'][1])
        weapon_list.append('⚔2 '+weapon2.name) 
        weapon_list.append(f'{weapon2.health_current} {weapon2.effect}')
    else:
        weapon_list.append('⚔2 '+i18n.empty()) 
        weapon_list.append('🔪0-0-5/🧪0-0-0/⚡️0-0-2')
    
    logger.info(f'Total list to return: {weapon_list}')
 
    return {'characters_weapon': i18n.characters.weapon(),
            'weapon_list': weapon_list,
            'button_back': i18n.button.back()}
