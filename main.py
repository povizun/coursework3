from utils.functions import get_list_of_ops, get_list_of_last_ops
from utils.Operation import Operation
import config

operations = get_list_of_ops(config.ROOT_DIR + "/operations.json")
final_message = ""
if operations != "Файл не найден":
    num_of_last = 5
    last_operations = get_list_of_last_ops(operations, num_of_last)
    for i in range(num_of_last):
        operation = Operation(last_operations[i])
        final_message += operation.get_message()
else:
    final_message = operations
print(final_message)
