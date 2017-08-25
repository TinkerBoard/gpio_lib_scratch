import re
PINPUT = 4
POUTPUT = 1
PPWM = 2
PUNUSED = 8
PCOUNT = 256
PINPUTDOWN = 512
PINPUTNONE = 1024

ConfigInpullUpCommand = ['in', 'input', 'inpullup', 'inputpullup']
ConfigInpullDownCommand = ['inpulldown', 'inputpulldown']
ConfigInpullNoneCommand = ['inpullnone', 'inputpullnone']
ConfigOutputCommand = ['out', 'output']
ConfigPWMCommand = ['pwm', 'outpwm', 'outputpwm']
ConfigCommand = ConfigInpullUpCommand + ConfigInpullDownCommand + ConfigInpullNoneCommand + ConfigOutputCommand + ConfigPWMCommand
ConfigRegularExpression = r'config([0-9]+)(%s)' % ('|'.join(sorted(ConfigCommand, key =lambda x: len(x), reverse=True)))

def QueryConfigCommand(command):
    result = re.findall(ConfigRegularExpression, command)
    if(len(result) <= 0):
        return None
    else:
        pin = int(result[0][0])
        c = result[0][1].strip()
        if (c in ConfigInpullUpCommand):
            return (pin, PINPUT)
        elif (c in ConfigInpullDownCommand):
            return (pin, PINPUTDOWN)
        elif (c in ConfigInpullNoneCommand):
            return (pin, PINPUTNONE)
        elif (c in ConfigOutputCommand):
            return (pin, POUTPUT)
        elif (c in ConfigPWMCommand):
            return (pin, PPWM)
        return None
