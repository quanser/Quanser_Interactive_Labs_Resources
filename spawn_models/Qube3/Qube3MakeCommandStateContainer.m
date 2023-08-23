function Container = Qube3MakeCommandStateContainer(DeviceNumber, MotorAngle, PendulumAngle, BaseColor_v3) %#codegen

%skip size for now

Container = flip(typecast(int32(61), 'uint8')); %Device ID
Container = [Container flip(typecast(int32(DeviceNumber), 'uint8'))];
Container = [Container uint8(10)]; %Device function
Container = [Container flip(typecast(single(MotorAngle), 'uint8'))];
Container = [Container flip(typecast(single(PendulumAngle), 'uint8'))];
Container = [Container flip(typecast(single(BaseColor_v3(1)), 'uint8'))];
Container = [Container flip(typecast(single(BaseColor_v3(2)), 'uint8'))];
Container = [Container flip(typecast(single(BaseColor_v3(3)), 'uint8'))];

%Prepend container size
Container = [flip(typecast(int32(length(Container) + 4), 'uint8')) Container]';