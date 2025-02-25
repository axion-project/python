import threading
import functools
import time

# Metaclass to dynamically modify the class behavior
class MetaHelloWorld(type):
    def __new__(cls, name, bases, dct):
        original_init = dct.get('__init__', None)

        def new_init(self, *args, **kwargs):
            print("MetaClass Initializer: Hello from Meta!")
            if original_init:
                original_init(self, *args, **kwargs)

        dct['__init__'] = new_init
        return super().__new__(cls, name, bases, dct)

# Decorator to modify the greeting message
def greeting_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorator: Preparing to greet.")
        result = func(*args, **kwargs)
        print("Decorator: Greeting complete.")
        return result
    return wrapper

# Generator function that yields pieces of the message
def hello_world_generator():
    yield "Hello"
    time.sleep(1)  # simulate time delay for complexity
    yield ","
    time.sleep(1)
    yield " World!"
    time.sleep(1)
    yield "\n"

# Threaded function to print the message asynchronously
def threaded_print(generator):
    for part in generator:
        print(part, end='', flush=True)
        time.sleep(0.5)

# Base class to start the process
class HelloWorld(metaclass=MetaHelloWorld):
    def __init__(self):
        self.message_parts = hello_world_generator()

    @greeting_decorator
    def start(self):
        print("Starting Hello World Process...\n")
        threading.Thread(target=threaded_print, args=(self.message_parts,)).start()

# Instantiate and run the class
if __name__ == "__main__":
    hello_world_instance = HelloWorld()
    hello_world_instance.start()