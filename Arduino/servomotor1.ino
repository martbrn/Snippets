#include <Servo.h>

Servo servo1;
int PINSERVO = 2;
int PULSOMIN = 500;
int PULSOMAX = 2600;
int VALORPOT;
int ANGULO;
int POT = 0;

void setup()
{
servo1.attach(PINSERVO,PULSOMIN,PULSOMAX);
  
}

void loop()
{
	VALORPOT = analogRead(POT);
	ANGULO = map (VALORPOT,0,1023,0,180);
  	servo1.write(ANGULO);
 	delay(20);
}