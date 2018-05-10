
byte sensorInterrupt = 0;  // 0 = digital pin 2
byte sensorPin       = 2;

float calibrationFactor = 4.5;

volatile byte pulseCount;  

float flowRate;
unsigned int flowMilliLitres;
unsigned long totalMilliLitres;

unsigned long oldTime;

const int sensor_pin = A0;
int soil_value ;

const int sensor_pin2 =A1;
int value;

const int sensor_pin3 =A2;
int sValue;

String s;
void setup()
{
  
  Serial.begin(9600);
   
  pinMode(sensorPin, INPUT);
  digitalWrite(sensorPin, HIGH);

  pulseCount        = 0;
  flowRate          = 0.0;
  flowMilliLitres   = 0;
  totalMilliLitres  = 0;
  oldTime           = 0;
  attachInterrupt(sensorInterrupt, pulseCounter, FALLING);
}

void loop()
{
   s="";
   if((millis() - oldTime) > 1000)   
  { 
    detachInterrupt(sensorInterrupt);
        
    flowRate = ((1000.0 / (millis() - oldTime)) * pulseCount) / calibrationFactor;
    oldTime = millis();
    
     flowMilliLitres = (flowRate / 60) * 1000;
    
    totalMilliLitres += flowMilliLitres;
      
    unsigned int frac;
    s+=int(flowRate);  // Print the integer part of the variable
    s+=" ";
    s+=int(totalMilliLitres);
    s+=" ";
    pulseCount = 0;
    
    attachInterrupt(sensorInterrupt, pulseCounter, FALLING);
   soil_value= analogRead(sensor_pin);
   soil_value = map(soil_value,1024,0,0,100);
   s+=int(soil_value);
   s+=" ";

   value=analogRead(sensor_pin2);
   if (value<=480){ 
      s+="0 0"; 
    }
    else if (value>480 && value<=530){ 
      s+="0 5"; 
    }
    else if (value>530 && value<=615){ 
      s+="5 10"; 
    }
    else if (value>615 && value<=660){ 
      s+="10 15"; 
    } 
    else if (value>660 && value<=680){ 
      s+="15 20"; 
    }
    else if (value>680 && value<=690){ 
      s+="20 25"; 
    }
    else if (value>690 && value<=700){ 
      s+="25 30"; 
    }
    else if (value>700 && value<=705){ 
      s+="30 35"; 
    }
    else if (value>705){ 
      s+="35 40"; 
    }
    sValue= analogRead(sensor_pin3);
    int voltage = sValue ;//*(5.0/1024.0);
    s+=" ";
    s+=int(voltage);
  Serial.println(s);
 
  }
  
  
}

void pulseCounter()
{
  pulseCount++;
}
