#file to turn the drone 90 degrees

from commander import Commander
import time

# create Commander instance
con = Commander()



#turn the drone
con.turn(90)
time.sleep(2)


# land
con.land()
