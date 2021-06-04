//Parameters
const int escPin = 5;
int min_throttle = 1000;
int max_throttle = 2000;
unsigned long currentMillis, previousMillis;

void setup() {
  //Init Serial USB
  Serial.begin(9600);
  Serial.println(F("Initialize System"));
  //Init ESC
  pinMode(escPin, OUTPUT);
  initProcedure();
}

void loop() {
  runBrushless();
  delay(10000);
}

void runBrushless() { /* function runBrushless */
  //// Test Brushless routine
  Serial.println("running");
  currentMillis = 0;
  previousMillis = millis();
  while (currentMillis < 2000) {
    currentMillis = millis() - previousMillis;
    digitalWrite(escPin, HIGH);
    delayMicroseconds(1350);
    digitalWrite(escPin, LOW);
    delay(20);
  }
  Serial.println("stop");
  currentMillis = 0;
  previousMillis = millis();
  while (currentMillis < 2000) {
    currentMillis = millis() - previousMillis;
    digitalWrite(escPin, HIGH);
    delayMicroseconds(min_throttle);
    digitalWrite(escPin, LOW);
    delay(20);
  }
}

void initProcedure() { /* function initProcedure */
  //// ESC inittialisation process
  previousMillis = millis();
  Serial.println("throttle up");
  while (currentMillis < 3000) {
    currentMillis = millis() - previousMillis;
    Serial.println(currentMillis);
    digitalWrite(escPin, HIGH);
    delayMicroseconds(max_throttle);
    digitalWrite(escPin, LOW);
    delay(20);
  } //beep- beep-
  currentMillis = 0;
  previousMillis = millis();
  Serial.println("throttle down");
  while (currentMillis < 4500) {
    currentMillis = millis() - previousMillis;
    Serial.println(currentMillis);
    digitalWrite(escPin, HIGH);
    delayMicroseconds(min_throttle);
    digitalWrite(escPin, LOW);
    delay(20);
  } // beep--
  // 1 2 3
}
