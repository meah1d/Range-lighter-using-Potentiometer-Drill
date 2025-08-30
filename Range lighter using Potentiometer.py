#define LED_1_PIN 8
#define LED_2_PIN 9
#define LED_3_PIN 10
#define LED_4_PIN 11
#define LED_5_PIN 12
#define POTENTIOMETER_PIN A0

#define LED_NUMBER 5

void setup()
{
  pinMode(LED_1_PIN, OUTPUT);
  pinMode(LED_2_PIN, OUTPUT);
  pinMode(LED_3_PIN, OUTPUT);
  pinMode(LED_4_PIN, OUTPUT);
  pinMode(LED_5_PIN, OUTPUT);
}

void loop()
{
  int potentiometerValue = analogRead(POTENTIOMETER_PIN);
  int ledChoice = potentiometerValue / (1024 / LED_NUMBER);
  
  if (ledChoice > LED_NUMBER - 1) {
    ledChoice = LED_NUMBER - 1;
  }
  
  if (ledChoice == 0) {
    digitalWrite(LED_1_PIN, HIGH);
    digitalWrite(LED_2_PIN, LOW);
    digitalWrite(LED_3_PIN, LOW);
    digitalWrite(LED_4_PIN, LOW);
    digitalWrite(LED_5_PIN, LOW);
  }
  else if (ledChoice == 1) {
    digitalWrite(LED_1_PIN, LOW);
    digitalWrite(LED_2_PIN, HIGH);
    digitalWrite(LED_3_PIN, LOW);
    digitalWrite(LED_4_PIN, LOW);
    digitalWrite(LED_5_PIN, LOW);
  }
  else if (ledChoice == 2) {
    digitalWrite(LED_1_PIN, LOW);
    digitalWrite(LED_2_PIN, LOW);
    digitalWrite(LED_3_PIN, HIGH);
    digitalWrite(LED_4_PIN, LOW);
    digitalWrite(LED_5_PIN, LOW);
  }
  else if (ledChoice == 3) {
    digitalWrite(LED_1_PIN, LOW);
    digitalWrite(LED_2_PIN, LOW);
    digitalWrite(LED_3_PIN, LOW);
    digitalWrite(LED_4_PIN, HIGH);
    digitalWrite(LED_5_PIN, LOW);
  }
  else {
    digitalWrite(LED_1_PIN, LOW);
    digitalWrite(LED_2_PIN, LOW);
    digitalWrite(LED_3_PIN, LOW);
    digitalWrite(LED_4_PIN, LOW);
    digitalWrite(LED_5_PIN, HIGH);
  }
}