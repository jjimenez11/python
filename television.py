class Television:
    min_volume = 0
    max_volume = 2
    min_channel1 = 0
    max_channel1 = 3

    def __init__(self) -> None:
        """"__init__ just defines that the variables status muted is False
        and that the channel variable should be in their minimum value of 0
        """
        self.__status = False
        self.__muted = False
        self.__volume = self.min_volume
        self.__channel1 = self.min_channel1

    def power(self) -> None:
        """the function is used to turn on or off the television"""
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        """the function is used to mute or unmute the television"""
        if self.__status and not self.__muted:
            self.__muted = True
            self.__volume = self.min_volume
        elif self.__status and self.__muted:
            self.__muted = False


    def channel_up(self) -> None:
        """the function is used to increase the channel number by 1"""
        if self.__status:
            if self.__channel1 == self.max_channel1:
                self.__channel1 = self.min_channel1
            else:
                self.__channel1 = self.__channel1 + 1

    def channel_down(self) -> None:
        """the function is used to decrease the channel number by 1"""
        if self.__status:
            if self.__channel1 == self.max_channel1:
                self.__channel1 = self.min_channel1
            else:
                self.__channel1 = self.__channel1 - 1

    def volume_up(self) -> None:
        """the function is used to increase the volume by 1 if it is not already at its maximum"""
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.max_volume
            if self.__volume != self.max_volume:
                self.__volume = self.__volume + 1

    def volume_down(self) -> None:
        """the function is used to decrease the volume by 1 if it is not already at its minimum"""
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.max_volume
            if self.__volume != self.min_volume:
                self.__volume = self.__volume - 1

    def __str__(self) -> str:
        """this function returns a string with the current status,
         channel and volume of the television"""
        return f'power = {self.__status}, channel = {self.__channel1}, volume = {self.__volume}.'
