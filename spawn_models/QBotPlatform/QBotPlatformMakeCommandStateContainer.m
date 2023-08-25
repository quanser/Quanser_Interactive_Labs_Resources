function Container = QBotPlatformMakeCommandStateContainer(DeviceNumber, WheelSpeeds, LeftColor, RightColor) %#codegen

%skip size for now

Container = flip(typecast(int32(23), 'uint8')); %Device ID
Container = [Container flip(typecast(int32(DeviceNumber), 'uint8'))];
Container = [Container uint8(10)]; %Device function
Container = [Container flip(typecast(single(WheelSpeeds(1)), 'uint8'))];
Container = [Container flip(typecast(single(WheelSpeeds(2)), 'uint8'))];
Container = [Container flip(typecast(single(LeftColor(1)), 'uint8'))];
Container = [Container flip(typecast(single(LeftColor(2)), 'uint8'))];
Container = [Container flip(typecast(single(LeftColor(3)), 'uint8'))];
Container = [Container flip(typecast(single(RightColor(1)), 'uint8'))];
Container = [Container flip(typecast(single(RightColor(2)), 'uint8'))];
Container = [Container flip(typecast(single(RightColor(3)), 'uint8'))];

%Prepend container size
Container = [flip(typecast(int32(length(Container) + 4), 'uint8')) Container]';