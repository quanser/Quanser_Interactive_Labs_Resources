function library_verification_qbot()
    close all;
    clear all;
    clc;
    addpath('../qvl')


    
    fprintf('\n\n------------------------------ Communications --------------------------------\n\n');
    
    qlabs = quanser_interactive_labs();
    connection_established = qlabs.open('localhost');
    
    if connection_established == false
        disp("Failed to open connection.")
        return
    end

   
    disp('Connected')
    
    num_destroyed = qlabs.destroy_all_spawned_actors();
    
    fprintf('%d actors destroyed', num_destroyed);

    use_verbose = true;



    fprintf('\n\n-------------------------------- Free Camera ----------------------------------\n\n');
    
    hCamera0 = qlabs_free_camera(qlabs, use_verbose);
    x = hCamera0.spawn_id(0, [0, 0, 8.538], [0, 1.209, 1.559]);
    eval(x, 0, 'Spawn camera with radians');
    

    fprintf('Attempt to spawn duplicate.\n')
    hCamera0Duplicate = qlabs_free_camera(qlabs, use_verbose);
    x = hCamera0Duplicate.spawn_id(0, [0, 0, 8.43], [0, 1.204, 1.548]);
    eval(x, 2, 'Spawn camera with duplicate ID (return code 2)');
    

    hCamera1 = qlabs_free_camera(qlabs, use_verbose);
    hCamera1.spawn_id(1, [0, 0, 3.482], [0, 0.349, -0.04]);
    x = hCamera1.destroy();
    eval(x, 1, 'Spawn and destroy existing camera (expect return 1)');
    

    hCamera10 = qlabs_free_camera(qlabs, use_verbose);
    hCamera10.actorNumber = 10;
    x = hCamera10.destroy();
    eval(x, 0, 'Destroy camera that does not exist (expect return 0)');
    
    loc2 = [0, 0, 3.745];
    rot2 = [0, 18.814, 0.326];
    hCamera2 = qlabs_free_camera(qlabs, use_verbose);
    x = hCamera2.spawn_id_degrees(2, loc2, rot2);
    eval(x, 0, 'Spawn camera with degrees');
    
    [x, loc, rot, scale] = hCamera2.get_world_transform();
    eval((sum(loc - loc2) < 0.001) && (x == true), true, 'Get world transform');


    x = hCamera2.ping();
    eval(x, true, 'Ping existing camera (expect True)');

    hCamera10.actorNumber = 10;
    x = hCamera10.ping();
    eval(x, false, 'Ping camera that does not exist (expect False)');

    hCamera3 = qlabs_free_camera(qlabs, use_verbose);
    hCamera3.spawn_id(3, [0, 0, 2.282], [0, 0.077, 0.564]);
    hCamera3.set_camera_properties(40, true, 2.3, 0.6);
    x = hCamera3.possess();
    eval(x, true, 'Possess camera (expect True)');

    for y = 1:51
        x = hCamera3.set_camera_properties(40, true, 2.3, (0.6 + ((y/50)^3)*23.7));
    end
    eval(x, true, 'Set camera properties');
    
    x = hCamera2.possess();
    eval(x, true, 'Possess camera 2');
     

%      for y = 0:25
%          x = hCamera2.set_transform(loc2, rot2/180*pi + [0, 0, y/25*pi*2] );
%      end
%      eval(x, true, 'Set transform');
     
% 
%     for y in range(26):
%         x = hCamera2.set_transform_degrees(loc2, np.add(rot2, [0, 0, y/25*360]))
%     vr.PrintWS(x == True, "Set transform degrees (expect True)")
% 
% 


    x = hCamera3.set_image_capture_resolution(820, 410);
    eval(x, true, 'Set image capture resolution');

    [success, data] = hCamera3.get_image();
    eval(x, true, 'Read image 820x410');

    if (success)
        image(data);
        truesize([size(data,1), size(data,2)])
    else
        fprintf("Image decoding failure\n");
    end
    pause(1.0)

    x = hCamera3.set_image_capture_resolution(640, 480);
    eval(x, true, 'Set image capture resolution');

    [success, data] = hCamera3.get_image();
    eval(x, true, 'Read image 640x480');

    if (success)
        image(data);
        truesize([size(data,1), size(data,2)])
    else
        fprintf("Image decoding failure\n");
    end
    pause(1.0)


    close all;



    fprintf("\n\n------------------------------ Qbot --------------------------------\n")
    fprintf("DEPRICATED")



    fprintf("\n\n------------------------------ Qbot2e --------------------------------\n")
    
    hQbot2eCamera = qlabs_free_camera(qlabs, true);
    hQbot2eCamera.spawn_id_degrees(9, [-5.5, 2, 2], [0, 40, -90]);
    x = hQbot2eCamera.possess();

    hQbot2e0 = qlabs_qbot2e(qlabs);
    hQbot2e0.spawn_id(0, [-5, 0, 0], [0, 0, pi], [1, 1, 1], 0, true);
    eval(x, 0, 'Spawn qbot with radians');

    x = hQbot2e0.spawn_id(0, [-5.5, 0, 0], [0,0,pi], [1,1,1], 0, true);
    eval(x, 2, 'Spawn qbot with duplicate ID (return code 2)');
    
    hQbot2e1 = qlabs_qbot2e(qlabs);
    hQbot2e1.spawn_id(1, [-5.5, 0, 0], [0,0,pi], [1,1,1], 0, true);
    x = hQbot2e1.destroy();
    eval(x, 1, 'Spawn and destroy existing qbot (expect return 1)');

    hQbot2e1.actorNumber=1;
    x = hQbot2e1.destroy();
    eval(x, 0, 'Destroy qbot that doesn"t exist (expect return 0)');

    hQbot2e2 = qlabs_qbot2e(qlabs);
    x = hQbot2e2.spawn_id_degrees(2, [-6, 0, 0], [0,0,180], [1,1,1], 0, true);
    eval(x, 0, 'Spawn qbot with degrees');

    x, loc, rot, scale = hQbot2e2.get_world_transform();

    x = hQbot2e2.ping();
    eval(x, true, 'Ping existing qbot (expect True)');

    hQbot2e1.actorNumber = 1;
    x = hQbot2e1.ping();
    eval(x, false, 'Ping qbot that doesn"t exist (expect False)');

    hQbot2e0.command_and_request_state(1, 1);
    pause(1);



    fprintf("\n\n------------------------------ Qbot3 --------------------------------\n")

    hQbot2eCamera = qlabs_free_camera(qlabs, true);
    hQbot2eCamera.spawn_id_degrees(9, [-7.5, 2, 2], [0, 40, -90]);
    x = hQbot2eCamera.possess();

    

end

function eval(return_value, expected_value, message)

    if (return_value == expected_value)
        fprintf('Good: %s (expected %d): %d\n', message, expected_value, return_value)
    else
        fprintf('*** ERROR: %s (expected %d): %d\n', message, expected_value, return_value)
    end
end