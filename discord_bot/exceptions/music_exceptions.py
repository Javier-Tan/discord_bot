class BotNotInChannelException(Exception):
    def __init__(self):
        self.message = "Bot not in a channel currently"
        super().__init__(self.message)

class NotPlayingAudioException(Exception):
    def __init__(self):
        self.message = "Not playing any music currently"
        super().__init__(self.message)

class UserNotInChannelException(Exception):
    def __init__(self):
        self.message = "User not in a channel currently"
        super().__init__(self.message)