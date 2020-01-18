from SkillResponse.common import common
# Make simple text(text only) answer json
def simpleText(text):
    response = common()
    output = {}
    output["simpleText"] = {"text" : text}
    return response

# Make simple image(image only) answer json
def simpleImage(imagelink, alttext):
    response = common()
    output = {}
    output["simpleImage"] = {"imageUrl" : imagelink, "altText" : alttext}
    response["template"]["outputs"] = [output]
    return response

# Make basic card(text + image) answer json
def basicCard(title=None, description=None, thumbnail=None, buttons=None):
    response = common()
    output = {}
    if title:
        output["title"] = title
    if description:
        output["description"] = description
    if thumbnail:
        output["thumbnail"] = thumbnail
    if buttons:
        output["buttons"] = buttons
    if output != {}:
        return response

# Make commerse card(text + image + price) answer json
def commersecard(description, price, discount=None, discountRate=None, discountedPrice=None, thumbnail=None, profile=None, buttons=None):
    response = {}
    response["description"] = description
    response["price"] = price
    response["currency"] = "won"
    if discountRate and discountedPrice:
        response["discountRate"] = discountRate
        response["discountedPrice"] = discountedPrice
    if discount and not discountRate:
        response["discount"] = discount
    if thumbnail:
        response["thumbnails"] = [thumbnail]
    if profile:
        response["profile"] = profile
    if buttons and len(buttons) > 0 and len(buttons) < 4:
        response["buttons"] = buttons
    return response

# Make card list
def listcardheader(title, imageUrl=None):
    header = {}
    header["title"] = title
    if imageUrl:
        header["imageUrl"] = imageUrl
    return header

def listcarditem(title, description=None, imageUrl=None, link=None):
    item = {}
    item["title"] = title
    if description:
        item["description"] = description
    if imageUrl:
        item["imageUrl"] = imageUrl
    if link:
        item["link"] = link
    return item

def listcard(header, items):
    response = {}
    response["header"] = header
    response["items"] = items
    return response

# Make carousel list
def carousel(cardtype, items, header=None):
    response = {}
    if cardtype == "basicCard":
        response["type"] = cardtype
        response["items"] = items
    elif cardtype == "commerceCard":
        response["type"] = cardtype
        response["items"] = items
        if header:
            response["header"] = header
    else:
        return
    return response