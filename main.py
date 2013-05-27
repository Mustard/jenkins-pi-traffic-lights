from Settings import Settings
from JenkinsClient import JenkinsClient
#from TrafficLights import TrafficLights

def main():
	print(Settings)
	client = JenkinsClient(Settings.JENKINS_SERVER)
	#self.traffic = TrafficLights()
	client.refresh()
	

if __name__ == '__main__': 
	main()
	
