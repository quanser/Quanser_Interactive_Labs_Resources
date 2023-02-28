function [Out2Connected, Tank1OutletSize, Tank2OutletSize] = CoupledTanksDecodeModeContainer(Payload, StartIndex) %#codegen

Out2Connected = uint8(Payload(StartIndex));
Tank1OutletSize = uint8(Payload(StartIndex+1));
Tank2OutletSize = uint8(Payload(StartIndex+2));

