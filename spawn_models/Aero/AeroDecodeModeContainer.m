function [YawLocked, PitchLocked, HeliMode, PropMode] = AeroDecodeModeContainer(Payload, StartIndex) %#codegen

YawLocked = uint8(Payload(StartIndex));
PitchLocked = uint8(Payload(StartIndex+1));
HeliMode = uint8(Payload(StartIndex+2));
PropMode = uint8(Payload(StartIndex+3));
