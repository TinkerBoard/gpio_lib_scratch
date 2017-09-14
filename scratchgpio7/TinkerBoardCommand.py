import re
PINPUT = 4
POUTPUT = 1
PPWM = 2
PUNUSED = 8
PCOUNT = 256
PINPUTDOWN = 512
PINPUTNONE = 1024



def QueryConfigCommand(command):
    ConfigInpullUpCommand = ['in', 'input', 'inpullup', 'inputpullup']
    ConfigInpullDownCommand = ['inpulldown', 'inputpulldown']
    ConfigInpullNoneCommand = ['inpullnone', 'inputpullnone']
    ConfigOutputCommand = ['out', 'output']
    ConfigPWMCommand = ['pwm', 'outpwm', 'outputpwm']
    ConfigCommand = ConfigInpullUpCommand + ConfigInpullDownCommand + ConfigInpullNoneCommand + ConfigOutputCommand + ConfigPWMCommand
    ConfigCommand = sorted(ConfigCommand, key =lambda x: len(x), reverse=True)
    ConfigRegularExpression = r'config([0-9]+)(%s)([0-9]+)?' % ('|'.join(ConfigCommand))
    result = re.findall(ConfigRegularExpression, command)
    if(len(result) <= 0):
        return None
    else:
        pin = int(result[0][0])
        c = result[0][1].strip()
        if (c in ConfigInpullUpCommand):
            return (pin, PINPUT, -1)
        elif (c in ConfigInpullDownCommand):
            return (pin, PINPUTDOWN, -1)
        elif (c in ConfigInpullNoneCommand):
            return (pin, PINPUTNONE, -1)
        elif (c in ConfigOutputCommand):
            return (pin, POUTPUT, -1)
        elif (c in ConfigPWMCommand):
            return (pin, PPWM, int(result[0][2].strip()) if result[0][2].strip().isdigit() else -1)
        return None

def QuerySetPinCommand(command):
    OnCommand = ['on', 'high', 'true']
    OffCommand = ['off', 'low', 'false']
    PWMCommand = ['pwm']
    PinCommand = OnCommand + OffCommand + PWMCommand
    PinCommand = sorted(PinCommand, key =lambda x: len(x), reverse=True)
    PinRegularExpression = r'(gpio|pin)([0-9]+)(%s)([0-9]+)?' % ('|'.join(PinCommand))
    result = re.findall(PinRegularExpression, command)
    if(len(result) <= 0):
        return None
    else:
        pin = int(result[0][1])
        value = result[0][2].strip()
        if (value in OnCommand):
            return (pin, 1)
        elif (value in OffCommand):
            return (pin, 0)
        elif (value in PWMCommand):
            if(result[0][3].strip().isdigit()):
                return (pin, int(result[0][3].strip()) ,'pwm')
            else:
                return (pin, 0,'pwm')
        return None
