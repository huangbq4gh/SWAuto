from ADBOperations import ADBOperations
from PIL import Image
import time


class ScreenVerification:

    def __init__(self):
        self.StartAdsCloseRGB = (153, 153, 153, 255)
        self.StartAdsPt = (115, 660)
        self.GiftWindowClosePt = (1005, 100)
        self.GiftWindowCloseRGB = (250, 242, 226, 255)
        self.DBRunVictoryPt = (405, 95)
        self.DBRunVictoryRGB = (255, 255, 51, 255)
        self.RuneSellPt = (410, 600)
        self.RuneSellRGB = (190, 132, 66, 255)
        self.RuneGetPt = (770, 570)
        self.RuneSixStarPt = (440, 240)
        self.RuneSixStarRGB = (244, 246, 245, 255)
        self.GetNonRunePt = (580, 580)
        self.DBReplayPt = (200, 400)
        self.CurrentScreenPath = '../screenshots/current.png'
        self.adbobj = ADBOperations()

    def check_rgb_by_point(self, image_path, point_tuple, expected_rgb_tuple):
        im = Image.open(image_path, 'r')
        print im.getpixel(point_tuple)
        return im.getpixel(point_tuple) == expected_rgb_tuple

    def close_all_startads(self):
        self.adbobj.get_current_screen('current.png', '../screenshots')
        while self.check_rgb_by_point(self.CurrentScreenPath, self.StartAdsPt, self.StartAdsCloseRGB):
            self.adbobj.input_tap('%d' % self.StartAdsPt[0], '%d' % self.StartAdsPt[1])
            self.adbobj.get_current_screen('current.png', '../screenshots')

    def close_gift_window(self):
        self.adbobj.get_current_screen('current.png', '../screenshots')
        while self.check_rgb_by_point(self.CurrentScreenPath, self.GiftWindowClosePt, self.GiftWindowCloseRGB):
            self.adbobj.input_tap('%d' % self.GiftWindowClosePt[0], '%d' % self.GiftWindowClosePt[1])
            self.adbobj.get_current_screen('current.png', '../screenshots')

    def handle_db_run_rewards(self):
        self.adbobj.get_current_screen('current.png', '../screenshots')
        # check if Victory
        if self.check_rgb_by_point(self.CurrentScreenPath, self.DBRunVictoryPt, self.DBRunVictoryRGB):
            # click to see the treasure box
            self.adbobj.input_tap('500', '500')
            # treasure box animation
            time.sleep(3)
            # open treasure box
            self.adbobj.input_tap('500', '500')
            # treasure box open animation
            time.sleep(3)
            # get current screen
            self.adbobj.get_current_screen('current.png', '../screenshots')
            if self.check_rgb_by_point(self.CurrentScreenPath, self.RuneSellPt, self.RuneSellRGB):
                # TO DO: add 6 star identification
                # if self.check_rgb_by_point(self.CurrentScreenPath, self.RuneSellPt, self.RuneSellRGB):
                print 'is rune'
                self.adbobj.input_tap('%d' % self.RuneGetPt[0], '%d' % self.RuneGetPt[1])
            else:
                print 'not rune'
                self.adbobj.input_tap('%d' % self.GetNonRunePt[0], '%d' % self.GetNonRunePt[1])

    def verify_on_home_screen(self):
        pass

