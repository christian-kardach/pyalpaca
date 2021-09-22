from flask import Blueprint
from flask import jsonify, request

from devices.observing_conditions_device import ObservingConditionsDevice

observing_conditions = Blueprint('observingconditions', __name__)

device = ObservingConditionsDevice()


def transaction_details(device_number, details):
    if 'ClientTransactionID' in details:
        device.client_transaction_id = int(details['ClientTransactionID'])
    if 'ClientID' in request.args:
        device.client_id = int(details['ClientID'])


# ----------------------
def action(value, error_number=0, error_message=""):
    return jsonify(
        {'Action': value, 'ClientTransactionID': device.client_id, 'ServerTransactionID': 0,
         'ErrorNumber': error_number,
         'ErrorMessage': error_message})


def command_blind(error_number=0, error_message=""):
    return jsonify(
        {'ClientTransactionID': device.client_id, 'ServerTransactionID': 0, 'ErrorNumber': error_number,
         'ErrorMessage': error_message})


def command_bool(value, error_number=0, error_message=""):
    return jsonify(
        {'Value': value, 'ClientTransactionID': device.client_id, 'ServerTransactionID': 0, 'ErrorNumber': error_number,
         'ErrorMessage': error_message})


def command_string(value, error_number=0, error_message=""):
    return jsonify(
        {'Value': value, 'ClientTransactionID': device.client_id, 'ServerTransactionID': 0, 'ErrorNumber': error_number,
         'ErrorMessage': error_message})


# ---------------------

def return_value(value, error_number=0, error_message=""):
    return jsonify(
        {'Value': value, 'ClientTransactionID': device.client_id, 'ServerTransactionID': 0, 'ErrorNumber': error_number,
         'ErrorMessage': error_message})


def return_empty(error_number=0, error_message=""):
    return jsonify(
        {'ClientTransactionID': device.client_id, 'ServerTransactionID': 0, 'ErrorNumber': error_number,
         'ErrorMessage': error_message})


##########################################
# Common Methods
##########################################
@observing_conditions.route('<int:device_number>/connected', methods=['GET'])
def connected_get(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.connected)


@observing_conditions.route('<int:device_number>/connected', methods=['PUT'])
def connected_put(device_number):
    transaction_details(device_number, request.args)
    return return_empty()


@observing_conditions.route('<int:device_number>/interfaceversion', methods=['GET'])
def interface_version(device_number):
    transaction_details(device_number, request.args)
    return return_value(1)


@observing_conditions.route('<int:device_number>/description', methods=['GET'])
def description(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.description)


@observing_conditions.route('<int:device_number>/driverinfo', methods=['GET'])
def driver_info(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.driver_info)


@observing_conditions.route('<int:device_number>/driverversion', methods=['GET'])
def driver_version(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.driver_version)


@observing_conditions.route('<int:device_number>/name', methods=['GET'])
def name(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.name)


@observing_conditions.route('<int:device_number>/supportedactions', methods=['GET'])
def supported_actions(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.supported_actions)


##########################################
# Device Specific Methods GET
##########################################

@observing_conditions.route('<int:device_number>/averageperiod', methods=['GET'])
def averageperiod(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.average_period)


@observing_conditions.route('<int:device_number>/couldcover', methods=['GET'])
def couldcover(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.cloud_cover)


@observing_conditions.route('<int:device_number>/dewpoint', methods=['GET'])
def dewpoint(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.dew_point)


@observing_conditions.route('<int:device_number>/humidity', methods=['GET'])
def humidity(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.humidity)


@observing_conditions.route('<int:device_number>/pressure', methods=['GET'])
def pressure(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.pressure)


@observing_conditions.route('<int:device_number>/rainrate', methods=['GET'])
def rainrate(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.rain_rate)


@observing_conditions.route('<int:device_number>/skybrightness', methods=['GET'])
def skybrightness(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.sky_brightness)


@observing_conditions.route('<int:device_number>/skyquality', methods=['GET'])
def skyquality(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.sky_quality)


@observing_conditions.route('<int:device_number>/skytemperature', methods=['GET'])
def skytemperature(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.sky_temperature)


@observing_conditions.route('<int:device_number>/starfwhm', methods=['GET'])
def starfwhm(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.star_fwhm)


@observing_conditions.route('<int:device_number>/temperature', methods=['GET'])
def temperature(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.temperature)


@observing_conditions.route('<int:device_number>/winddirection', methods=['GET'])
def winddirection(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.wind_direction)


@observing_conditions.route('<int:device_number>/windgust', methods=['GET'])
def windgust(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.wind_gust)


@observing_conditions.route('<int:device_number>/windspeed', methods=['GET'])
def windspeed(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.wind_speed)


##########################################
# Device Specific Methods PUT
##########################################
@observing_conditions.route('<int:device_number>/refresh', methods=['PUT'])
def refresh(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.refresh())

@observing_conditions.route('<int:device_number>/averageperiod', methods=['PUT'])
def averageperiod_put(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.average_period)
