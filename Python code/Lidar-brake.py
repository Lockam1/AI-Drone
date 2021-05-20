import serial
from dronekit import connect, VehicleMode, LocationGlobal, LocationGlobalRelative
from pymavlink import mavutil  # Needed for command message definitions
import time
import math

import argparse

parser = argparse.ArgumentParser(description='Control Copter and send commands in GUIDED mode ')
parser.add_argument('--connect',
                    help="Vehicle connection target string. If not specified, SITL automatically started and used.")
args = parser.parse_args()

connection_string = args.connect
sitl = None

# Start SITL if no connection string specified
##if not connection_string:
##    import dronekit_sitl
##
##    sitl = dronekit_sitl.start_default()
##    connection_string = sitl.connection_string()

# Connect to the Vehicle
print 'Connecting to vehicle on: %s' % connection_string
vehicle = connect(connection_string, wait_ready=True)



ser = serial.Serial('/dev/ttyUSB0',115200,timeout = 1)
##ser.write(0x42)
##ser.write(0x57)
##ser.write(0x02)
##ser.write(0x00)
##ser.write(0x00)
##ser.write(0x00)
##ser.write(0x01)
##ser.write(0x06)


def Land():
  print("Landing")
  vehicle.mode = VehicleMode("LAND")
  while vehicle.armed:
    time.sleep(1)
  vehicle.close()


def R_check_maneu(distance):
    right_turn()
    forward(distance)
    left_turn()
    time.sleep(2)
    
def L_check_maneu(distance):
    left_turn()
    forward(distance)
    right_turn()
    time.sleep(2)

def path_planning(brake_location):

    global end, pp_code
    fwd_time = 7 #7s 
    location_travel_time = 5 #5s
    count = 0
    clear = 0
    while ((count<6) and (not clear)):
        print "path planning algo count = ",count
        if(count<3):
            R_check_maneu(fwd_time)
            if(Lidar()>thr_dist):
                clear = 1
                print "Clear signal rec"
                forward(fwd_time)
            else:
                count += 1
                
        elif (count == 3):
            goto_location(brake_location)
            forward(location_travel_time)
            right_turn()
            if(Lidar()>thr_dist):
                clear = 1
                print "Clear signal rec"
                forward(fwd_time)
            else:
                count += 1
        else:
            L_check_maneu(fwd_time)
            if(Lidar()>thr_dist):
                clear = 1
                print "Clear signal rec"
                forward(fwd_time)
            else:
                count += 1
    
    if(not clear):
        goto_location(brake_location)
        Land()
        end = 1
    else:
        print "Auto mode"
        time.sleep(1)
        vehicle.mode = VehicleMode("AUTO")
        vehicle.flush()
        
        
 
 
def right_turn():
    condition_yaw(90, relative=True)
    set_velocity_body(vehicle, 0.0001, 0, 0)
    time.sleep(3)

def left_turn():
	condition_yaw(270, relative=True)
	set_velocity_body(vehicle, 0.0001, 0, 0)
	time.sleep(3)
	
	
def forward(t_sec):
	set_velocity_body(vehicle, 5, 0, 0)
	time.sleep(t_sec)

 
def condition_yaw(heading, relative=False):
	if relative:
		is_relative = 1  # yaw relative to direction of travel
	else:
		is_relative = 0  # yaw is an absolute angle
	# create the CONDITION_YAW command using command_long_encode()
	msg = vehicle.message_factory.command_long_encode(
		0, 0,  # target system, target component
		mavutil.mavlink.MAV_CMD_CONDITION_YAW,  # command
		0,  # confirmation
		heading,  # param 1, yaw in degrees
		0,  # param 2, yaw speed deg/s
		1,  # param 3, direction -1 ccw, 1 cw
		is_relative,  # param 4, relative offset 1, absolute angle 0
		0, 0, 0)  # param 5 ~ 7 not used
	# send command to vehicle
	vehicle.send_mavlink(msg)


def set_velocity_body(vehicle, vx, vy, vz):
	msg = vehicle.message_factory.set_position_target_local_ned_encode(
		0,
		0, 0,
		mavutil.mavlink.MAV_FRAME_BODY_NED,
		0b0000111111000111,  # -- BITMASK -> Consider only the velocities
		0, 0, 0,  # -- POSITION
		vx, vy, vz,  # -- VELOCITY
		0, 0, 0,  # -- ACCELERATIONS
		0, 0)
	vehicle.send_mavlink(msg)
	vehicle.flush()
      

def arm_and_takeoff(aTargetAltitude):

    print "Basic pre-arm checks"
    while not vehicle.is_armable:
        print " Waiting for vehicle to initialise..."
        time.sleep(1)

    print "Arming motors"
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True
    while not vehicle.armed:
        print " Waiting for arming..."
        time.sleep(1)
    print "Taking off!"
    vehicle.simple_takeoff(aTargetAltitude)
    while True:
        print " Altitude: ", vehicle.location.global_relative_frame.alt
        if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
            print "Reached target altitude"
            break
        time.sleep(1)


def goto_location(waypoint):
  vehicle.simple_goto(waypoint)
  time.sleep(2)
  reached = 0
  while(not reached):
    time.sleep(1)
    a = vehicle.velocity
    if (abs(a[1])< 0.2 and abs(a[2])< 0.2 and abs(a[0])< 0.2):
      reached = 1
  print "Waypoint reached!"

        

def Lidar():

    ser.flushOutput()
    ser.flushInput()
    time.sleep(0.1)
    while(ser.in_waiting >= 9):
        if(('Y' == ser.read()) and ('Y' == ser.read())):
            Dist_L = ser.read()
            Dist_H = ser.read()
            Dist_Total = (ord(Dist_H) * 256) + (ord(Dist_L))
            print "Lidar distance = ",Dist_Total
            for i in range (0,5):
                ser.read()
            return Dist_Total
    
def main():
 
    print('Starting main program')
    
    global pp_code, end, clear, thr_dist
    thr_dist = 20
    end = 0
    distance = 0
    pp_code = 0
    
    cmds = vehicle.commands
    cmds.clear()
    vehicle.flush()
    
    arm_and_takeoff(5)

    while (not end and vehicle.location.global_relative_frame.alt > 2):
        distance = Lidar()
        if(distance < thr_dist):
            vehicle.mode = VehicleMode("BRAKE")
            print "Brake"
            stop = 0
            while(not stop):
                time.sleep(1)
                a = vehicle.velocity
                if (abs(a[1])< 0.2 and abs(a[2])< 0.2 and abs(a[0])< 0.2):
                  stop = 1
            location = vehicle.location.global_frame
            vehicle.mode = VehicleMode("GUIDED")
            print "Guided"
            path_planning(location)
            
        time.sleep(0.5)


    Land()
    print('Exiting main program')
  
if __name__ == '__main__':
    main()