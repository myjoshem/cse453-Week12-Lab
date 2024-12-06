########################################################################
# COMPONENT:
#    MESSAGES
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary: 
#    This class stores the notion of a collection of messages
########################################################################

import message
from control import Control

##################################################
# MESSAGES
# The collection of high-tech messages
##################################################
class Messages:

    ##################################################
    # MESSAGES CONSTRUCTOR
    # Read a file to fill the messages
    ##################################################
    def __init__(self, filename):
        self._messages = []
        self._read_messages(filename)

    ##################################################
    # MESSAGES :: DISPLAY
    # Display the list of messages
    ################################################## 
    def display(self, user_level):
        """Display the list of messages the user has read privileges for."""
        print("Messages you have access to:")
        has_access = False  # Flag to track if any messages are accessible
        for m in self._messages:
            # Check if the user has read access to the message
            if Control.has_read_privileges(user_level, Control.SECURITY_LEVELS[m._text_control]):
                m.display_properties()  # Display the message's metadata (ID, author, date, security level)
                has_access = True

        if not has_access:
            print("No messages available at your clearance level.")
        print()  # Add an empty line for better formatting

    ##################################################
    # MESSAGES :: SHOW
    # Show a single message
    ################################################## 
    def show(self, id_, user_level):
        """Show a single message if the user has read privileges."""
        for m in self._messages:
            if m.get_id() == id_:
                # Check read access
                if not Control.has_read_privileges(user_level, Control.SECURITY_LEVELS[m._text_control]):
                    return "ACCESS_DENIED"
                m.display_text()
                return "SUCCESS"
        return "NOT_FOUND"

    ##################################################
    # MESSAGES :: UPDATE
    # Update a single message
    ################################################## 
    def update(self, id_, new_text, user_level):
        """Update a message if the user has write privileges."""
        for m in self._messages:
            if m.get_id() == id_:
                # Check write access
                if not Control.has_write_privileges(user_level, Control.SECURITY_LEVELS[m._text_control]):
                    return "ACCESS_DENIED"
                m.update_text(new_text)
                return "SUCCESS"
        return "NOT_FOUND"

    ##################################################
    # MESSAGES :: REMOVE
    # Remove a single message
    ################################################## 
    def remove(self, id_, user_level):
        """Remove a single message if the user has write privileges."""
        for m in self._messages:
            if m.get_id() == id_:
                # Check write access
                if not Control.has_write_privileges(user_level, Control.SECURITY_LEVELS[m._text_control]):
                    return "ACCESS_DENIED"
                self._messages.remove(m)  # Fully remove the message instead of clearing it
                return "SUCCESS"
        return "NOT_FOUND"

    ##################################################
    # MESSAGES :: ADD
    # Add a new message
    ################################################## 
    def add(self, text_control, text, author, date):
        """Add a new message with a security level."""
        message_level = Control.SECURITY_LEVELS[text_control]
        if not Control.has_write_privileges(Control.get_user_security_level(author), message_level):
            print("ACCESS DENIED: You do not have sufficient clearance to create this message.")
            return "ACCESS_DENIED"
        m = message.Message(text_control, text, author, date)
        self._messages.append(m)
        return "SUCCESS"

    ##################################################
    # MESSAGES :: READ MESSAGES
    # Read messages from a file
    ################################################## 
    def _read_messages(self, filename):
        try:
            with open(filename, "r") as f:
                for line in f:
                    try:
                        text_control, author, date, text = line.split('|')
                        self.add(text_control, text.rstrip('\r\n'), author, date)
                    except ValueError:
                        print(f"ERROR: Malformed line in {filename}: {line}")
        except FileNotFoundError:
            print(f"ERROR! Unable to open file \"{filename}\"")
