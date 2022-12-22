function Container = QArmMakeRequestGripperObject(DeviceNumber) %#codegen

%skip size for now

Container = flip(typecast(int32(10), 'uint8')); %Device ID
Container = [Container flip(typecast(int32(DeviceNumber), 'uint8'))];
Container = [Container uint8(50)]; %Device function
%No payload

%Prepend container size
Container = [flip(typecast(int32(length(Container) + 4), 'uint8')) Container]';