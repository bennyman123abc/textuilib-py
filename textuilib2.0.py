import os

header = []
debug = [False]

class menu:
    def __init__(self, name, menuItems):
        self.menuItems = []
        
        if isinstance(name, str):
            self.name = name
            
        if isinstance(menuItems, list):
            for m in menuItems:
                if isinstance(m, menuItem):
                    self.menuItems.append(m)
                    
    def getName(self):
        return self.name
    
    def getOptions(self):
        
