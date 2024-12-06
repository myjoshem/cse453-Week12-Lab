########################################################################
# COMPONENT:
#    MESSAGE
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary: 
#    This class stores the notion of a message
########################################################################

import control

##################################################
# MESSAGE
# One message to be displayed to the user or not
##################################################
class Message:

    # Static variable for the next id
    _id_next = 100

    ##################################################
    # MESSAGE DEFAULT CONSTRUCTOR
    # Set a message to empty
    ##################################################
    def __init__(self):
        self._text_control = "Public"  # Default security level for empty messages
        self._empty = True
        self._text = "Empty"
        self._author = ""
        self._date = ""
        self._id = Message._id_next
        Message._id_next += 1

    ##################################################
    # MESSAGE NON-DEFAULT CONSTRUCTOR
    # Create a message and fill it
    ##################################################   
    def __init__(self, text_control, text, author, date):
        self._text_control = text_control  # Security level (e.g., "Confidential")
        self._text = text  # Message content
        self._author = author  # Author of the message
        self._date = date  # Date of the message
        self._id = Message._id_next  # Auto-assign unique ID
        Message._id_next += 1
        self._empty = False  # Mark the message as non-empty

    ##################################################
    # MESSAGE :: GET ID
    # Determine the unique ID of this message
    ##################################################   
    def get_id(self):
        return self._id

    ##################################################
    # MESSAGE :: DISPLAY PROPERTIES
    # Display the attributes/properties but not the
    # content of this message
    ##################################################  
    def display_properties(self):
        if self._empty:
            return
        print(f"\t{self._id} [{self._text_control.upper()}] Message from {self._author} at {self._date}")

    ##################################################
    # MESSAGE :: DISPLAY TEXT
    # Display the contents or the text of the message
    ################################################## 
    def display_text(self):
        print(f"\tMessage: {self._text}")

    ##################################################
    # MESSAGE :: UPDATE TEXT
    # Update the contents or text of the message
    ################################################## 
    def update_text(self, new_text):
        self._text = new_text

    ##################################################
    # MESSAGE :: CLEAR
    # Delete the contents of a message and mark it as empty
    ################################################## 
    def clear(self):
        self._text = "Empty"
        self._author = ""
        self._date = ""
        self._empty = True
        self._text_control = ""
