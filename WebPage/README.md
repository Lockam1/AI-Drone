# Goal

The Idea for the webpage is to use it to comunitacte with the drone, so that you can send a pickup request and or dilivary 
request to the drone so it can take your item to or from your place. The drone will either have an onboard processor (Raspberry Pi)
or and computer at homebase wich will read and send data automatically and communicate with the drone when it touches base from 
its missions.

## Plan:

- Input coordanace from your current location or a intended destination.
- Drone to pull data and plot a waypoint to the destination.
	- This to be done using a python script that runs when the Pi is connected to the internet at home.
- Drone to take full ai control when it arrives within the poximity of the location to find a suitable place to land.

### Websites needed feauters:

- [ ] Publicly accessible webpage.
- [ ] Retrive input data for a location. (Maps API?)(Physical location?)
