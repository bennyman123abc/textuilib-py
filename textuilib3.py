import os
import time #debugging purposes

header = ["textuilib3"] #It's in an array for easy changing and making global
debug = [False] #We may actually do something with this :P
autopage = [False]
nopage = [False]

class menu:
	def __init__(self, name, menuPages):
		self.menuPages = []
		self.menuItems = [] #Only used if autopage or nopage is enabled
		
		#Set the name
		if isinstance(name, str):
			self.name = name
		elif isinstance(name, list):
			self.name = name[0]
		else:
			self.name = None
		
		#Set the list of menuPages
		if isinstance(menuPages, list):
			for p in menuPages:
				if isinstance(p, menuPage) and menuPage.menuItems != [] or None:
					self.menuPage.append(p)
		
	# TODO
	
class menuPage:
	def __init__(self, menuItems):
		self.menuItems = []
		
		for m in menuItems:
			if isinstance(m, menuItem):
				self.menuItems.append(m)
		
class menuItem:
    def __init__(self, text, function):
        if isinstance(text, str) and isinstance(function, str):
            self.text = text
            self.function = function
