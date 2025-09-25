class SmartTV():
    isTurnedOn = False
    selectedChannel = 1

    def __init__(self, amountOfChannels=5):
        self.amountOfChannels = amountOfChannels

    def is_on(self):
        return self.isTurnedOn
    
    def get_amount_of_channels(self):
        if self.isTurnedOn == True:
            return self.amountOfChannels
    
    def set_selected_channel(self, channel):
        if self.isTurnedOn == True:
            if channel not in range(1,self.amountOfChannels):
                return f"Channel {channel} does not exist"

            self.selectedChannel = channel
            return f"Selected channel {channel}"

    def get_selected_channel(self):
        if self.isTurnedOn == True:
            return self.selectedChannel
        
    def turn_on(self):
        self.isTurnedOn = True

    def turn_off(self):
        self.isTurnedOn = False