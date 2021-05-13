#include <Servo.h>
Servo ESC1;

void setup() {
  // Attach the ESC on pin 9
  ESC1.attach(9,1000,2000); // (pin, min pulse width, max pulse width in microseconds) 

}
void loop() {
  for (int i = 0; i <= 20; i++) {
    ESC1.write(i);
    delay(20);
  }
    delay(15000);
}
