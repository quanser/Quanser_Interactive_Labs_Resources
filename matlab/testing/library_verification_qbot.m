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

    fp = false;



    fprintf('\n\n-------------------------------- System ----------------------------------\n\n');
    
    hSys = qlabs_system(qlabs);
    hSys.set_title_string('QBot Verification');


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
    
    [x, loc, rot, scale] = hCamera2.get_world_transform()
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

    [x, loc, rot, scale] = hQbot2e2.get_world_transform()
    eval((sum(loc - loc2) < 0.001) && (x == true), true, 'Get world transform');

    x = hQbot2e2.ping();
    eval(x, true, 'Ping existing qbot (expect True)');

    hQbot2e1.actorNumber = 1;
    x = hQbot2e1.ping();
    eval(x, false, 'Ping qbot that doesn"t exist (expect False)');

    hQbot2e0.command_and_request_state(1, 1);
    pause(1);



    fprintf("\n\n------------------------------ Qbot3 --------------------------------\n")

    hQbot3Camera = qlabs_free_camera(qlabs, true);
    hQbot3Camera.spawn_id_degrees(10, [-7.5, 2, 2], [0, 40, -90]);
    x = hQbot3Camera.possess();

    hQbot3_0 = qlabs_qbot3(qlabs);
    x = hQbot3_0.spawn_id(0, [-7, 0, 0], [0, 0, pi], [1, 1, 1], 0, true);
    eval(x, 0, 'Spawn qbot with radians');

    x = hQbot3_0.spawn_id(0, [-7.5, 0, 0], [0,0,pi], [1,1,1], 0, true);
    eval(x, 2, 'Spawn qbot with duplicate ID (return code 2)');

    hQbot3_1 = qlabs_qbot3(qlabs);
    hQbot3_1.spawn_id(1, [-7.5, 0, 0], [0,0,pi], [1,1,1], 0, true);
    x = hQbot3_1.destroy();
    eval(x, 1, 'Spawn and destroy existing qbot (expect return 1)');

    hQbot3_1.actorNumber=1;
    x = hQbot3_1.destroy();
    eval(x, 0, 'Destroy qbot that doesn"t exist (expect return 0)');
    
    hQbot3_2 = qlabs_qbot3(qlabs);
    x = hQbot3_2.spawn_id_degrees(2, [-8, 0, 0], [0,0,180], [1,1,1], 0, true);
    eval(x, 0, 'Spawn qbot with degrees');

    [x, loc, rot, scale] = hQbot3_2.get_world_transform()
    eval((sum(loc - loc2) < 0.001) && (x == true), true, 'Get world transform');

    x = hQbot3_2.ping();
    eval(x, true, 'Ping existing qbot (expect True)');

    hQbot3_1.actorNumber=1;
    x = hQbot3_1.ping();
    eval(x, false, 'Ping qbot that doesn"t exist (expect False)');

    %Custom Functions
    hQbot3_0.command_and_request_state(1, 1);
    
    hQbot3_0.get_image_rgb();
    fprintf("got image RGB")

    hQbot3_0.get_image_depth();
    fprintf("\ngot image depth")
    
    pause(1);



    fprintf("\n\n------------------------------ QBot Platform --------------------------------\n")
   
    hQbotPFCamera = qlabs_free_camera(qlabs, true);
    hQbotPFCamera.spawn_id_degrees(11, [-9.5, 2, 2], [0, 40, -90]);
    x = hQbotPFCamera.possess();

    hQbotPF0 = qlabs_qbot_platform(qlabs);
    x = hQbotPF0.spawn_id(0, [-9, 0, 0], [0, 0, pi], [1, 1, 1], 0, true);
    eval(x, 0, 'Spawn qbot with radians');

    x = hQbotPF0.spawn_id(0, [-9.5, 0, 0], [0,0,pi], [1,1,1], 0, true);
    eval(x, 2, 'Spawn qbot with duplicate ID (return code 2)');

    hQbotPF1 = qlabs_qbot_platform(qlabs);
    hQbotPF1.spawn_id(1, [-9.5, 0, 0], [0,0,pi], [1,1,1], 0, true);
    x = hQbotPF1.destroy();
    eval(x, 1, 'Spawn and destroy existing qbot (expect return 1)');

    hQbotPF1.actorNumber=1;
    x = hQbotPF1.destroy();
    eval(x, 0, 'Destroy qbot that doesn"t exist (expect return 0)');

    hQbotPF2 = qlabs_qbot_platform(qlabs);
    x = hQbotPF2.spawn_id_degrees(2, [-10, 0, 0], [0,0,180], [1,1,1], 0, true);
    eval(x, 0, 'Spawn qbot with degrees');

    [x, loc, rot, scale] = hQbotPF2.get_world_transform()
    eval((sum(loc - loc2) < 0.001) && (x == true), true, 'Get world transform');

    x = hQbotPF2.ping();
    eval(x, true, 'Ping existing qbot (expect True)');

    hQbotPF1.actorNumber=1;
    x = hQbotPF1.ping();
    eval(x, false, 'Ping qbot that doesn"t exist (expect False)');

    %Custom

    hQbotPF0.command_and_request_state(1, 1);

    hQbotPF0.get_image(1);
    fprintf("got image")

    hQbotPF0.get_lidar();
    fprintf("\ngot LIDAR")

    pause(1);



    fprintf("\n\n------------------------------ Walls --------------------------------\n")
    
    wallCamera = qlabs_free_camera(qlabs, true);
    wallCamera.spawn_id_degrees(12, [-9.5, 2, 2], [0, 40, -90]);
    x = wallCamera.possess();

    hWall0 = qlabs_walls(qlabs);
    x = hWall0.spawn_id(0, [-9, 0, 0], [0, 0, pi], [1, 1, 1], 0, true);
    eval(x, 0, 'Spawn wall with radians');

    x = hWall0.spawn_id(0, [-9.5, 0, 0], [0,0,pi], [1,1,1], 0, true);
    eval(x, 2, 'Spawn wall with duplicate ID (return code 2)');

    hWall1 = qlabs_walls(qlabs);
    hWall1.spawn_id(1, [-9.5, 0, 0], [0,0,pi], [1,1,1], 0, true);
    x = hWall1.destroy();
    eval(x, 1, 'Spawn and destroy existing wall (expect return 1)');

    hWall1.actorNumber=1;
    x = hWall1.destroy();
    eval(x, 0, 'Destroy wall that doesn"t exist (expect return 0)');

    hWall2 = qlabs_walls(qlabs);
    x = hWall2.spawn_id_degrees(2, [-10, 0, 0], [0,0,180], [1,1,1], 0, true);
    eval(x, 0, 'Spawn wall with degrees');

    [x, loc, rot, scale] = hWall2.get_world_transform()
    eval((sum(loc - loc2) < 0.001) && (x == true), true, 'Get world transform');

    x = hWall2.ping();
    eval(x, true, 'Ping existing wall (expect True)');

    hWall1.actorNumber=1;
    x = hWall1.ping();
    eval(x, false, 'Ping wall that doesn"t exist (expect False)');

    %Custom stuff

    hWall2.set_enable_dynamics(true);
    fprintf("Wall dynamics enabled")

    pause(3);

    hWall2.set_transform_degrees([-10, 3, 0], [0, 0, 0], [1,1,1]);



    fprintf("\n\n------------------------------ Reference Frame --------------------------------\n")

    frameCamera = qlabs_free_camera(qlabs, true);
    frameCamera.spawn_id_degrees(13, [-12, 2, 2], [0, 40, -90]);
    x = frameCamera.possess();

    hFrame0 = qlabs_reference_frame(qlabs);
    x = hFrame0.spawn_id(0, [-12, 2, 0], [0, 0, 0], [1, 1, 1], 0, true);
    eval(x, 0, 'Spawn invisible frame with radians');
    
    hFrame1 = qlabs_reference_frame(qlabs);
    x = hFrame1.spawn_id(1, [-12, 0, 0], [0, 0, 0], [1, 1, 1], 1, true);
    eval(x, 0, 'Spawn frame with radians');

    hFrame2 = qlabs_reference_frame(qlabs);
    x = hFrame2.spawn_id(2, [-12, -2, 0], [0, 0, 0], [1, 1, 1], 2, true);
    eval(x, 0, 'Spawn second frame with radians');

    x = hFrame0.spawn_id(0, [-12, 2, 0], [0,0,pi], [1,1,1], 0, true);
    eval(x, 2, 'Spawn frame with duplicate ID (return code 2)');

    hFrame3 = qlabs_reference_frame(qlabs);
    hFrame3.spawn_id(3, [-13, 0, 0], [0,0,pi], [1,1,1], 0, true);
    x = hFrame3.destroy();
    eval(x, 1, 'Spawn and destroy existing frame (expect return 1)');

    hFrame1.actorNumber=4;
    x = hFrame1.destroy();
    eval(x, 0, 'Destroy frame that doesn"t exist (expect return 0)');

    hFrame4 = qlabs_reference_frame(qlabs);
    hFrame4.spawn_id_degrees(5, [-13, 0, 0], [0,0,0], [1,1,1], 1);
    eval(x, 0, 'Spawn frame with degrees');

    [x, loc, rot, scale] = hFrame0.get_world_transform()
    eval((sum(loc - loc2) < 0.001) && (x == true), true, 'Get world transform');

    % Custom functions:

    pause(1);
    hFrame4.set_transform_degrees([-13, -2, 0], [0,0,0], [1,4,1]);

    pause(0.5);

    hFrame4.set_icon_scale([2,2,2]);



    fprintf("\n\n------------------------------ Shredder --------------------------------\n")

    shredderCamera = qlabs_free_camera(qlabs, true);
    shredderCamera.spawn_id_degrees(14, [4, 2, 2], [0, 40, -90]);
    x = shredderCamera.possess();

    hShredder0 = qlabs_shredder(qlabs);
    x = hShredder0.spawn_id(0, [3, 0, 0], [0, 0, 0], [1,1,1], 0);
    eval(x, 0, 'Spawn shredder in configuration 0 with radians');

    hShredder1 = qlabs_shredder(qlabs);
    x = hShredder1.spawn_id(1, [4, 0, 0], [0, 0, 0], [3,3,3], 1);
    eval(x, 0, 'Spawn shredder in configuration 1 with radians');

    hShredder2 = qlabs_shredder(qlabs);
    x = hShredder2.spawn_id(2, [5, 0, 0], [0, 0, 0], [2,2,2], 2);
    eval(x, 0, 'Spawn shredder in configuration 2 with radians');

    hShredder3 = qlabs_shredder(qlabs);
    x = hShredder3.spawn_id(3, [6, 0, 0], [0, 0, 0], [2,0.5,0.5], 3);
    eval(x, 0, 'Spawn shredder in configuration 3 with radians');

    hShredder4 = qlabs_shredder(qlabs);
    hShredder4.spawn_id(4, [6, 0, 0], [0,0,pi], [1,1,1], 0, true);
    x = hShredder4.destroy();
    eval(x, 1, 'Spawn and destroy existing shredder (expect return 1)');

    hShredder1.actorNumber=5;
    x = hShredder1.destroy();
    eval(x, 0, 'Destroy shredder that doesn"t exist (expect return 0)');

    hShredder5 = qlabs_shredder(qlabs);
    hShredder5.spawn_id_degrees(6, [3, -2, 0], [0,0,0], [10,10,10], 2);
    eval(x, 0, 'Spawn shredder with degrees');

    [x, loc, rot, scale] = hShredder5.get_world_transform()
    eval((sum(loc - loc2) < 0.001) && (x == true), true, 'Get world transform');

%     for i = 0:50
%         sacrificialCube = qlabs_widget(qlabs);
%         sacrificialCube.spawn_degrees([3, -2, 4], [0,0,0], [1,1,1], 4, [0,1,1]);
%     end
% 
%     for i = 0:500
%         sacrificialCube = qlabs_widget(qlabs);
%         sacrificialCube.spawn_degrees([3, -2, 4+(i*0.1)], [0,0,0], [1,1,1], 4, [0,1,1]);
%     end

    pause(0.2);



    fprintf("\n\n------------------------------ Delivery Tube --------------------------------\n")

    tubeCamera = qlabs_free_camera(qlabs, true);
    tubeCamera.spawn_id_degrees(15, [8, 1.5, 2.5], [0, 10, -90]);
    x = tubeCamera.possess();

    hTube0 = qlabs_delivery_tube(qlabs);
    x = hTube0.spawn_id(0, [7, 0, 0], [0,0,0], [1,1,1]);
    eval(x, 0, 'Spawn delivery tube with radians');
    hTube0.set_height(2);

    hTube1 = qlabs_delivery_tube_bottles(qlabs);
    x = hTube1.spawn_id(0, [8, 0, 2], [0,0,0], [1,1,1]);
    eval(x, 0, 'Spawn delivery tube bottles with radians');
    hTube1.set_height(2);

    hTube2 = qlabs_delivery_tube(qlabs);
    x = hTube2.spawn_id_degrees(1, [9, 0, 0], [0,0,0], [1,1,1]);
    eval(x, 0, 'Spawn delivery tube with degrees');
    hTube2.set_height(2);

    [success, location, rotation, scale] = hTube2.get_world_transform()
    eval((sum(loc - loc2) < 0.001) && (x == true), true, 'Get world transform');

    %Custom Funcitons

    hTube0.spawn_block(hTube0.BLOCK_CUBE, 10, 0, [1,0,0]);

    hTube1.spawn_container(false, [1,0,0], 10, "supermansucks", 0.1, 0.65, 0.65);

    hTube2.spawn_block(hTube2.BLOCK_SPHERE, 10, 0, [1,0,0]);

    pause(2);



    fprintf("\n\n------------------------------ QArm --------------------------------\n")

    qArmCamera = qlabs_free_camera(qlabs, true);
    qArmCamera.spawn_id_degrees(15, [12, 2, 2], [0, 40, -90]);
    x = qArmCamera.possess();

    hQArm0 = qlabs_qarm(qlabs);
    x = hQArm0.spawn_id(0, [11, 0, 0], [0, 0, 0], [1,1,1], 0);
    eval(x, 0, 'Spawn QArm with radians');

    x = hQArm0.spawn_id(0, [11, 0, 0], [0,0,pi], [1,1,1], 0, true);
    eval(x, 2, 'Spawn QArm with duplicate ID (return code 2)');

    hQArm1 = qlabs_qarm(qlabs);
    hQArm1.spawn_id(1, [12, 0, 0], [0,0,pi], [1,1,1], 0, true);
    x = hQArm1.destroy();
    eval(x, 1, 'Spawn and destroy existing QArm (expect return 1)');

    hQArm1.actorNumber=2;
    x = hQArm1.destroy();
    eval(x, 0, 'Destroy QArm that doesn"t exist (expect return 0)');

    hQArm3 = qlabs_qarm(qlabs);
    x = hQArm3.spawn_id_degrees(3, [12, 0, 0], [0,0,180], [1,1,1], 0, true);
    eval(x, 0, 'Spawn QArm with degrees');

    [x, loc, rot, scale] = hQArm3.get_world_transform()
    eval((sum(loc - loc2) < 0.001) && (x == true), true, 'Get world transform');

    x = hQArm3.ping();
    eval(x, true, 'Ping existing QArm (expect True)');

    hWall1.actorNumber=4;
    x = hWall1.ping();
    eval(x, false, 'Ping QArm that doesn"t exist (expect False)');



    fprintf("\n\n------------------------------ Conveyor Curved --------------------------------\n")

    conveyorCurvedCam = qlabs_free_camera(qlabs, true);
    conveyorCurvedCam.spawn_id_degrees(16, [16, 2, 2], [0, 40, -90]);
    x = conveyorCurvedCam.possess();

    hBeltCurve0 = qlabs_conveyor_curved(qlabs);
    x = hBeltCurve0.spawn_id(0, [15, 0, 0], [0, 0, 0], [1,1,1]);
    eval(x, 0, 'Spawn conveyor with radians');

    conveyorPoint = qlabs_reference_frame(qlabs);
    conveyorPoint.spawn_id(20, [16, 0, 0], [0,0,0], [1,1,1], 0)
    
%     for i = 0:12
%         hBeltCurve1 = qlabs_conveyor_curved(qlabs);
%         hBeltCurve1.spawn_id_and_parent_with_relative_transform_degrees(1+i, [0,0,0], [0,0,i*30], [2,2,2], 0, conveyorPoint.classID, 20, 0);
%         hBeltCurve1.set_speed(7);
%         
%         fprintf("Conveyor Spawned\n")
%     end 

    for i = 0:3
        hBeltCurve1 = qlabs_conveyor_curved(qlabs);
        hBeltCurve1.spawn_id_and_parent_with_relative_transform_degrees(1+i, [0,0,0], [0,0,i*90], [2,2,2], 6, conveyorPoint.classID, 20, 0);
        hBeltCurve1.set_speed(7);
        
        fprintf("Conveyor Spawned\n")
    end 

    hCubeTube = qlabs_delivery_tube_bottles(qlabs);
    hCubeTube.spawn([15, 0.2, 1], [0,0,0], [1,1,1]);
    hCubeTube.set_height(10);

    for i = 0:5
        hCubeTube.spawn_container(false, [0,1,0], 10, 0.1, 0.65, 0.65);
        pause(0.5);
    end

    % Single section conveyor

    conveyorCurvedCam2 = qlabs_free_camera(qlabs, true);
    conveyorCurvedCam2.spawn_id_degrees(18, [19, 2, 2], [0, 40, -90]);
    x = conveyorCurvedCam2.possess();

    hBeltCurve2 = qlabs_conveyor_curved(qlabs);
    x = hBeltCurve2.spawn_id_degrees(20, [19, 0, 0], [0,0,0], [1,1,1], 12);
    eval(x, 0, 'Spawn Q-belt with degrees and 12 sections (configurations)');

    fprintf("\n\n------------------------------ Conveyor Straight --------------------------------\n")
    
    conveyorCurvedCam = qlabs_free_camera(qlabs, true);
    conveyorCurvedCam.spawn_id_degrees(19, [21, 2.5, 2], [0, 40, -90]);
    x = conveyorCurvedCam.possess();

    hBeltS0 = qlabs_conveyor_straight(qlabs);
    x = hBeltS0.spawn_id(0, [22, 0, 0], [0, 0, 0], [1,1,1]);
    eval(x, 0, 'Spawn conveyor with radians');

    hBeltS1 = qlabs_conveyor_straight(qlabs);
    x = hBeltS1.spawn_id_degrees(1, [20, 0, 0], [0, 0, 0], [2,2,2]);
    eval(x, 0, 'Spawn conveyor with degrees & at a larger scale');

    pause(0.5);
    hBeltS1.set_speed(0.1);

    pause(2);
    hBeltS1.set_speed(0.5);
    pause(0.5);

    conveyorLength = 3;

    hBeltS2 = qlabs_conveyor_straight(qlabs);
    x = hBeltS2.spawn_id_degrees(2, [20, 1, 0], [0, 0, 0], [2,2,2], conveyorLength);
    eval(x, 0, 'Spawn conveyor with degrees & with multipule sections');

    hCubeTube1 = qlabs_delivery_tube_bottles(qlabs);
    hCubeTube1.spawn([conveyorLength + 19.3, 1, 0.5], [0,0,0], [1,1,1]);
    hCubeTube1.set_height(10);

    %Spawn bottles on conveyor at different speeds

    pause(0.5);
    hBeltS2.set_speed(0.5);
    for i = 1:4
        hCubeTube1.spawn_container(false, [1,0.5,0], 10, 0.1, 0.65, 0.65);
        fprintf("Bottle Spawned\n")
        pause(0.5);
    end

    pause(0.5);
    hBeltS2.set_speed(1);
    for i = 1:4
        hCubeTube1.spawn_container(false, [1,0.5,0], 10, 0.1, 0.65, 0.65);
        fprintf("Bottle Spawned\n")
        pause(0.5);
    end

    pause(0.5);
    hBeltS2.set_speed(2);
    for i = 1:4
        hCubeTube1.spawn_container(false, [1,0.5,0], 10, 0.1, 0.65, 0.65);
        fprintf("Bottle Spawned\n")
        pause(0.5);
    end

    pause(0.5);
    hBeltS2.set_speed(10);
    for i = 1:4
        hCubeTube1.spawn_container(false, [1,0.5,0], 10, 0.1, 0.65, 0.65);
        fprintf("Bottle Spawned\n")
        pause(0.5);
    end

    pause(0.5);
    hBeltS2.set_speed(100);
    for i = 1:4
        hCubeTube1.spawn_container(false, [1,0.5,0], 10, 0.1, 0.65, 0.65);
        fprintf("Bottle Spawned\n")
        pause(0.5);
    end

    fprintf("\n\n------------------------------ Both Conveyors --------------------------------\n")

    x = conveyorCurvedCam2.possess();

    hBeltBoth0 = qlabs_conveyor_straight(qlabs);
    hBeltBoth0.spawn_id_degrees(3, [18.5,0,0], [0,0,-90], [1,1,1], 10);

    hBeltBoth1 = qlabs_conveyor_straight(qlabs);
    hBeltBoth1.spawn_id_degrees(4, [19.5,0,0], [0,0,-90], [1,1,1], 10);

    hBeltBoth2 = qlabs_conveyor_curved(qlabs);
    x = hBeltBoth2.spawn_id_degrees(21, [19, -3, 0], [0,0,-180], [1,1,1], 12);

    function loopSpeed(QBspeed)
        hBeltBoth0.set_speed(QBspeed*-1)
        hBeltBoth1.set_speed(QBspeed)
        hBeltBoth2.set_speed(QBspeed)
        hBeltCurve2.set_speed(QBspeed)
    end

    function spawnBottleBC(quantity)
        for i = 1:quantity
            hCubeTube2.spawn_container(false, [1,0,1], 10, 0.1, 0.65, 0.65);
            fprintf("Bottle Spawned")
            pause(0.5);
        end
    end

    hCubeTube2 = qlabs_delivery_tube_bottles(qlabs);
    hCubeTube2.spawn([19, 0.5, 0.5], [0,0,0], [1,1,1]);
    hCubeTube2.set_height(10);

    pause(0.5);
    loopSpeed(0.1);
    spawnBottleBC(4);

    pause(1);
    loopSpeed(0.5);
    spawnBottleBC(4);

    pause(0.5);
    loopSpeed(1);
    spawnBottleBC(4);

    pause(2);
    loopSpeed(2);
    spawnBottleBC(4);

    pause(0.5);
    loopSpeed(-1);
    spawnBottleBC(4);

    pause(2);



    fprintf("\n\n------------------------------ Flooring --------------------------------\n")

    floorCam0 = qlabs_free_camera(qlabs, true);
    floorCam0.spawn_id_degrees(20, [19, 7, 2], [0, 40, -90]);
    x = floorCam0.possess();

    hFloor0 = qlabs_flooring(qlabs);
    x = hFloor0.spawn_id(0, [19, 5, 0], [0,0,0], [1,1,1], 0);
    eval(x, 0, 'Spawn floor in configuration 0 with radians');

    pause(0.2);

    floorCam1 = qlabs_free_camera(qlabs, true);
    floorCam1.spawn_id_degrees(21, [14, 7, 2], [0, 40, -90]);
    x = floorCam1.possess();

    hFloor0 = qlabs_flooring(qlabs);
    x = hFloor0.spawn_id_degrees(1, [14, 5, 0], [0,0,0], [1,1,1], 1);
    eval(x, 0, 'Spawn floor in configuration 1 with degrees');

    %Modular QBot Platform Flooring
    floorCam2 = qlabs_free_camera(qlabs, true);
    floorCam2.spawn_id_degrees(21, [14, 7, 2], [0, 40, -90]);

    x = hFloor0.spawn_id_degrees(2, [10, 5, 0], [0,0,0], [1,1,1], 2);
    eval(x, 0, 'Spawn floor in configuration 2 with degrees');

    x = hFloor0.spawn_id_degrees(3, [10, 6.2, 0], [0,0,0], [1,1,1], 3);
    eval(x, 0, 'Spawn floor in configuration 3 with degrees');
 
    x = hFloor0.spawn_id_degrees(4, [10, 3.8, 0], [0,0,0], [1,1,1], 4);
    eval(x, 0, 'Spawn floor in configuration 4 with degrees');
 
    x = hFloor0.spawn_id_degrees(5, [11.2, 5, 0], [0,0,0], [1,1,1], 5);
    eval(x, 0, 'Spawn floor in configuration 5 with degrees');

    x = hFloor0.spawn_id_degrees(6, [12.4, 5, 0], [0,0,0], [1,1,1], 6);
    eval(x, 0, 'Spawn floor in configuration 6 with degrees');

    x = hFloor0.spawn_id_degrees(7, [8.8, 5, 0], [0,0,0], [1,1,1], 7);
    eval(x, 0, 'Spawn floor in configuration 7 with degrees');



    fprintf("\n\n------------------------------ Generic Sensor --------------------------------\n")

    floorCam0 = qlabs_free_camera(qlabs, true);
    floorCam0.spawn_id_degrees(22, [10, 7, 2], [0, 40, -90]);
    x = floorCam0.possess();

    hhitbox = qlabs_basic_shape(qlabs);
    hhitbox.spawn_id_degrees(7, [11, 5, 1], [0,0,0], [1,1,1]);
    hhitbox.set_material_properties([1,0,1], 0.2, false, true);

    hSensor = qlabs_generic_sensor(qlabs);
    hSensor.spawn_degrees([10, 5, 1], [0,0,0], [1,1,1]);
    hSensor.show_sensor(true, true, 0.2);
    hSensor.set_beam_size(1, 5, 0.2, 0.1);

    [success, hit, actorClass, actorNumber, distance] = hSensor.test_beam_hit();

    if hit == true
        fprintf("Actor class: %u, Actor Number: %u, Distance: %u", actorClass, actorNumber, distance);
    end
end

function eval(return_value, expected_value, message)

    if (return_value == expected_value)
        fprintf('Good: %s (expected %d): %d\n', message, expected_value, return_value)
    else
        fprintf('*** ERROR: %s (expected %d): %d\n', message, expected_value, return_value)
    end
end