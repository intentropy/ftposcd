#!/usr/bin/env python
"""
Fishman Tripleplay MIDI to OSC converter
    FTP.config

    Written By:
        Shane Hutter

    Description:
        This file contains modules for loading and returning data from the configuration file.
"""

from .  import (
        ZERO    ,
        REGEX   ,
        )
from re import match


# CONSTANTS
CONFIG_DIR  = "/etc"
CONFIG_FILE = "ftposcd.conf"

CONFIG  = {
        "dir"       : "/etc"            ,
        "file"      : "ftposcd.conf"    ,
        "comment"   : "#"               ,
        "INDEX"     : {
            "non-comment"   : ZERO  ,
            }                           ,
        }

config_data = {
        "remote-osc-host"   : str() ,
        "remote-osc-port"   : int() ,
        "local-osc-port"    : int() ,
        "local-cac-port"    : int() ,
        }



def load_config():
    """
        Load data out of the configuration file
    """

    with open( 
            "{dir}/{file}".format( **CONFIG )   , "r"   ,
            ) as config_file:
        config_lines    = list()
        for line in config_file.read().split( "\n" ):
            line_data = line.split(
                    CONFIG[ "comment" ]
                    )[
                            CONFIG[ "INDEX" ][ "non-comment" ]
                            ]
            if line_data:
                # Attempt to read the property and value from the line
                try:
                    config_property , config_value  = line_data.split()
                except:
                    # Ignore unreadable lines (better to error log)
                    pass
                
                if config_property in config_data:
                    # Store the value in the data dictionary, only if already present
                    if match( 
                            REGEX[ "only-numbers" ] ,
                            config_value            ,
                            ):
                        # Convert value to integer, because it is only numeric
                        config_value    = int( config_value )
                    config_data.update( 
                            { config_property : config_value }
                            )
    return config_data
