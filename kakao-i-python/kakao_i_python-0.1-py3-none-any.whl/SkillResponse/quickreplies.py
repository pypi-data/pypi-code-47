#Make quickreply entry
def createreplyentries():
    return []

#Make a quickreply button
def createquickreply(label, action, messageText, blockid=None):
    response = {}
    response["label"] = label
    if action == "message":
        response["action"] = action
    elif action == "block":
        if blockid:
            response["action"] = action
            response["blockId"] = blockid
        else:
            print("action : block need blockid!")
            return
    else:
        print("action for quickreply button should be message or block")
        return
    response["messageText"] = messageText
    return response

#Add a quickreply button to entry
def addquickreply(entry, quickreply):
    entry.append(quickreply)
    return entry