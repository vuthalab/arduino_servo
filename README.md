# arduino_servo
A servo controller for locking a laser's frequency to an absorption signal

arduino_servo is a servo controller for locking lasers to an error signal produced by saturated absorption. It uses an Arduino Uno or ChipKit uc32 microcontroller along with the Digilent AnalogShield add-on board to computer and produce the correction signals based on a PI^2 algorithm. 
Features: Auto relocking sequence that detects when laser is out of lock, starts scanning the laser frequency to find the error signal and re-engages the servo when the laser is in the capture region of the lock.

Bandwidth: 2kHz for chipkit uc32, 700Hz for arduino uno. 
