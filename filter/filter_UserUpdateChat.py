def chats_users(c):
    name = c.new_chat_member
    if name.status == "member":
	    return True
    elif name.status == "kicked":
	    return True
    elif name.status == "banned":
	    return True
    elif name.status not in ["member", 'administrator',"owner", "creator"]:
	    return True