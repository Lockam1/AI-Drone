# Goal

The idea for the webpage is to use it to communicate with the drone. This will allow you to send a pickup request and or delivery 
request to the drone so it can take your item to or from a chosen address. The drone will either have an onboard processor (Raspberry Pi),
or a computer at homebase wich will read and send data automatically and communicate with the drone when it touches base from 
its missions.

## Plan:

- Input coordinates from your current location or a intended destination.
- The drone will pull the data and plot a waypoint to the destination.
	- This will be done using a python script that runs when the Pi is connected to the internet at home.
- Find a sutiable waypoint mission route to get to the intended location in as little time as possiable.
- The drone will take full AI control when it arrives within the poximity of the location to find a suitable place to land.
- Static or dynamic site?
- Use a static website gen and a hosting programm so up keep in minmimal and the work to do is less.
- Netlify to host? or Local?

### Websites needed feauters:

- [ ] Publicly accessible webpage.
- [ ] Retrieve input data for a location. (Maps API?)(Physical location?)
