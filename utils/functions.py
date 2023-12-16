import json


def get_list_of_ops(input_file: str):
    try:
        with open(input_file) as file:
            operations = json.load(file)
        return operations
    except FileNotFoundError:
        return "Файл не найден"


def get_list_of_last_ops(list_of_ops: list, num_of_last: int):
    list_of_dates: list = []

    for operation in list_of_ops:
        try:
            if operation["state"] == "EXECUTED":
                list_of_dates.append(operation["date"])
        except KeyError:
            pass
    list_of_dates.sort()
    if len(list_of_dates) < num_of_last:
        num_of_last = len(list_of_dates)
    last_ops = [None] * num_of_last
    list_of_last_dates = list_of_dates[:-num_of_last-1:-1]
    for operation in list_of_ops:
        if "date" in operation and operation["date"] in list_of_last_dates:
            i = list_of_last_dates.index(operation["date"])
            last_ops[i] = operation
    return last_ops
