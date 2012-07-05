import time
import urllib
import urllib2


class Tracker(object):
    """
    Track events on Instahero.

    Usage:

    import instahero
    tracker = instahero.Track("your api key")
    tracker.track("event_name", {"property": "dict"})
    """
    def __init__(self, api_key):
        self._api_key = api_key

    def track(self, event, data):
        if "_t" not in data:
            data["_t"] = str(int(time.time()))

        data["_k"] = self._api_key
        data["_n"] = event

        urllib2.urlopen("http://track.instahero.com/api/track/?%s" % urllib.urlencode(data), timeout=2)
