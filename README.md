# RASPBERRY PI CAMERA MOVEMENT DETECTION

This project runs a Python file that captures a stream from a Raspberry Pi with a camera module and detects movement.
The intention is to keep the code simple and light, in order to run in Raspberry Pis with lower processing capabilities.

The code uses your Raspberry Pi IP address to run the stream. You will have to copy the IP to the main.py file. Also see the stream.sh file.

###  Main Files
* main.py -> Python file with movement detection
* stream.sh -> shell script to run stream in the Raspberry Pi
* requirements.txt -> requirements to run the code

### Raspberry Pi used
* Raspberry Pi 3B+
* 1.4GHz 64-bit quad-core processor
* 1GB LPDDR2 RAM

## Installation
Clone the repository
```python
git clone https://github.com/ds-kenwatanabe/raspberrypi_security_cam
```
Change to working directory and install requirements.txt
```python
cd raspberrypi_security_cam
pip install -r requirements.txt
```

## License
Licensed under the MIT License.
