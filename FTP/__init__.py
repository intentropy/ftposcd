#!/usr/bin/python3
"""
Fishman Tripleplay MIDI to OSC converter
    ftp package __init__

    Written By:
        Shane Hutter

        This contains shared CONSTANTS and functions for modules packaged in FTP
"""

from sys    import (
        platform    , version_info  ,
        )
from os     import (
        environ , uname ,
        )


ZERO    , ONE   = 0 , 1

MAXIMUM_SIGNED_BYTE   = 127

INPUT   , OUTPUT    = "input"   , "output"

# Global Indices
INDICES = {
        "only"  : ZERO  ,
        "first" : ZERO  ,
        }

# Replace these by assigning:
# for x in enumerate( y ):
#   iterate , value = x
ENUMERATE_ITERATE_INDEX = ZERO
ENUMERATE_VALUE_INDEX   = ONE

HEX_NOTATION    = "0x"

WITH_ITEM   = "{expression} as {target},"


## Program details
PROG    = {}
PROG_NAME           = "ftposcd"
PROG_VERSION        = "0.0.2"
PROG_AUTHOR         = "Shane Hutter"
PROG_AUTHOR_EMAIL   = "shane@intentropycs.com"
PROG_DESC           = """This software connects to the Fishman Triple Play USB MIDI
receiver and converts the MIDI data into Open Sound Control data, which is then sent to a
designated host.  This software will also recieve certain OSC messages, convert the message
into MIDI data, and send it into the Fishman Triple Play allowing for some control of the device"""
PROG_PACKAGES       = [ "FTP" , ]
PROG_EXECUTABLES    = [ 
        "ftposcd"       ,
        "ftposc2midi"   ,
        ]


## System Constants
HOSTNAME            = uname().nodename
PLATFORM            = platform
ROOT_FS             = "/"
PREFERED_PATHS      = (
        "/usr/bin"          ,
        "/usr/local/bin"    ,
        "/bin"              ,
        )
PATH_DELIMITER      = ":"
PATHS   = tuple(
        environ[ "PATH" ].split( PATH_DELIMITER )
        )
# Determine system path
PATH    = None
for path in PATHS:
    if path in PREFERED_PATHS:
        PATH    = path
        break
if not PATH:
    PATH    = PATHS[ FIRST_INDEX ]

# Systemd
SYSTEMD = {}
SYSTEMD_UNIT_DIR        = "/usr/lib/systemd/system"
SYSTEMD_SERVICE_UNIT    = "ftposcd.service"

# RegEx
REGEX   = {
        "only-numbers"  : "^[0-9]*$"    ,
        }

# Fishman Tripleplay specific
FTP = {}
MIDI_PICKUP_NAME    = "tripleplay"


LATENCY = .001
