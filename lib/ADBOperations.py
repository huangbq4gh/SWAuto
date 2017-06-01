import subprocess


class ADBOperations:

    def __init__(self):
        self.device_name = 'FA71ABR04681'

    def input_text(self, input_text):
        print 'writing text to device'
        # subprocess.call('adb -s %s shell input text %s' % self.device_name, input_text)
        subprocess.call(["adb", "-s", self.device_name, "shell", "input", "text", input_text])

    def input_tap(self, input_x, input_y):
        print 'sending tap event to device'
        # subprocess.call('adb -s %s shell input tap %d %d' % self.device_name, input_x, input_y)
        subprocess.call(["adb", "-s", self.device_name, "shell", "input", "tap", input_x, input_y])

    def get_current_screen(self, save_file_name, save_location):
        print 'taking screenshot'
        # subprocess.call('adb -s %s shell screencap -p /sdcard/%s' % (self.device_name, save_file_name))
        subprocess.call(["adb", "-s", self.device_name, "shell", "screencap", "-p", "/sdcard/swauto/" + save_file_name])
        print 'getting device screenshot and save at given location'
        # subprocess.call('adb -s %s pull /sdcard/%s %s' % (self.device_name, save_file_name, save_location))
        subprocess.call(["adb", "-s", self.device_name, "pull", "/sdcard/swauto/" + save_file_name, save_location])

    def get_process(self, process_name):
        print 'get process info'
        pass
