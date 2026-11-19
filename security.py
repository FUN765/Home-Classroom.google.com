
import re

# =====================================
# REILLY.AI SECURITY SYSTEM
# =====================================

class ReillyAISecurity:

    def __init__(self):
        self.inappropriate_words = [
            "badword1",
            "badword2",
            "badword3"
        ]

        self.blocked_messages = 0

    # Check every message
    def check_message(self, message):

        # 1. Detect phone numbers
        phone_pattern = (
            r'(?<!\d)(?:\+?1[-.\s]?)?'
            r'(?:\(?\d{3}\)?[-.\s]?)'
            r'\d{3}[-.\s]?\d{4}(?!\d)'
        )

        if re.search(phone_pattern, message):
            return self.block("Phone number detected")

        # 2. Detect possible full names
        name_pattern = (
            r'\b[A-Z][a-z]{1,20}\s+'
            r'[A-Z][a-z]{1,20}\b'
        )

        if re.search(name_pattern, message):
            return self.block("Possible full name detected")

        # 3. Detect inappropriate language
        words = re.findall(r'\b\w+\b', message.lower())

        for word in words:
            if word in self.inappropriate_words:
                return self.block("Inappropriate content detected")

        # Message is approved
        return {
            "approved": True,
            "deleted": False,
            "reason": "Message approved"
        }

    # Block message
    def block(self, reason):

        self.blocked_messages += 1

        return {
            "approved": False,
            "deleted": True,
            "reason": reason
        }


# =====================================
# REILLY.AI MESSAGE PROCESSOR
# =====================================

security = ReillyAISecurity()


def process_message(message):

    result = security.check_message(message)

    if result["approved"]:

        print("Reilly.AI: Message approved.")
        return message

    else:

        print("\n🛡️ REILLY.AI SECURITY ALERT")
        print("Reason:", result["reason"])
        print("Message blocked and discarded.")

        return None


# =====================================
# TEST THE SECURITY SYSTEM
# =====================================

if __name__ == "__main__":

    print("================================")
    print("       REILLY.AI SECURITY")
    print("================================")
    print("Security Status: ACTIVE")
    print("Phone Detection: ON")
    print("Full Name Detection: ON")
    print("Content Filtering: ON")
    print("================================")

    while True:

        message = input("\nEnter message: ")

        if message.lower() == "exit":
            break

        safe_message = process_message(message)

        if safe_message is not None:
            print("Approved:", safe_message)

    print("\n================================")
    print("REILLY.AI SECURITY REPORT")
    print("Blocked messages:",
          security.blocked_messages)
    print("Security System: OFFLINE")
    print("================================")
