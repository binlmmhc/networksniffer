#!/usr/bin/env python3

"""
    get system basic information
"""

class SysInfo():
    """
        this module will get basic system information,
        check the system whether it is 'Unix like'
    """
    
    def __init__(self):
        try:
            import platform as plf
        except ImportError:
            pass
        self.testtime = plf.python_build()[1]
        self.machinename = plf.node()
        self.machinearch = plf.machine()
        self.machinesystem = plf.system()
        self.machineprocessor = plf.processor()
        self.systemcheck = self.check()
    
    def display(self):
        """
            display basic system information
        """
        print("Test "+self.testtime)
        print("Machine Name:"+self.machinename)
        print("Machine arch:"+self.machinearch)
        print("Machine system:"+self.machinesystem)
        print("Machine Processer:"+self.machineprocessor)
        if self.systemcheck:
            print("It is an unix-like system")
    
    def check(self):
        """
            check the system whether it is unix like
        """
        if self.machinesystem in ('Linux', 'Unix', ):
            return True
        else:
            return False

def test():
    show = SysInfo()
    show.display()

if __name__ == '__main__':
    test()