#!/usr/bin/env python
"""
Fishman Tripleplay MIDI to OSC converter
    ftposcd setup.py

    Written By:
        Shane Hutter
    
    Description:
        This is the setup.py for installing this software as a python package.
"""

from distutils.core     import setup
from FTP                import (
        PROG_NAME           , PROG_VERSION          , PROG_AUTHOR   ,
        PROG_AUTHOR_EMAIL   , PROG_DESC             , PROG_PACKAGES ,
        PATH                , 
        SYSTEMD_UNIT_DIR    , SYSTEMD_SERVICE_UNIT  ,
        )
from FTP.config         import (
        CONFIG_DIR  , CONFIG_FILE   ,
        )

setup(
        name                = PROG_NAME                         ,
        version             = PROG_VERSION                      ,
        author              = PROG_AUTHOR                       ,
        author_email        = PROG_AUTHOR_EMAIL                 ,
        description         = PROG_DESC                         ,
        long_description    = open( "README.md", "r" ).read()   ,
        license             = open( "LICENSE" , "r" ).read()    ,
        packages            = PROG_PACKAGES                     ,
        data_files          = [
            (
                PATH                ,   # Installed executable in systems $PATH
                [
                    PROG_NAME               ,
                    ]   ,
                )   ,
            ( 
                CONFIG_DIR          ,   # Configuration file
                [ 
                    CONFIG_FILE             ,   # ftposcd.conf
                    ]   ,
                )   ,
            (
                SYSTEMD_UNIT_DIR    ,   # Systemd service unit
                [
                    SYSTEMD_SERVICE_UNIT    ,
                    ]   ,
                )   ,
            ]   ,
        )

