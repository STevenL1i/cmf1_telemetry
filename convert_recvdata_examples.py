import sys
import struct
#data = b'\xe8\x07\x18\x01\x0e\x01\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00BUTN@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
data = b"\xe8\x07\x18\x01\x0e\x01\x019\x99u\x91\x9d\x02\x9b\x14\x1d\xdd\x0eB\xcd\x02\x00\x00\xcd\x02\x00\x00\x00\xff\x00-\x1e\x01 \x15\x12\x03\x00\x00\x00X\x02P\x00\x00\xff\x00\x11\xb1Lt?\x00XG\xdc=\x00\xfd\xe00>\x00z\xee\x81>\x00p'\xa4>\x00fo\xb4>\x00H\x9a\xc1>\x00\xbf\xfb\xd2>\x00\x83\x01\xe4>\x00\xee\x84\xf7>\x00\rf\x03?\x00\xe34 ?\x00\x81=)?\x00P\x8f1?\x00\x83\x01@?\x00\x03iM?\x00^\xfdc?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x05\x02\xdc\x02\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x01\x01\x03\x01\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x01\x01\x02\x00\xff\x00\xff\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa9\x93\xe1D\xc6`zE"





header_dict = dict()
########################################### resolve header ###########################################
### Packet Format
packetformat_byte = data[0:2]
packetformat = struct.unpack('<H', packetformat_byte)[0]
header_dict["Format"] = {"data": packetformat, "bytes": packetformat_byte}

### Game Year
gameyear_byte = data[2:3]
gameyear = struct.unpack('<B', gameyear_byte)[0]
header_dict["Game Year"] = {"data": gameyear, "bytes": gameyear_byte}

### Game Major Version
gameMajorVersion_byte = data[3:4]
gameMajorVersion = struct.unpack('<B', gameMajorVersion_byte)[0]
header_dict["Major Ver."] = {"data": gameMajorVersion, "bytes": gameMajorVersion_byte}

### game Minor version
gameMinorVersion_byte = data[4:5]
gameMinorVersion = struct.unpack('<B', gameMinorVersion_byte)[0]
header_dict["Minor Ver."] = {"data": gameMinorVersion, "bytes": gameMinorVersion_byte}

### packet version
packetVersion_byte = data[5:6]
packetVersion = struct.unpack('<B', packetVersion_byte)[0]
header_dict["Packet Ver."] = {"data": packetVersion, "bytes": packetVersion_byte}

### packet id (decide what kind of packet is it)
packetID_byte = data[6:7]
packetID = struct.unpack('<B', packetID_byte)[0]
header_dict["Packet ID"] = {"data": packetID, "bytes": packetID_byte}

### session UID
sessionUID_byte = data[7:15]
sessionUID = struct.unpack('<LL', sessionUID_byte)[0]
header_dict["sessionUID"] = {"data": sessionUID, "bytes": sessionUID_byte}

### session time
sessionTime_byte = data[15:19]
sessionTime = struct.unpack('<f', sessionTime_byte)[0]
header_dict["sessionTime"] = {"data": sessionTime, "bytes": sessionTime_byte}

### frame identifier
frameID_byte = data[19:23]
frameID = struct.unpack('<I', frameID_byte)[0]
header_dict["frameID"] = {"data": frameID, "bytes": frameID_byte}

### overall frame identifier
overallframeID_byte = data[23:27]
overallframeID = struct.unpack('<I', overallframeID_byte)[0]
header_dict["overallframeID"] = {"data": overallframeID, "bytes": overallframeID_byte}

### player car index
playerCarIndex_byte = data[27:28]
playerCarIndex = struct.unpack('<B', playerCarIndex_byte)[0]
header_dict["playerCarIndex"] = {"data": playerCarIndex, "bytes": playerCarIndex_byte}

### second player car index (=255 if no second player, only in splitscreen)
secondCarIndex_byte = data[28:29]
secondCarIndex = struct.unpack('<B', secondCarIndex_byte)[0]
header_dict["secondCarIndex"] = {"data": secondCarIndex, "bytes": secondCarIndex_byte}





session_dict = dict()
########################################### reslove session ###########################################

### weather
weather_byte = data[29:30]
weather = struct.unpack('<B', weather_byte)[0]
session_dict["weather"] = {"data": weather, "bytes": weather_byte}

### track temperature
trackTemp_byte = data[30:31]
trackTemp = struct.unpack('<B', trackTemp_byte)[0]
session_dict["trackTemp"] = {"data": trackTemp, "bytes": trackTemp_byte}

### air temperature
airTemp_byte = data[31:32]
airTemp = struct.unpack('<B', airTemp_byte)[0]
session_dict["airTemp"] = {"data": airTemp, "bytes": airTemp_byte}

### total laps
totalLaps_byte = data[32:33]
totalLaps = struct.unpack('<B', totalLaps_byte)[0]
session_dict["totalLaps"] = {"data": totalLaps, "bytes": totalLaps_byte}

### track length
trackLength_byte = data[33:35]
trackLength = struct.unpack('<H', trackLength_byte)[0]
session_dict["trackLength"] = {"data": trackLength, "bytes": trackLength_byte}

### session type
sessionType_byte = data[35:36]
sessionType = struct.unpack('<B', sessionType_byte)[0]
session_dict["sessionType"] = {"data": sessionType, "bytes": sessionType_byte}

### track id
trackID_byte = data[36:37]
trackID = struct.unpack('<B', trackID_byte)[0]
session_dict["trackID"] = {"data": trackID, "bytes": trackID_byte}

### formula car type
formula_byte = data[37:38]
formula = struct.unpack('<B', formula_byte)[0]
session_dict["formula"] = {"data": formula, "bytes": formula_byte}








# print data
col1, col2, col3 = 40, 30, 10
for k in header_dict.keys():
    print(f'{k:<{col1}}{header_dict[k]["data"]:<{col2}}{header_dict[k]["bytes"]}')
print("\n\n")
for k in session_dict.keys():
    print(f'{k:<{col1}}{session_dict[k]["data"]:<{col2}}{session_dict[k]["bytes"]}')
