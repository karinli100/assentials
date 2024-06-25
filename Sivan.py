import requests

def log_in():
    """
    Stops the laser
    """
    response = requests.get("http://127.0.0.1:9010/Login?13&2&Int&Int123&EndOfGet")
    response.encoding = 'utf-8'
    print(response.text)


def turn(on_off):
    """
    Turns the laser on and off
    :param on_off:  1==on  0==off
    """
    response = requests.get("http://127.0.0.1:9010/TurnOn?13&1&{}&EndOfGet".format(on_off))
    response.encoding = 'utf-8'
    print(response.text)

def activate_low():
    """
    Start first 3 levels of amplification
    """
    response = requests.get("http://127.0.0.1:9010/ActivateLow?13&0&EndOfGet")
    response.encoding = 'utf-8'
    print(response.text)

def emission_off():
    """
    Stops the laser
    """
    response = requests.get("http://127.0.0.1:9010/EmissionOff?13&0&EndOfGet")
    response.encoding = 'utf-8'
    print(response.text)
def interlock_down_soft():
    """
    Stops the laser
    """
    response = requests.get("http://127.0.0.1:9010/InterlockDownSoft?13&0&EndOfGet")
    response.encoding = 'utf-8'
    print(response.text)

def interlock_up():
    """
    Stops the laser
    """
    response = requests.get("http://127.0.0.1:9010/InterlockUp?13&0&EndOfGet")
    response.encoding = 'utf-8'
    print(response.text)
def activate_high(start_stop_high_level):
    """
    Start==1 or stop==0 last 2 levels of amplification
    """
    response = requests.get("http://127.0.0.1:9010/ActivateHigh?13&1&{}&EndOfGet".format(start_stop_high_level))
    response.encoding = 'utf-8'
    print(response.text)

def get_params():
    """
    Gives info about the state of the laser
    high ==1/0
    all?
    duration = duration the laser will be on in seconds
    total number of active channels
    list of active channels 1!2!3!4....
    :return:
    """
    response = requests.get("http://127.0.0.1:9010/GetParameters?13&0&EndOfGet")
    response.encoding = 'utf-8'
    print(response.text)

def set_params(high, allic, duration, power, channel):
    """
    2 functions:
    1.  if allic == 0:
    activates a single channel
    Example: set_params(high=1, allic=0, duration=4000, power=4, channel=30)
    # only channel 30 will be selected! no metter what we add or remove before or after
s
    2.  if allic == 1
    activats all the channels on the list accept the removed ones
    Example: set_params(high=1, allic=1, duration=4000, power=4, channel=30)
    * in this case, 30 is not relevant at all
    ** all the add_channel() & remove_channel() actions should come before set_parameters to get validated
    """
    response = requests.get("http://127.0.0.1:9010/SetParameters?13&5&{}&{}&{}&{}&{}&EndOfGet".format(high, allic, duration, power, channel))
    response.encoding = 'utf-8'
    print(response.text)

def add_channel(channel_number):
    """
    Add a single channel to the list of active channels
    :param channel_number: channel number from 1 - 127
    :return:
    """
    response = requests.get("http://127.0.0.1:9010/AddSingleChannel?13&1&{}&EndOfGet".format(channel_number))
    response.encoding = 'utf-8'
    print(response.text)

def remove_channel(channel_number):
    """
    Remove a single channel from the list of active channels
    :param channel_number: channel number from 1 - 127
    """
    response = requests.get("http://127.0.0.1:9010/RemoveSingleChannel?13&1&{}&EndOfGet".format(channel_number))
    response.encoding = 'utf-8'
    print(response.text)

def turn_Off_single_channel(channel_number):
    """
    Turn off a single channel at level 5
    :param channel_number: channel number from 1 - 127
    """
    response = requests.get("http://127.0.0.1:9010/TurnOffSingleChannel?13&1&{}&EndOfGet".format(channel_number))
    response.encoding = 'utf-8'
    print(response.text)

def get_Status_single_channel(channel_number):
    """
    Get status of a single channel at level 5
    :param channel_number: channel number from 1 - 127
    """
    response = requests.get("http://127.0.0.1:9010/GetStatusSingleChannel?13&1&{}&EndOfGet".format(channel_number))
    response.encoding = 'utf-8'
    print(response.text)

def get_monitoring_laser():
    """
    Get status of a single channel at level 5
    :param channel_number: channel number from 1 - 127
    status ,  error cause,   amplification level,  com-ready-flag,  control-flags

    Status will be:
    0 if the system is down
    1 if the system is “Interlock up”
    2 if the laser is working
    3 if laser reached the requested power/ampere
    -1 if there was an error

    Note: In the case of an error, the cause of the error will be returned in the value of “error cause”.
    The error message is a string.
    It is empty when there is no error.
    In case of communication issues it includes the list of controllers that did not communicate.
    If there are such controllers, the response will be a concatenation of the controller names followed by “
    communication
    fault: ERROR
    No Communication” with the separator being “$”.
    In case of other errors, the separator is “|”
    Level is:
    Login -  3
    system off  -  2
    System on -  1
    Finished
    Initializing 0
    level 1 is on 1
    level 2 is on 2
    level 3 is on 3
    level 4 is on 4
    level 5 is on 5

    com-ready-flag
    and controlflags: These are a 8 bits number.
    Each bit represents the value of one of the controls.
    """
    response = requests.get("http://127.0.0.1:9010/GetMonitoringLaser?13&0&EndOfGet")
    response.encoding = 'utf-8'
    print(response.text)

def panic():
    """
    Get status of a single channel at level 5
    :param channel_number: channel number from 1 - 127
    """
    response = requests.get("http://127.0.0.1:9010/Panic?13&0&EndOfGet")
    response.encoding = 'utf-8'
    print(response.text)


interlock_down_soft()

"""exit()
log_in()
set_params(high=1, allic=0, duration=4000, power=2000, channel=16)

get_params()
get_monitoring_laser()

exit()
get_params()
remove_channel(10)
turn_Off_single_channel(40)
activate_high(0)


exit()
log_in()
turn()
get_params()
get_monitoring_laser()
get_Status_single_channel(12)
set_params(high=1, allic=0, duration=4000, power=2000, channel=14)
turn_Off_single_channel(20)
activate_low()
activate_high(1)
emission_off()
panic()

for i in range(120):
    add_channel(i)
set_params(high=1, allic=1, duration=4000, power=4, channel=5)
"""