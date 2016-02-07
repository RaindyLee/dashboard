#include <Wire.h>

#define RELAY1 7
#define RELAY2 6
#define RELAY3 5
#define RELAY4 4

#define SSR1 8
#define SSR2 9
#define SSR3 10
#define SSR4 11

void setup() {
  // LED 13 ON
  pinMode(13, OUTPUT);
  digitalWrite(13, HIGH);
  
  Wire.begin(4);                // join i2c bus with address #4
  Serial.begin(9600);           // start serial for output
  Wire.onReceive(receiveEvent); // register event
  // default HIGH
  digitalWrite(RELAY1, HIGH);
  digitalWrite(RELAY2, HIGH);
  digitalWrite(RELAY3, HIGH);
  digitalWrite(RELAY4, HIGH);
  // set up Relays
  pinMode(RELAY1, OUTPUT);
  pinMode(RELAY2, OUTPUT);
  pinMode(RELAY3, OUTPUT);
  pinMode(RELAY4, OUTPUT);
  
  pinMode(SSR1, OUTPUT);
  pinMode(SSR2, OUTPUT);
  pinMode(SSR3, OUTPUT);
  pinMode(SSR4, OUTPUT);
}


void loop() 
{
   delay(50);
}

// function that executes whenever data is received from master
// this function is registered as an event, see setup()
void receiveEvent(int howMany)
{
  int x = Wire.read();   
  // receive byte as an integer
  Serial.println("Command Received");
  Serial.print(x); 
  Serial.print("; "); 
  // print the integer
  
  switch(x) {
      // RELAY1
      case 0:
        digitalWrite(RELAY1, HIGH);
        Serial.println("RELAY1 OFF");
        Serial.println();
       break;
      case 1:
        digitalWrite(RELAY1, LOW);
        Serial.println("RELAY1 ON");
        Serial.println();
       break;
      // RELAY2 
      case 2:
        digitalWrite(RELAY2, HIGH);
        Serial.println("RELAY2 OFF");
        Serial.println();
       break;
      case 3:
        digitalWrite(RELAY2, LOW);
        Serial.println("RELAY2 ON");
        Serial.println();
       break;
      // RELAY3
      case 4:
        digitalWrite(RELAY3, HIGH);
        Serial.println("RELAY3 OFF");
        Serial.println();
       break;
      case 5:
        digitalWrite(RELAY3, LOW);
        Serial.println("RELAY3 ON");
        Serial.println();
       break;
      // RELAY4
      case 6:
        digitalWrite(RELAY4, HIGH);
        Serial.println("RELAY4 OFF");
        Serial.println();
       break;
      case 7:
        digitalWrite(RELAY4, LOW);
        Serial.println("RELAY4 ON");
        Serial.println();
       break;
       
       case 10:
        digitalWrite(SSR1, LOW);
        Serial.println("SSR1 OFF");
        Serial.println();
       break;
      case 11:
        digitalWrite(SSR1, HIGH);
        Serial.println("RELAY1 ON");
        Serial.println();
       break;
      // RELAY2 
      case 12:
        digitalWrite(SSR2, LOW);
        Serial.println("RELAY2 OFF");
        Serial.println();
       break;
      case 13:
        digitalWrite(SSR2, HIGH);
        Serial.println("RELAY2 ON");
        Serial.println();
       break;
      // RELAY3
      case 14:
        digitalWrite(RELAY3, HIGH);
        Serial.println("RELAY3 OFF");
        Serial.println();
       break;
      case 15:
        digitalWrite(RELAY3, LOW);
        Serial.println("RELAY3 ON");
        Serial.println();
       break;
      // RELAY4
      case 16:
        digitalWrite(RELAY4, HIGH);
        Serial.println("RELAY4 OFF");
        Serial.println();
       break;
      case 17:
        digitalWrite(RELAY4, LOW);
        Serial.println("RELAY4 ON");
        Serial.println();
       break;
  }
} 
