import RPi.GPIO as GPIO
import time
from Light import Light

class TrafficLights:

	def __init__(self):
		#GPIO.setmode(GPIO.BOARD)
		GPIO.setmode(GPIO.BCM)
		self.setup_lights()
		self.reset_lights()

	def setup_lights(self):
		"""
		Setup the GPIO ports for the lights
		"""
		GPIO.setup(Light.RED, GPIO.OUT)
		GPIO.setup(Light.ORANGE, GPIO.OUT)
		GPIO.setup(Light.GREEN, GPIO.OUT)

	def reset_lights(self):
		"""
		Turns off all the lights
		"""
		self.turn_off_light(Light.RED)
		self.turn_off_light(Light.ORANGE)
		self.turn_off_light(Light.GREEN)

	def turn_on_light(self, light):
		"""
		Turns a light on
		"""
		GPIO.output(light, GPIO.HIGH)

	def turn_off_light(self, light):
		"""
		Turns a light off
		"""
		GPIO.output(light, GPIO.LOW)

	def turn_on_light_for_period(self, light, seconds):
		"""
		Turns a light on for a number of seconds
		"""
		self.reset_lights()
		self.turn_on_light(light)
		time.sleep(seconds)
		self.turn_off_light(light)

	def cycle_lights(self):
		"""
		cycle through all the lights
		"""
		self.reset_lights()
		self.turn_on_light_for_period(Light.RED, 1)
		self.turn_on_light_for_period(Light.ORANGE, 1)
		self.turn_on_light_for_period(Light.GREEN, 1)
		self.reset_lights()
		
	def display(self):
		"""
		Cycle as traffic lights
		"""
		self.reset_lights()
		self.turn_on_light(Light.RED)
		time.sleep(1)
		self.turn_on_light(Light.ORANGE)
		time.sleep(1)
		self.turn_on_light(Light.GREEN)
		time.sleep(1)
		self.turn_off_light(Light.RED)
		self.turn_off_light(Light.ORANGE)
		self.turn_off_light(Light.GREEN)
		time.sleep(1)
		self.turn_on_light(Light.GREEN)
		time.sleep(1)
		self.turn_on_light(Light.ORANGE)
		time.sleep(1)
		self.turn_on_light(Light.RED)
		time.sleep(1)
		self.reset_lights()

	def display_status(self, solid, flashing=[], sleep_time=6):
		self.reset_lights()
		for light in solid:
			self.turn_on_light(light)
		for i in range(sleep_time):
			if i % 2 != 0:
				for flashing_light in flashing:
					self.turn_on_light(flashing_light)
			else:
				for flashing_light in flashing:
					self.turn_off_light(flashing_light)
			time.sleep(1)		 
		

	def blink(self, light, blink_delay, no_of_blinks):
		"""
		Flash a light the given number of times 
		"""
		self.reset_lights()
		for counter in range(0, no_of_blinks):
			print('on')
			self.turn_on_light(light)
			time.sleep(blink_delay)
			print('off')
			self.turn_off_light(light)
			time.sleep(blink_delay)
