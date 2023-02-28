function [Target, Actual] = QArmDecodeEndEffectorCollisionSpheres(Payload, StartIndex) %#codegen

Target = [single(0); single(0); single(0)];
Actual = [single(0); single(0); single(0)];

Target(1) = typecast(uint8(flip(Payload(StartIndex:StartIndex+3))), 'single');
Target(2) = typecast(uint8(flip(Payload(StartIndex+4:StartIndex+7))), 'single');
Target(3) = typecast(uint8(flip(Payload(StartIndex+8:StartIndex+11))), 'single');
Actual(1) = typecast(uint8(flip(Payload(StartIndex+12:StartIndex+15))), 'single');
Actual(2) = typecast(uint8(flip(Payload(StartIndex+16:StartIndex+19))), 'single');
Actual(3) = typecast(uint8(flip(Payload(StartIndex+20:StartIndex+23))), 'single');