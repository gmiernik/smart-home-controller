# Project: Smart Home Controller

This is one component of the semi-professional project for exploration new capabilities on the market supporting 
creation smart home solutions using cheap equipments like Raspberry PI integrated with Arduino or ESP32 modules.
This component is playing a main role in the project as a controller providing OPC UA server to get access to 
the functions and sensor data for the mobile application.

## Use Cases

### US01 - Door opener

- Based on the parameter of the door there should be a method to open the door using Arduino or ESP32 module.
- Server should provide information about available doors to open. So, the project should detect modules with such capabilities.

### US02 - Temperature

- Gathering temperature from available ESP32 modules using their senors
- Set target temperature in the heating system

## Technical requirements

- Project should generate executable code for Raspberry PI 4B with 4GB RAM
- Functionalities should have automatic tests to avoid regression during implementation next improvements
- Project should provide API using OPC UA protocol
- Access to the server should be protected using user tokens or another dynamic keys ensuring security
- Server will communicate with Arduino or ESP32 modules to get sensor data or perform an action
- Communication between Raspberry PI and Arduino will be via serial port
- Communication between Raspberry PI and ESP32 will be via wireless network