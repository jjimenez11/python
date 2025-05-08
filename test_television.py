import pytest
from television import *

class TestTelevision:
    def test_init(self):
        self.tv = Television()
        self.__init__()
        self.tv.power()
        assert self.tv.__str__() == f'power = True, channel = 0, volume = 0.'

    def test_power(self):
        self.tv = Television()
        self.__init__()
        self.tv.power()
        assert self.tv.__str__() == f'power = False, channel = 0, volume = 0.'
        self.tv.power()
        assert self.tv.__str__() == f'power = True, channel = 0, volume = 0.'

    def test_mute(self):
        self.tv = Television()
        self.tv2 = Television()
        self.tv3 = Television()
        self.tv4 = Television()
        self.__init__()

        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()
        assert self.tv.__str__() == f'power = True, channel = 0, volume = 0.'

        self.tv2.power()
        self.tv2.mute()
        self.tv2.mute()
        assert self.tv2.__str__() == f'power = True, channel = 0, volume = 0.'

        self.tv3.mute()
        assert self.tv3.__str__() == f'power = False, channel = 0, volume = 0.'

        self.tv4.power()
        self.tv4.mute()
        self.tv4.mute()
        assert self.tv4.__str__() == f'power = True, channel = 0, volume = 0.'

    def test_channel_up(self):
        self.tv = Television()
        self.__init__()
        self.tv.channel_up()
        assert self.tv.__str__() == f'power = False, channel = 0, volume = 0.'

        self.tv.power()
        self.tv.channel_up()
        assert self.tv.__str__() == f'power = True, channel = 1, volume = 0.'

        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_up()
        assert self.tv.__str__() == f'power = True, channel = 0, volume = 0.'

    def test_channel_down(self):
        self.tv = Television()
        self.__init__()
        self.tv.channel_down()
        assert self.tv.__str__() == f'power = False, channel = 0, volume = 0.'

        self.tv.power()
        self.tv.channel_down()
        assert self.tv.__str__() == f'power = True, channel = 3, volume = 0.'

    def test_volume_up(self):
        self.tv = Television()
        self.__init__()
        self.tv.volume_up()
        assert self.tv.__str__() == f'power = False, channel = 0, volume = 0.'

        self.tv.power()
        self.tv.volume_up()
        assert self.tv.__str__() == f'power = True, channel = 0, volume = 1.'

        self.tv.power()
        self.tv.volume_up()
        assert self.tv.__str__() == f'power = True, channel = 0, Volume = 2.'

        self.tv.volume_up()
        assert self.tv.__str__() == f'power = True, channel = 0, volume = 2.'

    def test_volume_down(self):
        self.tv = Television()
        self.__init__()
        self.tv.volume_down()
        assert self.tv.__str__() == f'power = False, channel = 0, volume = 0.'

        self.tv.power()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_down()
        assert self.tv.__str__() == f'power = True, channel = 0, volume = 1.'

        self.tv.mute()
        self.tv.volume_down()
        assert self.tv.__str__() == f'power = True, channel = 0, volume = 0.'

        self.tv.volume_down()
        assert self.tv.__str__() == f'power = True, channel = 0, volume = 0.'
