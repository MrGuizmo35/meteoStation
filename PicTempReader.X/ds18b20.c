#include "ds18b20.h"

uint8_t DS18B20_Reset()
{
    uint8_t i, presence;
    
    DS18B20_AS_OUTPOUT();
    DS18B20_CLEAR();
    for(i = 0; i < 5; i++)
    {
        DS18B20_TIMER = 0;
        while(DS18B20_TIMER < 200);
    }
    DS18B20_AS_INPUT();
    DS18B20_TIMER = 0;
    while(DS18B20_TIMER < 200);
    presence = DS18B20_READ();
    for(i = 0; i < 4; i++)
    {
        DS18B20_TIMER = 0;
        while(DS18B20_TIMER < 200);
    }
    
    return presence;    
}

void DS18B20_Write(uint8_t w)
{
    uint8_t i;
    
    for(i = 0; i < 8; i++)
    {
        DS18B20_AS_OUTPOUT();
        DS18B20_CLEAR();
        DS18B20_TIMER = 0;
        if(w & 1 << i)
        {
            while(DS18B20_TIMER < 2);
        }
        else
        {
            while(DS18B20_TIMER < 160);
        }
        DS18B20_SET();
        DS18B20_TIMER = 0;
        while(DS18B20_TIMER < 2);
    }
    DS18B20_AS_INPUT();
}