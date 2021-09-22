from ascom.enumerations import ShutterState


class DomeDevice:
    def __init__(self):
        self.__connected = False
        self.__client_transaction_id = 0
        self.__client_id = 0

        self.__description = "Dome Alpaca Device"
        self.__driver_info = ""
        self.__driver_version = 1.0
        self.__name = "TNC Dome"
        self.__supported_actions = list()

        self.__can_find_home = True
        self.__can_park = True
        self.__can_set_altitude = False
        self.__can_set_azimuth = False
        self.__can_set_park = False
        self.__can_set_shutter = False
        self.__can_slave = False
        self.__can_sync_azimuth = False

        self.__shutter_status = ShutterState.shutterClosed
        self.__slewing = False
        self.__at_home = False
        self.__at_park = False
        self.__azimuth = 0

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
    def can_find_home(self):
        return self.__can_find_home

    @property
    def can_park(self):
        return self.__can_park

    @property
    def can_set_altitude(self):
        return self.__can_set_altitude

    @property
    def can_set_azimuth(self):
        return self.__can_set_azimuth

    @property
    def can_set_park(self):
        return self.__can_set_park

    @property
    def can_set_shutter(self):
        return self.__can_set_shutter

    @property
    def can_slave(self):
        return self.__can_slave

    @property
    def can_sync_azimuth(self):
        return self.__can_sync_azimuth

    @property
    def shutter_status(self):
        return self.__shutter_status

    @property
    def slewing(self, *args, **kwargs):
        return self.__slewing

    @property
    def at_home(self):
        return self.__at_home

    @property
    def at_park(self):
        return self.__at_park

    @property
    def azimuth(self):
        return self.__azimuth

    # ----------------------------------------------

    def close_shutter(self):
        raise NotImplementedError
        # self.__shutter_status = ShutterState.shutterClosed
        # DeviceDriver.logger.info("Shutter is now closed")

    def open_shutter(self):
        raise NotImplementedError
        # self.__shutter_status = ShutterState.shutterOpen
        # DeviceDriver.logger.info("Shutter is now open")

    def park(self):
        raise NotImplementedError
        # self.__shutter_status = ShutterState.shutterOpen
        # DeviceDriver.logger.info("Dome is parking")
