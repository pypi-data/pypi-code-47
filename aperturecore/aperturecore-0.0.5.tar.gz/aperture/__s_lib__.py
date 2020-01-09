import importlib.util as imp


class modifiers:
    speed = 1
    pitch = 1
    volume = 100

    def __init__(self):
        pass


class _import:
    def __init__(self):
        self.a = None

    def ctp(name: str):
        try:
            ctp = open(name)

        except FileNotFoundError:
            raise FileNotFoundError
        finally:
            var = ctp.read()
            #print(var)  # Debugging
            p1, v1, s1 = 'pitch', 'volume', 'speed'
            d = var.replace(p1,"").replace(v1,"").replace(s1,"").replace(" ","").replace("\n","").split("=")

            #print(d)  # Debugging
            data = d
            v = data[1]
            p = data[2]
            s = data[3]
            try:
                g = data[4]
            except IndexError:
                pass
            out = {"volume": v, "pitch": p, "speed": s}

            return dict(out)
