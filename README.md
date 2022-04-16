# Door-Lock-Mechanism-Face-Recognition-with-RaspberryPi

## Topic: Door Lock Mechanism using Face Recognition
## Team Name: Ejderha

### Team Members & Roles: 
•Uğur AKYEL (Leader): Image Processing, Raspberry Pi Hardware &Software Configuration 
•Vesile ÇELİK: Backend Developer
•Simge HATİPOĞLU: Frontend Developer
•Enes DEMİRTAŞ: Image Processing, Raspberry Pi Hardware &Software Configuration

### Deliverables: 

•We are going to deliver a website thatallows clients to control the allowed and disallowed faces. Clients can manage the allowed and disallowed faces to unlock the door. They canview the log file tomonitor who opens the door and when. 

•We will have a database to keep the information of allowed and disallowed faces. Faces will have an ID, name, and photo. Photos’ paths will be kept in the database and actual photos will be stored on the server computer.  The database will also store the logs. •We are going to build a mechanism consisting of adoor latch solenoid, a relay, a webcam, and a Raspberry Pi 3. The webcam will capture the image and according to face recognition results, a message will be sent to the Raspberry Pi, then the Pi will activate the relay and the relay will activate the door latch solenoid. 

•We are going to use Python and OpenCV to capture the webcam image and process it. For facerecognition, we are considering using the DeepFace library.To control the general-purpose input-output pins of Raspberry Pi, we will use the pigpio library.

•As an advanceddevelopmentobjective, we thought that running the webcam all the time is not a logical way. Instead, we considered addingan ultrasonic sensor to identify whether there is a person or not. Thanks to the ultrasonic sensor, we can control the running status of the webcam and image processing algorithms.