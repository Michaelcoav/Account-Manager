import sqlite3

class Pin():
	def __init__(self):
		# establishes connects to accounts database
		self.con = sqlite3.connect("accounts.db")
		# creates cursor, allows to go through data
		self.cur = self.con.cursor()
		self.create_Table()

	def create_Table(self):
		self.cur.execute('''CREATE TABLE IF NOT EXISTS pin
							(id INTEGER PRIMARY KEY, pin_Number INTEGER)''')
		self.con.commit()

	def insert(self, pin_Number):
		self.cur.execute('''INSERT INTO pin
							VALUES (?, ?)''', (1, pin_Number))
		self.con.commit()

	def update(self, pin_Number):
		self.cur.execute('''UPDATE pin SET id = ? 
							WHERE pin_Number = ?''', (1, pin_Number))
		self.con.commit()

	def get_All(self):
		self.ls = []
		
		for row in self.cur.execute('''SELECT * FROM pin'''):
			self.ls.append(row)

		return self.ls

	def get_Pin(self):
		self.list = []
		return list(self.cur.execute('''SELECT pin_Number FROM pin
							WHERE id = ?''', (1,)))[0]




