#This is just a data holding class
class Package(object):
	def __init__(self):
		self.name = ""
		self.author = ""
		self.version = ""
		self.mcver = ""
		self.description = ""
	def __str__(self):
		return "Package '{0}' by '{1}' version '{2}' for Minecraft {3}".format(self.name, self.author, self.version, self.mcver)
