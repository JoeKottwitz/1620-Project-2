class Television:
    '''
    Class representing data of TV settings
    such as the power, volume, and channel
    '''
    MIN_VOLUME = 0
    MAX_VOLUME = 3
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        '''
        Method to initialize television data values
        '''
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        '''
        Method to turn on/off the TV
        '''
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def check_power(self) -> bool:
        '''
        Function to check if the power is on or off
        '''
        return self.__status

    def mute(self) -> None:
        '''
        Method to mute/unmute the volume
        '''
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True

    def check_mute(self) -> bool:
        '''
        Function to check if mute is on or off
        '''
        return self.__muted

    def channel_up(self) -> None:
        '''
        Method to switch the channel up 1
        '''
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        '''
        Method to switch the channel down 1
        '''
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def check_channel(self) -> int:
        '''
        Method to check what the channel number is
        :return: Channel number
        '''
        return self.__channel

    def volume_up(self) -> None:
        '''
        Method to turn the volume up 1
        '''
        if self.__status and self.__muted == False:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        '''
        Method to turn the volume down 1
        '''
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def check_volume(self) -> int:
        '''
        Method to check what the volume level is
        :return: Volume level
        '''
        return self.__volume