#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import cv2
import random
from clipboard import copy, paste

from urllib.request import urlopen, urlretrieve
from appdirs import user_cache_dir



def getUrl(event: str, x: int, y: int, flags: str, param: list ) -> None:
    if (event == 1):
        if (not param[1]):
            copy(param[0]);
            print("\nUrl copyed in your clipboard.")
        else:
            print("Url already in clipboard")




def playVideo(url: str) -> None:
    assert url is not None, "Some error in parsing the link :-("
    isCopied = False

    clip = cv2.VideoCapture(url)

    while (clip.isOpened()):
        rval, frame = clip.read()

        if rval:
            cv2.imshow('nice', frame)
            cv2.setMouseCallback('nice', getUrl, param=[url, isCopied])
            if (paste() == url):
                isCopied = True
            
        else:
            clip.set(cv2.CAP_PROP_POS_FRAMES, 0)

        if cv2.waitKey(40) & 0xFF == ord('q'):
            break

    clip.release()
    cv2.destroyAllWindows()


def main() -> None:

    data = json.loads(urlopen("https://api.giphy.com/v1/gifs/random?api_key=eEh43rHOfGpgGK5Y6wQxxxXy5Ypu3PwB&tag=&rating=G").read())
    vidUrl = data['data']['images']['looping']['mp4']

    del data

    print('Press \'q\' to quit')
    print('Click if you want to copy the link ;)')
    playVideo(vidUrl)


if __name__ == "__main__":
    main()
