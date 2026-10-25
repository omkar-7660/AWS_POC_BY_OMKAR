"""AWS Lambda handler for basic arithmetic operations."""

from helper.functions import add, divide, multiply, subtract


def lambda_handler(event, context):
	"""Perform the operation named in the event.

	Example event: {"operation": "add", "a": 10, "b": 5}
	"""
	operations = {
		"add": add,
		"subtract": subtract,
		"divide": divide,
		"multiply": multiply,
	}

	operation = event.get("operation")
	if operation not in operations:
		return {"error": "operation must be add, subtract, divide, or multiply"}

	try:
		a = event["a"]
		b = event["b"]
	except KeyError:
		return {"error": "event must include 'a' and 'b'"}

	try:
		result = operations[operation](a, b)
	except ZeroDivisionError:
		return {"error": "cannot divide by zero"}

	return {"operation": operation, "result": result}
