from ADBOperations import ADBOperations
from PIL import Image


class ScreenVerification:

    def __init__(self):
        self.StartAdsCloseRGB = (153, 153, 153)
        self.StartAdsPt = (115, 660)
        self.adbobj = ADBOperations()

    def check_rgb_by_point(self, image_path, point_tuple, expected_rgb_tuple):
        im = Image.open(image_path, 'r')
        return im.getpixel(point_tuple) == expected_rgb_tuple

    def close_all_startads(self):
        self.adbobj.get_current_screen('current.png', 'screenshots')
        while self.check_rgb_by_point('../screenshots/current.png', (115, 660), (153, 153, 153)):
            self.adbobj.input_tap(self.StartAdsPt[0], self.StartAdsPt[1])
            self.adbobj.get_current_screen('current.png', '../screenshots')
        return True

    def verify_on_home_screen(self):
        pass

