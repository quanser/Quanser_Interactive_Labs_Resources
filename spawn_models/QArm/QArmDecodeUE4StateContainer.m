function [Base, Shoulder, Elbow, Wrist, Gripper, StaticEnvCollision, FingerpadDetection] = QArmDecodeUE4StateContainer(Payload, StartIndex) %#codegen

Base = typecast(uint8(flip(Payload(StartIndex:StartIndex+3))), 'single');
Shoulder = typecast(uint8(flip(Payload(StartIndex+4:StartIndex+7))), 'single');
Elbow = typecast(uint8(flip(Payload(StartIndex+8:StartIndex+11))), 'single');
Wrist = typecast(uint8(flip(Payload(StartIndex+12:StartIndex+15))), 'single');
Gripper = typecast(uint8(flip(Payload(StartIndex+16:StartIndex+19))), 'single');
StaticEnvCollision = uint8(Payload(StartIndex+20));
FingerpadDetection =  uint8(Payload(StartIndex+21:StartIndex+24));
