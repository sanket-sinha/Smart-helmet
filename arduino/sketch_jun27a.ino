// Include RadioHead Amplitude Shift Keying Library
#include <RH_ASK.h>
// Include dependant SPI Library 
#include <SPI.h> 
 
// Create Amplitude Shift Keying Object
RH_ASK rf_driver;
int analogPin = A7; // potentiometer wiper (middle terminal) connected to analog pin 3
                   // outside leads to ground and +5V
int val = 0; 
int X=0;// variable to store the value read
void setup()
{
    Serial.begin(9600);           //  setup serial
    // Initialize ASK Object
    rf_driver.init();
}
 
void loop()
{
    val = analogRead(analogPin);  // read the input pin
    X = 10 * val;
    Serial.println(X);          // debug value
    if(X>2000){
      const char *msg = "Helmet Weared";
    }
    else{
      const char *msg = "Helmet Not Weared";
    }
    rf_driver.send((uint8_t *)msg, strlen(msg));
    rf_driver.waitPacketSent();
    delay(2000);
}
