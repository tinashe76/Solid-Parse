# Github => tinashe76
# The words Subroutine and function are used interchangeably

""" CONTENTS 

LINE 91: Subroutine for 'Mount'

LINE 110: Subroutine for 'Search'

LINE 207: Subroutine for 'Refresh'

LINE 335: Subroutine for 'Print'

LINE 413: Subroutines for String Manipulation Buttons

LINE 495: Button and Key binding

LINE 550: main() loop

"""

# NOTE: I created the string manipulation algorithms myself, the functions are not from tkinter or any other module, so
# calling them in a different isolated program will invoke an error or unexpected behaviour.
# Oh and feel free to write your own algorithms if you feel like the subroutines are not performing fast or well enough.
print("\n> initializing..")
import os
import tkinter
from tkinter import messagebox
from tkinter import *
import sys
import requests

# tkinter Object (this represents the parent window)
root = Tk()
root.title("Solid Parse ver. 1.0.1")
root.geometry('400x500')

# This Creates a Menu Bar
main_menu = Menu(root)

# This Creates a Sub Menu Bar
file_menu = Menu(root)
# Some variables for the Sub Menu Bar are initialized and assigned at the bottom because they contain commands that call
# subroutines that a created later in the program.

# Value is used later in the program as a list that carries multiple values
value = [""]

#-----------------------------------------------------------------------------------------------------------------------
# I intend to use these variables as 'textvariables' later in the program
# So assigning them StringVar() allows the program to treat them as strings when we use the get() method e.g data.get()

data = StringVar()
file_name = StringVar()

#------------------------------------------------------------------------------------------------------------------------

main_menu.add_cascade(label="File", menu=file_menu)
root.config(menu=main_menu)

# Display Window1
displayWindow = LabelFrame(root,text=f"", bd=1, bg="#111", fg="#fff", width=50, height=8, font="heveltica 10")
displayWindow.place(x=6, y=3, height=50, width=370)

# Display Window2
displayWindow2 = LabelFrame(root, text=f"", bd=1, bg="#111", fg="#fff", width=50, height=8, font="heveltica 10")
displayWindow2.place(x=6, y=50, height=50, width=370)

# Display Window3
displayWindow3 = LabelFrame(root, text=f"", bd=1, bg="#111", fg="#fff", width=50, height=8, font="heveltica 10")
displayWindow3.place(x=6, y=98, height=50, width=370)

# Display Window4
displayWindow4 = LabelFrame(root, text=f"", bd=1, bg="#111", fg="#fff", width=50, height=8, font="heveltica 10")
displayWindow4.place(x=6, y=146, height=50, width=370)

# Display Window5
displayWindow5 = LabelFrame(root, text=f"", bd=1, bg="#111", fg="#fff", width=50, height=8, font="heveltica 10")
displayWindow5.place(x=6, y=194, height=50, width=370)

# Log Window
displayWindowLog = LabelFrame(root, text=f"Waiting For File...", bd=0, bg="#111", fg="#fff", width=50, height=8, font="heveltica 10")
displayWindowLog.place(x=6, y=370, height=30, width=370)

# File Mount
file_mount = Entry(root, bd=3, textvariable=file_name, relief=GROOVE)
file_mount.place(x=6, y=260, height=50, width=370)


# Below you'll encounter a lot of code repetition, that is because to update a Widget e.g. Window 5, I had to create another
# Window 5 with updated text output, font-color and background color values.

# Subroutine for Importing a File to read data from
def mount():
	try:
		txtFile = str(file_name.get())

		if txtFile.startswith("http") or txtFile.startswith("www"):
			retrieve = requests.get(txtFile)
			print("\n> Downloading file...")

			with open("file.txt", "wb") as f:
				f.write(retrieve.content)

			print("\nDone!")

			file = open("file.txt", "r")
			# Log
			displayWindowLog = LabelFrame(root,text = f"Mounted", bd=0, bg="#111", fg="light Green", width=50, height=8, font="heveltica 10")
			displayWindowLog.place(x=6, y=370, height=30, width=370)
			print("\nso far so good...")
		else:
			file = open(f"{txtFile}", "r")
			# Log
			displayWindowLog = LabelFrame(root,text = f"Mounted", bd=0, bg="#111", fg="light Green", width=50, height=8, font="heveltica 10")
			displayWindowLog.place(x=6, y=370, height=30, width=370)
			print("so far so good...\n")


	except FileNotFoundError:
		# Log
		displayWindowLog = LabelFrame(root,text = f"File Not Found", bd=0, bg="#111", fg="#ff0000", width=50, height=8, font="heveltica 10")
		displayWindowLog.place(x=6, y=370, height=30, width=370)
		print("> Check whether your file Address is correct.\n")


	except:
		messagebox.showerror("Connection Error", "Bad Address or No Internet Connection")
		print("> Check Your Internet Connection.\n")



# Text Input1
text_entry = Entry(root, bd=5, textvariable=data, relief=GROOVE)
text_entry.place(x=120, y=440, height=40, width=260)


# Subroutine for retrieving and displaying data from mounted file
def write():
	print("\n> retrieving data...")
	clean_data = str(data.get())
	value = list(range(0, 100)) # For now, Creating a larger list may result in performance issues and crashes
	num = 0

	

	try:
		txtFile = str(file_name.get())
		file = open(f"{txtFile}", "r")
		for line in file:
			if clean_data in line:
				num += 1
				value[num] = line

				# The Program Only Stores and Displays 5 Lines of text but the actual number of lines (of retrieved text) may be greater.

				# Play around with 'value' and Display Windows if you wish to store and print all the retrieved text to display.

				try:
					# Display Window1
					displayWindow = LabelFrame(root,text = f"{value[1]}", bd=1, bg="#111", fg="#fff", width=50, height=8, font="heveltica 10")
					displayWindow.place(x=6, y=3, height=50, width=370)

				except:
					# Display Window1
					displayWindow = LabelFrame(root,text = f"", bd=1, bg="#111", fg="#fff", width=50, height=8, font="heveltica 10")
					displayWindow.place(x=6, y=3, height=50, width=370)


				try:
					# Display Window2
					displayWindow2 = LabelFrame(root,text = f"{value[2]}", bd=1, bg="#111", fg="#fff", width=50, height=8, font="heveltica 10")
					displayWindow2.place(x=6, y=50, height=50, width=370)

				except:
					# Display Window2
					displayWindow2 = LabelFrame(root,text = f"", bd=1, bg="#111", fg="#fff", width=50, height=8, font="heveltica 10")
					displayWindow2.place(x=6, y=50, height=50, width=370)

				try:
					# Display Window3
					displayWindow3 = LabelFrame(root,text = f"{value[3]}", bd=1, bg="#111", fg="#fff", width=50, height=8, font="heveltica 10")
					displayWindow3.place(x=6, y=98, height=50, width=370)

				except:
					# Display Window3
					displayWindow3 = LabelFrame(root,text = f"", bd=1, bg="#111", fg="#fff", width=50, height=8, font="heveltica 10")
					displayWindow3.place(x=6, y=98, height=50, width=370)

				try:
					# Display Window4
					displayWindow4 = LabelFrame(root,text = f"{value[4]}", bd=1, bg="#111", fg="#fff", width=50, height=8, font="heveltica 10")
					displayWindow4.place(x=6, y=146, height=50, width=370)

				except:
					# Display Window4
					displayWindow4 = LabelFrame(root,text = f"", bd=1, bg="#111", fg="#fff", width=50, height=8, font="heveltica 10")
					displayWindow4.place(x=6, y=146, height=50, width=370)

				try:
					# Display Window5
					displayWindow5 = LabelFrame(root,text = f"{value[5]}", bd=1, bg="#111", fg="#fff", width=50, height=8, font="heveltica 10")
					displayWindow5.place(x=6, y=194, height=50, width=370)

				except:
					# Display Window5
					displayWindow5 = LabelFrame(root,text = f"", bd=1, bg="#111", fg="#fff", width=50, height=8, font="heveltica 10")
					displayWindow5.place(x=6, y=98, height=50, width=370)

		print("> Done!")

	except IndexError:
		messagebox.showinfo("Index Error Handler", f"Large amounts of Data Retrieved.\n\nIt is good practice to narrow down your search by using specific keywords.")

	except FileNotFoundError:
		print("> failed")
		messagebox.showerror("Error", "No file to Process")

# NOTE: You cant use a scroll bar because the main displayWindows are LabelFrames and not Text Views or Text Areas.
# The display is made up of five displayWindows, each similar to an icon or button with a Label. So the text cant be copied
# or edited. However, I'm sure there's a way to use Text. This would enable the user to scroll down the search results 
# at the cost of stability probably. In such a case, I would advise you to use multi-threading or multi-processing.

# To use it, just change all Display windows to textView or something like that and uncomment all the code below

#Scroll Bar Code
#scrollBar = Scrollbar(root, command=displayWindow.yview())
#scrollBar.place(x=375, y=5, height=385)

# Loop
#######################################################################################################################################

# As the name suggests this is a subroutine for 'refreshing' the page.
# Well, it justs resets everything on display. After browsing through the tkinter usage guide in python 
# I still couldnt find a built in function for resetting  the panelWindow so
# I had to create 'refresh()' and cram 3 quarters of the original code inside.
# I ommitted the Parent Window and the Menu Bars because that would have created another instance of the program instead
# of just updating the output and input fields that were already present

def refresh():
	displayWindow = LabelFrame(root,text = f"", bd=1, bg="#111", fg="#fff", width=50, height=8, font="heveltica 10")
	displayWindow.place(x=6, y=3, height=50, width=370)

	# Display Window2
	displayWindow2 = LabelFrame(root,text = f"", bd=1, bg="#111", fg="#fff", width=50, height=8, font="heveltica 10")
	displayWindow2.place(x=6, y=50, height=50, width=370)

	# Display Window3
	displayWindow3 = LabelFrame(root,text = f"", bd=1, bg="#111", fg="#fff", width=50, height=8, font="heveltica 10")
	displayWindow3.place(x=6, y=98, height=50, width=370)

	# Display Window4
	displayWindow4 = LabelFrame(root,text = f"", bd=1, bg="#111", fg="#fff", width=50, height=8, font="heveltica 10")
	displayWindow4.place(x=6, y=146, height=50, width=370)

	# Display Window5
	displayWindow5 = LabelFrame(root,text = f"", bd=1, bg="#111", fg="#fff", width=50, height=8, font="heveltica 10")
	displayWindow5.place(x=6, y=194, height=50, width=370)

	# Log
	displayWindowLog = LabelFrame(root,text = f"running...", bd=0, bg="#111", fg="lime green", width=50, height=8, font="heveltica 10")
	displayWindowLog.place(x=6, y=370, height=30, width=370)

	# File Mount
	file_mount = Entry(root, bd=5, textvariable=file_name, relief=GROOVE)
	file_mount.place(x=6, y=260, height=50, width=370)

	try:
		# File Mount Button
		fileButton = Button(root, text='Mount', bg='gray', activebackground="lime green", width=12, height=5, font="System", command=mount)
		fileButton.place(x=6, y=300, height=40, width=369)

	except UnboundLocalError:
		print("")


	# Text Input1
	text_entry = Entry(root, bd=5, textvariable=data, relief=GROOVE)
	text_entry.place(x=120, y=440, height=40, width=260)

	# Handlers
	def write():
		print("\n> retrieving data...")
		check = ""
		check2 = ""
		clean_data = str(data.get())
		value = list(range(0, 100))
		num = 0

		txtFile = str(file_name.get())
		file = open(f"{txtFile}", "r")

		try:
			for line in file:
				if clean_data in line:
					num += 1
					value[num] = line.rstrip()

					try:
						# Display Window1
						displayWindow = LabelFrame(root,text = f"{value[1]}", bd=1, bg="#111", fg="#fff", width=50, height=8, font="heveltica 10")
						displayWindow.place(x=6, y=3, height=50, width=370)

					except:
						# Display Window1
						displayWindow = LabelFrame(root,text = f"", bd=1, bg="#111", fg="#fff", width=50, height=8, font="heveltica 10")
						displayWindow.place(x=6, y=3, height=50, width=370)


					try:
						# Display Window2
						displayWindow2 = LabelFrame(root,text = f"{value[2]}", bd=1, bg="#111", fg="#fff", width=50, height=8, font="heveltica 10")
						displayWindow2.place(x=6, y=50, height=50, width=370)

					except:
						# Display Window2
						displayWindow2 = LabelFrame(root,text = f"", bd=1, bg="#111", fg="#fff", width=50, height=8, font="heveltica 10")
						displayWindow2.place(x=6, y=50, height=50, width=370)

					try:
						# Display Window3
						displayWindow3 = LabelFrame(root,text = f"{value[3]}", bd=1, bg="#111", fg="#fff", width=50, height=8, font="heveltica 10")
						displayWindow3.place(x=6, y=98, height=50, width=370)

					except:
						# Display Window3
						displayWindow3 = LabelFrame(root,text = f"", bd=1, bg="#111", fg="#fff", width=50, height=8, font="heveltica 10")
						displayWindow3.place(x=6, y=98, height=50, width=370)

					try:
						# Display Window4
						displayWindow4 = LabelFrame(root,text = f"{value[4]}", bd=1, bg="#111", fg="#fff", width=50, height=8, font="heveltica 10")
						displayWindow4.place(x=6, y=146, height=50, width=370)

					except:
						# Display Window4
						displayWindow4 = LabelFrame(root,text = f"", bd=1, bg="#111", fg="#fff", width=50, height=8, font="heveltica 10")
						displayWindow4.place(x=6, y=146, height=50, width=370)

					try:
						# Display Window5
						displayWindow5 = LabelFrame(root,text = f"{value[5]}", bd=1, bg="#111", fg="#fff", width=50, height=8, font="heveltica 10")
						displayWindow5.place(x=6, y=194, height=50, width=370)

					except:
						# Display Window5
						displayWindow5 = LabelFrame(root,text = f"", bd=1, bg="#111", fg="#fff", width=50, height=8, font="heveltica 10")
						displayWindow5.place(x=6, y=98, height=50, width=370)

					# Remember To Fix Refresh Issue

		except IndexError:
			messagebox.showinfo("Index Error Handler", f"Large amounts of Data Retrieved.\n\nIt is good practice to narrow down your search by using specific keywords.")
			print("\nDone!")
		

	try:
		# Button to submit
		Button = Button(root,text='Search', bg='gray', activebackground="lime green", width=12, height=5, font="System", command=write)
		Button.place(x=6, y=440, height=40, width=100)

	except UnboundLocalError:
		print("")

	except UnicodeDecodeError:
		print("failed to decode one or more bytes.")
		messagebox.showinfo("Alert", f"Non-text files not supported.")
		print("> failed")

########################################################################################################################################

# Prints to Notepad    |    Works well with any text file
def advancedSearch():
	try:
		clean_data = str(data.get())

		txtFile = str(file_name.get())
		log = open("log.txt", "w")
		file = open(f"{txtFile}", "r")

		for line in file:
			if clean_data in line:
				log.write(f"{line}\n")

		log.close()
		# opens log.txt using Notepad++
		os.system("notepad.exe log.txt")

	except FileNotFoundError:
		messagebox.showerror("Error", "No file to process")


# Prints to Browser   |   Doesn't work well with parsed webpages
def browserPlugin():
	try:
		os.system("del index.html")

	except:
		print("File Not Found")

	try:
		clean_data = str(data.get())
		txtFile = str(file_name.get())
		html = open("index.txt", "w")
		file = open(f"{txtFile}", "r")

		for line in file:
			if clean_data in line:
				line = line.replace(',', '<a style="color: #ff0000">   |   </a>')
				html.write(f'<h2>{line}</h2><br />\n')


		html.close()		
		os.system(f"ren index.txt index.html")
		os.system(f"index.html")

	except FileNotFoundError:
		messagebox.showerror("Error", "No file to Process")

# ABOUT

def about():
	messagebox.showinfo("Solid Parse For Windows", "Author: Tinashe Mashindi Z\n\nSoftware is Licensed To the General public under the MIT license. Open ReadMe.html for more.")

def download():
	messagebox.showinfo("Download Latest Version","https://www.basicLogic.com/solidParse/releases")

def notes():
	try:
		# Checking to see if the file is available. 'try' wont except os.system() when an error is encountered on the terminal.
		file = open("_patch_notes.txt", "r")
		file.close()

		# Opening The file
		os.system("_patch_notes.txt")

	except FileNotFoundError:
		messagebox.showwarning("Error Encountered", "Patch Notes Not Found. Please Download the software\n from its official website. Your version might be modified, or contain malicious software")


# For this type of program, It's good practice to put most commands that call optional functions, at the
# bottom of the page - to avoid UnboundLocalError(s).
# In order to make the code easier to read I seperated subroutines from commands, by placing most of the
# optional commands at the bottom. This however results in UnboundLocalError(s) for some buttons called inside functions.
# But you can ignore it or except it with a nice message. In these cases, The code that is referenced before assignment
# is inside a function...so as long as the function is called at a point that is after the proper assignment of the code, 
# the error doesnt affect the program: *Dont try this in languages that have to compiled before execution e.g. C or Java

################################################## MINI BUTTONS SUBROUTINES #####################################################

# Files are declared and initiated inside each and every single variable, because their initialization process contains
# references to code that doesnt yet 'exist'. [Refering to removeWhiteSpace()] if you were to put 'example 1' and 'example 2' 
# outside of the function you'd get a FileNotFoundError because txtFile is created after you click on Search, during runtime.

def removeWhiteSpace():
	try:
		print("\n> Removing WhiteSpace...")
		clean_data = str(data.get())
		txtFile = str(file_name.get())	#example 1
		log = open("log.txt", "w")
		file = open(f"{txtFile}", "r")  #example 2

		for line in file:
			if clean_data in line:
				line = line.strip()
				log.write(f"{line}\n")

		print("\n> Done!")
		log.close()
		os.system("notepad.exe log.txt")

	except FileNotFoundError:
		print("> failed")
		messagebox.showerror("Error", "No file to process")


def removeComma():
	try:
		print("\n> Removing Comma...")
		clean_data = str(data.get())
		txtFile = str(file_name.get())
		log = open("log.txt", "w")
		file = open(f"{txtFile}", "r")

		for line in file:
			if clean_data in line:
				line = line.replace(",", " ")
				log.write(f"{line}\n")

		print("\n> Done!")
		log.close()
		os.system("notepad.exe log.txt")

	except FileNotFoundError:
		print("> failed")
		messagebox.showerror("Error", "No file to process")



def getLowercase():
	try:
		print("\n> getting lowercase...")
		clean_data = str(data.get())
		txtFile = str(file_name.get())
		log = open("log.txt", "w")
		file = open(f"{txtFile}", "r")

		for line in file:
			if clean_data.lower() in line.lower():
				log.write(f"{line}\n")

		print("\n> Done!")		
		log.close()
		os.system("notepad.exe log.txt")

	except FileNotFoundError:
		print("> failed")
		messagebox.showerror("Error", "No file to process")

def getRange():
	try:
		print("\n> getting range...")
		clean_data = str(data.get())
		txtFile = str(file_name.get())
		log = open("log.txt", "w")
		file = open(f"{txtFile}", "r")
		count = 0
		countChar = 0

		for line in file:
			count += 1
			for char in line.split():
				countChar += 1

		print("\n> Done!")		
		messagebox.showinfo("Range", f"File contains {count} lines and {countChar} characters.")
	
	except FileNotFoundError:
		print("> failed")
		messagebox.showerror("Error", "No file to process")


def lineNumber():
	try:
		print("\n> getting line number...")
		clean_data = str(data.get())
		txtFile = str(file_name.get())
		log = open("log.txt", "w")
		file = open(f"{txtFile}", "r")
		count = 0
		countChar = 0

		for line in file:
			count += 1
			if clean_data in line:
				line = line.strip()
				log.write(f"{count}:  {line}\n\n")

		print("\n> Done!")	
		log.close()
		os.system("notepad.exe log.txt")

	except FileNotFoundError:
		print("> failed")
		messagebox.showerror("Error", "No file to process")

def listResults():
	# Write code to remove any characters before "<img" and return the result
	try:
		print("\n> listing results...")
		clean_data = str(data.get())
		txtFile = str(file_name.get())
		log = open("log.txt", "w")
		file = open(f"{txtFile}","r")
		count = 0
		countChar = 0

		for line in file:
			if clean_data in line:
				line = line.strip()
				if line.startswith(f"{clean_data}"):
					log.write(f"{line}\n\n")

		print("\n> Done!")				
		log.close()
		os.system("notepad.exe log.txt")

	except FileNotFoundError:
		print("> failed")
		messagebox.showerror("Error", "No file to process")





#################################################################################################################################

# COMMANDS

# Remove Commas
removeComma = Button(root, text="RC", activebackground="lime green", width=12, height=5, font="System", command=removeComma)
removeComma.place(x=6, y=406, height=30, width=50)

# List Results
removeNumber = Button(root, text="LR", activebackground="lime green", width=12, height=5, font="System", command=listResults)
removeNumber.place(x=70, y=406, height=30, width=50)

# Remove White Space
removeWhiteSpace = Button(root, text="RW", activebackground="lime green", width=12, height=5, font="System", command=removeWhiteSpace)
removeWhiteSpace.place(x=130, y=406, height=30, width=50)

# Get Lowercase
getLowercase = Button(root, text="GL", activebackground="lime green", width=12, height=5, font="System", command=getLowercase)
getLowercase.place(x=190, y=406, height=30, width=50)

# Get Range
getRange = Button(root, text="GR", activebackground="lime green", width=12, height=5, font="System", command=getRange)
getRange.place(x=250, y=406, height=30, width=50)

# Line Number
insert = Button(root, text="LN", activebackground="lime green", width=12, height=5, font="System", command=lineNumber)
insert.place(x=310, y=406, height=30, width=60)

# Mount
fileButton = Button(root, text='Mount', bg='gray', activebackground="lime green", width=12, height=5, font="System", command=mount)
fileButton.place(x=6, y=300, height=40, width=369)

# Search
Button = Button(root,text='Search', bg='gray', activebackground="lime green", width=12, height=5, font="System", command=write)
Button.place(x=6, y=440, height=40, width=100)

# Print
file_menu.add_command(label="Print", command=advancedSearch)
file_menu.add_command(label="Print To Browser", command=browserPlugin)

# Refresh
main_menu.add_command(label="Clear", command=refresh)

# Update Menu
update_menu = Menu(root)
update_menu.add_command(label="Download", command=download)
update_menu.add_command(label="Patch Notes", command=notes)

# Update
main_menu.add_cascade(label="Updates", menu=update_menu)

# About
main_menu.add_command(label="About", command=about)

# Exit
main_menu.add_command(label="Exit", command=root.destroy)

print("\n> Done!")
root.mainloop()


