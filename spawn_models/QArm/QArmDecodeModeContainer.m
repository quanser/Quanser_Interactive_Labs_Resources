function [Mode] = QArmDecodeModeContainer(Payload, StartIndex) %#codegen

Mode = uint8(Payload(StartIndex));
