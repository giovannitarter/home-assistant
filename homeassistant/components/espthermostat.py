from homeassistant.components.discovery import load_platform
from homeassistant.loader import get_component
from homeassistant.helpers import discovery as hldisco

DOMAIN = 'espthermostat'

def setup(hass, config):
    """Your controller/hub specific code."""
    discovery = get_component('discovery')

    def espthermostat_discovered(service, info):
      
        hostname = info[0]
        hostname = hostname.replace(".local.", "")
        deviceid = hostname 
        devicename = deviceid[-4:].upper()
        
        load_platform(hass, 'switch', DOMAIN, {
            "deviceid" : deviceid,
            "switchnr" : "0",
            "name" : devicename,
            })
        
        load_platform(hass, 'switch', DOMAIN, {
            "deviceid" : deviceid,
            "switchnr" : "1",
            "name" : devicename,
            })
        
        load_platform(hass, 'sensor', DOMAIN, {
            "deviceid" : deviceid,
            "type" : "humidity",
            "name" : devicename,
            })
        
        load_platform(hass, 'sensor', DOMAIN, {
            "deviceid" : deviceid,
            "type" : "temperature",
            "name" : devicename,
            })
        
        load_platform(hass, 'climate', DOMAIN, {
            "name" : devicename,
            "deviceid" : deviceid,
            })

    
    hldisco.listen(
            hass, 
            discovery.ESP_THERMOSTAT, 
            espthermostat_discovered)
    
    return True

