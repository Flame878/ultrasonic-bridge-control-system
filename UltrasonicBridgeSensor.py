from gpiozero import PWMOutputDevice, DigitalOutputDevice, DistanceSensor, LED
from time import sleep

PWM = PWMOutputDevice(18)
PWM2 = PWMOutputDevice(12)
ledG = LED(9)
ledR = LED(16)
Dir = DigitalOutputDevice(24)
Dir2 = DigitalOutputDevice(23)

sensor1 = DistanceSensor(echo=27, trigger=17, max_distance=1, threshold_distance=0.5)

speed1 = 0.15
movement_forw = False    


def forward():
    Dir.on()
    Dir2.on()
    ledR.on()
    ledG.off()
    PWM.value = speed1
    PWM2.value = speed1


def backward():
    Dir.off()
    Dir2.off()
    ledR.on()
    ledG.off()
    PWM.value = speed1
    PWM2.value = speed1


def Stop():
    PWM.value = 0
    PWM2.value = 0
    ledR.off()
    ledG.on()

def In_Range():
    global movement_forw
    print("Interrupt: Object detected < 0.5m")

    if not movement_forw:
        forward()
        sleep(8)
        Stop()
        movement_forw = True


def Out_Range():
    global movement_forw
    print("Interrupt: Object > 0.5m")

    if movement_forw:
        backward()
        sleep(8)
        Stop()
        movement_forw = False



sensor1.when_in_range = In_Range        
sensor1.when_out_of_range = Out_Range  

print("Distance ISR working")

while True:
    sleep(1)
