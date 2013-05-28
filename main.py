from Settings import Settings
from JenkinsClient import JenkinsClient
from TrafficController import TrafficController 
import time

#from TrafficLights import TrafficLights

def main():
	print(Settings)
	client = JenkinsClient(Settings.JENKINS_SERVER)
	controller = TrafficController()
	#traffic = TrafficLights()
	while True:
		try:
			client.refresh()
			print('Built ------------------- ' + str(client.built))
			print('Building Total ---------- ' + str(client.building_total))
			print('Building Test Failures -- ' + str(client.building_test_failures))
			print('Building Build Failures - ' + str(client.building_build_failures))
			#print('Total Failures ' + str(client.failures) + ' (' + str(client.test_failures) + ' test failures ' + str(client.build_failures) + ' build failures)')
			print('Test Failures ----------- ' + str(client.test_failures))
			print('Build Failures ---------- ' + str(client.build_failures))
			controller.resolve(client.built, client.test_failures, client.build_failures, client.building_total, (client.building_test_failures > 0), (client.building_build_failures > 0))
			print('Flash Lights ' + str(controller.flash))
			print('Solid Lights ' + str(controller.solid))
		except Exception as ex:
			print('Communication Error...')
			print('Flash Lights ' + str([]))
			print('Solid Lights ' + str({'Orange, Red, Green'}))
		time.sleep(5)
		for i in range(100):
			print

if __name__ == '__main__': 
	main()
	
