# Commands and Responses

## Date/time

This command repeats the most recent `$DT` message, or queries or sets the `$DT` message rate. 

```
$DT <@|?|<rate>>*xx
```

Parameter  | Description 
 ------------- | ------------- 
`@`  |       Repeat most recent `$DT` message
`?`     |    Query current `$DT` rate
`rate` |   Disable or set rate of `$DT` messages

<strong>Returns one of:</strong>

Value  | Description 
 ------------- | ------------- 
`$DT <YYYY><MM><DD><hh><mm><ss>,<flag>*xx` | The most recent `$DT` message 
`$DT <rate>*xx` | The current `$DT` rate
`$DT OK*xx` | Parameters updated successfully
`$DT ERR*xx` | An error response


<strong>Notes:</strong>  
For the query option, the return value of `$DT <rate>*xx` requires different parsing than the normal `$DT` message format. The application should check if a comma is present in the `$DT` string, and, if so, assume it is the standard date/time format. If no comma is present and the value is a number, then the value is the rate being returned in response to the `$DT ?` query.

`<rate>` is a value between 1 and 2147483647 (2<sup>31</sup>-1). This is not a time in seconds, but rather a divider for each time the GPS emits the message. This is typically once a second, but some messages may be emitted less frequently. If the GPS emits a particular message once every 5 seconds, and the `<rate>` for that message is set to 2, the message will be emitted to the user every 10 seconds.

An `OK` response confirms that the parameters have been updated in response to a command with the `<rate>` parameter. An `ERR` response indicates that additional or invalid characters were included between the `T` and the `*` of the command. 

<strong>Example:</strong>

Calling the most recent date/time message:
```
DT @
$DT 2019,04,08,19,51,23,V*2d
```
Returns a date/time of `April 8th, 2018 7:51:23 PM GMT`. The date/time is `valid`

## Firmware version

This command returns the TileBEE’s firmware version. 

```
$FV*xx
```
<strong>Returns one of:</strong>

Value  | Description 
 ------------- | ------------- 
`$FV <version_string>*xx` | The current firmware version
`$FV ERR*xx` | An error response


<strong>Notes:</strong>  
An `ERR` response indicates that additional characters were included between the `V` and the `*` of the command. 

## Geospatial information

This command repeats the most recent `$GN` message, or queries or sets the `$GN` message rate. 

```
$GN <@|?|<rate>>*xx
```

Parameter  | Description 
 ------------- | ------------- 
`@`       |  Repeat most recent `$GN` message
`?`        | Query current `$GN` rate
`rate`  |  Disable or set rate of `$GN` messages


<strong>Returns one of:</strong>

Value  | Description 
 ------------- | ------------- 
`$GN <latitude>,<lat_dir>,<longitude>,<lon_dir>,<altitude>,<course>,<speed>*xx` | The most recent `$GN` message. See [Gesopatial Information - Unsolicited Messages](unsolicited.md#geospatial-information) for more detail on the outputs of this message
`$GN <rate>*xx` | The current `$GN` rate
`$GN OK*xx` | Parameters updated successfully
`$GN ERR*xx` | An error response
 

<strong>Notes:</strong>  
For the query option, the return value of `$GN <rate>*xx` requires different parsing than the normal `$GN` message format. The application should check if a comma is present in the `$GN` string, and, if so, assume it is the standard geospatial information format. If no comma is present and the value is a number, then the value is the rate being returned in response to the `$GN ?` query.

`<rate>` is a value between 1 and 2147483647 (2<sup>31</sup>-1). This is not a time in seconds, but rather a divider for each time the GPS emits the message. This is typically once a second, but some messages may be emitted less frequently. If the GPS emits a particular message once every 5 seconds, and the `<rate>` for that message is set to 2, the message will be emitted to the user every 10 seconds.

An `OK` response confirms that the parameters have been updated in response to a command with the `<rate>` parameter. An `ERR` response indicates that additional or invalid characters were included between the `N` and the `*` of the command. 

<strong>Example:</strong>

Calling the most recent GPS message:
```
GN @
$GN 37.4009492,N,-122.0571488,W,22,0,0*2d
```
Returns a location of `37.4009492N, 122.0571488"W`. The TileBEE's altitude is `22m`, its course is `2 degrees`, and it is moving at `5 kilometers per hour`.

## Geospatial information

This command repeats the most recent `$GS` message, or queries or sets the `$GS` message rate. 

```
$GS <@|?|<rate>>*xx
```


Parameter  | Description 
 ------------- | ------------- 
 `@`  |       Repeat most recent `$GS` message
`?`  |       Query current `$GS` rate
`rate`   | Disable or set rate of `$GS` messages


<strong>Returns one of:</strong>

Parameter  | Description 
 ------------- | ------------- 
`$GS <hdop>,<vdop>,<gps_sats>,<glonass_sats>,<fix>*xx` | The most recent `$GS` message. See [GPS Fix Quality - Unsolicited Messages](unsolicited.md#gps-fix-quality) for more detail on the outputs of this message
`$GS <rate>*xx` | The current `$GS` rate
`$GS OK*xx` | Parameters updated successfully
`$GS ERR*xx` | An error response

<strong>Notes:</strong>  
For the query option, the return value of `$GS <rate>*xx` requires different parsing than the normal `$GS` message format. The application should check if a comma is present in the `$GS` string, and, if so, assume it is the standard geospatial information format. If no comma is present and the value is a number, then the value is the rate being returned in response to the `$GS ?` query.

`<rate>` is a value between 1 and 2147483647 (2<sup>31</sup>-1). This is not a time in seconds, but rather a divider for each time the GPS emits the message. This is typically once a second, but some messages may be emitted less frequently. If the GPS emits a particular message once every 5 seconds, and the `<rate>` for that message is set to 2, the message will be emitted to the user every 10 seconds.

An `OK` response confirms that the parameters have been updated in response to a command with the `<rate>` parameter. An `ERR` response indicates that additional or invalid characters were included between the `S` and the `*` of the command. 

<strong>Example:</strong>

Setting the rate for geospatial information messages to 1
```
GS 1
$GS OK*30
```

## Manage received messages

This command enables management of received messages.

```
$MM <C=<U|*>|<D=<msg_id|*>|<M=<msg_id>|*>|R=<msg_id|O|N>>*xx
```

Parameter  | Description 
 ------------- | ------------- 
`C=<U\|*>`  |         Return count of unread (`U`) or all (`*`) messages
`D=<msg_id\|R\|*>`   | Delete message ID (`msg_id`), all read (`R`), or all (`*`) messages
`M=<msg_id\|*> `    | Mark message ID (`msg_id`) or all (`*`) as read
`R=<msg_id\|O\|N>`   | Read message ID (`msg_id`), oldest (`O`), or newest (`N`)


<strong>Returns one of:</strong>

Value  | Description 
 ------------- | ------------- 
`$MM OK*xx`                |  Delete message command succeeded
`$MM ERR,BADPARAM*xx` |         Invalid command or argument to `$MM` command
`$MM ERR,DBXINVMSGID*xx`   |   Invalid message ID in `D` or `R` command
`$MM ERR,DBXNOMORE*xx`      |  No more messages when using `R=<O\|N>` command
`$MM DELETED,<msg_id>*xx`    | `<msg_id>` deleted successfully
`$MM MARKED,<msg_id>*xx`     | `<msg_id>` marked as read successfully
`$MM <msg_count>`           |  Number of messages read/all/deleted (1)
`$MM <data>,<msg_id>,<es>`  |  Response to reading a message (2)


<strong>Notes:</strong>  
Messages have three states: unread, read, and deleted. Once an unread message is read, its state changes to read. It can subsequently be
read again. If a message is deleted, it can no longer be read. `All`
in the above context means both read and unread messages, but does not
include messages that have been deleted.

If a message is marked read using the `M=<msg_id>` or `M=*` command,
marking it as read again is not an error.

The GPIO1 pin can be configured to indicate whether or not unread messages are pending (see the `$OP GP=<mode>` command).

(1) `<msg_count>` is a number indicating the number of messages that
are unread in response to the `C=U` command, total number of read and unread messages in response to the `C=*` command, and the number of messages deleted in response to the `D=*` command.

(2) `<data>` is in the same format as an unsolicited `$RD` message. `<msg_id>` is the message ID. The message ID should be treated as a simple arbitrary number. `<es>` is the epoch seconds time when the message was received by the TileBEE.

## Disable/enable messages

This command allows selective disabling/enabling of messages from the TileBEE, as well as setting parameters including message delivery preferences, mobile vs. fixed-location operation, and disabling/enabling receive-only mode. 

```
$OP <?|p1=<val>[,p2=<val>[,...]]]*xx
```

Parameter  | Description 
 ------------- | ------------- 
`?` |                     Display current settings
`AL=S\|<altitude>`  |       Save or set fixed position altitude
`DT=0\|<rate>`            | Disable or set rate of $DT messages
`GN=0\|<rate>`            | Disable or set rate of $GN messages
`GP=<gpio1_mode>`        | Set GPIO1 pin mode
`GS=0\|<rate>`            | Disable or set rate of $GS messages
`LA=S\|<latitude>`        | Save or set fixed position latitude
`LG=<led_mode>`         | Set operating mode for green LED
`LO=S\|<longitude>`      | Save or set fixed position longitude
`LR=<led_mode>`          | Set operating mode for red LED
`MD=I\|P`                 | Set msg delivery immediate (default) or polled
`MF=M\|F`                 | Set mobile or fixed (default) station mode
`RO=0\|1`                 | Disable/enable receive-only mode
`RP=0\|1`                 | Select radio profile
`SV=0\|1`                 | Disable/enable $SV messages
`TM=<YYYYMMDDhhmmss>`    | Set system time



<strong>Returns one of:</strong>

Value  | Description 
 ------------- | -------------
 `$OP OK*xx` | Parameters updated successfully
`$OP ERR*xx` | An error response


<strong>Notes:</strong>

The `?` option allows reading back the current settings. This is a comma separated list of all options. NOTE: Options are in alphabetical order, therefore as new options are added, they may appear in the middle of the string. The user application should NOT rely on any given option being at any given position; the string should be parsed using the comma as a delimiter, and the desired option retrieved by name.  Note that the `TM` option does not appear in the output string.

`<rate>` is a value between 1 and 2147483647 (2<sup>31</sup>-1). This is not a time in seconds, but rather a divider for each time the GPS emits the message.  This is typically once a second, but some messages may be emitted less frequently. If the GPS emits a particular message once
every 5 seconds, and the `<rate>` for that message is set to 2, the message will be emitted to the user every 10 seconds. The default rate for each message type is 60 (once per minute).
Messages for DT, GN, and GS will not be emitted to the user until the GPS has obtained a fully resolved fix.

The `AL` option allows specifying the altitude of the TileBEE prior to a GPS position fix being obtained, or saving the current GPS altitude as a default. The altitude is specified in meters, and may be a floating point number (although any precision past 2 digits will be ignored).
Altitude values less than -415 meters or greater than 10,000 meters will return an error.

This option should ONLY be used during development, and only in an environment where the TileBEE is unable to obtain an adequate GPS signal. The TileBEE requires an accurate GPS fix to properly calculate the positions of the satellites in the Swarm network. Regardless of the `AL` option being set, should an adequate GPS fix be acquired, the position reported by the GPS will be used.

Note that if the GPS does acquire a valid position fix, it does not overwrite the user-specified `AL` values. However, if the GPS fix is valid, the current GPS position may be saved as the `AL` default by using the `$OP AL=S` command.

The `GP` option allows specifying how the GPIO1 pin will operate. The available modes are:

Mode | Description
----- | -----
`0` | Analog, pin is internally disconnected and not used
`1` | Input, low-to-high transition exits TileBEE sleep mode
`2` | Input, high-to-low transition exits TileBEE sleep mode
`3` | Output, low indicates TileBEE is in sleep mode <strong>(1)</strong>
`4` | Output, high indicates TileBEE is in sleep mode <strong>(1)</strong>
`5` | Output, low indicates TileBEE is in sleep mode <strong>(2)</strong>
`6` | Output, high indicates TileBEE is in sleep mode <strong>(2)</strong>
`7` | Output, low indicates TileBEE has messages pending for client <strong>(3)</strong>
`8` | Output, high indicates TileBEE has messages pending for client <strong>(3)</strong>
`9` | Output, set low <strong>(4)</strong>
`10` | Output, set high <strong>(4)</strong>

It is the responsibility of the client hardware to provide the appropriate pull-up or pull-down resistors. The output modes are open collector.

<strong>(1)</strong> - If either of these modes are selected, the pin will be set to
the selected state after the client has issued the `$SL` command. The
pin will continue to indicate the sleep state during the times the TileBEE
wakes to perform any internal housekeeping funtions, and return to the
awake state only if the the sleep mode is terminated by the `S` or `T`
parameter being reached, a GPIO wakeup (if configured), or activity on
the serial RX line.

<strong>(2)</strong> - If either of these modes are selected, the pin will be set to
the selected state after the client has issued the `$SL` command. The
pin will change to the awake state if the sleep mode is terminated (as
described in <strong>(1)</strong>, or when then TileBEE wakes to perform internal house-
keeping functions. In the latter case, the pin will return to the sleep
mode indication once the TileBEE has completed its house-keeping
functions and returns to sleep.

<strong>(3)</strong> - If either of these modes are selected, the pin will indicate
if the TileBEE has received one or more unread messages and is holding
them for the client.  If multiple messages are pending for the client,
the pin will maintain the state until all messages have been read.
This is only supported when the `MD=P` option is specified.

<strong>(4)</strong> - These two variations allow the user application to use GPIO1
as a general purpose output.


The `LA` option allows specifying the latitude of the TileBEE prior to a
GPS position fix being obtained, or saving the current GPS latitude as
a default. The latitude is specified in decimal degrees, with western
latitudes as a negative value, (e.g., the Georgia Aquarium, located in
Atlanta, GA, USA, is roughly 33.763314, -84.394279, at an altitude of
301 meters). The latitude is truncated to 6 digits of accuracy. Values less than
-90.00 or greater than 90.00 will return an error.

The `LG` option sets the operating mode for the green LED. The
available modes are:

Mode | Description
----- | -----
`0` | LED is off
`1` | LED is on
`2` | LED blinks 1 sec on/1 sec off until GPS fix acquired
`3` | LED follows GPS 1PPS output
`4` | LED is on when LoRa radio is transmitting
`5` | LED is on when LoRa radio is has received packet
`6` | LED is on when TileBEE is awake <strong>(1)</strong>
`7` | LED is heartbeat indicator (50ms on/4950ms off)

<strong>(1)</strong> - The LED will be lit when the TileBEE is awake, in both the user
mode and system mode. If the TileBEE is not put to sleep with the `$SL`
command, the LED will remain on. If the TileBEE is put to sleep with the
`$SL` command, the LED will be lit when the TileBEE wakes to perform
internal housekeeping tasks.

The `LO` option allows specifying the longitude of the TileBEE prior to a
GPS position fix being obtained, or saving the current GPS longitude
as a default. The longitude is specified in decimal degrees, with
southern longitudes as a negative value, (e.g., the Georgia Aquarium,
located in Atlanta, GA, USA, is roughly 33.763314, -84.394279, at an
altitude of 301 meters). The longitude is truncated to 6 digits of
accuracy. Values less than -180.0 or greater than 180.0 will return an
error.

The `LR` option sets the operating mode for the red LED. Please see
the `LG` option for the available modes.

The `MD` option allows setting whether messages received from the
hive are delivered immediately upon reception, or if they must be
polled for by the user via the `$RD` command.  When `MD` is set to `I`,
messages are delivered immediately via the unsolicited `$RD` message.
When `MD` is set to `P`, the user periodically needs to issue the
`$RD` command with one of the appropriate parameters.

The `MF` option specifies whether this station is a mobile or fixed
station. Fixed stations are permitted to use a user-defined latitude,
longitude, and altitude setting, whereas mobile stations require a
GPS position fix before a message may be transmitted. A fixed position
station allows the GPS to operate in a lower power mode, as it is not
moving about. Typically, a mobile station will want to configure the
`$DT`, `$GN`, and `$GS` commands to output more often than a fixed position
station.

The `RO` option places the TileBEE in receive-only mode. In this mode,
messages from satellites will be received but any data that would
normally be transmitted to the satellite will be discarded. If a `$TD`
command is issued to the TileBEE, the TileBEE will immediately return `$TX OK,<message ID>` and `$TX SENT,<message ID>`, as if the command had 
been sent. However, the TileBEE will never issue a `$TX HIVE,<message ID>`
as that requires a response from the hive.

The `RP` option allows selecting one of the two pre-defined radio
profiles. Unless explicitly instructed to do so by Swarm support
engineers, this option should not be changed. Changing it will most
likely result in permanent loss of communications with the satellite
network.

The `TM` option allows setting the system time in the event that the
GPS is unable to obtain a fix. The time MUST be GMT time, not the
local time (unless you happen to be in Greenwich, London), otherwise
the TileBEE will not be able to calculate satellite positions correctly.
Note that unlike other `$OP` options, the `TM` is not preserved when
power is removed from the TileBEE, or if the TileBEE is restarted via the
`RS` command.

This option should ONLY be used during development, and only in an
environment where the TileBEE is unable to obtain an adequate GPS signal.
The TileBEE requires an accurate GPS fix to properly calculate the
positions of the satellites in the Swarm network. Regardless of the
`TM` option being set, should an adequate GPS fix be acquired, the
system time will be updated to the time reported by the GPS.
The parameters are only updated if `OK` is returned. Should an error
occur in one or more parameters, `ERR` is returned and none of the
parameters are updated.  These settings are not retained across a
restart of the TileBEE.

The parameters are only updated if `OK` is returned. Should an error
occur in one or more parameters, `ERR` is returned and none of the
parameters are updated.  These settings are not retained across a
restart of the TileBEE.


## Restart TileBEE

This command restarts the TileBEE.

```
$RS*xx
```

<strong>Returns one of:</strong>

Value  | Description 
 ------------- | -------------
`$RS OK*xx` | Command has been accepted and the TileBEE will perform a hardware restart
`$RS ERR*xx` | An error message 

<strong>Notes:</strong>	
An `OK` response confirms that the TileBEE has restarted successfully. An `ERR` response indicates that additional or invalid characters were included between the `S` and the `*` of the command. 

## Sleep mode

This command puts the TileBEE into a low-power sleep mode.

```
$SL [S=<seconds>|U=<[YYYY-MM-DD ]hh:mm:ss>]*xx
```

Parameter  | Description 
 ------------- | ------------- 
`S=<seconds>` | Sleep for this many seconds
`U=<[YYYY-MM-DD ]hh:mm:ss>`  | Sleep until date (optional) and time

<strong>Returns one of:</strong>

Value  | Description 
 ------------- | -------------
`$SL OK*xx` |          Sleep period accepted, TileBEE is now non-responsive
`$SL WAKE,<cause>*xx` | TileBEE has woken from selected sleep mode
`$SL CLOCKNOTSET*xx`  | Clock not yet set from GPS
`$SL ERR*xx`      | Invalid number of seconds or date/time value
`$SL NOCOMMAND*xx` | No `S` or `U` parameter is present
`$SL ERR,NOTIME*xx` | Attempt to sleep before time is set


The `S` parameter is the number of seconds to sleep. This value may
range from 5 to 31536000 (approximately 1 year) seconds. A value not
within this range will return `$SL ERR`. If the command is accepted,
the TileBEE will emit `$SL OK` and enter sleep mode for the requested
duration.

The `U` parameter is a time and optional date the TileBEE should sleep
until and then wake. If the date is not specified and the time to
sleep until is less than the current time, the time is presumed to
be in the next day. For example, if the current time is 11:<zero-width space>00:<zero-width space>00 and
`$SL U=09:00:00` is issued, the TileBEE will wake 22 hours from now. If
a date and time are specified, and that date/time is before the
current date/time, `$SL WAKE` will be immediately issued.

The `$SL WAKE,<cause>` message is emitted after the TileBEE wakes from a
a user commanded sleep mode (as opposed to the TileBEE waking to perform
internal housekeeping and then returning to sleep). The value of `cause` will be
one of the following:

Cause  | Description 
 ------------- | -------------
`GPIO`    | GPIO input changed from inactive to active state
`SERIAL` | Activity was detected on the RX pin of the TileBEE's UART
`TIME`    | The `S` or `U` parameter time has been reached

If UART activity wakes the TileBEE, the `TIMEOUT` message will
not be emitted as the TileBEE is now awake.

In sleep mode, the real-time clock is not GPS disciplined,
and is therefore subject to some degree of drift. The longer the TileBEE
is asleep, the more the drift will accumulate. The user should be aware
of this when selecting a sleep with a long duration.

If the GPIO1 pin is configured as an input to wake the TileBEE,
the sleep mode will be terminated if activity occurs on GPIO1.

If the GPIO1 pin is configured as an output that indicates
the TileBEE's sleep mode, GPIO1 will transition to the appropriate state
if the `$SL OK` message is emitted.


<strong>Example:</strong>

Telling the TileBEE to sleep for 1 minute
```
SL S=60
$SL OK*3b
$SL WAKE,TIME @ 2019-04-11 18:58:03*7e
```

## Transmit data

This command transmits data to the Swarm network. 

```
$TD [HT=<hold_time>,][PR=<priority>,]<[string|data]>[..<data>]*xx
```	

Parameter  | Description 
 ------------- | ------------- 
`HT=<hold_time>` | Expiration time of message (optional, default = 3600 seconds)
`PR=<priority>`   | Priority of message (optional, default = 50)
`<string\|data>`   | 1 to 220 bytes of data

<strong>Returns one of:</strong>

Value  | Description 
 ------------- | -------------
`$TD OK,<msg_id>*xx`          | Message accepted for sending
`$TD SENT,<msg_id>*xx`        | Message sent over LoRa channel
`$TD HIVE,<msg_id>*xx`        | Hive acknowledged receiving message
`$TD ERR,BUSY,<msg_id>*xx`    | Channel is busy
`$TD ERR,BADDATA,0*xx`        | Message has odd number or non-hex characters
`$TD ERR,BADHOLDTIME,0*xx`    | Invalid hold time
`$TD ERR,BADPRIORITY,0*xx`    | Invalid priority
`$TD ERR,ERR,0*xx`            | Unspecified error
`$TD ERR,EXPIRED,<msg_id>*xx` | Unable to send within requested hold time
`$TD ERR,NOADDR,0*xx`         | The Swarm ID has not yet been set
`$TD ERR,NOCOMMAND,0*xx`      | `$TD` with no parameters was sent
`$TD ERR,NOSPACE,0*xx`        | No space for message
`$TD ERR,NOTCID,0*xx`         | The thin client ID has not yet been set
`$TD ERR,NOTIME,0*xx`         | Attempt to send message before time set
`$TD ERR,QUEUEFULL,0*xx`      | Queue for queued messages is full
`$TD ERR,TOOLONG,<msg_id>*xx` | Message is too large to send 

<strong>Notes:</strong>

The `HT` and `PR` parameters are optional, are position independent
(e.g., 'PR' may be specified before `HT`, or vice-versa), but must
occur before the `<data>` portion of the command.

`<hold_time>` is either the number of seconds to expire the message if
it has not been sent, or an epoch second date after which the message
will be expired if it has not been sent.  

Hold Time Value  | Description 
 ------------- | -------------
`0` | The message is sent immediately, regardless of whether or not a Swarm satellite is currently in view.
`1` to `31536000` | The message will be considered expired if a Swarm satellite has not come into view within the specified number of seconds.
`31536001` to `1514764800` | An error message (`$TD ERR,0*xx`) is returned.
>`1514764800` | The message will be considered expired if the TileBEE is unable to send it before the specified time. If the specified time is greater than `1514764800` and less than or equal to the current UTC time, the message will not be queued and an expired message `$TD EXPIRED,<msg_id>*xx` will be returned immediately. Note: `1514764800` is equal to 2018-01-01 00:<zero-width space>00:<zero-width space>00 in epoch seconds. 
None provided | A default hold time of `3600` seconds will be used.

`<priority>` specifies the priority of the message, and may be between 0
and 100. A higher number indicates a higher priority. If `<priority>` is
not specified, the default is 50. If `<priority>` is specified but not
`<hold_time>`, there must be a leading comma, e.g. `$TD ,40,<data>`,
otherwise the 40 would be interpreted as the `<hold_time>` value.

`<string|data>` may be expressed one of two different ways. If all the
data to be sent is in the ASCII character range from 0x20 (space) to
0x7e (tilde), then the data may be sent as a string. A string is
specified by enclosing the data in double quotes, e.g., "Hello,
world". It is permissible for the string to contain double quotes
within the string, e.g., "Today is a "new" day". If the data to be
sent includes one or more character outside the 0x20 to 0x7e range,
then it must be specified as pairs of hex characters ('0'..'9',
'A'..'F', 'a'..'f'), and must be a multiple of 2. Sending 'Hello' as
hex would be 48656C6C6F. Illegal characters or an odd number of
characters will cause a `BADDATA` message to be returned.

`<msg_id>` is assigned by the TileBEE, and is an unsigned 64-bit value
comprised of the device ID, a day of year counter, and a message of
day counter.  Responses that have a 0 as the message ID indicates the
message has not been placed in the queue and therefore has no ID. The
value should be treated as a simple arbitrary number.

<strong>Example:</strong>

Sending a message from the TileBEE
```
TD "Hello World!"
$TD OK,5354468575916*3b
$TD SENT,5354468575916*24
$TD HIVE,5354468575916*27
```


