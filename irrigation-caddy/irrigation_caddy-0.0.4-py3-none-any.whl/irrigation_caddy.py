from urllib.parse import urlencode
from urllib.request import Request, urlopen
class IrrigationCaddy:
    """Interface to the IrrigationCaddy device

    This class will work with the Irrigation Caddy ICETHS1. It will probably
    also work with the IC-W1 though this is untested.
    """

    def __init__(self, **kwargs):
        """
        Init with keywords.
         Parameters
         ----------
         kwargs: required
            * server: string, required
                The irrigation caddy device server name or IP address. If
                left unspecified, this will default to "irrigationcaddy.local"
                which may not actually work.

            * port: string or integer, optional
                The irrigation caddy server port, defaults to 80
        """
        self._server=kwargs["server"] or "irrigationcaddy.local"
        self._port=kwargs["port"] or "80"
    # end __init__

    def run_program(self, prog):
        """
        Run a program

        Runs a specified program on the Irrigation Caddy device specified in
        __init__(). This will return as soon as the program is sent to the
        device, not when the program runs to completion.

        Parameters
        ----------
        prog: doctionary, required
            The program to run; shaped like so:
            {
            "4 : "15",
            "1" : "10",
            "2" : "10",
            }
            Meaning: run zone 4 for 15 minutes, then zone 1 for 10 minutes,
            and finally zone 2 for 10 minutes. Currently, the durations must be
            less than 60 minutes.

        Returns
        -------
        boolean
            True on successful start of the irrigation program. False on failure.
        """
        uri = "http://{}:{}".format(self._server, self._port)
        post = {
            "pgmNum" : "4",
            "doProgram" : "1",
            "runNow" : "1"
        }
        for k, v in prog.items():
            post["z{}durMin".format(k)] = v
        request = Request(uri, data = urlencode(post).encode(), method = "POST")
        response = urlopen(request)
        return response.getcode() == 200
    # end run_program
# end class IrrigationCaddy
