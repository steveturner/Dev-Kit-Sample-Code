# Overview of TileBEE Software Interface

<h3>Message types</h3>

The TileBEE transmits two types of messages: 

- [Unsolicited messages](unsolicited.md), which include status messages, date/time and GPS information, and notifications that messages have been received by the TileBEE
- [Command responses](command.md), which include responses to message and power management commands, as well as notifications that messages have been sent or settings have been updated

<h3>General command structure</h3>

All messages to and from the TileBEE end with a `*xx`, where `xx` is a checksum of the characters in the command from next character after the `$` up to, but not including, the `*`. The checksum is the same as used by NMEA. Messages with a bad checksum are silently ignored. 

A `$` will never occur within a command, and may be used to reset the receiving state machine.

A `*` may occur within a command. The receiving state machine will verify the last three characters in the command are `*xx` after the `\n` is received. The `x` may be any legal ASCII character in the range `0..9`, `A..F`, or `a..f`.

<h3>Command timing</h3>

Once the `$` is received, the next character must occur within 5 milliseconds of the previous character. If the inter-character delay exceeds 5 ms, the command will be silently discarded, and the receiving state machine will consume and ignore any characters received until the next `$`.

<h3>Additional notes</h3>

The user application connected to the TileBEE should ignore any characters received from the tile after startup until the `$EGT BOOT*60` string is received. The EGT's bootloader will output messages as it starts up. These messages include, but are not limited to, status messages, firmware update progress messages, and error messages.


