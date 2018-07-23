""" This is the skeleton for the Person class - lots still to do on this """
import squares

class Skills:
	def __init__(self):
		self.customer_service = 0
		self.janitor = 0
		self.chef = 0
		self.manual_labor = 0
		self.mechanical = 0


class Job:
	def __init__(self,name,QoL,skills_needed,ideal_skills):
		self.name = name
		self.QoL = QoL               #This is the way this job affects a person's quality of life
		#skills_needed and max_skills are lists of tuples in format of (skill_index, skill_value)
		self.skills_needed = skills_needed
		self.max_skills = max_skills
	def efficiency(self,worker):
		#returns how efficient the worker is. It will be an int between 1 and 100
		#needs to compare the worker's skills to the needed skills and the max skills for the job.
		return 50 # for now just return 50

class Family:
	def __init__(self,adults):
		self.adults = adults # this is a list of 1 or 2 people who are adults
		self.desired_children = 0
		self.children = []
	def marriage(family1, family2):
		pass
		# merge the two families into a new family. Determine whose house the new family will live in and make all family members live there. Delete the old families.
	def updateQoL(self):
		cmod = -1
		for child in self.children:
			child.updateQoL
			cmod = cmod + child.QoL
		cmod = cmod / len(self.children)
		for adult in self.adults:
			adult.updateQoL(child_modifier=cmod)

class Person:
    # home_location and job_location should be the index
    # of the square where they live/work
	def __init__(self, age, job, job_location, home_location, index, ww):
        	self.age = age
		self.job = job
		self.work_week = ww   # this is how many hours a week the person works
		self.employment_tenure = 0  #number of turns this person has had this job
	        self.home_location = home_location
		self.home_length = 0 # number of turns person has lived in this square.
	        self.job_location = job_location
	        self.index = index
		self.QoL = 50

	# new QoL is based on living conditions, commute to work, quality of the work tile, and job type. Work related things are affected by the time spent working there. 
	# home based modifiers are affected by the time spent living there
        # the QoL is updated to be an average of the old QoL and the new QoL (life changes don't fully affect you all at once, after all!)
	# child_modifier is the average happiness of a person's children.
	# this function is called during job changes to update QoL. It is also called during the family updateQoL function at the end of each round and whenever they move to a new house
	def updateQoL(self,child_modifier=-1):
		newQoL = self.QoL
		if child_modifier > -1:
			newQoL = newQoL * 0.8 + childmodifer * 0.2
		self.QoL = (self.QoL + newQoL) / 2
