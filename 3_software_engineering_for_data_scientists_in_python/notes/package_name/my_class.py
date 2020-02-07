# Camel-case, never underscore
class MyClass:
    """A minimal class example
    
    :param value: value to set as the ''attribute'' attribute
    :ivar value: contains the contents of the ''value'' passed in init
    """
    
    # Method to create a new instance of MyClass
    def __init__(self, value):
        # Define aatribute with the contents of the value param
        self.attribute = value