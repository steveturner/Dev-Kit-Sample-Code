# Unsolicited Messages

## Date/time

This message indicates the current date/time obtained from the TileBEE’s GPS. This message is not sent until the GPS has obtained a fix sufficient to set its internal date and time. If the GPS loses its fix, the message is sent with a flag indicating an invalid state. Date/time messages can be enabled or disabled using the `$DT` or `$OP` command. 

```
$DT <YYYY><MM><DD><hh><mm><ss>,<flag>*xx
```


 Parameter  | Description 
 ------------- | ------------- 
 `YYYY`  | Year (1970..2038)  
 `MM`  | Month (01..12) 
 `DD`      |  Day (01..31) 
 `hh` | Hour (00..23) 
 `mm` |        Minutes (00..59) 
 `ss`  |      Seconds (00..59) 
 `flag`| <div style="line-height:1.8;">`I` Date/time is invalid<br> `V` Date/time is valid</div>


## TileBEE status

Status messages indicate that the TileBEE has booted and acquired date/time and position information from the GPS network. Error and debug messages are also sent as status messages. TileBEE status messages cannot be disabled. 

```
$EGT <msg>[,<data>]*xx
```

Parameter  | Description 
 ------------- | ------------- 
 `msg`  | <div style="line-height:1.8;">`BOOT` TileBEE has booted and is ready to receive commands <br> `DATETIME` TileBEE has acquired date/time from the GPS network <br> `POSITION`   TileBEE has acquired position from a valid 3D fix from the GPS network <br> `ERROR` Error message (typically text) <br> `DEBUG` Debug message (typically text)</div>
`data` | <div style="line-height:1.8;"> `POWERON` The TileBEE started as a result of power being applied <br> `UPDATED` A firmware update was performed <br> `FAULT` A firmware crash occurred and the TileBEE restarted </div>

<strong>Notes:</strong>  
A `data` message follows the `BOOT` message to indicate the reason for the startup. The `DATETIME` will be sent once the GPS has acquired the date/time from the GPS network. The `POSITION` will be sent once a valid 3D fix has been acquired from the GPS network. The `POSITION` message will typically occur before the `DATETIME` message. Depending on the GPS signal quality, it may take several minutes before the `DATETIME` message is emitted.

## Geospatial information

This message provides standard NMEA-formatted positional information, including latitude, longitude, altitude, course, and speed. Geospatial information messages can be enabled/disabled using the `$GN` or `$OP` command.

```
$GN <latitude>,<lat_dir>,<longitude>,<lon_dir>,<altitude>,<course>,<speed>*xx
```

Parameter  | Description 
 ------------- | ------------- 
`latitude` |    Latitude in d.dddd format (float)
`lat_dir`  |   N/S
`longitude` |   Longitude in d.dddd format (float)
`lon_dir` |     E/W
`altitude` |    Altitude in meters (integer)
`course` |      Course in degrees (0..359) (integer)
`speed`  |     Speed in KPH (0..999.99) (integer * 100)

## GPS fix quality

This message provides a standard NMEA-formatted description of the type of GPS fix currently in use. GPS fix quality messages can be enabled/disabled using the `$GS` or `$OP` command.

```
$GS <hdop>,<vdop>,<gps_sats>,<glonass_sats>,<fix_type>*xx
```

Parameter  | Description 
 ------------- | ------------- 
`hdop`           | Horizontal dilution of precision (integer * 100)
`vdop`           | Vertical dilution of precision (integer * 100)
`gps_sats`       | Number of GPS satellites used in solution (integer)
`glonass_sats`   | Number of GLONASS satellites used in solution (integer)
`fix_type`       | <div style="line-height:1.8;"> `NF` No fix <br> `DR` Dead reckoning only solution <br> `G2` Standalone 2D solution <br> `G3` Standalone 3D solution <br> `D2` Differential 2D solution <br> `D3` Differential 3D solution <br> `RK` Combined GPS + dead reckoning solution <br> `TT` Time only solution </div>

## Received data

This message contains ASCII-encoded data received from the Swarm network. Received messages can be enabled/disabled via the `$OP` command.

```
$RD <data>[..<data>]*xx
```

Parameter  | Description 
 ------------- | ------------- 
`data`  |    ASCII-encoded data in packet


## Telemetry or message notification

This message indicates that telemetry information or a message has been received by the TileBEE. Swarm vehicle messages can be enabled/disabled via the `$OP` command. The contents of a `TEL` message are not available to the third-party application. 

```
$SV <state>,<vid>*xx
```

Parameter  | Description 
 ------------- | ------------- 
`state` | <div style="line-height:1.8;"> `TEL` TileBEE has received a telemetry message <br> `MSG`    TileBEE has received a message </div>
`vid` | Swarm vehicle ID (6-digit hex value)        

## Error message

This message contains an error value.

```
$TE <err>*xx
```

Parameter  | Description 
 ------------- | ------------- 
`err` | <div style="line-height:1.8;">`0x0000`    No error <br> `0x0001`    TileBEE cannot communicate with radio transceiver <br> `0x0002`    GPS not sending data <br> `0x0004`    CPU watchdog triggered </div>




