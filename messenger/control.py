########################################################################
# COMPONENT:
#    CONTROL
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary: 
#    This class stores the notion of Bell-LaPadula
########################################################################

# The Control class is responsible for enforcing Bell-LaPadula security rules.
# It contains security levels, user levels, and methods for access control.
class Control:
    # Security levels as a class-level attribute
    SECURITY_LEVELS = {
        "Public": 0,
        "Confidential": 1,
        "Privileged": 2,
        "Secret": 3
    }

    # User security levels as a class-level attribute
    USER_SECURITY_LEVELS = {
        "AdmiralAbe": SECURITY_LEVELS["Secret"],
        "CaptainCharlie": SECURITY_LEVELS["Privileged"],
        "SeamanSam": SECURITY_LEVELS["Confidential"],
        "SeamanSue": SECURITY_LEVELS["Confidential"],
        "SeamanSly": SECURITY_LEVELS["Confidential"],
    }

    DEFAULT_SECURITY_LEVEL = SECURITY_LEVELS["Public"]

    @staticmethod
    def get_user_security_level(username):
        """Retrieve the security level for a given user."""
        return Control.USER_SECURITY_LEVELS.get(username, Control.DEFAULT_SECURITY_LEVEL)

    @staticmethod
    def has_read_privileges(user_level, message_level):
        """Check if the user has read privileges (No Read Up)."""
        return user_level >= message_level

    @staticmethod
    def has_write_privileges(user_level, message_level):
        """Check if the user has write privileges (No Write Down)."""
        return user_level <= message_level
    
    @staticmethod
    def check_update_privileges(user_level, message_level):
        """
        Check if the user has privileges to update or delete a specific message.
        - User level must match the message level (no editing up or down).
        """
        # Prevent editing up or down (user level must match message level)
        if user_level != message_level:
            return "ACCESS_DENIED"
        return "SUCCESS"
