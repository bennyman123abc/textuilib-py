import os

globalOptions = []
header = []

# Main class to declare a menu. This is what will be used the most.
# (Unless someone REALLY likes menuItems...)
class menu:
    def __init__(self, name, menuItems):
        # A blank list so we can append all of our valid menuItem objects
        self.menuItems = []

        # The name needs to be a string. 
        # Maybe we'll accept integers in the future but, it's very doubtful
        if instanceof(name, str):
            self.name = name
        
        # Here is the fun part
        # We need to first make sure that menuItems (Called in the beginning of the function) is a list
        # After we know it's a list, we need to append each item that's a menuItem to the menu's menuItems
        if instanceof(menuItems, list):
            for m in menuItems:
                if instanceof(m, menuItem):
                    self.menuItems.append(m)

    # We simply return the value of 'name' for the menu object
    def getName(self):
        return self.name

    # This time, I will do things simpler than they were previously.
    # All this will do is return self.menuItems which is an array of all of the options
    def getOptions(self):
        return self.menuItems

    # This is just a copy and paste from the last version of the lib.
    # Don't fix what ain't broken, right?
    def displayOptions(self):
        i = 1
        for o in self.getOptions():
            print str(i) + '. ' + o.text
            i += 1


# This is what determines what items are in the menu and what function call to return
class menuItem:
    def __init__(self, name, function):
        # We will just use standard str checks for the name and function
        if instanceof(name, str):
            self.name = name
        
        if instanceof(function, str):
            self.function = function