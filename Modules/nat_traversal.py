# Modules/nat_traversal.py

import miniupnpc
import socket

def open_port(port):
    upnp = miniupnpc.UPnP()
    upnp.discoverdelay = 200
    upnp.discover()
    upnp.selectigd()
    external_ip = upnp.externalipaddress()
    upnp.addportmapping(port, 'TCP', upnp.lanaddr, port, 'Benevolent Wormhole', '')
    return external_ip

def close_port(port):
    upnp = miniupnpc.UPnP()
    upnp.discoverdelay = 200
    upnp.discover()
    upnp.selectigd()
    upnp.deleteportmapping(port, 'TCP')
