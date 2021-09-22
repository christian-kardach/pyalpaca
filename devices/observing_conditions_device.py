
class ObservingConditionsDevice:
    def __init__(self):
        self.__connected = False
        self.__client_transaction_id = 0
        self.__client_id = 0

        self.__description = "Observing Conditions Alpaca Device"
        self.__driver_info = ""
        self.__driver_version = 1.0
        self.__name = "Observing Conditions"
        self.__supported_actions = list()

        self.__average_period = 5.0
        self.__cloud_cover = 0.0
        self.__dew_point = 0.0
        self.__humidity = 0.0
        self.__pressure = 0.0
        self.__rain_rate = 0.0
        self.__sky_brightness = 0.0
        self.__sky_quality = 0.0
        self.__sky_temperature = 0.0
        self.__star_fwhm = 0.0
        self.__temperature = 0.0
        self.__wind_direction = 0.0
        self.__wind_gust = 0.0
        self.__wind_speed = 0.0

        self.__sensor_description = ""
        self.__time_since_last_update = 0.0

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
    def average_period(self):
        return self.__average_period

    @property
    def cloud_cover(self):
        return self.__cloud_cover

    @property
    def dew_point(self):
        return self.__dew_point

    @property
    def humidity(self):
        return self.__humidity

    @property
    def pressure(self):
        return self.__pressure

    @property
    def rain_rate(self):
        return self.__rain_rate

    @property
    def sky_brightness(self):
        return self.__sky_brightness

    @property
    def sky_quality(self):
        return self.__sky_quality

    @property
    def sky_temperature(self):
        return self.__sky_temperature

    @property
    def star_fwhm(self):
        return self.__star_fwhm

    @property
    def temperature(self):
        return self.__temperature

    @property
    def wind_direction(self):
        return self.__wind_direction

    @property
    def wind_gust(self):
        return self.__wind_gust

    @property
    def wind_speed(self):
        return self.__wind_speed

    def refresh(self):
        raise NotImplementedError
