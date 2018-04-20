import requests
from hcloud.exceptions import MonitorError

class Monitor(object):
    
    @classmethod
    def reload(cls, url):
        reload_url = url + '/-/reload'
        r = requests.post(reload_url)
        if r.status_code != 200:
            msg = "Monitor reload failed."
            raise MonitorError(msg)
