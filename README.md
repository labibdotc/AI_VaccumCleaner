# AI_VaccumCleaner
This new type of robotic vacuum cleaner has quite simple reflex rules. It will always check the battery level first. If the level is below 30%, it will plan a path to its charging base (“home”), go there, and start the docking procedure. If the battery is sufficient, it will start the function it was commanded to perform. There are two available commands:

Spot cleaning: it will perform a 20s intensive cleaning in a specific area.
General cleaning: go around the room and vacuum dust until the battery falls under 30% or completes the task. If the dust sensor detects a particularly dirty spot, the robot will perform a 35s spot cleaning.
The blackboard must contain at least the following elements, but you can add more if your implementation requires it:

BATTERY_LEVEL: an integer number between 0 and 100.
SPOT_CLEANING: a Boolean value – TRUE if the command was requested, FALSE
GENERAL_CLEANING: a Boolean value – TRUE if the command was requested, FALSE
DUSTY_SPOT: a Boolean value – TRUE if the sensor detected a dusty spot during the cycle, FALSE
HOME_PATH: The path to the docking station.

## Behavior tree
<img width="933" alt="Screenshot 2023-02-14 at 11 31 23 AM" src="https://user-images.githubusercontent.com/98433990/218798695-d15f3e42-1877-4d78-93e2-6ace08acb8c5.png">

## Setup and run
fork the project to your github and then
```
git clone <https address for your repository>
cd AI_VaccumCleaner
python main.py
```
