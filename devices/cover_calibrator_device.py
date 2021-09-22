class CoverCalibratorDevice:
    def __init__(self):
        self.__connected = False
        self.__client_transaction_id = 0
        self.__client_id = 0

        self.__description = "Observing Conditions Alpaca Device"
        self.__driver_info = ""
        self.__driver_version = 1.0
        self.__name = "Cover Calibrator Device"
        self.__supported_actions = list()

        self.__brightness = 0
        self.__calibrator_state = 0
        self.__cover_state = 0
        self.__max_brightness = 0

    ##########################################
    # Common Properties
    ##########################################
    @property
    def connected(self):
        return self.__connected

    @connected.setter
    def connected(self, value):
        self.__connected = value

    @property
    def client_transaction_id(self):
        return self.__client_transaction_id

    @client_transaction_id.setter
    def client_transaction_id(self, value):
        self.__client_transaction_id = value

    @property
    def client_id(self):
        return self.__client_id

    @client_id.setter
    def client_id(self, value):
        self.__client_id = value

    @property
    def description(self):
        return self.__description

    @property
    def driver_info(self):
        return self.__driver_info

    @property
    def driver_version(self):
        return self.__driver_version

    @property
    def name(self):
        return self.__name

    @property
    def supported_actions(self):
        return self.__supported_actions

    ##########################################
    # Device Specific Properties
    ##########################################
    @property
    def brightness(self):
        return self.__brightness

    @property
    def calibrator_state(self):
        return self.__calibrator_state

    @property
    def cover_state(self):
        return self.__cover_state

    @property
    def max_brightness(self):
        return self.__max_brightness

    def calibrator_on(self):
        pass

    def calibrator_off(self):
        pass

    def close_cover(self):
        pass

    def halt_cover(self):
        pass

    def open_cover(self):
        pass
