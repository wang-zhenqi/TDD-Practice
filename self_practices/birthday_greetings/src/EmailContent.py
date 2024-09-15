class EmailContent:
    def __init__(self, sender, recipient, subject, body):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body

    def __eq__(self, other):
        return self.sender == other.sender and self.recipient == other.recipient and self.subject == other.subject and self.body == other.body