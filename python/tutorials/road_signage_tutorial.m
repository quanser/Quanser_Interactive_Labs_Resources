% Road signage Library Example
% -------------------------
% 
% .. note::
% 
%     Make sure you have Quanser Interactive Labs open before running this
%     example.  This example is designed to best be run in QCar Cityscape
%     or Cityscape Lite

close all;
clear all;
clc;

fprintf('\n\n------------------------------ Communications --------------------------------\n\n');

qlabs = QuanserInteractiveLabs();
connection_established = qlabs.open('localhost');

if connection_established == false
    disp("Failed to open connection.")
    return
end


disp('Connected')

num_destroyed = qlabs.destroy_all_spawned_actors();

fprintf('%d actors destroyed', num_destroyed);

%set any of these flags to False if you don't want to see the output
CROSSWALK_FLAG = 1;
ROUNDABOUT_FLAG = 1;
YIELDSIGN_FLAG = 1;
STOPSIGN_FLAG = 1;
TRAFFICCONE_FLAG = 1;
TRAFFICLIGHT_FLAG = 1;

function crosswalk(qlabs)
    % This function demonstrates some basic commands with the crosswalk class

    % initialize a camera - See Camera Actor Library Reference for more information
    cameraCrosswalk = QLabsFreeCamera(qlabs);
    cameraCrosswalk.spawn([-19.286, 43, 5.5], [-0, 0.239, -0.043]);
    cameraCrosswalk.possess();

    % create a crosswalk in this qlabs instance
    crosswalk = QLabsCrosswalk(qlabs);

    % spawn crosswalk with radians in config
    crosswalk.spawn_id(0, [-10.788, 45, 0.00], [0, 0, pi/2], [1, 1, 1], 0, 1);
    % waits so we can see the output
    pause(1);
    % spawn crosswalk with degrees in config 1
    crosswalk.spawn_id_degrees(1, [-6.788, 45, 0.00], [0, 0, 90], [1, 1, 1], 1, 1);
    % waits so we can see the output
    pause(1);
    % spawn crosswalk with degrees in config 2
    crosswalk.spawn_id_degrees(2, [-2.8, 45, 0.0], [0, 0, 90], [1, 1, 1], 2, 1);

    % collecting the world transform coordinates of the crosswalk
    [x, loc, rot, scale] = crosswalk.get_world_transform();
    disp([x, loc, rot, scale]);

    % pinging existing sign - this should return True if we printed it
    crosswalk.ping();
end

function roundabout_sign(qlabs)
    % Create two roundabouts in this qlabs instance
    roundabout = QLabsRoundaboutSign(qlabs);
    roundabout2 = QLabsRoundaboutSign(qlabs);

    % Spawn the sign using radians and specifying the actorNumber
    roundabout.spawn_id(0, [-17, 29, 0.0], [0, 0, pi], [1, 1, 1], 0, 1);
    % Spawn the second sign using degrees and allowing the computer to
    % generate an actorNumber internally
    roundabout2.spawn_id_degrees(2, [-15, 29, 0.0], [0, 0, 180], [1, 1, 1], 0, 1);

    % Collecting the world transform coordinates of the roundabout sign
    [x, loc, rot, scale] = roundabout2.get_world_transform();
    disp(['x: ', num2str(x)]);
    disp(['Location: ', num2str(loc)]);
    disp(['Rotation: ', num2str(rot)]);
    disp(['Scale: ', num2str(scale)]);

    % Pinging existing sign
    roundabout2.ping();
    % Wait to see the output
    pause(1);

    % Destroying the sign we just created
    roundabout.destroy();
end

function yield_sign(qlabs)
    % Create two yield signs in this qlabs instance
    yieldsign = QLabsYieldSign(qlabs);
    yieldsign2 = QLabsYieldSign(qlabs);

    % Spawn the sign using radians and specifying the actorNumber
    yieldsign.spawn_id(0, [-17, 31, 0.0], [0, 0, pi], [1, 1, 1], 0, 1);
    % Spawn the second sign using degrees and allowing the computer to
    % generate an actorNumber internally
    yieldsign2.spawn_degrees([-15, 31, 0.0], [0, 0, 180], [1, 1, 1], 0, 1);

    % Collecting the world transform coordinates of the yield sign
    [x, loc, rot, scale] = yieldsign2.get_world_transform();
    disp(['x: ', num2str(x)]);
    disp(['Location: ', num2str(loc)]);
    disp(['Rotation: ', num2str(rot)]);
    disp(['Scale: ', num2str(scale)]);

    % Pinging existing sign
    yieldsign2.ping();
    % Wait to see the output
    pause(1);

    % Destroying the sign we just created
    yieldsign.destroy();
end

function stop_sign(qlabs)
    % Create two stop signs in this qlabs instance
    stop = QLabsStopSign(qlabs);
    stop2 = QLabsStopSign(qlabs);

    % Spawn the sign using radians
    stop.spawn_id(1, [-16, 30, 0.0], [0, 0, pi], [1, 1, 1], 0, 1);
    % Spawn the second sign using degrees and allowing the computer to
    % generate an actorNumber internally
    stop2.spawn_degrees([-15, 30, 0.0], [0, 0, 180], [1, 1, 1], 0, 1);

    % Collecting the world transform coordinates of the stop sign
    [x, loc, rot, scale] = stop2.get_world_transform();
    disp(['x: ', num2str(x)]);
    disp(['Location: ', num2str(loc)]);
    disp(['Rotation: ', num2str(rot)]);
    disp(['Scale: ', num2str(scale)]);

    % Pinging existing sign
    stop2.ping();
    % Wait to see the output
    pause(1);

    % Destroying the sign we just created
    stop.destroy();
end

function traffic_cone(qlabs)
    % Create 5 cones in this qlabs instance
    cone = QLabsTrafficCone(qlabs);
    cone1 = QLabsTrafficCone(qlabs);
    cone2 = QLabsTrafficCone(qlabs);
    cone3 = QLabsTrafficCone(qlabs);
    cone4 = QLabsTrafficCone(qlabs);

    % Spawn a small traffic cone using radians
    cone.spawn([-17, 28, 1.0], [0, 0, pi], [1, 1, 1], 0, 1);
    % Wait to see the output
    pause(1);

    % Destroy the cone
    cone.destroy();
    % Wait to see the output
    pause(1);

    % Spawn another small traffic cone using radians in the same place
    cone1.spawn_id(1, [-17, 28, 1.0], [0, 0, pi], [1, 1, 1], 0, 1);
    % Spawn a construction pylon using degrees and generating the actorNumber internally
    cone2.spawn_degrees([-15, 28, 1.0], [0, 0, 180], [1, 1, 1], 1, 1);
    % Spawn a small cone with one color stripe initialized using actor number and a position in degrees
    cone3.spawn_id_degrees(3, [-15, 26.5, 1.0], [0, 0, 90], [1, 1, 1], 2, 1);
    % Spawn a bigger cone with two color stripes using radians and generating the actorNumber internally
    cone4.spawn([-17, 26.5, 1.0], [0, 0, pi/4], [1, 1, 1], 3, 1);

    % Wait to see the output
    pause(1.5);

    % % Change the color of the cones (materialSlot 0 is the base color, and 1 is the stripes)
    % cone1.set_material_properties(0, [0, 0, 1], 1);
    % % Wait to see the output
    % pause(0.5);
    % 
    % cone2.set_material_properties(0, [1, 0, 0], 1, 0);
    % cone2.set_material_properties(1, [1, 0.5, 0]);
    % pause(0.5);
    % 
    % cone3.set_material_properties(0, [0, 1, 1]);
    % cone3.set_material_properties(1, [0, 0.3, 1], 1, 1);
    % pause(0.5);
    % 
    % cone4.set_material_properties(0, [1, 0, 1], 0, 0);
    % cone4.set_material_properties(1, [0.3, 0, 1]);
    
    % Wait to see the output
    pause(3);

    % Collecting the world transform coordinates of the traffic cone
    [x, loc, rot, scale] = cone2.get_world_transform();
    disp(['x: ', num2str(x)]);
    disp(['Location: ', num2str(loc)]);
    disp(['Rotation: ', num2str(rot)]);
    disp(['Scale: ', num2str(scale)]);

    % Pinging existing cone
    cone2.ping();
end

function traffic_light(qlabs)
    % Initialize a camera
    cameraTraffic = QLabsFreeCamera(qlabs);
    cameraTraffic.spawn([0.131, 2.05, 2.047], [0, -0.068, 1.201]);
    cameraTraffic.possess();

    % Initialize three traffic light instances in qlabs
    trafficLight = QLabsTrafficLight(qlabs);
    trafficLight2 = QLabsTrafficLight(qlabs);
    trafficLight3 = QLabsTrafficLight(qlabs);

    % Spawn a traffic light in config 1 - vertical using radians and specifying a specific actorNumber
    trafficLight.spawn_id(0, [5.616, 14.131, 0.215], [0, 0, 0], [1, 1, 1], 0, 1);
    % Spawn a second traffic light using degrees in config 1 - vertical and specifying a specific actorNumber
    trafficLight2.spawn_id_degrees(2, [-3.078, 14.136, 0.215], [0, 0, 180], [1, 1, 1], 1, 1);
    % Spawn traffic light using degrees in config 2 - horizontal and generating the actorNumber internally
    trafficLight3.spawn_degrees([6.703, 5.6, 0.215], [0, 0, -90], [1, 1, 1], 2, 1);

    % Collecting the world transform coordinates of the traffic light
    [x, loc, rot, scale] = trafficLight2.get_world_transform();
    disp(['x: ', num2str(x)]);
    disp(['Location: ', num2str(loc)]);
    disp(['Rotation: ', num2str(rot)]);
    disp(['Scale: ', num2str(scale)]);

    % Pinging existing traffic light - this should return True if we printed it
    trafficLight2.ping();

    % Changing the state of the traffic lights from green to red
    pause(2);

    trafficLight.set_state(trafficLight.STATE_YELLOW, 1);
    trafficLight2.set_state(trafficLight2.STATE_YELLOW, 1);

    pause(1);

    trafficLight.set_state(trafficLight.STATE_RED, 1);
    trafficLight2.set_state(trafficLight2.STATE_RED, 1);

    pause(1);

    trafficLight3.set_state(trafficLight3.STATE_GREEN, 1);

    % Destroying a traffic light
    trafficLight.destroy();
end


    % Create a server connection with Quanser Interactive Labs and manage communications
    qlabs = QuanserInteractiveLabs();

    disp('Connecting to QLabs...');
    % Try to connect to QLabs and open the instance we have created
    try
        qlabs.open('localhost');
    catch
        disp('Unable to connect to QLabs');
        return;
    end

    % Destroy any spawned actors in our QLabs that currently exist
    qlabs.destroy_all_spawned_actors();

    % Flags for different types of objects
    CROSSWALK_FLAG = true;  % Set this flag to true if crosswalk is enabled
    ROUNDABOUT_FLAG = true;  % Set this flag to true if roundabout sign is enabled
    YIELDSIGN_FLAG = true;   % Set this flag to true if yield sign is enabled
    STOPSIGN_FLAG = true;    % Set this flag to true if stop sign is enabled
    TRAFFICCONE_FLAG = true; % Set this flag to true if traffic cone is enabled
    TRAFFICLIGHT_FLAG = true; % Set this flag to true if traffic light is enabled

    if CROSSWALK_FLAG
        crosswalk(qlabs);
        pause(2);
    end

    % Switch the camera angle to see where we will be spawning the rest of the objects
    % See Camera Actor Library Reference for more information
    if ROUNDABOUT_FLAG || YIELDSIGN_FLAG || STOPSIGN_FLAG || TRAFFICCONE_FLAG
        camera0 = QLabsFreeCamera(qlabs);
        camera0.spawn([-20.14, 29.472, 2.071], [0, 0.203, -0.024]);
        camera0.possess();

        if ROUNDABOUT_FLAG
            roundabout_sign(qlabs);
            pause(1);
        end

        if YIELDSIGN_FLAG
            yield_sign(qlabs);
            pause(1);
        end

        if STOPSIGN_FLAG
            stop_sign(qlabs);
            pause(1);
        end

        if TRAFFICCONE_FLAG
            traffic_cone(qlabs);
            pause(1);
        end
    end

    if TRAFFICLIGHT_FLAG
        traffic_light(qlabs);
    end

    % Closing qlabs
    qlabs.close();
    disp('Done!');