from message import Message
from messages import Messages
from interact import Interact

class TestMethods:
    def __init__(self, messages):
        self.messages = messages

    def test_show_message_allowed(self):
        print("\nRunning: test_show_message_allowed")
        interact = Interact("CaptainCharlie", "password", self.messages)
        result = interact._p_messages.show(1, 2)  # Show message ID 1 for Privileged user
        if result == "SUCCESS":
            print("PASS: User can show the message they have access to.")
        else:
            print("FAIL: User could not show the message they have access to.")

    def test_show_message_denied(self):
        print("\nRunning: test_show_message_denied")
        interact = Interact("SeamanSam", "password", self.messages)
        result = interact._p_messages.show(3, 1)  # Show message ID 3 for Confidential user
        if result == "ACCESS_DENIED":
            print("PASS: User cannot show a message above their clearance.")
        else:
            print("FAIL: User incorrectly accessed a restricted message.")

    def test_remove_message_allowed(self):
        print("\nRunning: test_remove_message_allowed")
        interact = Interact("CaptainCharlie", "password", self.messages)
        result = interact._p_messages.remove(2, 2)  # Remove message ID 2 for Privileged user
        if result == "SUCCESS":
            print("PASS: User successfully removed the message they have access to.")
        else:
            print("FAIL: User failed to remove the message they have access to.")

    def test_remove_message_denied(self):
        print("\nRunning: test_remove_message_denied")
        interact = Interact("SeamanSam", "password", self.messages)
        result = interact._p_messages.remove(3, 1)  # Remove message ID 3 for Confidential user
        if result == "ACCESS_DENIED":
            print("PASS: User cannot remove a message above their clearance.")
        else:
            print("FAIL: User incorrectly removed a restricted message.")

    def run_all_tests(self):
        print("\nStarting Tests...")
        self.test_show_message_allowed()
        self.test_show_message_denied()
        self.test_remove_message_allowed()
        self.test_remove_message_denied()
        print("\nAll tests completed.\n")
