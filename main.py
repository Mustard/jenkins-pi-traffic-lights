from Settings import Settings
from JenkinsClient import JenkinsClient
from TrafficController import TrafficController 
from Light import Light
import RPi.GPIO as GPIO
import time

from TrafficLights import TrafficLights

def main():
	print 'Starting...'
	client = JenkinsClient(Settings.JENKINS_SERVER)
	controller = TrafficController()
	traffic = TrafficLights()
	print 'Checking lights...'
	traffic.display()	
	while True:
		try:
			client.refresh()
			print(client)
			controller.resolve(client.built, client.test_failures, client.build_failures, client.building_total, (client.building_test_failures > 0), (client.building_build_failures > 0))
			print(controller)	
			traffic.display_status(controller.solid, controller.flash)
		except Exception as ex:
			print('Error...')
			print('Flash Lights ' + str([]))
			print('Solid Lights ' + str({'Orange, Red, Green'}))
			print ex
		time.sleep(5)

if __name__ == '__main__': 
	main()
	
