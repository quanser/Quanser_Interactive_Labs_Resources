function [Yaw, Shoulder, Elbow, Wrist, FingerLP, FingerLD, FingerRP, FingerRD] = QArmDecodeSegmentCollisions(Payload, StartIndex) %#codegen


Yaw = single(bitget(Payload(StartIndex), 1));
Shoulder = single(bitget(Payload(StartIndex), 2));
Elbow = single(bitget(Payload(StartIndex), 3));
Wrist = single(bitget(Payload(StartIndex), 4));
FingerLP = single(bitget(Payload(StartIndex), 5));
FingerLD = single(bitget(Payload(StartIndex), 6));
FingerRP = single(bitget(Payload(StartIndex), 7));
FingerRD = single(bitget(Payload(StartIndex), 8));