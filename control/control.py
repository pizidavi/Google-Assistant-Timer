from lib.IFTTT import IFTTT
from threading import Timer


class Control:

    def __init__(self, deviceName, config):
        self.__ifttt = IFTTT(config['KEY'])

        self.__eventOn = deviceName + config['ON_suffix']
        self.__eventOff = deviceName + config['OFF_suffix']

    def on_for(self, durationInMinutes):
        self.__ifttt.execute(self.__eventOn)
        Timer(durationInMinutes, self.__ifttt.execute, args=[self.__eventOff]).start()

    def on_after(self, durationInMinutes):
        Timer(durationInMinutes, self.__ifttt.execute, args=[self.__eventOn]).start()

    def off_for(self, durationInMinutes):
        self.__ifttt.execute(self.__eventOff)
        Timer(durationInMinutes, self.__ifttt.execute, args=[self.__eventOn]).start()

    def off_after(self, durationInMinutes):
        Timer(durationInMinutes, self.__ifttt.execute, args=[self.__eventOff]).start()
