class Message():
    def __init__(self, content, replyTo=None, messageType="normal"):
        self.content = content
        self.replyTo = replyTo
        self.messageType = messageType