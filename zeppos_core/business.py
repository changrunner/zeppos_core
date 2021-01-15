from datetime import datetime
from zeppos_logging.app_logger import AppLogger


class Business:
    @staticmethod
    def are_we_during_business_hours(business_open, business_closed):
        business_open = float(business_open)
        business_closed = float(business_closed)
        current_hour = float(
            datetime.now().hour + (datetime.now().minute * 0.01))
        if current_hour < business_open or \
                current_hour > business_closed:
            AppLogger.logger.info(f'\nNot checking if things are up, because we are outside business hours. \n' \
                                  f'[{business_open} - ' \
                                  f'{business_closed}] ' \
                                  f'Current hour [{current_hour}] \n' \
                                  f'Let\'s have some sleep. Will ya!')
            return False
        return True
