String command1; //command from Touchscreen
const int Dir1 = 0; //direction for mototr 1
const int Dir2 = 1; //direction for motor 2
//const int Dir3 = 4; //direction for actuators
//const int Dir4 = 5;
//const int Dir5 = 8;
//const int Dir6 = 9;
//const int Dir7 = 7; 

//PWM for each of the 7 motors
const int PWM1 = 2; 
const int PWM2 = 3;
//const int PWM3 = 6;
//const int PWM4 = 7;
//const int PWM5 = 10;
//const int PWM6 = 11;
//const int PWM7 = 13;

//Analog positions 
int FootConv = 14;
int HeadConv = 15;
//int FootPos = 16;
//int HeadPos = 17;
//int LiftPos = 18;
//int ChairslidePos = 19;
//int SeatRotatePos = 20;



void setup() {
Serial.begin(9600);
pinMode(Dir1, OUTPUT);
pinMode(Dir2, OUTPUT);
//pinMode(Dir3, OUTPUT); //not currently used
//pinMode(Dir4, OUTPUT);
//pinMode(Dir5, OUTPUT);
//pinMode(Dir6, OUTPUT);
//pinMode(Dir7, OUTPUT);

pinMode(PWM1, OUTPUT);
pinMode(PWM2, OUTPUT);
//pinMode(PWM3, OUTPUT);//not currently used
//pinMode(PWM4, OUTPUT);
//pinMode(PWM5, OUTPUT);
//pinMode(PWM6, OUTPUT);
//pinMode(PWM7, OUTPUT);

pinMode(FootConv, INPUT);
pinMode(HeadConv, INPUT);
//pinMode(FootPos, INPUT);
//pinMode(HeadPos, INPUT);
//pinMode(LiftPos, INPUT); 
//pinMode(ChairslidePos , INPUT);
//pinMode(SeatRotatePos , INPUT);

  //Safety button inturrupt 
attachInterrupt(digitalPinToInterrupt(29),safetyswitch1,RISING); //inturrupt activated when button on pin 29 is pressed, leading to low to high transition
  
}

void safetyswitch1() 
{
//  //Function to Turn off all the motors when safety switch is pressed
analogWrite(PWM1,0);
analogWrite(PWM2,0);
//analogWrite(PWM3,0);
//analogWrite(PWM4,0);
//analogWrite(PWM5,0);
//analogWrite(PWM6,0);
//analogWrite(PWM7,0);
}

void loop() {
   // put your main code here, to run repeatedly:

int val1 = analogRead(HeadConv);    // read the value from the positions
int val2 = analogRead(FootConv);
//only when positions are in these limiits accept input from user
//if (((val1<800) && (val1>50)) && ((val2<800) && (val2>50))){
  
  if (Serial.available()){
    command1= Serial.readStringUntil('\n');
    command1.trim();

    if (command1.equals("HeadConvClk")){
      if ((val1>50) && (val1<800)) {
      digitalWrite(Dir1, HIGH); //clockwise head conv 
      analogWrite(PWM1, 255);
      delay(1000);
      digitalWrite(Dir2, LOW); //turn off all motors
       analogWrite(PWM2, 0);
       digitalWrite(Dir1, LOW); 
        analogWrite(PWM1, 0);
      }  
    }
    else if (command1.equals("HeadConvAntiClk")){
      if ((val1>50) && (val1<800)) {
      digitalWrite(Dir1, LOW); //Anti clockwise head conv 
      analogWrite(PWM1, 255);
      delay(1000);
      digitalWrite(Dir2, LOW); //turn off all motors
      analogWrite(PWM2, 0);
      digitalWrite(Dir1, LOW); 
      analogWrite(PWM1, 0);
    }
    }

   else if (command1.equals("FootConvClk")){
    if ((val2>50) && (val2<800)) {
      digitalWrite(Dir2, HIGH); //Foot conveyer clockwise
      analogWrite(PWM2, 255);
      delay(1000);
      digitalWrite(Dir2, LOW); //turn off all motors
      analogWrite(PWM2, 0);
      digitalWrite(Dir1, LOW); 
      analogWrite(PWM1, 0);
    }
   }

     else if (command1.equals("FootConvAntiClk")){
      if ((val2>50) && (val2<800)) {
      digitalWrite(Dir2, HIGH); //Foot conveyer Anti clockwise
      analogWrite(PWM2, 255);
      delay(1000);
      digitalWrite(Dir2, LOW); //turn off all motors
      analogWrite(PWM2, 0);
      digitalWrite(Dir1, LOW); 
      analogWrite(PWM1, 0);
    }
     }

    else if (command1.equals("BothConvClk")){
      if (((val1<800) && (val1>50)) && ((val2<800) && (val2>50))){
      digitalWrite(Dir1, HIGH); //Foot and head conveyer clockwise
      analogWrite(PWM1, 255);
      digitalWrite(Dir2, HIGH); 
      analogWrite(PWM2, 255);
      delay(1000);
      digitalWrite(Dir2, LOW); //turn off all motors
      analogWrite(PWM2, 0);
      digitalWrite(Dir1, LOW); 
      analogWrite(PWM1, 0);
    }
    }

    else if (command1.equals("BothConvAntiClk")){
      if (((val1<800) && (val1>50)) && ((val2<800) && (val2>50))){
      digitalWrite(Dir1, LOW); //Foot and head conveyer Anti clockwise
      analogWrite(PWM1, 255);
      digitalWrite(Dir2, LOW); 
      analogWrite(PWM2, 255);
      delay(1000);
      digitalWrite(Dir2, LOW); //turn off all motors
      analogWrite(PWM2, 0);
      digitalWrite(Dir1, LOW); 
      analogWrite(PWM1, 0);
    }
    }
      
    else {
      digitalWrite(Dir1,LOW);
      digitalWrite(Dir2,LOW);
      digitalWrite(PWM1,LOW);
      digitalWrite(PWM2,LOW); 
    }
  }
delay(200);
}

    
