#!/usr/bin/env python3
""" A play at multiple inheritance """

class Top(object):
    """ Stubbed class inherits directly from built-in object class.
    
    Allows user to build a cooperative multiple inheritance hierachy that 
    allows the various class constructors to accept varied arguments. All 
    other classes will in the hierachy will be derived directly or indirectly.
    """

    def __init__(self, **kwargs):
        """ Init """
        pass    # Terminate the constructor call chain


class A(Top):
    def __init__(self, **kwargs):
        print('Making an A object')
        super().__init__(**kwargs)
        self.value_A = 0

class B(Top):
    def __init__(self, **kwargs):
        print('Making a B object')
        self.value_B = kwargs['val']
        kwargs.pop('val')   # Remove the parameter from the kwargs
        super().__init__(**kwargs)

class C(A, B):
    def __init__(self, **kwargs):
        print('Making a C object')
        super().__init__(**kwargs)
        self.value_C = 2 
    
if __name__ == '__main__':
    c_obj = C(val=5) # Supply keyword arg here
    print('-------------------')
    print(c_obj.__dict__)