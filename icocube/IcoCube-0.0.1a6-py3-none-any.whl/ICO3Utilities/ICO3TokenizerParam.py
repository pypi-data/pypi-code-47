
class ICO3TokenizerParam:

    #TokenSuite = None
    #separatorList = None
    @staticmethod
    def processString(xString, separatorList):
        if separatorList is None:
            return
        TokenList = []
        # PartialString = None
        if xString is None:
            return TokenList
        xToken = ICO3TokenItem()
        for char in xString:
            charProccessed = False
            for sep in separatorList:
                if char == sep:
                    if xToken.TokenValue is not None:
                        if len(xToken.TokenValue) > 0:
                            xToken.TokenType = "STRING"
                            TokenList.append(xToken)
                            xToken = ICO3TokenItem()
                            xToken.TokenValue = ""
                    xToken.TokenValue = str(char)
                    xToken.TokenType = "TOKEN"
                    TokenList.append(xToken)
                    xToken = ICO3TokenItem()
                    xToken.TokenValue = ""
                    charProccessed = True
                    break
            if not charProccessed:
                if xToken.TokenValue is None:
                    xToken.TokenValue = ""
                xToken.TokenValue += str(char)
        if xToken.TokenValue is None:
            xToken.TokenValue = ""

        if len(xToken.TokenValue) > 0:
            xToken.TokenType = "STRING"
            TokenList.append(xToken)
            xToken = ICO3TokenItem()
        return TokenList


    @staticmethod
    def getString(xTokenList):
        xString = ""
        for xT in xTokenList:
            if xT.TokenNew  is not None:
                xString += xT.TokenNew
            else:
                xString += xT.TokenValue
        return xString


class ICO3TokenItem:
    TokenValue = None
    TokenType = None
    TokenNew = None

