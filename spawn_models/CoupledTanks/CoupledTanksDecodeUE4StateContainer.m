function [Tank1Disturbance] = CoupledTanksDecodeUE4StateContainer(Payload, StartIndex) %#codegen

Tank1Disturbance = single(0);

Tank1Disturbance = typecast(uint8(flip(Payload(StartIndex:StartIndex+3))), 'single');