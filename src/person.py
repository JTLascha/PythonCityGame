""" This is the skeleton for the Person class - lots still to do on this """
import squares
from enum import Enum

class Skills(Enum):
	def __init__(self):
		CUSTOMER_SERVICE = 0
		JANITOR = 1
		CHEF = 2
		MANUAL_LABOR = 3
		MECHANICAL = 4
		CREATIVE = 5
		total = 6	# this isn't a skill. It's just the number of skills that exist.

# jobs will be instaniated as part of a building, so each building can offer fully custom jobs.
class Job:
	def __init__(self,name,QoL,skills_index,min_skill,max_skill):
		self.name = name
		self.QoL = QoL               #This is the way this job affects a person's quality of life
		#skills_needed and max_skills are lists of tuples in format of (skill_index, skill_value)
		self.skill_index = skills_index # this is a list of the skills needed for the job
		self.min_skill = min_skill 	#this is a list of the minimum value needed for each skill
		self.max_skill = max_skill	#this is the highest value that a skill can use. There is no bonus for being higher than this, and this job cannot level the skill past this point
	def efficiency(self,worker):
		#returns how efficient the worker is. It will be an int between 1 and 100
		#needs to compare the worker's skills to the needed skills and the max skills for the job.
		e = 0
		for i in self.skill_index:
			e = e + ((worker.skills[i] - min_skill[i]) /(max_skill[i] - min_skill[i]))
		e = e * 100  / len(self.skill_index)
		return e # for now just return 50


class Family:
	all = []  # list of all families
	def __init__(self,adults):
		self.adults = adults # this is a list of 1 or 2 people who are adults
		self.desired_children = 0
		self.children = []
		all.append(self)
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
	all = []	# list of all people
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
		self.skills = []
		for i in Range(0,Skils.total):
			skills.append(10)	# skills should be randomized. Add that later. For now they're all set to 10.
		all_people.appen(self)
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
