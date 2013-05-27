import RPi.GPIO as GPIO
import time
from Lights import Lights

class TrafficLights:

	def __init__(self):
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
		GPIO.output(light, False)

	def turn_off_light(self, light):
		"""
		Turns a light off
		"""
		GPIO.output(light, True)

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
		self.turn_on_light_for_period(Light.ORANGE, 1)
		self.turn_on_light_for_period(Light.GREEN, 1)
		self.reset_lights()
		
	def go(self):
		"""
		Cycle as traffic lights
		"""
		self.reset_lights()
		self.turn_on_light(self.lights.Red)
		time.sleep(2)
		self.turn_on_light(self.lights.Amber)
		time.sleep(2)
		self.turn_off_light(self.lights.Red)
		self.turn_off_light(self.lights.Amber)
		self.turn_on_light(self.lights.Green)
		time.sleep(10)
		self.turn_on_light(self.lights.Amber)
		self.turn_off_light(self.lights.Green)
		time.sleep(2)
		self.turn_on_light(self.lights.Red)
		self.turn_off_light(self.lights.Amber)

	def blink(self, light, blink_delay, no_of_blinks):
		"""
		Blinks a light 15 times
		"""
		self.reset_lights()
		for counter in range(0, no_of_blinks):
			print('on')
			self.turn_on_light(light)
			time.sleep(blink_delay)
			print('off')
			self.turn_off_light(light)
			time.sleep(blink_delay)
