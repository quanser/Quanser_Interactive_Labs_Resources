function Container = QArmMakeCommandStateContainer(DeviceNumber, Base, Shoulder, Elbow, Wrist, Gripper, BaseColor_v3, ArmBrightness) %#codegen

%skip size for now

Container = flip(typecast(int32(10), 'uint8')); %Device ID
Container = [Container flip(typecast(int32(DeviceNumber), 'uint8'))];
Container = [Container uint8(10)]; %Device function
Container = [Container flip(typecast(single(Base), 'uint8'))];
Container = [Container flip(typecast(single(Shoulder), 'uint8'))];
Container = [Container flip(typecast(single(Elbow), 'uint8'))];
Container = [Container flip(typecast(single(Wrist), 'uint8'))];
Container = [Container flip(typecast(single(Gripper), 'uint8'))];
Container = [Container flip(typecast(single(BaseColor_v3(1)), 'uint8'))];
Container = [Container flip(typecast(single(BaseColor_v3(2)), 'uint8'))];
Container = [Container flip(typecast(single(BaseColor_v3(3)), 'uint8'))];
Container = [Container flip(typecast(single(ArmBrightness), 'uint8'))];

%Prepend container size
Container = [flip(typecast(int32(length(Container) + 4), 'uint8')) Container]';