# ESP8266 Hydroponics
This is part of a little project to create a small hydroponics garden that can be placed in a window 
that uses flood drain style hydroponics 
The intention at this point is for the garden to be self contained and run from a solar charged 
battery pack, however providing for a hardwired version also especially during testing
Once a base system has been tested I will post a parts list and other design information up as part of this repo.
## Use cases
1. Small kitchen herb garden
2. Bedroom window flower garden
3. Office window plants

## Features
1. A small and self contained window garden
2. Easily accessable and easily cleaned reservoir
3. Overflow prevention
4. Use of cheap commodity parts
5. Either mains or solar/battery powered

## Requirements/Features
1. Must be able to cope with real time for scheduling etc
2. Must connect to a wifi network
3. Must be able to sense water level in both the reservoir and bed
4. Must be able to feedback via lcd
5. Can operate:
   1. a small pump
   2. a grow light
6. Can sense:
   1. battery voltage
   2. solar input voltage
   3. Solution conductivity
   4. solution ph
   5. light

## Parts list
1. ESP8266 Microcontroller
2. Water pump (get specs)
3. Clay beads

## Phasing
### MVP
Apply Dave's razor, what are the minimum number of features/capabilities required for the current project intention to be realised?
**Intention for MVP** - provide a development platform for testing the flood drain and timing capabilities.
A basic working model that provides pump control and the minimum number of sensors for operation