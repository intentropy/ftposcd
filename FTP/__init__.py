#!/usr/bin/python3
"""
Fishman Tripleplay MIDI to OSC converter
    ftp package __init__

    Written By:
        Shane Hutter

        This contains shared CONSTANTS and functions for modules packaged in FTP
"""


ZERO    = 0
ONE     = 1

MAXIMUM_SIGNED_BYTE   = 127

INPUT   = "input"
OUTPUT  = "output"

ENUMERATE_ITERATE_INDEX = ZERO
ENUMERATE_VALUE_INDEX   = ONE

HEX_NOTATION    = "0x"

WITH_ITEM   = "{expression} as {target},"


## Program details
PROG_NAME           = "ftposcd"
PROG_VERSION        = "0.0.0"
PROG_AUTHOR         = "Shane Hutter"
PROG_AUTHOR_EMAIL   = "shane@intentropycs.com"
PROG_DESC           = """This software connects to the Fishman Triple Play USB MIDI
receiver and converts the MIDI data into Open Sound Control data, which is then sent to a
designated host.  This software will also recieve certain OSC messages, convert the message
into MIDI data, and send it into the Fishman Triple Play allowing for some control of the device"""
PROG_PACKAGES       = [ "FTP" , ]



## System Constants
PLATFORM            = platform
ROOT_FS             = "/"
PREFERED_PATHS      = (
        "/usr/bin"          ,
        "/usr/local/bin"    ,
        "/bin"              ,
        )
PATH_DELIMITER      = ":"
ENVIRONMENT_PATHS   = tuple(
        environ[ "PATH" ].split( PATH_DELIMITER )
        )
# Determine system path
PATH    = None
for path in PREFERED_PATHS:
    if path in ENVIRONMENT_PATHS:
        PATH    = path
        break
if not PATH:
    PATH    = ENVIRONMENT_PATHS[ FIRST_INDEX ]
# Systemd
SYSTEMD_UNIT_DIR        = "/usr/lib/systemd/system"
SYSTEMD_SERVICE_UNIT    = "ftposcd.service"



# Fishman Tripleplay specific
MIDI_PICKUP_NAME    = "tripleplay"
