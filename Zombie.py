def mistake():
	print("Please enter 1 or 2.")

def retry():
	choice = input("Would you like to try again?\n1)Yes\n2)No\n\n>>")
	if choice == "1":
		start()
	elif choice == "2":
		quit()
	else:
		mistake()
		retry()

def start():
	choice = input("\nIt was a hot summer evening when you and your friend went to the biggest club in the city for a wild night...\nYou told your parents you would be back before midnight, but while you were enjoying yourself, a group of zombies started attacking the club...\nThere is complete chaos and nothing but darkness and screaming...\nYou must get back home safe...\n\nWill you look for your friend in the crowd?\n1)Yes\n2)No\n\n>>")
	if choice == "1":
		friend()
	elif choice == "2":
		noFriend()
	else:
		mistake()
		start()

def friend():
	choice = input("\nFortunately, you found your friend! Your friend seems very drunk, so you carry him on your back. You think you know where the exit is...\n\nShould you hide first, or go striaght to the exit?\n1)Hide\n2)Go straight to the exit\n\n>>")
	if choice == "1":
		friendExit()
	elif choice == "2":
		friendHide()
	else:
		mistake()
		friend()

def friendExit():
	choice = input("\nWhile you were running to the exit, your friend got attacked by a zombie.\nYou survived, though, and now you are left in the middle of the club.\n\nShould you continue to the exit, or hide in a bathroom?\n1)Continue to exit\n2)Hide in a bathroom\n\n>>")
	if choice == "1":
		gotoExit()
	elif choice == "2":
		bathroom()
	else:
		mistake()
		friendExit()

def gotoExit():
	choice = input("You successfully reached the exit, but the exit is locked! There are zombies running toward you!\nOn your left is a group of people and on your right is a staircase.\n\nWhich way should you go?\n1)Group of people\n2)Staircase\n\n>>")
	if choice == "1":
		people()
	elif choice == "2":
		staircase()
	else:
		mistake()
		gotoExit()

def people():
	pass

def staircase():
	pass

def bathroom():
	pass

def friendHide():
	pass

def noFriend():
	choice = input("You are on your own, and you think you know where the exit is.\n\nShould you hide first, or head straight to the exit?\n1)Hide first\n2)Head to the exit\n\n>>")
	if choice == "1":
		exitAlone()
	elif choice == "2":
		hideAlone()
	else
		mistake()
		noFriend()

def exitAlone():
	pass

def hideAlone():
	pass

start()