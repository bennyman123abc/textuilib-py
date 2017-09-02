#!/usr/bin/python2.7

names = []
globalOptions = []

class menu:
    def __init__(self, name, options):
        self.name = name
        self.options = options

        names.append([self, name])
        for o in options:
            optionsArray = []
            optionsArray.append([self, o])
            globalOptions.append(optionsArray)

    def getName(self):
        for n in names:
            if n[0] == self:
                return n[1]

    def getOptions(self):
        optionsArray = []
        i = 0
        for o in globalOptions:
            if o[0][0] == self:
                optionsArray.append(o[0][1])
        return optionsArray

    def displayOptions(self):
        i = 1
        for o in self.getOptions():
            print(str(i) + ". " + o)
            i += 1
    
    def displayName(self):
        print self.getName()
        
# DEBUG          
menu1 = menu("Test Menu", ["Test 1", "Test 2", "Test 3"])
menu1.displayName()
print("")
menu1.displayOptions()
