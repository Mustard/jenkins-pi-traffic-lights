from Light import Light

class TrafficController: 
	
	def __init__(self): 
		self.flash = []
		self.solid = []

	def __str__(self):
		return \
		'Flash Lights ' + str(self.flash) + "\n" \
		'Solid Lights ' + str(self.solid) 

	def resolve(self, built, test_failures, build_failures, building_total, building_tests_failures=False, building_build_failures=False):
		self.flash = []
		self.solid = []

		if building_tests_failures:
			self.flash.append(Light.ORANGE)
		if building_build_failures:
			self.flash.append(Light.RED)

		if not building_tests_failures and not building_build_failures:
			if building_total > 0:
				self.flash.append(Light.GREEN)
		
		# Solid lights 
		if not building_build_failures and build_failures > 0: 
			self.solid.append(Light.RED)

		if not building_tests_failures and test_failures > 0:
			self.solid.append(Light.ORANGE)

		if not building_build_failures and not building_tests_failures:
			if test_failures <= 0 and build_failures <= 0:
				self.solid.append(Light.GREEN)
