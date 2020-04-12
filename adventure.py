#TextTown Adventure

#class person:
#  answer = {}
#  def __init__(self, name):
#    #fucking bullshit

def print_color(col, text, *args, **kwargs):
	print('\033[38;2;'+str(col[0])+';'+str(col[1])+';'+str(col[2])+'m'+text +'\033[0m', *args, **kwargs)

class Place:
	actions = {}
	needs = []
	responses = {}
	solved = ""
	def __init__(self, name):
		self.name = name

	def action(self, action, *args):
		return getattr(self, action)(*args)
	
	def take(self, thing=None):
		if thing == None:
			print("You can't take " + self.name)
			return
		if thing in self.actions["take"]:
			self.actions["take"].remove(thing)
			inventory.append(thing)
			print("You took " + thing)
		else:
			print("There is no " + thing + " here")

	def talk(self, subject):
		if subject in self.responses:
			print(self.responses[subject])
			if subject in self.actions["talk"]:
				self.actions["talk"].remove(subject)
				self.possibly_solved()
		else:
			print("I don't know anything about that")
	
	def possibly_solved(self):
		if len(self.needs) == 0 and "problem" in self.responses:
			if "talk" not in self.actions or self.actions["talk"] == None or len(self.actions["talk"]) == 0:
				self.responses["problem"] = self.solved
	
	def give(self, thing):
		if thing in inventory:
			if thing in self.actions["give"]:
				inventory.remove(thing)
				self.actions["give"].remove(thing)
				print("Thanks for this " + thing)
				if thing in self.needs:
					self.needs.remove(thing)
					self.possibly_solved()
			else:
				print("I don't need this")
		else:
			print("You don't have " + thing)

inventory = []

town = Place("the town")
town.actions = {
	"take": ["easter egg"],
	"go": None
}

angela = Place("Angela")
angela.actions = {
	"talk": None,
	"give": ["herb"],
	"go": None,
	"take": ["bread", "easter egg"]
}
angela.responses = {
	"problem": "Father sick (needs herbs)",
	"job": "Baker",
	"baker": "Not only bread also easter egg",
	"sickness": "GO Bert"
}
angela.solved = "Not sick anymore thanks"

bert = Place("Bert")
bert.actions = {
	"talk": ["solution"],
	"go": None
}
bert.responses = {
	"problem": "Needs to send package to unknown place",
	"job": "Herbalist",
	"sickness": "Herb by the lake",
	"solution": "Talking about this solves his problem"
}

chris = Place("Chris")
chris.actions = {
	"talk": None,
	"go": None,
	"take": ["love letter"]
}
chris.responses = {
	"problem": "Crush Diana",
	"job": "Librarian"
}

diana = Place("Diana")
diana.actions = {
	"talk": None,
	"give": ["bread", "love letter"],
	"go": None
}
diana.need = ["bread"]
diana.responses = {
	"problem": "Hungry no bread",
	"job": "Cheesefarmer",
	"chris": ""
}

rinus = Place("Rinus")
rinus.actions = {
	"talk": None,
	"go": None
}
rinus.responses = {
	"job": "Florist",
	"supermarket": "C1000"
}

marius = Place("Marius")
marius.actions = {
	"talk": None,
	"go": None
}
marius.talk = lambda *a: print("3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823...")

lake = Place("the lake")
lake.actions = {
	"take": ["herb"],
	"go": None
}


places = {
    "angela": angela,
	"bert": bert,
	"chris": chris,
	"diana": diana,
	"town": town,
	"lake": lake,
	"rinus": rinus,
	"marius": marius
}

def go_to(place):
	global current_place
	if place in places:
		current_place = places[place]
		print("You go to " + places[place].name)
	else:
		print("There's no " + place + " here")
town.go = go_to

current_place = town

def get_command():
	global current_place

	print_color((255, 255, 0), "test:", end=' ')
	inp = input()

	parts = inp.lower().split(" ", 1)
	if parts[0] == 'leave':
		print('You leave ' + current_place.name + ' and go back to the town')
		current_place = town
	if parts[0] in current_place.actions:
		current_place.action(*parts)
	else:
		print("Command not recognized")

while True:
	try:
		get_command()
	except KeyboardInterrupt:
		print("")
		break
	except EOFError:
		print("")
		break

exit()











#add intro here
print("Welcome to TextTown! The goal is to help all 4 citizens. Talk to the citizens to find out how to help them. Type \"help\" while in the town square for instructions on how to do this.")

townsquare = True

while townsquare == True:
  townsquare = input(
      "You are in the town square. In front of you are the houses of Angela, Bert, Chris and Diane.\n").lower()
  if townsquare == "help":
    #add instructions here
    print("Ask Waddleduck how to play.")
    townsquare = True
  elif townsquare == "go angela":
    pass
    #Angela-stuff
  elif townsquare == "go bert":
    pass
    #Bert-stuff
  elif townsquare == "go chris":
    pass
    #Chris-stuff
  elif townsquare == "go diane":
    pass
    #Diane-stuff
  else:
    print("The command wasn’t recognised. Please try again.")
    townsquare = True

