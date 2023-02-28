function [WeightOffset0, WeightOffset1] = Aero2DecodeCommandAckContainer(Payload, StartIndex) %#codegen


WeightOffset0 = single(0);
WeightOffset1 = single(0);

WeightOffset0 = typecast(uint8(flip(Payload(StartIndex:StartIndex+3))), 'single');
WeightOffset1 = typecast(uint8(flip(Payload(StartIndex+4:StartIndex+7))), 'single');
