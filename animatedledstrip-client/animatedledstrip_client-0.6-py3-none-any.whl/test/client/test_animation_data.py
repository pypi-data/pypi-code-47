#   Copyright (c) 2019-2020 AnimatedLEDStrip
#
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#   of this software and associated documentation files (the "Software"), to deal
#   in the Software without restriction, including without limitation the rights
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#   copies of the Software, and to permit persons to whom the Software is
#   furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in
#   all copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#   THE SOFTWARE.

from client.AnimationData import AnimationData
from client.Animation import *
from client.ColorContainer import ColorContainer
from client.Direction import *


def test_constructor():
    data = AnimationData()

    assert data.animation == Animation.COLOR
    assert data.center == -1
    assert data.continuous is None
    assert data.delay == -1
    assert data.delayMod == 1.0
    assert data.direction == Direction.FORWARD
    assert data.distance == -1
    assert data.endPixel == -1
    assert data.id == ""
    assert data.spacing == -1
    assert data.startPixel == 0


def test_animation():
    data = AnimationData()

    data.animation = Animation.SPARKLE
    assert data.animation == Animation.SPARKLE

    try:
        data.animation = 3
        data.json()
        raise AssertionError
    except ValueError:
        pass


def test_center():
    data = AnimationData()

    data.center = 5
    assert data.center == 5

    try:
        data.center = Direction.FORWARD
        data.json()
        raise AssertionError
    except ValueError:
        pass


def test_continuous():
    data = AnimationData()

    data.continuous = True
    assert data.continuous

    data.continuous = None
    assert data.continuous is None

    try:
        data.continuous = 5
        data.json()
        raise AssertionError
    except ValueError:
        pass


def test_delay():
    data = AnimationData()

    data.delay = 10
    assert data.delay == 10

    try:
        data.delay = Animation.BOUNCE
        data.json()
        raise AssertionError
    except ValueError:
        pass


def test_delaymod():
    data = AnimationData()

    data.delayMod = 0.5
    assert data.delayMod == 0.5

    try:
        data.delayMod = 3
        data.json()
        raise AssertionError
    except ValueError:
        pass


def test_direction():
    data = AnimationData()

    data.direction = Direction.BACKWARD
    assert data.direction == Direction.BACKWARD

    try:
        data.direction = 1
        data.json()
        raise AssertionError
    except ValueError:
        pass


def test_distance():
    data = AnimationData()

    data.distance = 5
    assert data.distance == 5

    try:
        data.distance = 5.0
        data.json()
        raise AssertionError
    except ValueError:
        pass


def test_endpixel():
    data = AnimationData()

    data.endPixel = 10
    assert data.endPixel == 10

    try:
        data.endPixel = 30.0
        data.json()
        raise AssertionError
    except ValueError:
        pass


def test_id():
    data = AnimationData()

    data.id = "TEST"
    assert data.id == "TEST"

    try:
        data.id = 5
        data.json()
        raise AssertionError
    except ValueError:
        pass


def test_spacing():
    data = AnimationData()

    data.spacing = 10
    assert data.spacing == 10

    try:
        data.spacing = 3.0
        data.json()
        raise AssertionError
    except ValueError:
        pass


def test_start_pixel():
    data = AnimationData()

    data.startPixel = 5
    assert data.startPixel == 5

    try:
        data.startPixel = 1.0
        data.json()
        raise AssertionError
    except ValueError:
        pass


def test_json():
    data = AnimationData()

    data.animation = Animation.METEOR
    data.center = 50
    data.continuous = False
    data.delay = 10
    data.delayMod = 1.5
    data.direction = Direction.BACKWARD
    data.distance = 45
    data.endPixel = 200
    data.id = "TEST"
    data.spacing = 5
    data.startPixel = 15

    cc = ColorContainer()
    cc.add_color(0xFF)
    cc.add_color(0xFF00)
    cc2 = ColorContainer()
    cc2.add_color(0xFF0000)
    data.add_color(cc)
    data.add_color(cc2)

    assert data.json() == "DATA:{\"animation\":\"METEOR\",\"colors\":[{\"colors\":[255, 65280]},{\"colors\":[" \
                          "16711680]}],\"center\":50,\"continuous\":False,\"delay\":10,\"delayMod\":1.5," \
                          "\"direction\":\"BACKWARD\",\"distance\":45,\"endPixel\":200,\"id\":\"TEST\",\"spacing\":5," \
                          "\"startPixel\":15}"


def test_json_no_cc():
    data = AnimationData()

    data.animation = Animation.METEOR
    data.center = 50
    data.continuous = False
    data.delay = 10
    data.delayMod = 1.5
    data.direction = Direction.BACKWARD
    data.distance = 45
    data.endPixel = 200
    data.id = "TEST"
    data.spacing = 5
    data.startPixel = 15

    assert data.json() == "DATA:{\"animation\":\"METEOR\",\"colors\":[],\"center\":50,\"continuous\":False," \
                          "\"delay\":10,\"delayMod\":1.5,\"direction\":\"BACKWARD\",\"distance\":45," \
                          "\"endPixel\":200,\"id\":\"TEST\",\"spacing\":5,\"startPixel\":15}"


def test_add_bad_color():
    data = AnimationData()

    try:
        data.add_color(-1)
        raise AssertionError
    except ValueError:
        pass

    data.colors = [-1]

    try:
        data.json()
        raise AssertionError
    except ValueError:
        pass
