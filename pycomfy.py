# pycomfy, an easy way to set up and use config files, by caeserlettuce
# lmao lets do this

# GENERAL IDEAS:
# open config file with pycomfy.openConfig('./path/to/configfile.txt'). will make a object i think its called
# make config file with pycomfy.makeConfig('./path/to/configfile.txt', ['element1=', 'element2']). will make a object i think its called
# set an element with pycomfy.setElement(CONFIGOBJECT, line_in_file, 'element_name')
from os import path


def makeConfig(CONFPATH, ELEMENTLIST):  # FUNCTION TO MAKE THE CONFIG
    print("Making Config at " + CONFPATH + " with " + str(ELEMENTLIST) + " as elements")    # cash money debug
    CONFIGCONTENTS = ""                     # to make the variable global but not ™
    for pope in range(len(ELEMENTLIST)):    # repeat for all elements to be added
        CONFIGCONTENTS = CONFIGCONTENTS + ELEMENTLIST[pope] + "=\n" # adds the element to the config
    CONFYFILE = open(CONFPATH, 'w')         # open config file
    CONFYFILE.write(CONFIGCONTENTS)         # print the output

def openConfig(CONFPATH):                   # OPEN CONFNIG
    print("OPening Config at " + CONFPATH)  # debub
    CONFYFILE = open(CONFPATH, 'r')
    COM = CONFYFILE.readlines()             # read all lines of config
    for pope in range(len(COM)):            # repeat
        COM[pope] = COM[pope].strip()       # remove any newline characters
    return COM                              # return a list of all elements in config

def getElement(CONFOBJ, CONFLINE, ELEMENTNAME):     # SET ELEMENT IN CONFIG
    print("Setting element " + str(ELEMENTNAME) + " on line " + str(CONFLINE) + " in config " + str(CONFOBJ))
    CURELEM = CONFOBJ[CONFLINE]
    ELEMSTRING = str(ELEMENTNAME) + "="
    CURELEM = CURELEM.replace(ELEMSTRING, "")
    return CURELEM

#makeConfig('./config.txt', ['naw', 'no'])

#CONFIG = openConfig('./config.txt')
#print(CONFIG)

#ELEM1 = getElement(CONFIG, 0, "naw")
#print(ELEM1)
#ELEM2 = getElement(CONFIG, 1, "no")
#print(ELEM2)