# The Story Files

## Stories are customizable
As long as the story files conform to the specific formate detailed below, any story can be loaded into the game mechanics. 

## Story File Formating

### The required files are:
- text document with the description of the room
- text document with a list of the items in the room 
- text document with a list of rooms that connect to the current room
- text document with a list all rooms

### Naming Convention

The files follow a strict naming convention. Each file must start with the room name followed by the file name.  

file names include:
- "Desc" for the room description
- "Items" for the list of items in the room
- "Neighbors" for the list of neighbors connecting to the room

The exception to the rule is the roomsList.  It does not include the room name since it includes all rooms. 

### File Specific Requirements

The items list in the file list must have one item per line.  The item name should be just one word without spaces.  Each line should have the item name, the name of the item it can be used on, the description of the item, and the description when the item is used. Each part should be separated by colons.  If the Item can't be used on anything, use and useDescription should be None.    

The list of rooms in the Neighbor document need to correspond to the points of the compass.  Going clockwise around the compass, the rooms must be in the following order: North, East, South, West. Each room listed in the Neighbors file must be on a line by itself.  If a room does not have a neighbor at one of the directions, list None as the room in that position.  

 
