Setup Scratchgpio environment

* Install\
    Step1. Install gpio_lib_python from https://github.com/TinkerBoard/gpio_lib_python \
    Step2. Install NumPy. ex: pip install numpy\
    Step3. sh ./setup.sh
* Uninstall\
    sh ./uninstall.sh

* Run\
    Click the Desktop's shortcut.

* Broadcast Command\
    Set Pin Mode\
        config[pin] (in|input) ex: config11in\
        config[pin] inpulldown|inputpulldown) ex: config11inpulldown\
        config[pin] (out|output) ex:config11out\
        config[pin] (pwm|outpwm|outputpwm) ex: config11pwm\
    Set Output\
        gpio[pin] (on|high|true) ex: gpio11on\
        pin[pin] (on|high|true) ex:pin11on\
        gpio[pin] (off|low|false) ex: gpio11off\
        pin[pin] (off|low|false) ex: pin11off\
        gpio[pin] pwm(0-100) ex: gpio11pwm50\
        pin[pin] pwn(0-100) ex:pin11pwm50
