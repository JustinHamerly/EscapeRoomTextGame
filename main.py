class GameObject:

	def __init__(self, name, appearance, feel, smell):
		self.name = name
		self.appearance = appearance
		self.feel = feel
		self.smell = smell

	def look(self):
		return f"You look at the {self.name}. {self.appearance}\n"
	
	def touch(self):
		return f"You touch the {self.name}. {self.feel}\n"
	
	def sniff(self):
		return f"You sniff the {self.name}. {self.smell}\n"

game_object = GameObject("Knife", "Sharp, short and very clean", "warm to the touch", "iron like blood and oak");

print(game_object.look(), game_object.touch(), game_object.sniff())
