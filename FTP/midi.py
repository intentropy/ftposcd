#!/usr/bin/python3
"""
Fishman Tripleplay MIDI to OSC converter
    MIDI Module
        ftp.midi

    Written By:
        Shane Hutter

        A module for functions related to MIDI operations.
"""

from .      import (
        ENUMERATE_VALUE_INDEX   , ENUMERATE_ITERATE_INDEX   , HEX_NOTATION  ,
        MAXIMUM_SIGNED_BYTE     , ONE                       ,
        WITH_ITEM               , ZERO                      ,
        )
from mido   import (
        get_input_names , get_output_names  ,
        )


MIDI_TYPE_INDEX         = MIDI_DATA_KEY_INDEX  = FTP_FIRST_DEVICE_INDEX = ZERO
MIDI_DATA_VALUE_INDEX   = ONE

MIDI_FALSE              = ZERO
MIDI_TRUE               = MAXIMUM_SIGNED_BYTE

MIDI_DATA_DELIMITER     = "="
MIDI_TUPLE_LENGTH       = 4
FTP_MIDI_NAME           = "Fishman TriplePlay MIDI"


def ftp_inputs():
    """
        Return a dictionary of MIDI inputs for the for the Fishman TriplePlay

        Intputs are relative to this program, and will have notes sent into them
        from connected MIDI devices.
    """
   
    # Generate a list of only Tripleplay inputs
    ftp_inputs = list()
    for midi_input in get_input_names():
        if FTP_MIDI_NAME in midi_input:
            ftp_inputs.append( midi_input )

    return ftp_inputs


def ftp_outputs():
    """
        Return a list of MIDI outputs for the for the Fishman TriplePlay

        Outputs are relative to this program, and will have notes sent out of them
        and into MIDI devices.
    """
    
    # Generate a list of only Tripleplay outputs
    ftp_outputs = list()
    for midi_output in get_output_names():
        if FTP_MIDI_NAME in midi_output:
            ftp_outputs.append( midi_output )

    return tuple( ftp_outputs )



def midi_dict(  message ):
    """
        Convert a mido midi message into a dictionary.
        
        Split by whitespace
        Index 0 in the type MIDI_TYPE_INDEX
        all following indexes can be determined by splitting with =
            MIDI_DATA_DELIMITER = ="
            index 0 is the key MIDI_DATA_KEY_INDEX
            index 1 is the value MIDI_DATA_VALUE_INDEX
    """
    midi_data   = dict()

    for iterate , value in enumerate(
            str( message ).split()
            ):
        if iterate == MIDI_TYPE_INDEX:
            midi_data.update(
                    {
                        "type"  : value[ MIDI_TYPE_INDEX ]  ,
                        }
                    )
        else:
            midi_data.update(
                    {
                        value.split( MIDI_DATA_DELIMITER )[ MIDI_DATA_KEY_INDEX ]   :
                        value.split( MIDI_DATA_DELIMITER )[ MIDI_DATA_VALUE_INDEX ] ,
                        }
                    )
    return midi_data

def midi_tuple( message ):
    """
        Convert a mido midi message into a tuple of 4 integers.

        This is the format used to send an OSC Midi message

        message.bytes() will give a list of integer values
        If the final values are 0, then they will not be present in the list.
            You will need to pad the returned list with zeros so its len() == 4
            then return the list as a tuple
    """
    '''
        Does the midi tuple take the channel into account?
    '''

    # Convert message into a list
    midi_data  = message.bytes()
    # Pad the list with 0's so it is always has a length of 4 (and ot greater)
    if len( midi_data ) <= MIDI_TUPLE_LENGTH:
        for padding in range(
                len( midi_data )    ,
                MIDI_TUPLE_LENGTH   ,
                ):
            midi_data.append( ZERO )
    else:
        # Siliently log as a warning
        pass
    return tuple( midi_data )


def ftp_control():
    """
        Recieve a MIDI Tuple
    """


def ftp_mono_mode( *args ):
    """
        Send CC to FTP to place it in mono mode.

        Mono mode will allow for each string to be on a seperate midi
            channel when the FTP is in hardware mode.

        If True then send the cc for mono mode.
        If False then send the cc for poly mode.

        Any type as input, True and non-zero are True, everything else is False.
    """
    print( args )
    return


def ftp_poly_mode(
        poly    = True  ,
        ):
    """
        Send CC to FTP to place it in poly mode.

        Poly mode will send all strings out midi channel 0.

        If True then send the cc for poly mode.
        If False then send the cc for mono mode.

        Any type as input, True and non-zero are True, everything else is False.
    """
    return


def ftp_sustain():
    return


def ftp_pedal():
    return


'''
Notes on controlling the triple play:
    Controlling uses FTP

    Hold up when powering on to boot into hardware mode.

    In hardware mode you can send in midi data to change between poly and mono mode
        control_change, control=126, channel=0, value=64
            cc 126 is mono (6 strings), cc 127 in poly (all one channel)
            output to tp for controller changes is channel 0
            a value must be sent with these controller changes, 64 is arbitrary but
                I dont think it will work sending 0

    There is a whole rang of CCs that can be sent in.  Check FTP images in documents in 
        your home directory

    In hardware mode you should be able to save splits at fretts to preset options (win10 VM)
        save a preset splitting at each frett, starting with no split
            You shopuld be able to change the split on the fly by sending in the correct cc
        in mono mode, this should split the channels to
            0-5     before the split
            10-15   after the split

    All channels in Hardware mode (out from tp)
    Mono
        strings 0-5 (10-15)
        pedal   6
        FTP     7
    Poly
        strings 0
        pedal   1
        FTP     7

    FTP from the TP is intended for interal use, but could be used for what ever I want really
        seeing that I am writting this software to interace with the pickup, instead of officeial
        TP software. ;-)
'''


'''
MIDI Notes:
    Send a midi panic
        midi_out.panic()

    Non blocking iteration of incoming midi
        for message in midi_in.iter_pending()
            print( message)
'''
