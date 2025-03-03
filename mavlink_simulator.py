import random
import time
from pymavlink import mavutil
import logging
import sys

# Initialize logger
logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
logger = logging.getLogger(__name__)

# Initialize the connection to the Mavlink system
master = mavutil.mavlink_connection('udpout:localhost:14550')

# Function to create and send random heartbeat messages
def send_random_heartbeat():
    #type = random.randint(0, 255)
    #mavlink.MAV_TYPE_QUADROTOR
    veh_type = mavutil.mavlink.MAV_TYPE_QUADROTOR
    autopilot = random.randint(0, 255)
    base_mode = random.randint(0, 255)
    custom_mode = random.randint(0, 4294967295)
    system_status = random.randint(0, 255)

    logger.info("Heartbeat => Type: %d, Autopilot Type: %d, Base Mode: %d, Custom Mode: %d, System Status: %d" % (veh_type, autopilot, base_mode, custom_mode, system_status))
    master.mav.heartbeat_send(veh_type, autopilot, base_mode, custom_mode, system_status)

# Function to create and send random GPS messages
def send_random_gps_raw_int():
    time_usec = int(time.time() * 1000000)
    fix_type = random.randint(0, 255)
    lat = random.randint(-900000000, 900000000)
    lon = random.randint(-1800000000, 1800000000)
    alt = random.randint(0, 10000)
    eph = random.randint(0, 65535)
    epv = random.randint(0, 65535)
    vel = random.randint(0, 65535)
    cog = random.randint(0, 65535)
    satellites_visible = random.randint(0, 255)
    
    logger.info("GPS Data")
    master.mav.gps_raw_int_send(time_usec, fix_type, lat, lon, alt, eph, epv, vel, cog, satellites_visible)

# Function to create and send random attitude messages
def send_random_attitude():
    time_boot_ms = random.randint(0, 4294967295)
    roll = random.uniform(-3.14, 3.14)
    pitch = random.uniform(-3.14, 3.14)
    yaw = random.uniform(-3.14, 3.14)
    rollspeed = random.uniform(-3.14, 3.14)
    pitchspeed = random.uniform(-3.14, 3.14)
    yawspeed = random.uniform(-3.14, 3.14)
    
    logger.info("Altitude Data")
    master.mav.attitude_send(time_boot_ms, roll, pitch, yaw, rollspeed, pitchspeed, yawspeed)

# Main function to continuously send random messages
def main():
    logging.basicConfig(filename='mavlink-sim.log', level=logging.INFO)
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    logger.addHandler(consoleHandler)

    logger.info('Start sending random messages')
    while True:
        send_random_heartbeat()
        send_random_gps_raw_int()
        send_random_attitude()
        time.sleep(1)  # Adjust the frequency of messages here

if __name__ == "__main__":
    main()
