function Container = QBotPlatformMakeCameraRequestContainer(DeviceNumber, CameraNumber) %#codegen

%skip size for now

Container = flip(typecast(int32(23), 'uint8')); %Device ID
Container = [Container flip(typecast(int32(DeviceNumber), 'uint8'))];
Container = [Container uint8(100)]; %Device function
Container = [Container uint8(CameraNumber)];
%No payload

%Prepend container size
Container = [flip(typecast(int32(length(Container) + 4), 'uint8')) Container]';