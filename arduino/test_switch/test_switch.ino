const int button = 3;
const int led = 2;
int lastState = HIGH;

void setup() {
  // put your setup code here, to run once:
  pinMode(button, INPUT);
  pinMode(led, OUTPUT);
  int lastState = digitalRead(button);
}

void loop() {
  // put your main code here, to run repeatedly:
  int state = digitalRead(button);
  digitalWrite(led, state);
}
