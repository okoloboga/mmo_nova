import logging

from aiogram_dialog import DialogManager
from aiogram_dialog.api.exceptions import NoContextError
from aiogram.types import User
from fluentogram import TranslatorRunner

from sqlalchemy.ext.asyncio import AsyncSession

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format='%(filename)s:%(lineno)d #%(levelname)-8s '
           '[%(asctime)s] - %(name)s - %(message)s')


# Main Registration Getter
async def registration_getter(dialog_manager: DialogManager,
                              session: AsyncSession,
                              i18n: TranslatorRunner,
                              event_from_user: User,
                              **kwargs) -> dict:
    # Check for 0 speech - every turn
    try:
        speech = dialog_manager.current_context().dialog_data['speech']
    except (NoContextError, KeyError):
        speech = 0
        dialog_manager.current_context().dialog_data['speech'] = speech
    
    
    logger.info(f'User {event_from_user.id} go to speech {speech}')
    
    speech_map = {'0': i18n.registration.speech0(),
                  '1': i18n.registration.speech1(),
                  '2': i18n.registration.speech2(),
                  '3': i18n.registration.speech3(),
                  '4': i18n.registration.speech4(),
                  '5': i18n.registration.speech5()
                  }

    buttons_map = {'0': i18n.button.begin(),
                   '1': i18n.button.understand(),
                   '2': i18n.button.next(),
                   '3': i18n.button.ok(),
                   '4': i18n.button.good(),
                   '5': i18n.button.ok()
                   }

    return {'start_speech': speech_map[str(speech)],
            'button_next': buttons_map[str(speech)]}

    
