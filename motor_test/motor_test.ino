#define PWMA 5      //right side motors
#define AIN1 7

#define PWMB 6      //left side motors
#define BIN1 8

#define STBY 3      //standby pin

void setup() {
  pinMode(PWMA, OUTPUT);
  pinMode(AIN1, OUTPUT);

  pinMode(PWMB, OUTPUT);
  pinMode(BIN1, OUTPUT);

  pinMode(STBY, OUTPUT);

  digitalWrite(STBY, HIGH); //enable motor driver
}

bool test = false;
void loop() {
  while (test){
    //move both motors forward
    digitalWrite(AIN1, HIGH);  //right forward
    analogWrite(PWMA, 200);

    digitalWrite(BIN1, HIGH);  //left forward
    analogWrite(PWMB, 200);

    delay(2000);

    //reverse both motors
    digitalWrite(AIN1, LOW);   //right backward
    analogWrite(PWMA, 200);

    digitalWrite(BIN1, LOW);   //left backward
    analogWrite(PWMB, 200);

    delay(2000);

    //stop all motors
    analogWrite(PWMA, 0);
    analogWrite(PWMB, 0);
    delay(2000);
  }
  
}
