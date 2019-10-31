#define echo 13
#define trig 12
#define vcc 11
#define deltaT 15
#define ms_to_cm 58.2

void setup() {
  Serial.begin(9600);
  pinMode(trig, OUTPUT);
  digitalWrite(trig, LOW);
  pinMode(echo, INPUT);
  pinMode(vcc, OUTPUT);
  digitalWrite(vcc, HIGH); // +5v
}

void loop() {
  int distance = readSonar();
  Serial.println(distance);
}

int readSonar() {
  digitalWrite(trig, HIGH);
  delayMicroseconds(deltaT);
  digitalWrite(trig, LOW);
  int echoT = pulseIn(echo, HIGH);
  int distance = echoT / ms_to_cm;

  return distance;
}
