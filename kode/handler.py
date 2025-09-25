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
        
    elif cmd == "channel":
        if args == "amount":
            return f"There are {tv.get_amount_of_channels()} channels"
        elif args == "selected":
            return f"Channel {tv.get_selected_channel()} is currently selected"
        elif args == "up":
            return tv.set_selected_channel(tv.get_selected_channel() + 1)
        elif args == "down":
            return tv.set_selected_channel(tv.get_selected_channel() - 1)

    elif cmd == "help":
        return (
            "Supported commands:\n"
            "-on\n"
            "-off\n"
            "-channel amount\n"
            "-channel selected\n"
            "-channel up\n"
            "-channel down\n"
            "-help\n"
        )
    
    else:
        return "Error: Unkown command"