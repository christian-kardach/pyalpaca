from flask import Blueprint
from flask import jsonify, request

from devices.cover_calibrator_device import CoverCalibratorDevice

cover_calibrator = Blueprint('covercalibrator', __name__)

device = CoverCalibratorDevice()


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
@cover_calibrator.route('<int:device_number>/connected', methods=['GET'])
def connected_get(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.connected)


@cover_calibrator.route('<int:device_number>/connected', methods=['PUT'])
def connected_put(device_number):
    transaction_details(device_number, request.args)
    return return_empty()


@cover_calibrator.route('<int:device_number>/interfaceversion', methods=['GET'])
def interface_version(device_number):
    transaction_details(device_number, request.args)
    return return_value(1)


@cover_calibrator.route('<int:device_number>/description', methods=['GET'])
def description(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.description)


@cover_calibrator.route('<int:device_number>/driverinfo', methods=['GET'])
def driver_info(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.driver_info)


@cover_calibrator.route('<int:device_number>/driverversion', methods=['GET'])
def driver_version(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.driver_version)


@cover_calibrator.route('<int:device_number>/name', methods=['GET'])
def name(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.name)


@cover_calibrator.route('<int:device_number>/supportedactions', methods=['GET'])
def supported_actions(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.supported_actions)


##########################################
# Device Specific Methods GET
##########################################

@cover_calibrator.route('<int:device_number>/brightness', methods=['GET'])
def brightness(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.brightness)


@cover_calibrator.route('<int:device_number>/calibratorstate', methods=['GET'])
def calibrator_state(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.calibrator_state)


@cover_calibrator.route('<int:device_number>/coverstate', methods=['GET'])
def cover_state(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.cover_state)


@cover_calibrator.route('<int:device_number>/maxbrightness', methods=['GET'])
def max_brightness(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.max_brightness)


##########################################
# Device Specific Methods PUT
##########################################
@cover_calibrator.route('<int:device_number>/calibratoron', methods=['PUT'])
def refresh(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.calibrator_on())


@cover_calibrator.route('<int:device_number>/calibratoroff', methods=['PUT'])
def calibrator_off(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.calibrator_off())


@cover_calibrator.route('<int:device_number>/closecover', methods=['PUT'])
def close_cover(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.close_cover())


@cover_calibrator.route('<int:device_number>/haltcover', methods=['PUT'])
def halt_cover(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.halt_cover())


@cover_calibrator.route('<int:device_number>/opencover', methods=['PUT'])
def open_cover(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.open_cover())
