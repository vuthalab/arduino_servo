# arduino_servo

An arduino-based servo controller for locking a laser's frequency to an error signal

arduino_servo is a servo controller for locking lasers to an error signal produced by saturated absorption. It uses an Arduino Uno or ChipKit uc32 microcontroller along with the Digilent AnalogShield add-on board to computer and produce the correction signals based on a PI^2 algorithm. 
Features: Auto relocking sequence that detects when laser is out of lock, starts scanning the laser frequency to find the error signal and re-engages the servo when the laser is in the capture region of the lock.

Bandwidth: 2kHz for chipkit uc32, 700Hz for arduino uno. 

code/laser_frequency_servo contains code to use an arduino uno or chipkit uc32 to provide PI^2 feedback for locking a 780 nm laser to the Rb87 F=2 DAVLL signal.

code/rb_laser lock contains code to publish the error and correction signals from the serial port to a zeroMQ socket, as well as send serial commands to the Arduino from the command line. 
