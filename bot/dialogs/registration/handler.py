import logging

from aiogram import Router
from aiogram.utils.deep_linking import decode_payload
from aiogram.filters import CommandStart, CommandObject
from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from sqlalchemy.ext.asyncio import AsyncSession

from states import RegistrationSG, MainSG
from services import get_user, create_user


registration_router = Router()

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format='%(filename)s:%(lineno)d #%(levelname)-8s '
           '[%(asctime)s] - %(name)s - %(message)s')


# Process START command
@registration_router.message(CommandStart(deep_link_encoded=True))
async def command_start_process(message: Message,
                                dialog_manager: DialogManager,
                                command: CommandObject):

    user_id = message.from_user.id
    logger.info(f'Start command pressed by {user_id}')
    session: AsyncSession = dialog_manager.middleware_data['session']
    
    # If user start bot by referral link
    if command.args:
        logger.info(f'CommandObject is {command}')
        args = command.args
        payload = decode_payload(args)
    else:
        payload = None
        
    # Try to get User from Database
    # If exist - skip Registration
    user = await get_user(session, user_id)
    logger.info(f'User from Database {user}')
    
    if user is not None:
        logger.info(f'User exists: {user}')
        await dialog_manager.start(MainSG.main)
        
    else:
        # Set Speech page = 0 of Registration process
        await dialog_manager.start(RegistrationSG.speech_a)


# Switching to next speech
async def registration(callback: CallbackQuery,
                       button: Button,
                       dialog_manager: DialogManager):

    speech = dialog_manager.current_context().dialog_data['speech']
    dialog_manager.current_context().dialog_data['speech'] = speech + 1
    logger.info(f'User {callback.from_user.id} pressed Registration. Page {speech + 1}')

    
    if speech == 5:
        session: AsyncSession = dialog_manager.middleware_data.get('session')
        user = await get_user(session, 
                              callback.from_user.id)
        
        # Is it new User? If yes - add to Database
        if user is None:
            await create_user(session, 
                              callback.from_user.id,
                              callback.from_user.first_name,
                              callback.from_user.last_name)
    
        await dialog_manager.start(MainSG.main)
    
    elif int(speech) % 2 == 0:
        await dialog_manager.switch_to(RegistrationSG.speech_a)
    else:
        await dialog_manager.switch_to(RegistrationSG.speech_b)
    

        
    
