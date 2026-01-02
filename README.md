# ultrasonic-bridge-control-system
Event driven automated bridge system using ultrasonic distance sensing

--Overview--
This project is an automated bridge system that raises and lowers based on distance measurements from an ultrasonic sensor. The system uses event-driven callbacks to control motor movement when an object enters or leaves a defined range.

--Hardware Used--
- Raspberry Pi
- Ultrasonic distance sensor (HC-SR04)
- DC motors
- Motor driver
- LEDs for status indication
- External power supply

--How It Works
- The ultrasonic sensor continuously monitors distance.
- When an object is detected within a threshold range, the bridge is raised.
- When the object leaves the range, the bridge is lowered.
- Event-driven callbacks are used instead of polling to improve efficiency.
- LEDs indicate movement and idle states.

--My ideas--
This project was completed as a team project. My contributions focused on ultrasonic sensor integration, event-driven control logic, motor control using PWM, and system testing.

--Future Improvements--
- Add safety limit switches
- Improve motor speed ramping
- Add manual override controls like buttons and a stop system
- use better equipment to raise the brigde (Rope was used works but not the safest)
