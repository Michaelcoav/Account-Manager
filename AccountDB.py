import sqlite3

class Account():
	def __init__(self):
		# establishes connects to accounts database
		self.con = sqlite3.connect("accounts.db")
		# creates cursor, allows to go through data
		self.cur = self.con.cursor()
		self.create_Table()

	def create_Table(self):
		self.cur.execute('''CREATE TABLE IF NOT EXISTS accounts
							(acc TEXT PRIMARY KEY, username TEXT, password TEXT)''')
		self.con.commit()

	def insert(self, account, username, password):
		self.cur.execute('''INSERT INTO accounts
							VALUES (?, ?, ?)''', (account, username, password))
		self.con.commit()

	def update(self, account, username, password):
		self.cur.execute('''UPDATE accounts SET username = ? 
							WHERE acc = ?''', (username, account))
		self.cur.execute('''UPDATE accounts SET password = ? 
							WHERE acc = ?''', (password, account))
		self.con.commit()

	def get_All(self):
		ls = []
		
		for row in self.cur.execute('''SELECT * FROM accounts'''):
			ls.append(row)

		return ls

	def remove(self, account):
		self.cur.execute('''DELETE FROM accounts 
							WHERE acc = ?''', (account,))
		self.con.commit()

	def remove_All(self):
		for row in self.get_All():
			self.remove(row[0])

