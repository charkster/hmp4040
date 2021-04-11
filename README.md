# hmp4040
Rohde &amp; Schwarz HMP4040 Power Supply Python control

This python class implements a method called get_unique_scpi() which returns a list of scpi commands that are different to the *RST state of the instrument.

This class is not about hiding cryptic SCPI commands from the user as many other classes do... it is about querying the device with all SCPI commands and comparing that response against the RESET response in order to obtain a list of SCPI commands (and arguement) which define the present state of the instrument. This list can be used to restore the state of the instrument, and can be distributed as a file or embedded into an oscilloscope PNG screen capture.

SCPI is very portable and human readable. A settings file created by the instrument is not human readable and is relatively large in size (compared to a txt file that has a list of unique scpi commands with their arguements).
