from utils import Operation
import pytest


def operation_dict():
    return {
    "id": 667307132,
    "state": "EXECUTED",
    "date": "2019-07-13T18:51:29.313309",
    "operationAmount": {
      "amount": "97853.86",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на счет",
    "from": "Maestro 1308795367077170",
    "to": "Счет 96527012349577388612"
  }


def test_get_date():
    operation = Operation.Operation(operation_dict())
    assert operation.get_date() == "13.07.2019"


def test_get_encrypted_from():
    assert Operation.Operation.get_encrypted_from("Maestro 1308795367077170") == "Maestro 1308 79** **** 7170"
    assert Operation.Operation.get_encrypted_from("Счет 18889008294666828266") == "Счет **8266"


def test_get_message():
    operation = Operation.Operation(operation_dict())
    assert operation.get_message() == """13.07.2019 Перевод с карты на счет
Maestro 1308 79** **** 7170 -> Счет **8612
97853.86 руб.

"""
