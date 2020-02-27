# Python_P2P-Chat

>**Parts of the program have been taken over by grakshith/p2p-chat-python and extended.**

The P2P chat is programmed in Python and is based on the client/server principle.

## Installation
To use this script, you have to install it's dependencies first. This can be done with the additional requirements file.
To do so, run the command "pip install -r requirements.txt" in the folder where the requirements.txt file is placed.

## Usage
1. After starting you will be asked for a hostname. Enter the target IP address or hostname here. 
2. After this entry follows the destination port (by default 8080).
3. After the server has connected to the one opposite, a success message is displayed. Now you can chat!

## Features
* End-to-End chat (Simply enter text and press Enter)
* Coinflip (with the codeword coinflip you can play a coin toss with the one opposite)
  * correct way to use coinflip:
    * Partner A -> Partner B: let us make a coinflip 
    * Partner B -> Partner A: Okey, let´s go!
    * A -> B: coinflip
    * B -> A: coinflip
    * A and B gets the output of the coinflip, otherwise there will be multiple errors!
  
### Informations
* The Code is self-explanatory commented

### Known Bugs
Unfortunately there are still some errors in this version. These as follows:

* if Partner A/B sends 'coinflip' and Partner B/A sends message, hash of coinflip will be interpreted as message and will be shown as message
  * connection errors
  * errors by building hashes
  * multiple errors can make thread-errors
  * in actual version no bugfix!
  * **!!! only solution until now**: both have to restart program and establish connection by new

* if Partner A/B connected but B/A isn´t, messages will be shown after one message back, all of them in one line.
  * **!!! temporarily solution**: wait until Partner A/B is connected

* if some Partner multiply type in 'coinflip' successively while in this time Partner B 'only' one time, multiple hashes will be used 
	* higher count of setted bits will be shown at both partners
	* Because only the number of setted bits will be interpreted as odd or even, this won't make the protocoll useless as well
	* **!!! temporarily solution**: type in coinflip only one time and wait for other partner 

* presentation errors because of using one window for client and server
* much more... :D

### The following is still being implemented
* GUI for Server and Client
* End-to-End Encryption
* Better Exception handling
* More functions
