function [Location, Forward, Up, BumpForward, BumpLeft, BumpRight, Gyro, Heading, EncoderLeft, EncoderRight] = QBotPlatformDecodeUE4StateContainer(Payload, StartIndex) %#codegen

Location = [single(0); single(0); single(0)];
Forward = [single(0); single(0); single(0)];
Up = [single(0); single(0); single(0)];
BumpForward = uint8(0);
BumpLeft = uint8(0);
BumpRight = uint8(0);
Gyro = single(0);
Heading = single(0);

Location(1) = typecast(uint8(flip(Payload(StartIndex:StartIndex+3))), 'single');
Location(2) = typecast(uint8(flip(Payload(StartIndex+4:StartIndex+7))), 'single');
Location(3) = typecast(uint8(flip(Payload(StartIndex+8:StartIndex+11))), 'single');

Forward(1) = typecast(uint8(flip(Payload(StartIndex+12:StartIndex+15))), 'single');
Forward(2) = typecast(uint8(flip(Payload(StartIndex+16:StartIndex+19))), 'single');
Forward(3) = typecast(uint8(flip(Payload(StartIndex+20:StartIndex+23))), 'single');

Up(1) = typecast(uint8(flip(Payload(StartIndex+24:StartIndex+27))), 'single');
Up(2) = typecast(uint8(flip(Payload(StartIndex+28:StartIndex+31))), 'single');
Up(3) = typecast(uint8(flip(Payload(StartIndex+32:StartIndex+35))), 'single');

BumpForward = uint8(Payload(StartIndex+36));
BumpLeft = uint8(Payload(StartIndex+37));
BumpRight = uint8(Payload(StartIndex+38));

Gyro = typecast(uint8(flip(Payload(StartIndex+39:StartIndex+42))), 'single');
Heading = typecast(uint8(flip(Payload(StartIndex+43:StartIndex+46))), 'single');
EncoderLeft = typecast(uint8(flip(Payload(StartIndex+47:StartIndex+50))), 'int32');
EncoderRight = typecast(uint8(flip(Payload(StartIndex+51:StartIndex+54))), 'int32');