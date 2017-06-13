# *** STUDENTS: ADD YOUR NAME AND APPROPRIATE FILE PROLOGUE COMMENT, THEN REMOVE THIS LINE ***

# ---------------------- Needed for both parts  -----------------------------

# Address book manipulation functions

# STUDENTS: Complete these for Part I, then use them for Part II
# You may want to add other functions - REMOVE THESE LINES!

def createEmptyAddressBook():
  """Create a new document containing an empty address book.

     Returns: A document containing an empty address book.
  """


def addPerson(root, lastname, firstname, address, phone, email):
  """Add a person to the address book, unless they are already in it.

     Parameter: root - root element of xml document to add person to
     Parameter: lastname - last name of person to add
     Parameter: firstname - first name of person to add
     Parameter: address - address of person to add
     Parameter: phone - phone number of person to add
     Parameter: email - email address of person to add
     Returns: True if the person was successfully added, or False if a person
              with the same first and last name is already in the document.
  """


def removePerson(root, lastname, firstname):
  """Remove a person from the address book of an XML document.

     Parameter: root - root element of xml document to remove person from
     Parameter: lastname - last name of person to remove
     Parameter: firstname - first name of person to remove
     Returns: True if the person was successfully removed, or False if no person
              with that first and last name is in the document.
  """

def printPerson(root, lastname, firstname):
  """Print information about a person, nicely formatted.

     Parameter: root - root element of xml document containing address book
     Parameter: lastname - last name of person to print
     Parameter: firstname - first name of person to print
     Returns: True if the person's info was successfully printed, or False if
              no person with that first and last name is in the document.
  """

def printAll(root):
  """Print information about every person in the address book, nicely formatted 

     Parameter: root - root element of xml document containing address book
  """

# ------------------- Needed just for Part I  --------------------

def testPartI():
  """Test the functions required for part I."""
  doc = createEmptyAddressBook()
  root = doc.getroot()
  print "True should be printed 6 times for the next 6 functions"
  print addPerson(root, "Aardvark","Anthony", "244 KOSC", "978-555-1212", \
		"anthony.aardvark@gordon.edu")
  print addPerson(root, "Buffalo", "Boris", "Gordon Quad", "978-123-4567", \
		"boris.buffalo@gordon.edu")
  print addPerson(root, "Cat", "Charlene", "10 Litterbox Lane", "978-765-4321", \
		"charlene.cat@gordon.edu")
  print addPerson(root, "Dog", "Donna", "Fire Hydrant 37", "978-999-9999", \
		"donna.dog@gordon.edu")
  print addPerson(root, "Elephant", "Emily", "Big Top Circus", "978-000-0000", \
		"emily.elephant@gordon.edu") 
  print removePerson(root, "Cat", "Charlene")
  print "The following should print information for Donna Dog and then True"
  print printPerson(root, "Dog", "Donna")
  print "False should be printed 3 times for the next 3 functions"
  print addPerson(root, "Aardvark", "Anthony", "", "", "") # duplicate
  print removePerson(root, "Gopher", "Gus") # does not exist
  print printPerson(root, "Cat", "Charlene") # removed
  print "The following should print information for Anthony Aardvark, Boris Buffalo"
  print "Donna Dog, and Emily Elephant but not Charlene Cat" 
  printAll(root)
  # The following will save the final XML to the file "addressbook.xml"
  doc.write("addressbook.xml")
  

# Run tester for Part I.  Runs only when run by direct execution, but not when imported
if __name__ == "__main__":
  testPartI()	# This calls the tester for Part I

# ------------------- Needed just for Part II -------------------

def project4(fileName):
  """Main program for project4.
  
	 Parameter: fileName - name of file containing commands to be executed
				program exits when end of file reached on this file
  """


