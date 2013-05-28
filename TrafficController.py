from Light import Light

class TrafficController: 
	
	def __init__(self): 
		self.flash = []
		self.solid = []

	def resolve(self, built, test_failures, build_failures, building_total, building_tests_failures=False, building_build_failures=False):
		self.flash = []
		self.solid = []

		if building_tests_failures:
			self.flash.append('Orange') #Light.ORANGE)
		if building_build_failures:
			self.flash.append('Red') #Light.RED)

		if not building_tests_failures and not building_build_failures:
			if building_total > 0:
				self.flash.append('Green') #Light.GREEN)
		
		# Solid lights 
		if not building_build_failures and build_failures > 0: #Light.RED 
			self.solid.append('Red') #Light.RED

		if not building_tests_failures and test_failures > 0: #Light.ORANGE
			self.solid.append('Orange') #Light.ORANGE

		if test_failures <= 0 and build_failures <= 0:
			self.solid.append('Green') #Light.GREEN
