########################################################################
# COMPONENT:
#    INTERACT
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary: 
#    This class allows one user to interact with the system
########################################################################

import messages
from control import Control

###############################################################
# USER
# User has a name and a password
###############################################################
class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

userlist = [
   [ "AdmiralAbe",     "password" ],  
   [ "CaptainCharlie", "password" ], 
   [ "SeamanSam",      "password" ],
   [ "SeamanSue",      "password" ],
   [ "SeamanSly",      "password" ]
]

###############################################################
# USERS
# All the users currently in the system
###############################################################
users = [*map(lambda u: User(*u), userlist)]

ID_INVALID = -1

######################################################
# INTERACT
# One user interacting with the system
######################################################
class Interact:

    ##################################################
    # INTERACT CONSTRUCTOR
    # Authenticate the user and get him/her all set up
    ##################################################
    def __init__(self, username, password, messages):
        self._authenticate(username, password)
        self._username = username
        self._p_messages = messages

         # Retrieve the user's security level from Control
        self._security_level = Control.get_user_security_level(username)

        # Print user security level for debugging (optional)
        print(f"User '{username}' authenticated with security level: {self._security_level}")
    

    ##################################################
    # INTERACT :: SHOW
    # Show a single message
    ##################################################
    def show(self):
        id_ = self._prompt_for_id("display")
        # Attempt to display the message
        result = self._p_messages.show(id_, self._security_level)
        if result == "NOT_FOUND":
            print(f"ERROR! Message ID '{id_}' does not exist.")
        elif result == "ACCESS_DENIED":
            print(f"ACCESS DENIED! You do not have sufficient clearance to view message ID '{id_}'.")
        print()

    ##################################################
    # INTERACT :: DISPLAY
    # Display the set of messages
    ################################################## 
    def display(self):
        """Delegate the display of messages to the Messages class."""
        print("Messages:")
        self._p_messages.display(self._security_level)  # Pass the user's security level
        print()  # Add a blank line for better formatting

    ##################################################
    # INTERACT :: ADD
    # Add a single message
    ################################################## 
    def add(self):
        # Display available levels for selection
        print("Select a security level for your message:")
        available_levels = [
            (level_name, level_value)
            for level_name, level_value in Control.SECURITY_LEVELS.items()
            if Control.has_write_privileges(self._security_level, level_value)
        ]
        
        for i, (level_name, _) in enumerate(available_levels, start=1):
            print(f"{i}. {level_name}")
        
        # Prompt user for their selection
        try:
            selection = int(input("Enter the number corresponding to the security level: ")) - 1
            if selection < 0 or selection >= len(available_levels):
                raise ValueError
        except ValueError:
            print("ERROR: Invalid selection. Please try again.")
            return

        # Retrieve the selected security level
        selected_level = available_levels[selection][0]  # This applies to the message, not the user

        # Warn the user if they may lose access
        if Control.SECURITY_LEVELS[selected_level] > self._security_level:
            print(f"WARNING: You may not be able to access this message later because it is at a higher level than your current clearance ({selected_level}).")
        
        # Add the message
        self._p_messages.add(
            selected_level,  # Security level of the message
            self._prompt_for_line("message"),
            self._username,
            self._prompt_for_line("date"),
        )
        print("Message successfully added.")


    ##################################################
    # INTERACT :: UPDATE
    # Update a single message
    ################################################## 
    def update(self):
        id_ = self._prompt_for_id("update")
        # Attempt to show the message for updating
        result = self._p_messages.show(id_, self._security_level)
        if result == "NOT_FOUND":
            print(f"ERROR! Message ID '{id_}' does not exist.")
            return
        elif result == "ACCESS_DENIED":
            print(f"ACCESS DENIED! You do not have sufficient clearance to update message ID '{id_}'.")
            return

        # Update the message content
        new_text = self._prompt_for_line("updated message content")
        self._p_messages.update(id_, new_text, self._security_level)
        print(f"Message ID '{id_}' successfully updated.")
        print()
            
    ##################################################
    # INTERACT :: REMOVE
    # Remove one message from the list
    ################################################## 
    def remove(self):
        id_ = self._prompt_for_id("delete")
        # Attempt to remove the message
        result = self._p_messages.remove(id_, self._security_level)
        if result == "NOT_FOUND":
            print(f"ERROR! Message ID '{id_}' does not exist.")
        elif result == "ACCESS_DENIED":
            print(f"ACCESS DENIED! You do not have sufficient clearance to delete message ID '{id_}'.")
        else:
            print(f"Message ID '{id_}' successfully deleted.")
        print()

    ##################################################
    # INTERACT :: PROMPT FOR LINE
    # Prompt for a line of input
    ################################################## 
    def _prompt_for_line(self, verb):
        return input(f"Please provide a {verb}: ")

    ##################################################
    # INTERACT :: PROMPT FOR ID
    # Prompt for a message ID
    ################################################## 
    def _prompt_for_id(self, verb):
        return int(input(f"Select the message ID to {verb}: "))

    ##################################################
    # INTERACT :: AUTHENTICATE
    # Authenticate the user: find their control level
    ################################################## 
    def _authenticate(self, username, password):
        id_ = self._id_from_user(username)
        return ID_INVALID != id_ and password == users[id_].password

    ##################################################
    # INTERACT :: ID FROM USER
    # Find the ID of a given user
    ################################################## 
    def _id_from_user(self, username):
        for id_user in range(len(users)):
            if username == users[id_user].name:
                return id_user
        return ID_INVALID

#####################################################
# INTERACT :: DISPLAY USERS
# Display the set of users in the system
#####################################################
def display_users():
    for user in users:
        print(f"\t{user.name}")
