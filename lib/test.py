from ScreenVerification import ScreenVerification
from ADBOperations import *

adbobj = ADBOperations()
sv = ScreenVerification()

# sv.close_all_startads()
# sv.check_rgb_by_point('../screenshots/ref/SixStarRune.png', (440, 240), (0, 0, 0, 0))
# sv.check_rgb_by_point('../screenshots/current.png', (405, 95), (0, 0, 0, 0))
# sv.handle_db_run_rewards()

adbobj.get_current_screen('current.png', '../screenshots')