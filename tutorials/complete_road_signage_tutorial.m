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

% Select if you would like to spawn the signs for right or left hand
% orientation.
right_hand_driving = true;

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


main(right_hand_driving);

function main(right_hand_driving)
    
    % creates a server connection with Quanser Interactive Labs and manages the communications
    qlabs = QuanserInteractiveLabs();
    connection_established = qlabs.open('localhost');
    
    % trying to connect to QLabs and open the instance we have created - program will end if this fails
    if connection_established == false
        disp("Failed to open connection.")
        return
    end
    
    disp('Connected')
    
    % destroying any spawned actors in our QLabs that currently exist
    num_destroyed = qlabs.destroy_all_spawned_actors();
    fprintf('%d actors destroyed\n', num_destroyed);

    % Use hSystem to set the tutorial title on the qlabs display screen
    hSystem = QLabsSystem(qlabs);
    hSystem.set_title_string('Complete Road Signage Tutorial');

    spawn_crosswalk(qlabs);
    spawn_signs(qlabs, right_hand_driving);
    spawn_traffic_lights(qlabs, right_hand_driving);
    spawn_cones(qlabs);
    
    fly_through_animation(qlabs);

    % Closing qlabs
    qlabs.close();
    disp('Done!');

end

function spawn_crosswalk(qlabs)
    % Create a crosswalk in this qlabs instance. Since we don't need
    % to access the actors again after creating them, we can use a single
    % class object to spawn all the varieties. We also don't need to use
    % the waitForConfirmation because we don't need to store the actor ID
    % for future reference.

    crosswalk = QLabsCrosswalk(qlabs);

    % spawn crosswalk with degrees in config 0
    crosswalk.spawn_degrees([-12.992, -7.407, 0.005], [0,0,48], [1,1,1], 0, false);
    
    % spawn crosswalk with degrees in config 1
    crosswalk.spawn_degrees([-6.788, 45, 0.00], [0,0,90], [1,1,1], 1, false);
    
    % spawn crosswalk with degrees in config 2
    crosswalk.spawn_degrees([21.733, 3.347, 0.005], [0,0,0], [1,1,1], 2, false);

    % spawn the last crosswalk with waitForConfirmation=True to confirm everything is flushed from the send buffers
    crosswalk.spawn_degrees([21.733, 16, 0.005], [0,0,0], [1,1,1], 2, true);
end

function spawn_signs(qlabs, right_hand_driving)
    % Like the crosswalks, we don't need to access the actors again after
    % creating them.

    roundabout_sign = QLabsRoundaboutSign(qlabs);
    yield_sign = QLabsYieldSign(qlabs);
    stop_sign = QLabsStopSign(qlabs);

    if (right_hand_driving)
        stop_sign.spawn_degrees([17.561, 17.677, 0.215], [0,0,90]);
        stop_sign.spawn_degrees([24.3, 1.772, 0.2], [0,0,-90]);
        stop_sign.spawn_degrees([14.746, 6.445, 0.215], [0,0,180]);

        roundabout_sign.spawn_degrees([3.551, 40.353, 0.215], [0,0,180]);
        roundabout_sign.spawn_degrees([10.938, 28.824, 0.215], [0,0,-135]);
        roundabout_sign.spawn_degrees([24.289, 32.591, 0.192], [0,0,-90]);

        yield_sign.spawn_degrees([-2.169, -12.594, 0.2], [0,0,180]);
    else
        stop_sign.spawn_degrees([24.333, 17.677, 0.215], [0,0,90]);
        stop_sign.spawn_degrees([18.03, 1.772, 0.2], [0,0,-90]);
        stop_sign.spawn_degrees([14.746, 13.01, 0.215], [0,0,180]);

        roundabout_sign.spawn_degrees([16.647, 28.404, 0.215], [0,0,-45]);
        roundabout_sign.spawn_degrees([6.987, 34.293, 0.215], [0,0,-130]);
        roundabout_sign.spawn_degrees([9.96, 46.79, 0.2], [0,0,-180]);

        yield_sign.spawn_degrees([-21.716, 7.596, 0.2], [0,0,-90]);
    end
end

function spawn_traffic_lights(qlabs, right_hand_driving)
    % In this case, we want to track each traffic light individually so we
    % can subsequently set the color state.  By using spawning with an ID,
    % we'll know exactly which one is which and this will allow us to also
    % reference them in separate programs, and we can also spawn without
    % waiting for confirmation because the object already knows its own ID.


    % initialize four traffic light instances in qlabs
    trafficLight1 = QLabsTrafficLight(qlabs);
    trafficLight2 = QLabsTrafficLight(qlabs);
    trafficLight3 = QLabsTrafficLight(qlabs);
    trafficLight4 = QLabsTrafficLight(qlabs);

    if (right_hand_driving)
        
        trafficLight1.spawn_id_degrees(0, [5.889, 16.048, 0.215], [0,0,0], [1,1,1], 0, false);
        trafficLight2.spawn_id_degrees(1, [-2.852, 1.65, 0], [0,0,180], [1,1,1], 0, false);
        trafficLight1.set_color(trafficLight1.COLOR_GREEN, false);
        trafficLight2.set_color(trafficLight2.COLOR_GREEN, false);

        trafficLight3.spawn_id_degrees(3, [8.443, 5.378, 0], [0,0,-90], [1,1,1], 0, false);
        trafficLight4.spawn_id_degrees(4, [-4.202, 13.984, 0.186], [0,0,90], [1,1,1], 0, false);
        trafficLight3.set_color(trafficLight3.COLOR_RED, false);
        trafficLight4.set_color(trafficLight4.COLOR_RED, false); 

    else
        trafficLight1.spawn_id_degrees(0, [-2.831, 16.643, 0.186], [0,0,180], [1,1,1], 1, false);
        trafficLight2.spawn_id_degrees(1, [5.653, 1.879, 0], [0,0,0], [1,1,1], 1, false);
        trafficLight1.set_color(trafficLight1.COLOR_GREEN, false);
        trafficLight2.set_color(trafficLight2.COLOR_GREEN, false);

        trafficLight3.spawn_id_degrees(3, [8.779, 13.7, 0.215], [0,0,90], [1,1,1], 1, false);
        trafficLight4.spawn_id_degrees(4, [-4.714, 4.745, 0], [0,0,-90], [1,1,1], 1, false);
        trafficLight3.set_color(trafficLight3.COLOR_RED, false);
        trafficLight4.set_color(trafficLight4.COLOR_RED, false);         
    end
end


function spawn_cones(qlabs)
    
    % We'll assume the cones don't need to be referenced after they're spawned so a
    % single class object will suffice for spawning.
    
    cone = QLabsTrafficCone(qlabs, true);

    for count = 1:10
        % Since we're going to set the color, we need to wait for QLabs to assign
        % an actor number.  This can be executed more quickly if you spawn by ID
        % instead and manually assign the numbers.
        %
        % Also note that since this are physics objects, it's a good idea to
        % spawn the actors slight above the surface so they can fall into place.
        % If you spawn exactly at ground level, they may "pop" up from the surface.

        cone.spawn([-15.313, 35.374+(count-1)*-1.3, 0.25], [0,0,0], [1,1,1], 1, true);
        cone.set_material_properties(0, [0,0,0], 1, true);
        cone.set_material_properties(1, HSVtoRGB([(count-1)/10, 1, 1]));
    end
end


function color = HSVtoRGB(hsv)

    H = hsv(1);
    S = hsv(2);
    V = hsv(3);

    kr = mod((5+H*6), 6);
    kg = mod((3+H*6), 6);
    kb = mod((1+H*6), 6);

    r = 1 - max(min(min(kr, 4-kr), 1), 0);
    g = 1 - max(min(min(kg, 4-kg), 1), 0);
    b = 1 - max(min(min(kb, 4-kb), 1), 0);
    
    color = [r, g, b];
end

function fly_through_animation(qlabs)
    % Linearly interpolate through a series of points to fly the camera
    % around the map. For each source and destination, calculate the distance
    % so the step size is an even multiple that is approximately equal to the 
    % desired velocity. 

    % Translation/rotation point pairs
    points = [[1.5, -12.558, 1.708], [-0, 0.023, 1.405]
              [0.721, -0.922, 1.721], [-0, 0.027, 1.255]
              [6.082, 7.208, 1.566], [-0, 0.027, -0.309]
              [20.732, 3.179, 1.997], [0, 0.049, 1.452]
              [26.083, 30.157, 2.459], [0, 0.153, 2.491]
              [17.211, 46.775, 11.61], [-0, 0.348, -2.189+2*pi]
              [-17.739, 38.866, 0.956], [0, 0.142, -1.385+2*pi]
              [-16.068, 24.53, 0.628], [-0, -0.043, -1.484+2*pi]
              [-20.302, 1.82, 1.815], [-0, 0.03, -0.872+2*pi]
              [-3.261, -14.664, 1.597], [-0, -0.038, 0.894+2*pi]];

    speed = 0.3;
    filter_translation_weight = 0.1;
    filter_rotation_weight = 0.1;


    camera = QLabsFreeCamera(qlabs);
    camera.spawn_id(0,points(1,1:3), points(1, 4:6));
    camera.possess();

    fx = points(1,1);
    fy = points(1,2);
    fz = points(1,3);

    froll  = points(1,4);
    fpitch = points(1,5);
    fyaw   = points(1,6);

    for index = 1:(size(points,1)-1)
        % Calculate the integer number of steps by dividing the distance by speed
        translation_distance = dist(points(index, 1:3), points(index+1, 1:3));
        total_steps = round(translation_distance/speed);
        

        for step = 1:total_steps
            % Linearly interpolate between each of the target points
            x = interp(points(index,1), points(index+1,1), step, total_steps);
            y = interp(points(index,2), points(index+1,2), step, total_steps);
            z = interp(points(index,3), points(index+1,3), step, total_steps);

            roll  = interp(points(index,4), points(index+1,4), step, total_steps);
            pitch = interp(points(index,5), points(index+1,5), step, total_steps);
            yaw   = interp(points(index,6), points(index+1,6), step, total_steps);

            % Filter the calcuated values to smooth out the camera motion
            fx = fx*(1-filter_translation_weight) + x*filter_translation_weight;
            fy = fy*(1-filter_translation_weight) + y*filter_translation_weight;
            fz = fz*(1-filter_translation_weight) + z*filter_translation_weight;

            froll = froll*(1-filter_rotation_weight) + roll*filter_rotation_weight;
            fpitch = fpitch*(1-filter_rotation_weight) + pitch*filter_rotation_weight;
            fyaw = fyaw*(1-filter_rotation_weight) + yaw*filter_rotation_weight;     


            % To try to make the animation as consistent as possible across different
            % hardware, measure the elapsed time and delay a variable amount to try
            % to maintain 33 fps. If QLabs can't run at 33fps, it will just
            % run as fast as possible.

            tic
            camera.set_transform([fx, fy, fz], [froll, fpitch, fyaw]);
            while (toc < 0.03)
                pause(0.001);
            end
        end
    end
end

function value = dist(v1, v2)
    value = ((v1(1)-v2(1))^2 + (v1(2)-v2(2))^2 + (v1(3)-v2(3))^2)^0.5;
end

function value = interp(start, finish, step, total_steps)
    value = (finish-start)/total_steps*step + start;
end
