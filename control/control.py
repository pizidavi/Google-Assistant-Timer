from lib.IFTTT import IFTTT
from threading import Timer


class Control:

    def __init__(self, deviceName, config):
        self.__ifttt = IFTTT(config['KEY'])

        self.__eventOn = deviceName + config['ON_suffix']
        self.__eventOff = deviceName + config['OFF_suffix']

    def off_to_on(self, seconds):
        self.__ifttt.execute(self.__eventOff)
        Timer(seconds, self.__ifttt.execute, args=[self.__eventOn]).start()

    def on_to_off(self, seconds):
        self.__ifttt.execute(self.__eventOn)
        Timer(seconds, self.__ifttt.execute, args=[self.__eventOff]).start()
