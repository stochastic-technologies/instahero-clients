import time
import urllib
import urllib2


class Tracker(object):
    """
    Track events on Instahero.

    Usage:

    import instahero
    tracker = instahero.Tracker("your api key")
    tracker.track("event_name", {"property": "dict"})
    """
    def __init__(self, api_key):
        self._api_key = api_key

    def track(self, event_name, data):
        if "_t" not in data:
            data["_t"] = str(int(time.time()))

        data["_k"] = self._api_key
        data["_n"] = event_name

        urllib2.urlopen("http://track.instahero.com/api/track/?%s" % urllib.urlencode(data), timeout=10)

    def track_multiple(self, events):
        import json
        encoded_events = urllib.urlencode({"data": json.dumps(events)})
        request = urllib2.Request("http://track.instahero.com/api/track_multiple/?_k=%s" % self._api_key, encoded_events)
        response = urllib2.urlopen(request, timeout=10)
        response.read()
