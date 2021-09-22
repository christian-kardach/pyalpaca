from flask import jsonify


def action(value, client_id, error_number=0, error_message=""):
    return jsonify(
        {'Action': value, 'ClientTransactionID': client_id, 'ServerTransactionID': 0,
         'ErrorNumber': error_number,
         'ErrorMessage': error_message})


def command_blind(client_id, error_number=0, error_message=""):
    return jsonify(
        {'ClientTransactionID': client_id, 'ServerTransactionID': 0, 'ErrorNumber': error_number,
         'ErrorMessage': error_message})


def command_bool(value, client_id, error_number=0, error_message=""):
    return jsonify(
        {'Value': value, 'ClientTransactionID': client_id, 'ServerTransactionID': 0, 'ErrorNumber': error_number,
         'ErrorMessage': error_message})


def command_string(value, client_id, error_number=0, error_message=""):
    return jsonify(
        {'Value': value, 'ClientTransactionID': client_id, 'ServerTransactionID': 0, 'ErrorNumber': error_number,
         'ErrorMessage': error_message})
