function [ObjectID, Mass, PropertyString] = QArmDecodeGripperObject(Payload, StartIndex) %#codegen

ObjectID = uint8(Payload(StartIndex));
Mass = typecast(uint8(flip(Payload(StartIndex+1:StartIndex+4))), 'single');
StringSize = typecast(uint8(flip(Payload(StartIndex+5:StartIndex+8))), 'int32');
PropertyString = char(Payload(StartIndex+9:StartIndex+9+StringSize));
