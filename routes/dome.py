from flask import Blueprint
from flask import jsonify, request

from devices.dome_device import DomeDevice

import ascom_reply

dome = Blueprint('dome', __name__)

device = DomeDevice()


def transaction_details(device_number, details):
    if 'ClientTransactionID' in details:
        device.client_transaction_id = int(details['ClientTransactionID'])
    if 'ClientID' in request.args:
        device.client_id = int(details['ClientID'])

# ---------------------

def return_value(value, error_number=0, error_message=""):
    return jsonify(
        {'Value': value, 'ClientTransactionID': device.client_id, 'ServerTransactionID': 0, 'ErrorNumber': error_number,
         'ErrorMessage': error_message})


def return_empty(error_number=0, error_message=""):
    return jsonify(
        {'ClientTransactionID': device.client_id, 'ServerTransactionID': 0, 'ErrorNumber': error_number,
         'ErrorMessage': error_message})


# --------------------------------------

@dome.route('<int:device_number>/connected', methods=['GET'])
def connected_get(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.connected)


@dome.route('<int:device_number>/connected', methods=['PUT'])
def connected_put(device_number):
    transaction_details(device_number, request.args)
    return return_empty()


@dome.route('<int:device_number>/interfaceversion', methods=['GET'])
def interface_version(device_number):
    transaction_details(device_number, request.args)
    return return_value(1)


@dome.route('<int:device_number>/description', methods=['GET'])
def description(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.description)


@dome.route('<int:device_number>/driverinfo', methods=['GET'])
def driver_info(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.driver_info)


@dome.route('<int:device_number>/driverversion', methods=['GET'])
def driver_version(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.driver_version)


@dome.route('<int:device_number>/name', methods=['GET'])
def name(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.name)


@dome.route('<int:device_number>/supportedactions', methods=['GET'])
def supported_actions(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.supported_actions)


# ---------------------------------------

@dome.route('<int:device_number>/canfindhome', methods=['GET'])
def canfindhome(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.can_find_home)


@dome.route('<int:device_number>/canpark', methods=['GET'])
def canpark(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.can_park)


@dome.route('<int:device_number>/cansetaltitude', methods=['GET'])
def cansetaltitude(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.can_set_altitude)


@dome.route('<int:device_number>/cansetazimuth', methods=['GET'])
def cansetazimuth(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.can_set_azimuth)


@dome.route('<int:device_number>/cansetpark', methods=['GET'])
def cansetpark(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.can_set_park)


@dome.route('<int:device_number>/cansetshutter', methods=['GET'])
def cansetshutter(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.can_set_shutter)


@dome.route('<int:device_number>/canslave', methods=['GET'])
def canslave(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.can_slave)


@dome.route('<int:device_number>/cansyncazimuth', methods=['GET'])
def cansyncazimuth(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.can_sync_azimuth)


@dome.route('<int:device_number>/shutterstatus', methods=['GET'])
def shutterstatus(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.shutter_status)


# --------------------------
@dome.route('<int:device_number>/slewing', methods=['GET'])
def slewing(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.slewing)


@dome.route('<int:device_number>/athome', methods=['GET'])
def athome(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.at_home)


@dome.route('<int:device_number>/atpark', methods=['GET'])
def atpark(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.at_park)


@dome.route('<int:device_number>/azimuth', methods=['GET'])
def azimuth(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.azimuth)


# -------------------------
@dome.route('<int:device_number>/openshutter', methods=['PUT'])
def openshutter(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.open_shutter())


@dome.route('<int:device_number>/closeshutter', methods=['PUT'])
def closeshutter(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.close_shutter())


@dome.route('<int:device_number>/park', methods=['PUT'])
def park(device_number):
    transaction_details(device_number, request.args)
    return return_value(device.park())
