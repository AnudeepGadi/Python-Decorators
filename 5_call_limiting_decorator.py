from functools import wraps

def limit_calls(max_calls: int):
    def decorator(func):
        call_count = 0
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal call_count
            if call_count >= max_calls:
                return "Call limit exceeded"
            call_count += 1
            return func(*args, **kwargs)
        
        return wrapper
    return decorator

@limit_calls(max_calls=3)
def fetch_data(query):
    return f"Fetching data for query: {query}"

# Testing the call limit decorator
print(fetch_data("select * from users"))  # Should execute
print(fetch_data("select * from orders"))  # Should execute
print(fetch_data("select * from products")) # Should execute
print(fetch_data("select * from sales"))    # Should print: Call limit exceeded
