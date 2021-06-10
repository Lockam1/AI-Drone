#include <Arduino_LSM9DS1.h>
const int pingPin = 1; // Trigger Pin of Ultrasonic Sensor
const int echoPin = 2; // Echo Pin of Ultrasonic Sensor
const int pingPin1 = 3; // Trigger Pin of Ultrasonic Sensor
const int echoPin1 = 4; // Echo Pin of Ultrasonic Sensor
const int pingPin2 = 5; // Trigger Pin of Ultrasonic Sensor
const int echoPin2 = 6; // Echo Pin of Ultrasonic Sensor
const int pingPin3 = 7; // Trigger Pin of Ultrasonic Sensor
const int echoPin3 = 8; // Echo Pin of Ultrasonic Sensor


void setup() {
  Serial.begin(9600);
  while (!Serial);
  Serial.println("Started");

  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }

  Serial.print("Accelerometer sample rate = ");
  Serial.print(IMU.accelerationSampleRate());
  Serial.println(" Hz");
  Serial.println();
  Serial.println("Acceleration in G's");
  Serial.println("X\tY\tZ");
}

void loop() {
   long duration, cm;
   long duration1, cm1;
   long duration2, cm2;
   long duration3, cm3;
   pinMode(pingPin, OUTPUT);
   digitalWrite(pingPin, LOW);
   delayMicroseconds(2);
   digitalWrite(pingPin, HIGH);
   delayMicroseconds(10);
   digitalWrite(pingPin, LOW);
   pinMode(echoPin, INPUT);
   duration = pulseIn(echoPin, HIGH);

   pinMode(pingPin1, OUTPUT);
   digitalWrite(pingPin1, LOW);
   delayMicroseconds(2);
   digitalWrite(pingPin1, HIGH);
   delayMicroseconds(10);
   digitalWrite(pingPin1, LOW);
   pinMode(echoPin1, INPUT);
   duration1 = pulseIn(echoPin1, HIGH);

   pinMode(pingPin2, OUTPUT);
   digitalWrite(pingPin2, LOW);
   delayMicroseconds(2);
   digitalWrite(pingPin2, HIGH);
   delayMicroseconds(10);
   digitalWrite(pingPin2, LOW);
   pinMode(echoPin2, INPUT);
   duration2 = pulseIn(echoPin2, HIGH);

   pinMode(pingPin3, OUTPUT);
   digitalWrite(pingPin3, LOW);
   delayMicroseconds(2);
   digitalWrite(pingPin3, HIGH);
   delayMicroseconds(10);
   digitalWrite(pingPin3, LOW);
   pinMode(echoPin3, INPUT);
   duration3 = pulseIn(echoPin3, HIGH);
   
   cm = microsecondsToCentimeters(duration);
   cm1 = microsecondsToCentimeters(duration1);
   cm2 = microsecondsToCentimeters(duration2);
   cm3 = microsecondsToCentimeters(duration3);
   Serial.print(cm);
   Serial.print("cm(front)");
   Serial.println();
   delay(100);


   Serial.print(cm1);
   Serial.print("cm(left)");
   Serial.println();
   delay(100);

   Serial.print(cm2);
   Serial.print("cm(Back)");
   Serial.println();
   delay(100);

   Serial.print(cm3);
   Serial.print("cm(Right)");
   Serial.println();
   delay(100);
  float x, y, z;

  if (IMU.accelerationAvailable()) {
    IMU.readAcceleration(x, y, z);

    Serial.print(x);
    Serial.print('\t');
    Serial.print(y);
    Serial.print('\t');
    Serial.println(z);
  }
}
long microsecondsToInches(long microseconds) {
   return microseconds / 74 / 2;
}

long microsecondsToCentimeters(long microseconds) {
   return microseconds / 29 / 2;
}
