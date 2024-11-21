def singleton(cls):
    instances = {}  

    def get_instance(*args, **kwargs):
        if cls not in instances:
            # Create a new instance and store it
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class SingletonClass:
    def __init__(self, data):
        self.data = data

    def display(self):
        print(f"Singleton instance with data: {self.data}")


# Creating instances of SingletonClass using the decorator
instance1 = SingletonClass("Instance 1")
instance2 = SingletonClass("Instance 2")

# Both instances will refer to the same instance
instance1.display()
instance2.display()