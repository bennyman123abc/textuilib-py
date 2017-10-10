import os

header = ["textuilib"]
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
        return self.menuItems
    
    def displayOptions(self):
        i = 1
        for o in self.menuItems:
            if isinstance(o, menuItem):
                print(str(i) + ". " + o.text)
                i += 1
    
    def displayName(self):
        print self.name
        
    def displayMenu(self):
        clear()
        displayHeader(self)
        self.displayOptions()
        if self.menuItems != []:
            return choice(self)
        
    def addMenuItem(self, item):
        if isinstance(item, menuItem):
            self.menuItems.append(item)
            
    def removeMenuItem(self, item):
        if isinstance(item, menuItem):
            for o in self.menuItems:
                if item == o:
                    self.menuItems.remove(o)
        
    def clearMenuItems(self):
        for o in self.menuItems:
            self.menuItems.remove(o)
            
class menuItem:
    def __init__(self, text, function):
        if isinstance(text, str) and isinstance(function, str):
            self.text = text
            self.function = function
            
class TypeMismatch(Exception):
    def __init__(self, mismatch):
        Exception.__init__(self, mismatch)
        
def setHeader(h):
    try:
        header.remove(header[0])
        if h[len(h)] != " ":
            h = h + " "
            header.append(h)
        else:
            header.append(h)
    except:
        if h[len(h) - 1] != " ":
            h = h + " "
            header.append(h)
        else:
            header.append(h)

def displayHeader(menu):
    print header[0] + '- ' + menu.getName()
    print ''

def clear():
    if os.name == 'nt':
        clr = 'cls'
    else:
        clr = 'clear'
    os.system(clr)

def choice(menu):
    print ''
    print 'Choose an Option:'
    try:
        option = input('Option: ')
        i = 0
        for o in menu.menuItems:
            if i == option - 1:
                return o.function
            i += 1

    except (KeyboardInterrupt, SystemExit):
        raise

    except:
        return
