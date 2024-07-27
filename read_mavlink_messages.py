from pymavlink import mavutil

def read_mavlink_messages():
    # Create a mavlink connection using pymavlink
    mavlink_connection = mavutil.mavlink_connection('tcp:localhost:14551')

    while True:
        # Wait for a message
        msg = mavlink_connection.recv_match(blocking=True)
        if msg.get_type() == 'HEARTBEAT':
            print(f"Heartbeat from system {msg.get_srcSystem()} component {msg.get_srcComponent()}: type={msg.type}, autopilot={msg.autopilot}, base_mode={msg.base_mode}, custom_mode={msg.custom_mode}, system_status={msg.system_status}")
        elif msg.get_type() == 'GPS_RAW_INT':
            print(f"GPS_RAW_INT: lat={msg.lat}, lon={msg.lon}, alt={msg.alt}, eph={msg.eph}, epv={msg.epv}, vel={msg.vel}, cog={msg.cog}, satellites_visible={msg.satellites_visible}")
        elif msg.get_type() == 'ATTITUDE':
            print(f"Attitude: roll={msg.roll}, pitch={msg.pitch}, yaw={msg.yaw}, rollspeed={msg.rollspeed}, pitchspeed={msg.pitchspeed}, yawspeed={msg.yawspeed}")
        else:
            print(msg)
            
if __name__ == "__main__":
    read_mavlink_messages()
