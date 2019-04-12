import serial #pySerial is not native to python distributions, and needs to be downloaded: https://pyserial.readthedocs.io/en/latest/index.html
import random
import time
import math
import argparse




def column(matrix, i):
    return [row[i] for row in matrix]

def sendMessage(data): #function to format and send message through 'TD' command
	current_message = str(data) 
	message = "%TD "+'"'+current_message+'"\r' #very important to include carriage return (enter key, \r) or newline (\n) in every sent message for TileBEE to acknowlege
	message_list.append([current_message,"",0,0,0]) #adds a line in database with message contents for analysis at end of script
	ser.write(message.encode()) #encode all messages to byte strings


def randomPayload(num): #generates a random sequence of characters from chars list 
	payload = ""
	for i in range (0, num):
		currentChar = random.sample(range(0,len(chars)),1)
		payload = payload + chars[currentChar[0]]
	return payload

def numberedMessage(num, total, data): #formats message to include message number (ex: 1/100 hJl42H)
	message = str(num)+"/"+str(total)+" "+data
	return message


def readLine(): #reads lines in connection and returns line if not empty
	line = ser.readline().decode()
	if len(line)>0:
		if line[0] == '$':
			line = line[1:]
		if len(line)>2:
			return line

def lineInterpret(line): #logic to interpret output from TileBEE
	preamble = ""
	printline = ""
	preamble = line[0:2]
	if(preamble=='TD'): #logic for 'TD' responses
		if line[3:5] == 'OK': #TD,OK - means that the message was accepted by the TileBEE and it is in the queue to be sent to the StratoBEE
			message_ID = line[6:-4]
			printline = "Message accepted by TileBEE. Message ID: "+message_ID
			message_list[-1][1] = message_ID #adds message ID to database
			message_list[-1][2] = 1 #value indicating message was successfully sent to TileBEE
		elif line[3:7] == 'SENT': #TD,SENT - message was sent to StratoBEE
			message_ID = line[8:-4]
			try:
				index = column(message_list,1).index(message_ID) #looks for message ID in database. If it's not there, then it is likely from an earlier test
				message_list[index][3] = 1 #value indicating message was transmitted to StratoBEE
				printline = "Message sent to StratoBEE. Message ID: "+message_ID
			except IndexError as error:
				printline = "Message ID: "+message_ID+" is not found. Message was sent to StratoBEE"
			except Exception as exception:
				printline = "Message ID: "+message_ID+" is not found. Message was sent to StratoBEE"
		elif line[3:7] == 'HIVE': #TD,HIVE - ACK packet from Hive indicating that it was received by Hive
			message_ID = line[8:-4]
			try:
				index = column(message_list,1).index(message_ID)
				message_list[index][4] = 1 #Value indicating message was ACK'ed by Hive
				printline = "Message acknowleged by Hive. Message ID: "+message_ID
			except IndexError as error:
				printline = "Message ID: "+message_ID+" is not found. Message was acknowleged by Hive"
			except Exception as exception:
				printline = "Message ID: "+message_ID+" is not found. Message was acknowleged by Hive"
		elif line[3:4] == '"':
			printline = "Attempting to send message to TileBEE: "+line[3:]
		else:
			printline ="Error - "+line
	elif(preamble=='DT' and mute_unsolicited == 0): #logic for 'DT' unsolicitied response
		if line[3:4] == '2':
			parse = line[3:-4].split(',')
			if parse[-1] == 'V':
				printline = "Date/Time Message from TileBEE. Date is "+parse[0]+"-"+parse[1]+"-"+parse[2]+", at "+parse[3]+":"+parse[4]+":"+parse[5]+" GMT. The Date/Time is VALID"
			else:
				printline = "Date/Time is INVALID - "+line		
		else:
			printline = "Date/Time error - "+line		
	elif(preamble=='GN' and mute_unsolicited == 0): #logic for 'GN' unsolicited response
		if len(line)>10:
			parse = line[3:-4].split(',')
			printline = "GPS Message from TileBEE. Latitude: "+parse[0]+", Longitude: "+parse[2]+", Altitude: "+parse[4]+"m, Speed: "+parse[5]+"kph, Course: "+parse[6]+" degrees"
		else:
			printline = "GPS error - "+line	
	elif(preamble=='GS' and mute_unsolicited == 0): #logic for 'GS' unsolicited response
		if len(line)>8:
			parse = line[3:-4].split(',')
			if parse[-1] == "NF":
				fix_type = "No fix"
			elif parse[-1] == "DR":
				fix_type = "Dead reckoning"
			elif parse[-1] == "G2":
				fix_type = "Standalone 2S solution"
			elif parse[-1] == "G3":
				fix_type = "Standalone 3D solution"
			elif parse[-1] == "D2":
				fix_type = "Differential 2D solution"
			elif parse[-1] == "D3":
				fix_type = "Differential 3D solution"
			elif parse[-1] == "RK":
				fix_type = "Combined GPS and dead reckoning solution"
			else:
				fix_type = "Time only solution"	
			printline = "Geospatial Message from TileBEE. hdop: "+parse[0]+", vdop: "+parse[1]+", # of GPS satellites used in solution: "+parse[2]+", # of GLONASS satellites used in solution: "+parse[3]+", fix type: "+fix_type
		else:
			printline = "Geospatial error - "+line		
	elif(mute_unsolicited == 0):
		printline ="Error - other - "+line
	if printline:
		print(printline)


maxChars = 210
chars = """qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"""
ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM3'#sets the serial port that the TileBEE is on
ser.bytesize = 8
ser.parity = 'N'
ser.stopbits = 1
ser.timeout = 1

start_time = time.time()
num_messages = 10 #total number of messages to be sent
message_rate = 30 #number of seconds in between each message
wait_time = 20 #minutes
message_list = [["message","messageID","sent To TileBEE","sent to StratoBEE","acknowleged by Hive"]]
current_message = ""
messages_length = 0
packet_size = maxChars #sets the packet size of each randmoized message
message_current = 0
mute_unsolicited = 0 #if set to 1, will mute all non-transmission related messages

parser = argparse.ArgumentParser()
parser.add_argument("serialPortName")
parser.add_argument("numberOfMessages")
parser.add_argument("packetSize")
parser.add_argument("messageRate")
parser.add_argument("muteUnsolicitedMessages")
args = parser.parse_args()

ser.port = args.serialPortName
num_messages = min(int(args.numberOfMessages), 50)
packet_size = min(int(args.packetSize), maxChars)
message_rate = int(args.messageRate)
mute_unsolicited = int(args.muteUnsolicitedMessages)

ser.open()




while message_current<num_messages: #while loop to send messages every x seconds
	current_time = time.time()-start_time
	if current_time>=message_current*message_rate:
		sendMessage(numberedMessage(message_current+1,num_messages,randomPayload(packet_size))) #sends message with random payload
		message_current=message_current+1
	currentline = readLine() #constantly reads lines from TileBEE
	if (type(currentline) is str):
		lineInterpret(currentline)


print("\nWaiting up to "+str(wait_time)+" minutes to allow packets to go to/from the Hive ...\n") #waits (typically 10) minutes to allow packets to go to/from Hive
start_time = time.time()

while time.time()-start_time<wait_time*60:
	currentline = readLine()
	if (type(currentline) is str):
		lineInterpret(currentline)
	if sum(column(message_list[1:],4)) == num_messages:
		break
	
message_list = message_list[1:][:]
print("Test Done...") #below are statistics on number of messages accepted by TileBEE, sent to StratoBEE, and ACK'ed by Hive
for message in column(message_list,0):
	messages_length = messages_length+ len(message)
print("Number of sent messages: "+str(num_messages)+". Messages were sent every "+str(message_rate)+" seconds, with an average message size of "+str((messages_length/len(column(message_list,0))))+" characters")
print("Number of messages accepted by TileBEE: "+str(sum(column(message_list,2)))+"/"+str(num_messages)+" = "+str(round((sum(column(message_list,2))/num_messages)*10000)/100)+"%")
print("Number of messages sent to Hive: "+str(sum(column(message_list,3)))+"/"+str(num_messages)+" = "+str(round((sum(column(message_list,3))/num_messages)*10000)/100)+"%")
print("Number of messages acknowleged by Hive: "+str(sum(column(message_list,4)))+"/"+str(num_messages)+" = "+str(round((sum(column(message_list,4))/num_messages)*10000)/100)+"%")