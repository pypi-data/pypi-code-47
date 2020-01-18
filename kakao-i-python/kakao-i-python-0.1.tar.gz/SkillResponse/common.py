# Make common answer json
def common():
    response = {}
    response["version"] = "2.0"
    response["template"] = {}
    return response

#Make thumbnail
def thumbnail(imageurl, link=None, fixedratio=None, width=None, height=None):
    response = {}
    response["imageurl"] = imageurl
    if link:
        response["link"] = link
    if fixedratio and width and height:
        response["fixedratio"] = True
        response["width"] = width
        response["height"] = height
    return response

#Make button
def button(label, action, webLinkUrl=None, osLink=None, messageText=None, phoneNumber=None, blockId=None, extra=None):
    response = {}
    response["label"] = label
    if action in ["webLink", "osLink", "message", "block", "phone"]:
        response["action"] = action
    else:
        return
    if action == "webLink" and webLinkUrl:
        response["webLinkUrl"] = webLinkUrl
    elif action == "osLink" and osLink:
        response["osLink"] = osLink
    elif action == ["message"] and messageText:
        response["messageText"] = messageText
    elif response == "block" and messageText and blockId:
        response["messageText"] = messageText
        response["blockId"] = blockId
    elif action == "phone" and phoneNumber:
        response["phoneNumber"] = phoneNumber

#Make link
def link(mobile=None, ios=None, android=None, pc=None, mac=None, win=None, web=None):
    response = {}
    if mobile:
        response["mobile"] = mobile
    if ios:
        response["ios"] = ios
    if android:
        response["android"] = android
    if pc:
        response["pc"] = pc
    if mac:
        response['mac'] = mac
    if win:
        response["win"] = win
    if web:
        response["web"] = web
    return response

#Make carosel header
def caroselheader(title, description=None, thumbnailurl=None):
    response = {}
    response["title"] = title
    if description:
        response["description"] = description
    
    if thumbnailurl:
        response["thumbnail"] = {}
        response["thumbnail"]["imageUrl"] = thumbnailurl

    return response

#Make profile
def profile(nickname, imageurl=None):
    response = {}
    response["nickname"] = nickname
    if imageurl:
        response["imageUrl"] = imageurl
    return response