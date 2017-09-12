from bunch import Bunch
import os

class DotDict(Bunch):
	''' Syntactic sugar on Bunch. '''
	pass

class PersistentDotDict(DotDict):

	''' Persistent Bunch-based dictionary with the ability
		to be saved to disk on modification.
		
		Operations passing through the modify method/property
		will be immediately written out to disk as a YAML file.
		
		>>> a = PDD()
		>>> a.setSavePath('./preferences.yml')
		>>> a.modify.x = 25 # this will save
		>>> a.modify.y = 54 # this will also save
		>>> a.z = 2 # this will not save
	'''
	save_path = ''
	save_mode = 'yaml'
	
	def set_save_mode(self, savemode):
		sm = savemode.lower()
		assert savemode in ['yaml', 'json', 'yml']
		self.save_mode = savemode		
	
	def set_save_path(self, path):
		self.save_path = path
	
	def save(self):
		spath = os.path.abspath(self.save_path)
		with open(spath, 'w') as sfile:
			if self.save_mode in ['yaml', 'yml']:	
				sfile.write(self.toYAML())
			else:
				sfile.write(self.toJSON())
				
	def commit(self):
		self.save()
			
	@property
	def modify(self):
		self.save()
		return self
		
	def modify_many(self, **kwargs):
		self.update(**kwargs)
		self.save()

		
# SHORTHANDS
PDD = PersistentDotDict
pdd = PersistentDotDict
dd  = DotDict


# MAIN/TESTING
if __name__ == "__main__":
	a = PDD()
	a.set_save_path('./tests.yml')
	a.set_save_mode('yml')
	a.modify.x = 25
	a.modify.y = 32
	a.modify.z = 35
	a.modify_many(stuff=25, things=['a','b'])
	print(a)
 
