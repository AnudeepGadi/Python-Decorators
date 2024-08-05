from functools import wraps

# Decorator to log function execution
def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executing function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} executed successfully.")
        return result
    return wrapper

# Decorator to validate input data
def validate_data(func):
    @wraps(func)
    def wrapper(data, *args, **kwargs):
        if not isinstance(data, dict):
            raise ValueError("Data must be a dictionary")
        if 'value' not in data:
            raise ValueError("Data must contain a 'value' key")
        return func(data, *args, **kwargs)
    return wrapper

# Decorator to transform input data
def transform_data(func):
    @wraps(func)
    def wrapper(data, *args, **kwargs):
        # Example transformation: convert 'value' to uppercase
        data['value'] = data['value'].upper()
        return func(data, *args, **kwargs)
    return wrapper

@log_execution
@validate_data
@transform_data
def process_data(data):
    # Process the data (just return it in this example)
    return f"Processed data: {data['value']}"

# log_execution(validate_data(transform_data(process_data)))(data)

# Testing the chained decorators
try:
    #print(process_data({'value': 'hello world'}))  # Should execute and process the data
    print(process_data({'not_value': 'hello world'}))  # Should raise a validation error
    #print(process_data('invalid_data'))  # Should raise a validation error
except ValueError as e:
    print(f"Error: {e}")
