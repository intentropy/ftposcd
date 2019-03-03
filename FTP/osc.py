#!/usr/bin/python3
"""
Fishman Tripleplay MIDI to OSC converter
    OSC Module
        ftp.osc

    Written By:
        Shane Hutter

        A module for functions related to OSC operations.
"""

from .      import (
        MIDI_PICKUP_NAME    , OUTPUT    ,
        )
from .midi  import (
        ftp_mono_mode   , ftp_pedal     , ftp_poly_mode , ftp_sustain   ,
        MIDI_FALSE      , MIDI_TRUE     ,
        )
from liblo  import (
        Address , AddressError  , Message       ,
        send    , ServerError   , ServerThread  ,
        )
from os     import uname
from sys    import exit


FTP_POLY_PATH       = "poly"
FTP_MONO_PATH       = "mono"
FTP_SUSTAIN_PATH    = "sustain"
FTP_PEDAL_PATH      = "pedal"
FTP_MIDI_PANIC_PATH = "panic"

OSC_TYPETAGS    = {
        "midi"      : "m"       ,
        "int32"	    : "i"	,
        "int64"     : "h"	,
        "float"     : "f"	,
        "double"    : "d"	,
        "char"      : "c"	,
        "string"    : "s"	,
        "symbol"    : "S"	,
        "timetag"   : "t"       ,
        "true"	    : "T"       ,
        "false"	    : "F"       ,
        "nil"	    : "N"	,
        "infinitum" : "I"	,
        "blob"      : "b"	,
        "any"       : "*"       ,
        "none"      : None      ,
        }

OSC_PATH_TO_CC = {
        FTP_POLY_PATH       : 127   ,
        FTP_MONO_PATH       : 126   ,
        FTP_SUSTAIN_PATH    : 66    ,
        FTP_PEDAL_PATH      : 66    ,
        }


# OSC_PATH info
'''
    hostname is the systems host name, uname().nodename
    midi_pickup is the pickup name MIDI_PICKUP_NAME
    direction is relative the midi pickups perspective
        OUTPUT is data leaving the pickup
        INPUT is data entering the pickup
    
    channel refers to the midi channel of the message OUTPUT only


    INPUT is always channel 0, but specifies the cc command name, then provides
        the relevent value.
        format channel as the command sent to ftp
            i.e. mono, poly, pedal
'''
OSC_PATH = "/{hostname}/{midi_pickup}/{direction}/{channel}"



class OSCServer( ServerThread ):
    """
        Used to instatiate an Open Sound Control server.
        
        Inherits Server Thread from liblo, and adds an
            __enter__ and __exit__ method to allow for 
            use in a with statement.
        
        The server will automatically start upon intantiation


        ServerThread methods:
            add_bundle_handlers
            add_method
            del_method
            fileno
            free            free will destroy the object
            get_port
            get_protocol
            get_url
            register_methods
            send
            start
            stop
    """

    def __init__( 
            self    ,
            port    ,
            ):
        """
            Initialize the OSC Server
        """
        # Inherit port from parent class
        super().__init__( port )


    def __enter__( self ):
        """
            Start the OSC Server when entering with block
        """
        self.start()
        return self

    def close( self ):
        """
           Destroy, and clean up when destruction occurs.
        """
        self.stop()
        return self.free()


    def __exit__(
            self        ,
            *exception  ,
            ):
        """
            Destroy the object when leaving with block.
        """
        return self.close()




def osc_target(
        osc_target_ip   ,
        osc_target_port ,
        ):
    """
        Create an OSC Address object that targets an OSC server.

        This should only create one client, targeting one IP and one PORT.
        OSC Whispers has already been developed to forward to multiple OSC targets.
    """
    try:
        return Address(
                osc_target_ip   ,
                osc_target_port ,
                )
    except AddressError as error:
        # Log errors instead
        exit( error )



def send_osc_midi( 
        osc_target  ,
        osc_path    ,
        osc_midi    ,
        ):
    """
        Send an OSC Midi message.  This is a tuple of 4 ints.

        To explicitly send a MIDI message, the *args of the message must be (typetage, data )
            for midi this will be Message( path , ( 'm' ,  midi_tuple  ) )
    """
    return send(
            osc_target      ,
            Message(
                osc_path                    ,
                (
                    OSC_TYPETAGS[ "midi" ]  ,
                    osc_midi                ,
                    )
                )
            )


def register_ftp_osc_input( osc_server ):
    """
        This method registers all incoming osc messages to methods
        in ftp.midi with the osc_server as the instatiated OSCServer.

        These methods are for sending midi cc commands to the FTP.
    """

    '''
        CC messages for hardware mode:
           Poly Mode        127     non zero value
           Mono Mode        126     non zero value
           Sustain          66      if no pedal channel is defined then sustain
           Pedal Channel    66      
        
        add_method usage
            methods contains:
                path        this path associates the message with the method
                typespec    such as "m" for midi, as this is intended to send specific cc
                                messages to the pickup, 32bit ints "i" should be used
                function    the callback function
                user_data   a value always passed back when the message is recieved
                                default is none
                                may be useful for command and control
    '''
    # Poly and Mono mode
    '''
        Poly and mono mode are inverses of each other, and are ultimately boolean
            These methods should take any type, and if the value is either non-zero
            or True, then they should pass a 127 to the CC
    '''
    # Poly
    osc_server.add_method(
            OSC_PATH.format(
                hostname    = uname().nodename  ,
                midi_pickup = MIDI_PICKUP_NAME  ,
                direction   = OUTPUT            ,
                channel     = FTP_POLY_PATH     , 
                )                   ,
            OSC_TYPETAGS[ "any" ]   ,
            ftp_poly_mode           ,
            )
    # Mono
    osc_server.add_method(
            OSC_PATH.format(
                hostname    = uname().nodename  ,
                midi_pickup = MIDI_PICKUP_NAME  ,
                direction   = OUTPUT            ,
                channel     = FTP_MONO_PATH     , 
                )                   ,
            OSC_TYPETAGS[ "any" ]   ,
            ftp_mono_mode           ,
            )


    # Sustain and Pedal Channel
    '''
        Passing no pedal channel activate sustain.
            If this means passing a 0 to sustain, then how do you remove sustain?
                Will passing a 0 a second time deactivate the sustain?

        Passing a pedal channel with change to the channel
            Are these the preset banks?
                use for defining frettboard split point
            Does any non zero value count?

        Pass an int to either while this is being worked out.
    '''
    # Sustain
    osc_server.add_method(
            OSC_PATH.format(
                hostname    = uname().nodename  ,
                midi_pickup = MIDI_PICKUP_NAME  ,
                direction   = OUTPUT            ,
                channel     = FTP_SUSTAIN_PATH     , 
                )                   ,
            OSC_TYPETAGS[ "int32" ] ,
            ftp_sustain             ,
            )
    # Pedal
    osc_server.add_method(
            OSC_PATH.format(
                hostname    = uname().nodename  ,
                midi_pickup = MIDI_PICKUP_NAME  ,
                direction   = OUTPUT            ,
                channel     = FTP_PEDAL_PATH     , 
                )                   ,
            OSC_TYPETAGS[ "int32" ] ,
            ftp_pedal               ,
            )







    return



def register_coc_osc_input( osc_server ):
    """
        This method registers Command and Control methods for handeling
        OSC messages that are used to control ftposcd.
    """
    return
