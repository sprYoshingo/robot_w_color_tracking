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
  Serial.begin(9600);
}


void loop() {
  if (Serial.available()){
    char command = Serial.read();
    

    if (command == 'F'){ //forwards
      //move both motors forward
      digitalWrite(AIN1, HIGH);  //right forward
      analogWrite(PWMA, 200);

      digitalWrite(BIN1, HIGH);  //left forward
      analogWrite(PWMB, 200);
    }

    else if (command == 'B'){ //backwards
      //reverse both motors
      digitalWrite(AIN1, LOW);   //right backward
      analogWrite(PWMA, 200);

      digitalWrite(BIN1, LOW);   //left backward
      analogWrite(PWMB, 200);

  }
    else if (command == 'S'){ //stop
      //stop all motors
      analogWrite(PWMA, 0);
      analogWrite(PWMB, 0);
    }
    else if (command == 'R'){ // right forward
      digitalWrite(AIN1,HIGH); //only move the right motors forward
      analogWrite(PWMA,200);

      analogWrite(PWMB,0);
    }

    else if (command == 'L'){ //left forward
      digitalWrite(BIN1,HIGH);
      analogWrite(PWMB,200);

      analogWrite(PWMA,0);
    }

    else if (command == 'X'){ // right backwards **SEE send-data.py FOR NOTE ON MOVEMENT FOR BACKWARDS COMMANDS**
      digitalWrite(AIN1,LOW);
      analogWrite(PWMA,200);

      analogWrite(PWMB,0);
    }

    else if (command == 'Q'){ //left backwards
      digitalWrite(BIN1,LOW);
      analogWrite(PWMB,200);

      analogWrite(PWMA,0);
    }


  }
}
