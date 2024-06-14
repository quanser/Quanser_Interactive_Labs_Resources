% Weather Example
% -------------------------
% 
% .. note::
% 
%     Make sure you have Quanser Interactive Labs open before running this
%     example.  This example is designed to best be run in QCar Cityscape

close all;
clear all;
clc;

% --------------------------------------------------------------
% Setting MATLAB Path for the libraries
% Always keep at the start, it will make sure it finds the correct references
newPathEntry = fullfile(getenv('QAL_DIR'), 'libraries', 'matlab', 'qvl');
pathCell = regexp(path, pathsep, 'split');
if ispc  % Windows is not case-sensitive
  onPath = any(strcmpi(newPathEntry, pathCell));
else
  onPath = any(strcmp(newPathEntry, pathCell));
end

if onPath == 0
    path(path, newPathEntry)
    savepath
end
% --------------------------------------------------------------
fprintf('\n\n----------------- Communications -------------------\n\n');

qlabs = QuanserInteractiveLabs();
connection_established = qlabs.open('localhost');

if connection_established == false
    disp("Failed to open connection.")
    return
end


disp('Connected')

num_destroyed = qlabs.destroy_all_spawned_actors();

fprintf('%d actors destroyed', num_destroyed);


hSystem = QLabsSystem(qlabs);


%%% Outdoor Environment
fprintf("\n\n---Outdoor Environment---")

hEnvironmentOutdoors2 = QLabsEnvironmentOutdoors(qlabs);
hEnvironmentOutdoors2.set_outdoor_lighting(0)

% Create a camera at spawn location to allow us to see the weather changes
hCameraWeather = QLabsFreeCamera(qlabs);
x = hCameraWeather.spawn([0.075, -8.696, 1.576], [0, -0.141, 1.908]);
hCameraWeather.possess()

pause(2.5);

% Run through different weather possibilities in QLabs
hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.CLEAR_SKIES)
hSystem.set_title_string('Clear skies')
pause(2.5);

hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.PARTLY_CLOUDY)
hSystem.set_title_string('Partly cloudy')
pause(2.5);

hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.CLOUDY)
hSystem.set_title_string('Cloudy')
pause(2.5);

hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.OVERCAST)
hEnvironmentOutdoors2.set_outdoor_lighting(1)
hSystem.set_title_string('Overcast')
pause(2.5);

hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.FOGGY)
hSystem.set_title_string('Foggy')
pause(2.5);

hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.LIGHT_RAIN)
hEnvironmentOutdoors2.set_outdoor_lighting(0)
hSystem.set_title_string('Light rain')
pause(2.5);

hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.RAIN)
hEnvironmentOutdoors2.set_outdoor_lighting(1)
hSystem.set_title_string('Rain')
pause(2.5);

hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.THUNDERSTORM)
hSystem.set_title_string('Thunderstorm')
pause(2.5);

hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.LIGHT_SNOW)
hEnvironmentOutdoors2.set_outdoor_lighting(0)
hSystem.set_title_string('Light snow')
pause(2.5);

hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.SNOW)
hEnvironmentOutdoors2.set_outdoor_lighting(1)
hSystem.set_title_string('Snow')
pause(2.5);

hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.BLIZZARD)
hSystem.set_title_string('Blizzard')
pause(2.5);

hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.PARTLY_CLOUDY)
hEnvironmentOutdoors2.set_outdoor_lighting(0)
hSystem.set_title_string('QLABS WEATHER')


fprintf("\n\n------------------------------ Communications --------------------------------\n")

qlabs.close()
disp("Done!")



