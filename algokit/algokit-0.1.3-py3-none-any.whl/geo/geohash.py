base32 = "0123456789bcdefghjkmnpqrstuvwxyz"


def getGeohash(bits, longitude, latitude):
    """
    :param bits: the bits of geohash
    :param longitude: longitude of the location
    :param latitude: latitude of the location
    :return: the geohash that the location in, and the box of the geohash area
    get the geohash in bits of the location
    """
    print('getGeohash({0},{1},{2})'.format(bits, longitude, latitude))

    latlen = bits * 5 // 2
    lonlen = latlen if bits % 2 == 0 else latlen + 1

    lonBits, left, right = toBinary(-180.0, 180.0, longitude, lonlen)
    latBits, bottom, top = toBinary(-90.0, 90.0, latitude, latlen)

    theBits = ""
    for i in range(latlen):
        theBits += lonBits[i]
        theBits += latBits[i]
    if lonlen > latlen:
        theBits += lonBits[-1]

    i = 0
    theGeohash = ""
    while i < len(theBits):
        c = base32[int(theBits[i:i + 5], 2)]
        theGeohash += c
        i += 5

    return theGeohash, (left, right, bottom, top)


def toBinary(lower, upper, value, length):
    low = lower
    upp = upper
    s = ''
    while len(s) < length:
        mid = (low + upp) / 2
        if value < mid:
            s += '0'
            upp = mid
        else:
            s += '1'
            low = mid
    return s, low, upp


def fishnet(bits, minlonLimit=-180, maxlonLimit=180, minlatLimit=-90, maxlatLimit=90):
    '''
    get geohash grids that intersect with the rectangle
    :param bits:
    :param minlonLimit:
    :param maxlonLimit:
    :param minlatLimit:
    :param maxlatLimit:
    :return:
    '''
    latlen = bits * 5 // 2
    lonlen = latlen if bits % 2 == 0 else latlen + 1

    lonSplit = sorted(list(_split(-180.0, 180.0, 0, lonlen, minlonLimit, maxlonLimit)))
    latSplit = sorted(list(_split(-90.0, 90.0, 0, latlen, minlatLimit, maxlatLimit)))

    return lonSplit, latSplit


def _split(lower, upper, theLen, maxLen, lowerLimit, upperLimit):
    # print lower,upper,theLen,maxLen

    if upper < lowerLimit or lower > upperLimit:
        return set()

    if theLen < maxLen:
        mid = (lower + upper) / 2
        theSet = set()
        theSet.update(_split(lower, mid, theLen + 1, maxLen, lowerLimit, upperLimit))
        theSet.update(_split(mid, upper, theLen + 1, maxLen, lowerLimit, upperLimit))
        return theSet
    else:
        return {lower, upper}


def fastFishnet(bits, minlon=-180, maxlon=180, minlat=-90, maxlat=90):
    '''
    the fast version of fishnet
    :param bits:
    :param minlon:
    :param maxlon:
    :param minlat:
    :param maxlat:
    :return:
    '''
    print("fastFishnet({0},{1},{2},{3},{4})".format(bits, minlon, maxlon, minlat, maxlat))

    lowbox = getGeohash(bits, minlon, minlat)[1]
    lonLowest = lowbox[0]
    latLowest = lowbox[2]
    lonStep = lowbox[1] - lowbox[0]
    latStep = lowbox[3] - lowbox[2]

    lonSplit = []
    latSplit = []

    theLon = lonLowest
    theLat = latLowest
    lonEnd = False
    latEnd = False
    while True:
        if not lonEnd:
            lonSplit.append(theLon)
            if theLon > maxlon: lonEnd = True
            theLon += lonStep

        if not latEnd:
            latSplit.append(theLat)
            if theLat > maxlat: latEnd = True
            theLat += latStep

        if lonEnd and latEnd:
            break

    return lonSplit, latSplit


def autoGeohashesByEvelope(numGrid=20, minlon=-180, maxlon=180, minlat=-90, maxlat=90):
    return geohashesByFishnet(*autoFishnet(numGrid, minlon, maxlon, minlat, maxlat))


def autoFishnet(numGrid=20, minlon=-180, maxlon=180, minlat=-90, maxlat=90):
    bits = 1
    while True:
        lonSplit, latSplit = fastFishnet(bits, minlon, maxlon, minlat, maxlat)
        if ((len(lonSplit) - 1) * (len(latSplit) - 1) >= numGrid):
            break
        bits += 1

    return bits, lonSplit, latSplit


def geohashesByFishnet(bits, lonSplit, latSplit):
    geohashes = []
    for ilon in range(len(lonSplit) - 1):
        for ilat in range(len(latSplit) - 1):
            centriod = ((lonSplit[ilon] + lonSplit[ilon + 1]) / 2, (latSplit[ilat] + latSplit[ilat + 1]) / 2)
            geohashes.append(getGeohash(bits, *centriod)[0])
    return sorted(geohashes)


def splitKeyByEnvelope(numSplit=20, minlon=-180, maxlon=180, minlat=-90, maxlat=90):
    '''
    For Hbase rowkey split
    :return:
    '''
    factor = 4
    geohashes = autoGeohashesByEvelope(numSplit * factor, minlon, maxlon, minlat, maxlat)
    splits = []
    numGeohash = len(geohashes)
    step = numGeohash // numSplit
    for i in range(0, len(geohashes), step):
        splits.append(geohashes[i])
    return splits[1:]


if __name__ == '__main__':
    # lonSplit,latSplit = fastFishnet(7,50,55,40,45)
    # print lonSplit
    # print latSplit
    print(splitKeyByEnvelope(20,115.433342,118.482667,27.803542,29.933930))
    pass
