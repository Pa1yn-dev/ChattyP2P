from distutils.debug import DEBUG
import datetime
import logging
from _global import *


def LOGGINGINIT():

    
    logging.basicConfig (filename= 'ChattyP2P_Cli.log', encoding='utf-8', level=logging.DEBUG)
    
    LOGEVENTS_INFO(f"Logging started")
   
    

def LOGEVENTS_INFO(input):

    currentdateandtime = datetime.datetime.now()
    currentdateandtimestr = currentdateandtime.strftime("%m/%d/%Y, %H:%M:%S")
    
    print(f"{currentdateandtimestr} " + input)
    logging.info(f"{currentdateandtimestr} " + input)

def LOGEVENTS_DEBUG(input):

    currentdateandtime = datetime.datetime.now()
    currentdateandtimestr = currentdateandtime.strftime("%m/%d/%Y, %H:%M:%S")
    
    print(f"{currentdateandtimestr} " + input)
    logging.debug(f"{currentdateandtimestr} " + input)

def LOGEVENTS_ERROR(input):

    currentdateandtime = datetime.datetime.now()
    currentdateandtimestr = currentdateandtime.strftime("%m/%d/%Y, %H:%M:%S")
    
    print(f"{currentdateandtimestr} " + input)
    logging.error(f"{currentdateandtimestr} " + input)

def LOGEVENTS_CRITICAL(input):

    currentdateandtime = datetime.datetime.now()
    currentdateandtimestr = currentdateandtime.strftime("%m/%d/%Y, %H:%M:%S")
    
    print(f"{currentdateandtimestr} " + input)
    logging.critical(f"{currentdateandtimestr} " + input)




