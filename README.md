# pycomfy, by caeserlettuce
HELLO!! I am back with a brand new python thing!
have you ever wanted to simply make a configuration file for your script? i sure have, so I made this.

Basically you can make a configuration file, open it, and read the inputted values from it, straight from the script easily!

that's it

## HOW TO USE

either git clone or download the zip into the same folder as your main script. at the top of your script, type `import pycomfy as comfy`.
### Making a config file
make a config file by using:

`comfy.makeConfig("/path/to/config.txt", ['config_element_1', 'config_element_2'])`

Example:

`comfy.makeConfig("./config.txt", ['name', 'date'])`

### Opening a config file
open a config file by using:

`CONFIG_OBJECT = comfy.openConfig("/path/to/config.txt")`

Example: 

`CONFIG = comfy.openConfig("./config.txt")`

if you were to print the output of openConfig, it'll print a list of all the lines inside the config file.

### Getting elements inside config
get config element by using:

`ELEMENT_1 = comfy.getElement(CONFIG_OBJECT, CONFIG_LINE, ELEMENT_NAME)`

Example:

`INPUT_NAME = comfy.getElement(CONFIG, 0, 'name')`

`CONFIG_OBJECT` is the where you opened the config to.

`CONFIG_LINE` is what line in the config the element is (starting at 0)

`ELEMENT_NAME` is the name of the element (the text before the equal sign)

## anything else??

I don't think so. if there is, I will update here. if you have any issues / questions post them in wherever you usually put them, i'm new to github