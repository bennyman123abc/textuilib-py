import os
names = []
globalOptions = []
header = 'Plaintext Database '

class menu:

    def __init__(self, name, options):
        self.name = name
        self.options = options
        names.append([self, name])
        for o in options:
            optionsArray = []
            optionsArray.append([self, menuItem(o[0], o[1])])
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
            print str(i) + '. ' + o.text
            i += 1

    def displayName(self):
        print self.getName()

    def displayMenu(self):
        clear()
        displayHeader(self)
        self.displayOptions()


class menuItem:

    def __init__(self, text, function):
        self.text = text
        self.function = function


def displayHeader(menu):
    print header + '- ' + menu.getName()
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
        for o in menu.getOptions():
            if i == option - 1:
                return o.function
            i += 1

    except:
        clear()
        menu.displayMenu()
        print ''
        print 'Option does not exist!'
        choice(menu)