from ICO3Utilities.ICO3TokenizerParam import ICO3TokenizerParam, ICO3TokenItem


class ICO3NodeWayProcessor:

    @staticmethod
    def process(xString):
        if xString is None:
            return None
        XR = ICO3TokenizerParam.processString(xString, ['>', ':'])
        BTagIdx = -1
        ETagIdx = -1
        Xidx = 0
        for Ti in XR:
            if Ti is not None:
                if BTagIdx < 0:
                    if Ti.TokenValue == ">":
                        BTagIdx = Xidx
                if ETagIdx < 0:
                    if Ti.TokenValue == ":":
                        ETagIdx = Xidx
            Xidx +=1

        if BTagIdx < 1:
            return None
        if ETagIdx < 1:
            return None
        if ETagIdx < BTagIdx:
            return None

        xx = XR[3:]
        BL = XR[0:BTagIdx+1]
        Ante = ICO3TokenItem()
        Ante.TokenValue = ICO3TokenizerParam.getString(BL)
        Ante.TokenType = "POST"
        W = XR[BTagIdx +1: ETagIdx]
        EL = XR[ETagIdx :]
        Post = ICO3TokenItem()
        Post.TokenValue = ICO3TokenizerParam.getString(EL)
        Post.TokenType = "POST"
        WS = ICO3TokenizerParam.getString(W)

        XWW = ICO3TokenizerParam.processString(WS, ['/'])
        XWW.insert(0, Ante)
        XWW.append(Post)
        return XWW