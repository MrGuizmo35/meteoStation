#ifndef __DS1820__
#define __DS1820__

#include <xc.h>
#include <stdint.h>

#define DS18B20_AS_OUTPOUT() TRISA4 = 0
#define DS18B20_AS_INPUT() TRISA4 = 1
#define DS18B20_SET() LATA4 = 1
#define DS18B20_CLEAR() LATA4 = 0
#define DS18B20_READ() PORTA4

#define DS18B20_TIMER TMR0

uint8_t DS18B20_Reset();

#endif //__DS1820__