function Container = CoupledTanksMakeCommandStateContainer(DeviceNumber, ReservoirLevel, ReservoirToPumpLevel, TJunctionToTank1Level, Tank1Level, Tank1Inflow, Tank1to2Outflow, DisturbanceTapOutflow, DisturbanceTubeLevel, TJunctionToTank2Level, TJunctionToTank2Outflow, Tank2Level, Tank2Inflow, Tank2Outflow, PumpToTJunctionLevel, PumpFlow, Tank1RGBA, Tank2RGBA, ReservoirRGBA) %#codegen

%skip size for now

Container = flip(typecast(int32(30), 'uint8')); %Device ID
Container = [Container flip(typecast(int32(DeviceNumber), 'uint8'))];
Container = [Container uint8(10)]; %Device function
Container = [Container flip(typecast(single(ReservoirLevel), 'uint8'))];
Container = [Container flip(typecast(single(ReservoirToPumpLevel), 'uint8'))];
Container = [Container flip(typecast(single(PumpToTJunctionLevel), 'uint8'))];
Container = [Container flip(typecast(single(TJunctionToTank1Level), 'uint8'))];
Container = [Container flip(typecast(single(Tank1Level), 'uint8'))];
Container = [Container flip(typecast(single(Tank1Inflow), 'uint8'))];
Container = [Container flip(typecast(single(Tank1to2Outflow), 'uint8'))];
Container = [Container flip(typecast(single(DisturbanceTapOutflow), 'uint8'))];
Container = [Container flip(typecast(single(DisturbanceTubeLevel), 'uint8'))];
Container = [Container flip(typecast(single(TJunctionToTank2Level), 'uint8'))];
Container = [Container flip(typecast(single(TJunctionToTank2Outflow), 'uint8'))];
Container = [Container flip(typecast(single(Tank2Level), 'uint8'))];
Container = [Container flip(typecast(single(Tank2Inflow), 'uint8'))];
Container = [Container flip(typecast(single(Tank2Outflow), 'uint8'))];
Container = [Container flip(typecast(single(PumpFlow), 'uint8'))];

Container = [Container flip(typecast(single(Tank1RGBA(1)), 'uint8'))];
Container = [Container flip(typecast(single(Tank1RGBA(2)), 'uint8'))];
Container = [Container flip(typecast(single(Tank1RGBA(3)), 'uint8'))];
Container = [Container flip(typecast(single(Tank1RGBA(4)), 'uint8'))];

Container = [Container flip(typecast(single(Tank2RGBA(1)), 'uint8'))];
Container = [Container flip(typecast(single(Tank2RGBA(2)), 'uint8'))];
Container = [Container flip(typecast(single(Tank2RGBA(3)), 'uint8'))];
Container = [Container flip(typecast(single(Tank2RGBA(4)), 'uint8'))];

Container = [Container flip(typecast(single(ReservoirRGBA(1)), 'uint8'))];
Container = [Container flip(typecast(single(ReservoirRGBA(2)), 'uint8'))];
Container = [Container flip(typecast(single(ReservoirRGBA(3)), 'uint8'))];
Container = [Container flip(typecast(single(ReservoirRGBA(4)), 'uint8'))];

%Prepend container size
Container = [flip(typecast(int32(length(Container) + 4), 'uint8')) Container]';