# ftposcd
This software connects to the Fishman Triple Play USB MIDI receiver and converts the MIDI data into Open Sound Control data, which is then sent to a designated host.  This software will also recieve certain OSC messages, convert the message into MIDI data, and send it into the Fishman Triple Play allowing for some control of the device.



## Installation
### Required Dependencies
* Python >= 3.6
* python-mido
* python-rtmidi
* python-liblo

## Usage

### Configuration

### Controlling the Fishman Triple Play
Sending information into the Fishman Triple Play requires sending an OSC messages to ftposcd.  These messages are sent into the port configured as local-osc-port, which defaults to 9191.  

When sending messages the OSC path will have this format:
``/$HOSTNAME/tripleplay/input/$CHAN``
$HOSTNAME is the hostname of system in which ftposcd is running.  This can be determined by running ``echo $HOSTNAME`` on the system.
$FUNCTION is the function being passed as a command into the Fishman Triple Play.  For example, "poly", is a function used for toggeling The Triple Play's poly mode.

The following messages are accepted:
* /$HOSTNAME/tripleplay/input/poly
	* 1	: Put Fishman Triple Play into Poly Mode
	* 0	: Put Fishman Triple Play into Mono Mode
* /$HOSTNAME/tripleplay/input/mono
	* 1	: Put Fishman Triple Play into Mono Mode
	* 0	: Put Fishman Triple Play into Poly Mode

The following messages are in development:
* /$HOSTNAME/tripleplay/input/sustain
* /$HOSTNAME/tripleplay/input/pedal
* /$HOSTNAME/tripleplay/input/panic
