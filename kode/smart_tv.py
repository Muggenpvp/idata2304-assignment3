class SmartTV():
    isTurnedOn = False
    selectedChannel = 1

    def __init__(self, amountOfChannels):
        self.amountOfChannels = amountOfChannels

    def isOn(self):
        return self.isTurnedOn
    
    def getAmountOfChannels(self):
        return self.amountOfChannels
    
    def setSelectedChannel(self, channel):
        if channel not in range(1,self.amountOfChannels):
            return f"Channel {channel} does not exist"

        self.selectedChannel = channel

    def getSelectedChannel(self):
        return self.selectedChannel