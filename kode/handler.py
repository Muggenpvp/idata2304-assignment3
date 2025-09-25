def handle_command(tv, command):

    parts = command.strip().split(" ", 1)
    if not parts:
        return "Error: No command received"
    cmd = parts[0].lower()

    if len(parts) > 1:
        args = parts[1]
    else:
        args = ""
    
    if cmd == "on":
        if tv.is_on() == True:
            return "TV is already turned on"
        tv.turn_on()
        return "TV turned on"
    
    elif cmd == "off":
        if tv.is_on() == False:
            return "TV is already turned off"
        tv.turn_off()
        
    elif cmd == "help":
        return (
            "Supported commands:\n"
            "-on\n"
            "-off\n"
            "-help\n"
        )
    
    else:
        return "Error: Unkown command"