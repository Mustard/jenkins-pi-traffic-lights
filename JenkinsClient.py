#import urllib.request
import json
import requests 

class JenkinsClient:

	# From http://javadoc.jenkins-ci.org/hudson/model/BallColor.html
	ANIME = 'anime'

	ABORTED = 'aborted'
	ABORTED_ANIME = 'aborted_anime'
	BLUE = 'blue' 
	BLUE_ANIME = 'blue_anime'
	DISABLED = 'disabled'
	DISABLED_ANIME = 'disabled_anime'
	GREY = 'grey'
	GREY_ANIME = 'grey_anime'
	NOTBUILT = 'notbuilt'
	NOTBUILT_ANIME = 'notbuilt_anime'
	RED = 'red'
	RED_ANIME = 'red_anime'
	YELLOW = 'yellow'
	YELLOW_ANIME = 'yellow_anime'
	
	def __init__(self, jenkins_url):
		self.built = 0
		self.failures = 0
		self.test_failures = 0		
		self.building = 0
		self.building_test_failures = 0
		self.building_build_failures = 0
		self.jenkins_url = jenkins_url

	def __str__(self):
		# TODO 
		return 'Built: ' + self.built
		#'Failures: ' + self.failures
								

	def refresh(self):
		r = requests.get(self.jenkins_url + 'api/json')
		data = r.json()
		#print data['jobs']
		# Create a list of build statuses (colors)
		statuses = []
		for job in data['jobs']:
			statuses.append(job['color'])
		# Current completed job statuses
		self.building = 0
		for status in statuses:
			if self.ANIME in status.lower():
				self.building = self.building + 1
		self.built = statuses.count(self.BLUE)
		self.test_failures = statuses.count(self.YELLOW)
		self.failures = statuses.count(self.RED)		
		self.building_test_failures = statuses.count(self.YELLOW_ANIME)
		self.building_build_failures = statuses.count(self.RED_ANIME)
		

