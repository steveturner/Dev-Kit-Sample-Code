# Sample Code

## Sending a message to the Hive

This example will walk you through sending a simple message <strong>Bees are awesome!</strong> from your TileBEE (in Developer's Kit) to the Hive

On your terminal of choice, enter:

```
%TD "Bees are awesome!"
```
Followed by the enter/return key. The `%` may not show up on your terminal - this is the character used to initiate character input over a serial connection. Immediately the following message will appear on your terminal:

```
$TD OK,534468609232*3b
```
This indicates that the message <strong>Bees are awesome!</strong> was valid, and was assigned a <strong>Message ID</strong> of 534468609232. The last bit (`*3b`) is just the checksum of the characters in the command - this will likely be different for every command sent/received. This message is now waiting to be sent to the StratoBEE. THe next message you will receive is:

```
$TD SENT,534468609232*44
```

This indicates that the message has been successfully sent to the StratoBEE. You may need to wait a few minutes (<5 minutes) until the StratoBEE initiates a conversation with your TileBEE. This siumlates a satellite coming over the horizon. After this you should see:

```
$TD HIVE,534468609232*9a
```
This indicates that the TileBEE has received an acknowlegment message from the Hive. Congratulations! You have sent your first message to the Hive. To verify this, log onto the [Hive](http://hive.swarm-technologies.com/hive/login) with your provided credentials, and click on the tab titled <strong>User Apps</strong>. Select the TileBEE's ID from the dropdown menu labeled <strong>Destination device</strong>, and then click the button labeled <strong>Show Data Received</strong>

## Receiving a message from the Hive

This example will walk you through sending a simple message <strong>Bees are great!</strong> from the Hive to your TileBEE.

Log onto the [Hive](http://hive.swarm-technologies.com/hive/login) with your provided credentials, and click on the tab titled <strong>User Apps</strong>. Select the TileBEE's ID from the dropdown menu labeled <strong>Destination device</strong>, and then enter <strong>Bees are great!</strong> into the text box labeled <strong>User App Data</strong>. After that, click the button labeled <strong>Send Data</strong>

After up to 5 minutes later, you will see the following message on your terminal:

```
$RD 7b2266223a226e756c6c222c2274223a226e756c6c222c2273223a226e756c6c222c226d223a226e756c6c227d*34
```

