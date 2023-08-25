function library_verification_qcar()
    close all;
    clear all;
    clc;
    addpath('../qvl')


    require_user_input = false;
    
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

    






    fprintf("\n\n------------------------- System Libraries ---------------------------\n")


%     ### System
%     """
%     vr.PrintWSHeader("System")
%     hSystem = QLabsSystem(qlabs)
%     x = hSystem.set_title_string('QLABS VERIFICATION SCRIPT', waitForConfirmation=True)
%     vr.PrintWS(x == True, "Set title string")
%     vr.checkFunctionTestList("system", "../docs/source/System/system_library.rst")
%     """

    if (true)
%     ### Free Camera
    fprintf('\n\n-------------------------------- Free Camera ----------------------------------\n\n');
    
    hCamera0 = qlabs_free_camera(qlabs, use_verbose);
    x = hCamera0.spawn_id(0, [-8.248, 39.575, 8.538], [0, 1.209, 1.559]);
    eval(x, 0, 'Spawn camera with radians');
    

    fprintf('Attempt to spawn duplicate.\n')
    hCamera0Duplicate = qlabs_free_camera(qlabs, use_verbose);
    x = hCamera0Duplicate.spawn_id(0, [-13.74076819, 36.68400671, 8.43], [0, 1.204, 1.548]);
    eval(x, 2, 'Spawn camera with duplicate ID (return code 2)');
    

    hCamera1 = qlabs_free_camera(qlabs, use_verbose);
    hCamera1.spawn_id(1, [-25.78776819, 29.01500671, 3.482], [0, 0.349, -0.04]);
    x = hCamera1.destroy();
    eval(x, 1, 'Spawn and destroy existing camera (expect return 1)');
    

    hCamera10 = qlabs_free_camera(qlabs, use_verbose);
    hCamera10.actorNumber = 10;
    x = hCamera10.destroy();
    eval(x, 0, 'Destroy camera that does not exist (expect return 0)');
    
    loc2 = [-21.456, 31.995, 3.745];
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
    hCamera3.spawn_id(3, [-33.17276819, 13.50500671, 2.282], [0, 0.077, 0.564]);
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



%     print('Testing parenting.')
%     loc3 = [5.252, 20.852, 9.461]
%     hCubeCameraHook = QLabsBasicShape(qlabs, True)
%     x = hCubeCameraHook.spawn_id(1000, loc3, [0,0,0], [1,1,1], configuration=hCubeCameraHook.SHAPE_CUBE, waitForConfirmation=True)
% 
%     hCamera5Child = QLabsFreeCamera(qlabs, True)
%     x = hCamera5Child.spawn_id_and_parent_with_relative_transform(5, [0, -10, 0], [0,0,math.pi/2], [1,1,1], 0, hCubeCameraHook.ID_BASIC_SHAPE, hCubeCameraHook.actorNumber, 0)
%     vr.PrintWS(x == 0, "Spawn and parent with relative transform")
%     x = hCamera5Child.possess()
%     for y in range(26):
%         x = hCubeCameraHook.set_transform(loc3, [0, 0, y/25*math.pi*2], [1,1,1])
% 
%     time.sleep(0.5)
% 
%     hCamera5Child.destroy()
%     x = hCamera5Child.spawn_id_and_parent_with_relative_transform_degrees(5, [0, -10, 0], [0,0,90], [1,1,1], 0, hCubeCameraHook.ID_BASIC_SHAPE, hCubeCameraHook.actorNumber, 0)
%     vr.PrintWS(x == 0, "Spawn and parent with relative transform degrees")
%     x = hCamera5Child.possess()
%     for y in range(26):
%         x = hCubeCameraHook.set_transform(loc3, [0, 0, y/25*math.pi*2], [1,1,1])
% 
%     hCameraSpawnAutogen1 = QLabsFreeCamera(qlabs)
%     x, CameraSpawn1Num = hCameraSpawnAutogen1.spawn(location=[-11.154, 42.544, 8.43], rotation=[0, 1.204, 1.548])
%     vr.PrintWS(x == 0, "Spawn with automatically generated ID ({})".format(CameraSpawn1Num))
% 
%     hCameraSpawnAutogen2 = QLabsFreeCamera(qlabs)
%     x, CameraSpawn2Num = hCameraSpawnAutogen2.spawn_degrees(location=[-11.154, 42.544, 8.43], rotation=[0, 0, 0])
%     vr.PrintWS(x == 0, "Spawn with automatically generated ID ({})".format(CameraSpawn2Num))
% 
% 
%     vr.checkFunctionTestList("free_camera", "../docs/source/Objects/camera_library.rst", "actor")
% 
%     cv2.destroyAllWindows()
     x = hCamera2.possess();
 


fprintf('\n\n-------------------------------- Yield Sign ----------------------------------\n\n');


    hYield0 = qlabs_yield_sign(qlabs);
    x = hYield0.spawn_id(0, [-17, 32.5, 0.0], [0,0,pi], [1,1,1], 0, true);
    eval(x, 0, 'Spawn sign with radians');

    x = hYield0.spawn_id(0, [-17, 32.5, 0.0], [0,0,pi], [1,1,1], 0, true);
    eval(x, 2, 'Spawn sign with duplicate ID (return code 2)');

    hYield1 = qlabs_yield_sign(qlabs);
    hYield1.spawn_id(1, [-16, 32.5, 0.0], [0,0,pi], [1,1,1], 0, true);
    x = hYield1.destroy();
    eval(x, 1, 'Spawn and destroy existing sign (expect return 1)');

    hYield1.actorNumber=1;
    x = hYield1.destroy();
    eval(x, 0, 'Destroy sign that doesn"t exist (expect return 0)');

    hYield2 = qlabs_yield_sign(qlabs);
    x = hYield2.spawn_id_degrees(2, [-15, 32.5, 0.0], [0,0,180], [1,1,1], 0, true);
    eval(x, 0, 'Spawn sign with degrees');

    x, loc, rot, scale = hYield2.get_world_transform();
%     vr.PrintWS(np.array_equal(loc, [-15, 32.5, 0.0]) and x == True, "Get world transform")

    x = hYield2.ping();
    eval(x, true, 'Ping existing sign (expect True)');

    hYield1.actorNumber=1;
    x = hYield1.ping();
    eval(x, false, 'Ping sign that doesn"t exist (expect False)');

%     vr.checkFunctionTestList("yield_sign", "../docs/source/Objects/road_signage.rst", "actor")
% 
%     ### Stop Sign
    fprintf('\n\n-------------------------------- Stop Sign ----------------------------------\n\n');
    % Spawn two signs
    hStop0 = qlabs_stop_sign(qlabs);
    x = hStop0.spawn_id(0, [-17, 33.5, 0.0], [0,0,pi], [1,1,1], 0, true);
    eval(x, 0, 'Spawn sign with radians');

    x = hStop0.spawn_id(0, [-17, 33.5, 0.0], [0,0,pi], [1,1,1], 0, true);
    eval(x, 2, 'Spawn sign with duplicate ID (return code 2)');

    hStop1 = qlabs_stop_sign(qlabs);
    hStop1.spawn_id(1, [-16, 33.5, 0.0], [0,0,pi], [1,1,1], 0, true);
    x = hStop1.destroy();
    eval(x, 1, 'Spawn and destroy existing sign (expect return 1)')
   
    hStop1.actorNumber=1;
    x = hStop1.destroy();
    eval(x, 0, 'Destroy sign that doesn"t exist (expect return 0)')

    hStop2 = qlabs_stop_sign(qlabs);
    x = hStop2.spawn_id_degrees(2, [-15, 33.5, 0.0], [0,0,180], [1,1,1], 0, true);
    eval(x, 0, 'Spawn sign with degrees')

    x, loc, rot, scale = hStop2.get_world_transform();
%    vr.PrintWS(np.array_equal(loc, [-15, 33.5, 0.0]) and x == True, "Get world transform")


    x = hStop2.ping();
    eval(x, true, 'Ping existing sign (expect True)');

    hStop1.actorNumber=1;
    x = hStop1.ping();
    eval(x, false, 'Ping sign that doesn"t exist (expect False)');


    fprintf('\n\n-------------------------------- Roundabout Sign ----------------------------------\n\n');
    %Spawn a roundabout sign
    roundaboutSign = qlabs_roundabout_sign(qlabs, use_verbose);
    status = roundaboutSign.spawn_id(0, [1.193, 11.417, 0.005], [0,0,pi], [1,1,1], true);
    eval(status, 0, 'roundaboutSign.spawn_id 0')

    hRoundabout0 = qlabs_roundabout_sign(qlabs);
    x = hRoundabout0.spawn_id(0, [-17, 31.5, 0.0], [0,0,pi], [1,1,1], 0, true);
    eval(status, 0, 'Spawn sign with radians')
    
    x = hRoundabout0.spawn_id(0, [-17, 31.5, 0.0], [0,0,pi], [1,1,1], 0, true);
    eval(status, 2, 'Spawn sign with duplicate ID (return code 2)')
    
    hRoundabout1 = qlabs_roundabout_sign(qlabs);
    hRoundabout1.spawn_id(1, [-16, 31.5, 0.0], [0,0,pi], [1,1,1], 0, true);
    x = hRoundabout1.destroy();
    eval(status, 1, 'Spawn and destroy existing sign (expect return 1)')
    
    hRoundabout1.actorNumber = 1;
    x = hRoundabout1.destroy();
    eval(status, 0, 'Destroy sign that doesn"t exist (expect return 0)')
    
    hRoundabout2 = qlabs_roundabout_sign(qlabs);
    x = hRoundabout2.spawn_id_degrees(2, [-15, 31.5, 0.0], [0,0,180], [1,1,1], 0, true);
    eval(status, 0, 'Spawn sign with degrees');
    
    
    x, loc, rot, scale = hRoundabout2.get_world_transform();
    eval(status, 0, 'Spawn sign with degrees');
    
    x = hRoundabout2.ping();
    eval(status, true, 'Ping existing sign (expect True)');
    
    hRoundabout1.actorNumber = 1;
    x = hRoundabout1.ping();
    eval(status, false, 'Ping sign that doesn"t exist (expect False)');

%     vr.checkFunctionTestList("roundabout_sign", "../docs/source/Objects/road_signage.rst", "actor")


    fprintf('\n\n-------------------------------- Traffic Cone ----------------------------------\n\n');
    %Spawn a traffic cone
    trafficCone = qlabs_traffic_cone(qlabs, use_verbose);
    status = trafficCone.spawn_id(3, [2.193, 11.417, 0.005], [0,0,pi], [1,1,1], 0, true);
    eval(status, 0, 'trafficCone.spawn_id 0')

    %Spawn a second traffic cone
    trafficCone = qlabs_traffic_cone(qlabs, use_verbose);
    status = trafficCone.spawn_id(1, [3.193, 11.417, 0.005], [0,0,pi], [1,1,1], 1, true);
    eval(status, 0, 'trafficCone.spawn_id 1')
 
    hCone0 = qlabs_traffic_cone(qlabs);
    x = hCone0.spawn_id(0, [-17, 30.5, 1.0], [0,0,pi], [1,1,1], 0, true);
    eval(status, 0, 'Spawn cone with radians')
    
    x = hCone0.spawn_id(0, [-17, 30.5, 1.0], [0,0,pi], [1,1,1], 0, true);
    eval(status, 2, 'Spawn cone with duplicate ID (return code 2)')
    
    hCone1 = qlabs_traffic_cone(qlabs);
    hCone1.spawn_id(1, [-16, 30.5, 1.0], [0,0,pi], [1,1,1], 0, true);
    x = hCone1.destroy();
    eval(status, 1, 'Spawn and destroy existing cone (expect return 1)')

    hCone1.actorNumber = 1;
    x = hCone1.destroy();
    eval(status, 0, 'Destroy cone that doesn"t exist (expect return 0)');

    hCone2 = qlabs_traffic_cone(qlabs);
    x = hCone2.spawn_id_degrees(2, [-15, 30.5, 1.0], [0,0,180], [1,1,1], 1, true);
    eval(status, 0, 'Spawn cone with degrees in config 1')

    x, loc, rot, scale = hCone2.get_world_transform();
    eval(status, true, 'Get world transform')


    x = hCone2.ping();
    eval(status, true, 'Ping existing cone (expect True)')

    hCone1.actorNumber = 1;
    x = hCone1.ping();
    eval(status, false, 'Ping cone that doesn"t exist (expect False)')

%     vr.checkFunctionTestList("traffic_cone", "../docs/source/Objects/road_signage.rst", "actor")



%     Change view points

    pause(0.5)
    hCamera0.possess()
    fprintf('Possess camera 0')


    fprintf('\n\n-------------------------------- Crosswalk ----------------------------------\n\n');
    %Spawn a crosswalk 
    hCrosswalk = qlabs_crosswalk(qlabs, use_verbose);
    x = hCrosswalk.spawn_id(0, [-10.5 45 0.00], [0 0 pi/2], [1 1 1], 0, true);
    eval(x, 0, 'Spawn crosswalk with radians')

    x = hCrosswalk.spawn_id(0, [-7.5, 45, 0.00], [0,0,pi/2], [1,1,1], 0, true);
    eval(x, 2, 'Spawn crosswalk with duplicate ID (return code 2)')


    hCrosswalk.spawn_id(1, [-7.5, 45, 0.00], [0,0,pi/2], [1,1,1], 0, true);
    x = hCrosswalk.destroy();
    eval(x, 1, 'Spawn and destroy existing crosswalk (expect return 1)')
    

    hCrosswalk.actorNumber = 10;
    x = hCrosswalk.destroy();
    eval(x, 0, 'Destroy crosswalk that does not exist (expect return 0)')

    x = hCrosswalk.spawn_id_degrees(2, [-7.5, 45, 0.00], [0,0,90], [1,1,1], 1, true);
    eval(x, 0, 'Spawn crosswalk with degrees in config 1');

    x = hCrosswalk.spawn_id_degrees(3, [-4.5, 45, 0.00], [0,0,90], [1,1,1], 2, true);
    eval(x, 0, 'Spawn crosswalk with degrees in config 2');


    %x, loc, rot, scale = hCrosswalk.get_world_transform()
    %vr.PrintWS(abs(np.sum(np.subtract(loc, [-7.8, 47.5, 0.0]))) < 0.001 and x == True, "Get world transform")

    hCrosswalk.actorNumber = 2;
    x = hCrosswalk.ping();
    eval(x, true, 'Ping existing crosswalk (expect True)');
 
    hCrosswalk.actorNumber = 4;
    x = hCrosswalk.ping();
    eval(x, false, 'Ping crosswalk that does not exist (expect False)');

    
    fprintf('\n\n-------------------------------- People ----------------------------------\n\n');

    hPersonRight = qlabs_person(qlabs, use_verbose);
    hPersonRight.spawn_id(0, [-4.5, 41, 0.005], [0,0,pi/2], [1,1,1], 6, true);

    hPersonMiddle = qlabs_person(qlabs, use_verbose);
    hPersonMiddle.spawn_id(1, [-7.5, 41, 0.005], [0,0,pi/2], [1,1,1], 7, true);

    hPersonLeft = qlabs_person(qlabs, use_verbose);
    hPersonLeft.spawn_id_degrees(2, [-10.5, 41, 0.005], [0,0,90], [1,1,1], 8, true);

    hPersonRight.move_to([-4.5, 48, 0.005], hPersonRight.WALK, true);
    hPersonMiddle.move_to([-7.5, 48, 0.005], hPersonMiddle.JOG, true);
    hPersonLeft.move_to([-10.5, 48, 0.005], hPersonLeft.RUN, true);

    pause(3);

%     x, pos, rot, scale = hPersonLeft.get_world_transform()
%     vr.PrintWS(x == True, "Got world transform ({}), ({}), ({})".format(pos, rot, scale))
% 
%     x, pos, rot, scale = hPersonLeft.get_world_transform_degrees()
%     vr.PrintWS(x == True, "Got world transform degrees ({}), ({}), ({})".format(pos, rot, scale))
% 
%     x = hPersonLeft.ping()
%     vr.PrintWS(x == True, "Ping person left (expect True)")
% 
%     x = hPersonLeft.destroy()
%     vr.PrintWS(x == 1, "Person left destroyed (expect 1)")
% 
%     hPersonLeft.actorNumber = 2
%     x = hPersonLeft.ping()
%     vr.PrintWS(x == False, "Ping person left after manual assignment of actor number (expect False)")
% 
% 
%     time.sleep(1)
% 
% 
% 
% 
%     vr.checkFunctionTestList("person", "../docs/source/Objects/person_library.rst", "character", "actor")
% 
% 
   

%     ### QCar
    fprintf('\n\n-------------------------------- QCar ----------------------------------\n\n');

   hCameraQCars = qlabs_free_camera(qlabs);
   hCameraQCars.spawn_id(33, [-15.075, 26.703, 6.074], [0, 0.564, -1.586]);
   hCameraQCars.possess();

    hQCar0 = qlabs_qcar(qlabs);
    x = hQCar0.spawn_id(0, [-8.700, 14.643, 0.005], [0,0,pi/2], true);
    eval(x, 0, 'Spawn QCar with radians')

    hQCar0Duplicate = qlabs_qcar(qlabs, true);
    x = hQCar0Duplicate.spawn_id(0, [-14.386, 17.445, 0.005], [0,0,pi/2], true);
    eval(x, 2, 'Spawn QCar with duplicate ID (return code 2)')

    hQCar1 = qlabs_qcar(qlabs);
    hQCar1.spawn_id(1, [-15.075, 26.703, 6.074], [0,0,pi/2], true);
    x = hQCar1.destroy();
    eval(x, 1, 'Spawn and destroy existing QCar (expect return 1)')

    hQCar1.actorNumber = 10;
    x = hQCar1.destroy();
    eval(x, 0, 'Destroy QCar that doesn"t exist (expect return 0)')

    hQCar2 = qlabs_qcar(qlabs);
    x = hQCar2.spawn_id_degrees(2, [-11.048, 14.643, 0.005], [0,0,90], true);
    eval(x, 0, 'Spawn QCar with degrees')

%     lights
    hEnvironmentOutdoors = qlabs_environment_outdoors(qlabs);
    for env_time = 0:60
        hEnvironmentOutdoors.set_time_of_day(12+env_time/10*2);
    end

    pause(0.5);

    hQCar2.set_velocity_and_request_state(1, -pi/6, true, false, true, false, false);
    pause(1);
    hQCar2.set_velocity_and_request_state(0.0, -pi/6, true, false, true, false, false);
%     if require_user_input == true
%         x = input("Moving forward towards the right of the screen, headlights on? (Enter yes, anything else no):");
%     else
%         eval(x, '', 'Headlights')
%         eval(x, '', 'Set velocity')
%     end

    hQCar2.set_velocity_and_request_state_degrees(1, 30, true, true, false, false, false);
    pause(1);
    hQCar2.set_velocity_and_request_state_degrees(0.0, 30, true, true, false, false, false);
%     success, location, rotation, frontHit, rearHit = hQCar2.set_velocity_and_request_state_degrees(0.0, 30, true, true, false, false, false);
%     fprintf(rotation)
%     if require_user_input == true
%         x = input("Moving forward towards the left of the screen? Enter yes, anything else no):");
%     else
%         x = "";
%     end
%     eval(x, '', 'Set velocity degrees')
    


    x = hQCar2.possess();

    pause(0.1);
    hQCar2.set_velocity_and_request_state(1, 0, true, true, true, true, true);
    pause(1);
    hQCar2.set_velocity_and_request_state(0.0, 0, true, true, true, true, true);

%     if require_user_input == True:
%         x = input("Brake lights on and casting red glow? (Enter yes, anything else no):")
%     else:
%         x = ""
%     vr.PrintWS(x == "", "Brake lights")


    hQCar2.set_velocity_and_request_state(0, 0, false, false, false, false, false);

    for env_time = 1:60
        hEnvironmentOutdoors.set_time_of_day(env_time/10*2);
    end


%     bumper test
    fprintf("Testing bumper response...")
    hCameraQCars.possess();
    hCameraQCars.set_transform([-17.045, 32.589, 6.042], [0, 0.594, -1.568]);

    hCubeQCarBlocks = qlabs_basic_shape(qlabs);
    hCubeQCarBlocks.spawn_id(100, [-11.919, 26.289, 0.5], [0,0,0], [1,1,1], hCubeQCarBlocks.SHAPE_CUBE, true);
    hCubeQCarBlocks.spawn_id(101, [-19.919, 26.289, 0.5], [0,0,0], [1,1,1], hCubeQCarBlocks.SHAPE_CUBE, true);

    hQCar3 = qlabs_qcar(qlabs);
    hQCar3.spawn_id(3, [-13.424, 26.299, 0.005], [0,0,pi]);

    for count = 0:10
        %x, location, rotation, frontHit, rearHit = 
        hQCar3.set_velocity_and_request_state(2, 0, false, false, false, false, false);

        pause(0.25);
    end

%     vr.PrintWS(x == True and frontHit == True, "Front bumper hit")
    x = hQCar3.ghost_mode();
    eval(x, true, 'Ghost Mode');
  
    for count = 0:10
        %x, location, rotation, frontHit, rearHit  = 
        hQCar3.set_velocity_and_request_state(-2, 0, false, false, false, false, false);

        pause(0.25)
    end

    hQCar3.ghost_mode(true, [1,0,0]);

%     vr.PrintWS(x == True and rearHit == True, "Rear bumper hit")
    hQCar3.set_velocity_and_request_state(0, 0, false, false, false, false, false);

%     x, location, rotation, forward_vector, up_vector, frontHit, rearHit = 
    hQCar3.set_transform_and_request_state([-16.1, 26.299, 0.005], [0,0,pi-0.01], true, false, false, false, false, false);
%     vr.PrintWS(x == True and frontHit == True, "Front bumper hit with transform")

    x = hQCar3.get_world_transform();
    loc = hQCar3.get_world_transform();
    rot = hQCar3.get_world_transform();
    scale = hQCar3.get_world_transform();
    
%     eval(x, abs(loc - [-16.1, 26.299, 0.005]) < 0.01 && abs(rot - [0, 0, pi-0.01]) < 0.01 && x == true, 'Get world transform');
    
%     vr.PrintWS(abs(np.sum(np.subtract(loc, [-16.1, 26.299, 0.005]))) < 0.01 and abs(np.sum(np.subtract(rot, [0,0,math.pi-0.01]))) < 0.01 and x == True, "Get world transform")


%     x, location, rotation, forward_vector, up_vector, frontHit, rearHit = hQCar3.set_transform_and_request_state_degrees(location=[-13.1, 26.299, 0.005], rotation=[0,0,179], enableDynamics=True, headlights=False, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)
%     vr.PrintWS(x == True and rearHit == True, "Rear bumper hit with transform")
% 
%     x, loc, rot, scales = hQCar3.get_world_transform_degrees()
%     vr.PrintWS(abs(np.sum(np.subtract(loc, [-13.1, 26.299, 0.005]))) < 0.01 and abs(np.sum(np.subtract(rot, [0,0,179]))) < 0.01 and x == True, "Get world transform degrees")

    hQCar3.ghost_mode(false, [1,0,0]);


%     #camera tests
%     print("\nQCar camera tests...")
%     hQCar2.possess(hQCar2.CAMERA_OVERHEAD)
%     if require_user_input == True:
%         x = input("Overhead camera? (Enter yes, anything else no):")
%     else:
%         x = ""
%         time.sleep(0.5)
%     vr.PrintWS(x == "", "Possess overhead camera")
% 
%     hQCar2.possess(hQCar2.CAMERA_TRAILING)
%     if require_user_input == True:
%         x = input("Trailing camera? (Enter yes, anything else no):")
%     else:
%         x = ""
%         time.sleep(0.5)
%     vr.PrintWS(x == "", "Possess trailing camera")
% 
%     hQCar2.possess(hQCar2.CAMERA_CSI_FRONT)
%     if require_user_input == True:
%         x = input("Front camera? (Enter yes, anything else no):")
%     else:
%         x = ""
%         time.sleep(0.5)
%     vr.PrintWS(x == "", "Possess front camera")
% 
%     hQCar2.possess(hQCar2.CAMERA_CSI_RIGHT)
%     if require_user_input == True:
%         x = input("Right camera? (Enter yes, anything else no):")
%     else:
%         x = ""
%         time.sleep(0.5)
%     vr.PrintWS(x == "", "Possess right camera")
% 
%     hQCar2.possess(hQCar2.CAMERA_CSI_BACK)
%     if require_user_input == True:
%         x = input("Back camera? (Enter yes, anything else no):")
%     else:
%         x = ""
%         time.sleep(0.5)
%     vr.PrintWS(x == "", "Possess back camera")
% 
%     hQCar2.possess(hQCar2.CAMERA_CSI_LEFT)
%     if require_user_input == True:
%         x = input("Left camera? (Enter yes, anything else no):")
%     else:
%         x = ""
%         time.sleep(0.5)
%     vr.PrintWS(x == "", "Possess left camera")
% 
%     hQCar2.possess(hQCar2.CAMERA_RGB)
%     if require_user_input == True:
%         x = input("Real Sense RGB camera? (Enter yes, anything else no):")
%     else:
%         x = ""
%         time.sleep(0.5)
%     vr.PrintWS(x == "", "Possess Real Sense RGB camera")
% 
%     hQCar2.possess(hQCar2.CAMERA_DEPTH)
%     if require_user_input == True:
%         x = input("Real Sense Depth camera? (Enter yes, anything else no):")
%     else:
%         x = ""
%         time.sleep(0.5)
%     vr.PrintWS(x == "", "Possess Real Sense Depth camera")
% 
%     cv2.namedWindow('QCarImageStream', cv2.WINDOW_AUTOSIZE)
%     camera_image = cv2.imread('Quanser640x480.jpg')
%     cv2.imshow('QCarImageStream', camera_image)
%     cv2.waitKey(1)
% 
% 
%     x, camera_image = hQCar2.get_image(camera=hQCar2.CAMERA_CSI_FRONT)
%     if (x == True):
%         cv2.imshow('QCarImageStream', camera_image)
%         cv2.waitKey(1)
%     else:
%         print("Image decoding failure")
% 
%     vr.PrintWS(x == True, "Image read CSI Front")
%     cv2.waitKey(1000)
% 
%     x, camera_image = hQCar2.get_image(camera=hQCar2.CAMERA_CSI_RIGHT)
%     if (x == True):
%         cv2.imshow('QCarImageStream', camera_image)
%         cv2.waitKey(1)
%     else:
%         print("Image decoding failure")
% 
%     vr.PrintWS(x == True, "Image read CSI Right")
%     cv2.waitKey(1000)
% 
%     x, camera_image = hQCar2.get_image(camera=hQCar2.CAMERA_CSI_BACK)
%     if (x == True):
%         cv2.imshow('QCarImageStream', camera_image)
%         cv2.waitKey(1)
%     else:
%         print("Image decoding failure")
% 
%     vr.PrintWS(x == True, "Image read CSI Back")
%     cv2.waitKey(1000)
% 
%     x, camera_image = hQCar2.get_image(camera=hQCar2.CAMERA_CSI_LEFT)
%     if (x == True):
%         cv2.imshow('QCarImageStream', camera_image)
%         cv2.waitKey(1)
%     else:
%         print("Image decoding failure")
% 
%     vr.PrintWS(x == True, "Image read CSI Left")
%     cv2.waitKey(1000)
% 
%     x, camera_image = hQCar2.get_image(camera=hQCar2.CAMERA_RGB)
%     if (x == True):
%         cv2.imshow('QCarImageStream', camera_image)
%         cv2.waitKey(1)
%     else:
%         print("Image decoding failure")
% 
%     vr.PrintWS(x == True, "Image read Real Sense RGB")
%     cv2.waitKey(1000)
% 
%     x, camera_image = hQCar2.get_image(camera=hQCar2.CAMERA_DEPTH)
%     if (x == True):
%         cv2.imshow('QCarImageStream', camera_image)
%         cv2.waitKey(1)
%     else:
%         print("Image decoding failure")
% 
%     vr.PrintWS(x == True, "Image read Real Sense Depth")
%     cv2.waitKey(1000)
% 
% 
%     #ping
%     print("Testing ping response...")
%     x = hQCar2.ping()
%     vr.PrintWS(x == True, "Ping existing QCar (expect True)")
% 
%     x = hQCar1.ping()
%     vr.PrintWS(x == False, "Ping QCar that doesn't exist (expect False)")
% 
% 
%     #LIDAR
    fprintf('LIDAR')

    hQCar3.possess(hQCar3.CAMERA_OVERHEAD);
% 
%     lidarPlot = pg.plot(title="LIDAR")
%     squareSize = 100
%     lidarPlot.setXRange(-squareSize, squareSize)
%     lidarPlot.setYRange(-squareSize, squareSize)
%     lidarData = lidarPlot.plot([], [], pen=None, symbol='o', symbolBrush='r', symbolPen=None, symbolSize=2)
% 
% 
%     time.sleep(1)
% 
%     print("Reading from LIDAR... if QLabs crashes, make sure FPS > 100 or fix the crash bug!")
% 
% 

    hFigure = figure();
    hQCar3.set_velocity_and_request_state(-1, 0, false, false, false, false, false);
    
    for count = 0:20

        [success, angle, distance] = hQCar3.get_lidar(400);
        %success
        %x = angle;
        %y = distance;

%         for i = 1:length(distance)
%             if (distance(i) == 0)
%                 distance(i) = NaN;
%             end
%         end

        x = sin(angle).*distance;
        y = cos(angle).*distance;

        plot(x,y, '.');
        axis([-60 60 -60 60]);
        drawnow;
        pause(0.05);
        
    end

    hQCar3.set_velocity_and_request_state(0, 0, false, false, false, false, false);
    
    close(hFigure);
% 
%         lidarData.setData(x,y)
%         QtWidgets.QApplication.instance().processEvents()
%         time.sleep(lidar_rate)
% 
%     vr.PrintWS(True, "LIDAR didn't crash QLabs!")
%     vr.PrintWS(lidar_rate == 0.01, "Passed LIDAR test with 100Hz (lidar_rate = 0.01 expected)")
% 
%     time.sleep(1)
% 
%     vr.checkFunctionTestList("qcar", "../docs/source/Objects/car_library.rst", "actor")
% 
% 


    fprintf('\n\n-------------------------------- Basic Shape ----------------------------------\n\n');

    x = hCamera2.possess();
 
    hCube200 = qlabs_basic_shape(qlabs);
    x = hCube200.spawn_id(200, [-4.852, 36.977, 0.5], [0,0,pi/4], [0.5,0.5,0.5], hCube200.SHAPE_CUBE, true);
    eval(x, 0, 'Spawn sign with radians')
 
    hCube200Duplicate = qlabs_basic_shape(qlabs);
    x = hCube200Duplicate.spawn_id(200, [-5.852, 36.977, 0.5], [0,0,pi/4], [0.5,0.5,0.5], hCube200Duplicate.SHAPE_CUBE, true);
    eval(x, 2, 'Spawn with duplicate ID')
 
    hCube220 = qlabs_basic_shape(qlabs);
    x = hCube220.spawn_id_degrees(220, [-4.832, 34.147, 0.5], [0,0,45], [0.5,0.5,0.5], hCube220.SHAPE_CUBE, true);
    eval(x, 0, 'Spawn sign with degrees')
 
    hCube221 = qlabs_basic_shape(qlabs, true);
    x = hCube221.spawn_id_degrees(221, [-4.832, 35.147, 0.5], [0,0,45], [0.5,0.5,0.5], hCube221.SHAPE_CUBE, true);
    x = hCube221.destroy();
    fprintf('Num actors destroyed: %u\n', x)
    eval(x, 1, 'Spawn and destroy existing (expect return 1)')

    hCube221.actorNumber = 221;
    x = hCube221.destroy();
    fprintf('Num actors destroyed: %u', x)
    eval(x, 0, 'Destroy shape that doesn"t exist (expect return 0)')
 
    x = hCube220.ping();
    eval(x, true, 'Ping existing sign (expect True)')
    

    hCube221.actorNumber = 221;
    x = hCube221.ping();
    eval(x, false, 'Ping sign that does not exist (expect False)')

    [x, loc, rot, scale] = hCube200.get_world_transform();
    eval(sum(loc - [-4.852, 36.977, 0.5]) < 0.001 && (x == true), true, 'Get world transform');
    
    x = hCube200.ping();

    hCube201 = qlabs_basic_shape(qlabs, true);
    x = hCube201.spawn_id_and_parent_with_relative_transform(201, [0,2,0], [0,0,pi/4], [1,1,1], hCube201.SHAPE_CUBE, hCube200.ID_BASIC_SHAPE, hCube200.actorNumber, 0, true);
    eval(x, 0, 'Spawn with parent relative transform (expect 0)')

    x = hCube220.set_material_properties([0,0.5,1], 0.0, false, true); %fourth cube's colour
 
    hCube202 = qlabs_basic_shape(qlabs, true);
    x = hCube202.spawn_id_and_parent_with_relative_transform_degrees(202, [0,-2,0], [0,0,45], [1,1,1], hCube202.SHAPE_CUBE, hCube200.ID_BASIC_SHAPE, hCube200.actorNumber, 0, true);
    eval(x, 0, 'Spawn with parent relative transform degrees (expect 0)')

    x = hCube202.set_material_properties([0,1,0], 0.0, true, true);
    x = hCube201.set_material_properties([1,0,0], 0.0, true, true);
    eval(x, true, 'Set material properties (expect True)')
    
    for y = 0:10
        x = hCube201.set_transform([0,2,0], [0,0,pi/4-pi/25*y], [1,1,1], false);
        x = hCube202.set_transform_degrees([0,-2,0], [0,0,45-180/25*y], [1,1,1], false);
        x = hCube200.set_transform([-4.852, 36.977, 0.5], [0,0,pi/4+2*pi/50*y], [0.5+0.5*y/50,0.5+0.5*y/50,0.5+0.5*y/50]);
        pause(0.1)
    end

%   parenting without spawn
    hCube301 = qlabs_basic_shape(qlabs);
    hCube301.spawn([-4.93, 36.985, 1.5], [0,0,0], [0.2,0.2,0.2], hCube301.SHAPE_CUBE, true);

    hCube302 = qlabs_basic_shape(qlabs);
    hCube302.spawn([-4.93, 35.985, 1.5], [0,0,0], [0.5,0.5,0.5], hCube302.SHAPE_CUBE, true);

    for y = 0:10
        x = hCube301.set_transform_degrees([-4.93, 36.985, 1.5], [0,0,y*10], [0.2,0.2,0.2], true);
        pause(0.1)
    end

    x = hCube302.parent_with_relative_transform([0,1.2/0.2,0], [0,0,0], [0.5,0.5,0.5], hCube301.classID, hCube301.actorNumber, 0, true);
    eval(x, 0, 'Parent with relative transform')
    pause(0.5)

    for y = 0:10
        x = hCube301.set_transform_degrees([-4.93, 36.985, 1.5], [0,0,y*10], [0.2,0.2,0.2], true);
    end

    x = hCube302.parent_break();
    eval(x, 0, 'Parent break')

    for y = 0:10
        x = hCube301.set_transform_degrees([-4.93, 36.985, 1.5], [0,0,y*10], [0.2,0.2,0.2], true);
    end

    x = hCube302.parent_with_current_world_transform(hCube301.classID, hCube301.actorNumber, 0, true);
    eval(x, 0, 'Parent break')
    pause(0.5)

    for y = 0:10
        x = hCube301.set_transform_degrees([-4.93, 36.985, 1.5], [0,0,y*10], [0.2,0.2,0.2], true);
    end

    x = hCube302.parent_break();
    x = hCube302.parent_with_relative_transform_degrees([0,1.2/0.2,0], [0,0,0], [0.5,0.5,0.5], hCube301.classID, hCube301.actorNumber, 0, true);
    eval(x, 0, 'Parent with relative transform degrees')
    pause(0.5)

    for y = 0:10
        x = hCube301.set_transform_degrees([-4.93, 36.985, 1.5], [0,0,y*10], [0.2,0.2,0.2], true);
    end


%   collisions

    hSphere203 = qlabs_basic_shape(qlabs);
    x = hSphere203.spawn_id(203, [-4.75, 32.5, 0.25], [0,0,0], [0.5,0.5,0.5], hSphere203.SHAPE_SPHERE, true);
    x = hSphere203.set_material_properties([0,1,0], 0.0, false, true);

    hSphere204 = qlabs_basic_shape(qlabs);
    x = hSphere204.spawn_id(204, [-4.75, 31.5, 0.25], [0,0,0], [0.5,0.5,0.5], hSphere204.SHAPE_SPHERE, true);
    x = hSphere204.set_material_properties([0,0,1], 0.0, false, true);
    x = hSphere204.set_enable_collisions(false, true);
    eval(x, true, 'Enable collisions')

    hSphere205 = qlabs_basic_shape(qlabs);
    hSphere206 = qlabs_basic_shape(qlabs);
    hSphere207 = qlabs_basic_shape(qlabs);

    x = hSphere205.spawn_id(205, [-4.6, 32.5, 2], [0,0,0], [0.6,0.6,0.6], hSphere205.SHAPE_SPHERE, true);
    x = hSphere206.spawn_id(206, [-4.6, 31.5, 2], [0,0,0], [0.6,0.6,0.6], hSphere206.SHAPE_SPHERE, true);
    x = hSphere207.spawn_id(207, [-4.6, 30.5, 2], [0,0,0], [0.6,0.6,0.6], hSphere207.SHAPE_SPHERE, true);

    x = hSphere207.set_physics_properties(false, 1, 10, 0);
    eval(x, true, 'Set physics properties')

    x = hSphere205.set_enable_dynamics(true, false);
    x = hSphere206.set_enable_dynamics(true, false);
    x = hSphere207.set_enable_dynamics(true, true);
    eval(x, true, 'Enable dynamics')

    x = hSphere205.set_enable_dynamics(true, false);

    hBoxSpawn = qlabs_basic_shape(qlabs);
    x = hBoxSpawn.spawn_id_box_walls_from_center([210, 211, 212, 213, 214], [-1.103, 32.404, 0.005], pi/4, 2, 2, 0.5, 0.1, 0.1, [1,0,0], [0,0,1], true);
    eval(x, true, 'Spawn box walls from center')

    x = hBoxSpawn.spawn_id_box_walls_from_center_degrees([270, 271, 272, 273, 274], [0.35, 30.4, 0.005], 45, 2, 2, 0.5, 0.1, 0.1, [1,0,0], [0,0,1], true);
    eval(x, true, 'Spawn box walls from center degrees')

    x = hBoxSpawn.spawn_id_box_walls_from_end_points(280, [-3.232, 31.439, 0.01], [-1.403, 29.383, 0.01], 0.1, 0.1, [0.2,0.2,0.2], true);
    eval(x, true, 'Spawn box walls from end points')

    x, shapeHandle1 = hBoxSpawn.spawn([-5.632, 34.162, 0.25], [0,0,pi/4], [0.5,0.5,0.5], hBoxSpawn.SHAPE_CUBE, true);
    x, shapeHandle2 = hBoxSpawn.spawn([-5.632, 33.162, 0.25], [0,0,pi/4], [0.5,0.5,0.5], hBoxSpawn.SHAPE_CUBE, true);
    x, shapeHandle3 = hBoxSpawn.spawn([-5.632, 32.162, 0.25], [0,0,pi/4], [0.5,0.5,0.5], hBoxSpawn.SHAPE_CUBE, true);
    eval(x, 0, 'Spawn next')

    x, shapeHandle4 = hBoxSpawn.spawn_degrees([-5.632, 31.162, 0.25], [0,0,45], [0.5,0.5,0.5], hBoxSpawn.SHAPE_CUBE, true);
    x, shapeHandle5 = hBoxSpawn.spawn_degrees([-5.632, 30.162, 0.25], [0,0,45], [0.5,0.5,0.5], hBoxSpawn.SHAPE_CUBE, true);
    eval(x, 0, 'Spawn next degrees')

    hBoxSpawn.actorNumber = shapeHandle2;
    x = hBoxSpawn.set_material_properties([1,0,1], 0.0, true, true);
%    vr.checkFunctionTestList("basic_shape", "../docs/source/Objects/basic_shapes.rst", "actor");


fprintf('\n\n-------------------------------- Widget ----------------------------------\n\n');
    
    x = hCamera2.possess();
    hQLabsWidget = qlabs_widget(qlabs);
    hQLabsWidget.widget_spawn_shadow(true);

    for y = 0:600
        x = hQLabsWidget.spawn([-0.974, 32.404, 1], [0,0,0], [1,1,1], hQLabsWidget.METAL_CAN, [1,1,1], 0, 0, '', false);
        x = hQLabsWidget.spawn([-0.974, 32.904, 1], [0,0,0], [1,1,1], hQLabsWidget.METAL_CAN, [1,1,1], 0, 0, '', false);
        x = hQLabsWidget.spawn([-0.474, 32.904, 1], [0,0,0], [1,1,1], hQLabsWidget.METAL_CAN, [1,1,1], 0, 0, '', false);
        x = hQLabsWidget.spawn([-0.474, 32.404, 1], [0,0,0], [1,1,1], hQLabsWidget.METAL_CAN, [1,1,1], 0, 0, '', true);
        pause(0.01)
        fprintf("%u\n", y*4)
    end
    
    for y= 0:500
        x = hQLabsWidget.spawn([-0.974, 32.404, 1], [0,0,0], [1,1,1], hQLabsWidget.METAL_CAN, [1,1,1], 0, 0, '', false);
    end

    eval(x, true, 'Widget spawn (expect True)')

    pause(1);

    for y = 0:20
        x = hQLabsWidget.spawn_degrees([-0.974, 32.404, 1+y*0.2], [90,0,0], [1,1,1], hQLabsWidget.METAL_CAN, [1,0,0], 0, 0, '', true);
    end

    for y = 0:50
        x = hQLabsWidget.spawn_degrees([-0.974, 32.404, 1+y*0.2], [90,0,0], [1,1,1], hQLabsWidget.METAL_CAN, [0,0.5,1], 0, 0, '', true);
    end

    eval(x, true, 'Widget spawn degrees(expect True)')

    pause(3);
    
    x = hQLabsWidget.destroy_all_spawned_widgets();
    eval(x, true, 'Widgets destroyed (expect True)')
    
    hQLabsWidget.widget_spawn_shadow(false);

 
    for y = 0:10
        x = hQLabsWidget.spawn_degrees([-0.974, 32.404+y*0.01, 1+y*0.6], [90,0,0], [0.5,0.5,0.5], hQLabsWidget.SPHERE, [1,0,0], 0, 0, '', true);
    end

    pause(1);

    hQLabsWidget.destroy_all_spawned_widgets();
    hQLabsWidget.widget_spawn_shadow(true);

    for y = 0:10
        x = hQLabsWidget.spawn_degrees([-0.974, 32.404+y*0.01, 1+y*0.6], [90,0,0], [0.5,0.5,0.5], hQLabsWidget.SPHERE, [1,0,0], 0, 0, '', true);
    end



%     vr.checkFunctionTestList("widget", "../docs/source/Objects/widgets.rst")

 
    fprintf('\n\n-------------------------------- Traffic Light ----------------------------------\n\n');

    hCameraTraffic = qlabs_free_camera(qlabs);
    x = hCameraTraffic.spawn([-6.891, 3.568, 2.127], [0, 0.049, 1.105]);
    hCameraTraffic.possess();

    hTrafficLight0 = qlabs_traffic_light(qlabs);
    x = hTrafficLight0.spawn_id(0, [6, 14.328, 0.215], [0,0,0], [1,1,1], 0, true);
    eval(x, 0, 'Spawn traffic light with radians')
     
    x = hTrafficLight0.spawn_id(0, [6, 14.328, 0.215], [0,0,0], [1,1,1], 0, true);
    eval(x, 2, 'Spawn traffic light with duplicate ID (return code 2)')
    
    hTrafficLight1 = qlabs_traffic_light(qlabs);
    hTrafficLight1.spawn_id(1, [-2.44, 15, 0.215], [0,0,0], [1,1,1], 0, true)
    x = hTrafficLight1.destroy();
    eval(x, 1, 'Spawn and destroy existing light (expect return 1)')
 
    hTrafficLight1.actorNumber = 1;
    x = hTrafficLight1.destroy();
    eval(x, 0, 'Destroy traffic light that doesn"t exist (expect return 0)')    
    
    hTrafficLight2 = qlabs_traffic_light(qlabs);
    x = hTrafficLight2.spawn_id_degrees(2, [-2.44, 15, 0.215], [0,0,180], [1,1,1], 1, true);
    eval(x, 0, 'Spawn traffic light with degrees in config 1')
    
    hTrafficLight3 = qlabs_traffic_light(qlabs);
    [x, assignedActorNum] = hTrafficLight3.spawn_degrees([6.686, 5.802, 0.215], [0,0,-90], [1,1,1], 2, true);
    eval(x, 0, 'Spawn traffic light with degrees in config 2')
 
    x, loc, rot, scale = hTrafficLight2.get_world_transform();
    eval(x, true, 'Get world transform')

    x = hTrafficLight2.ping();
    eval(x, true, 'Ping existing traffic light (expect True)')

    hTrafficLight1.actorNumber = 1;
    x = hTrafficLight1.ping();
    eval(x, false, 'Ping traffic light that doesn"t exist (expect False)')
 
    hTrafficLight0.set_state(hTrafficLight0.STATE_GREEN, true);
    hTrafficLight2.set_state(hTrafficLight2.STATE_GREEN, true);
    hTrafficLight3.set_state(hTrafficLight3.STATE_GREEN, true);

    pause(1);
 
    hTrafficLight0.set_state(hTrafficLight0.STATE_YELLOW, true);
    hTrafficLight2.set_state(hTrafficLight2.STATE_YELLOW, true);
    hTrafficLight3.set_state(hTrafficLight3.STATE_YELLOW, true);

    pause(1);
 
    hTrafficLight0.set_state(hTrafficLight0.STATE_RED, true);
    hTrafficLight2.set_state(hTrafficLight2.STATE_RED, true);
    hTrafficLight3.set_state(hTrafficLight3.STATE_RED, true);
 
    pause(1);
 
    x = hTrafficLight0.destroy_all_actors_of_class();
    eval(x, 3, 'Delete all actors of class (expect 3), received {}')
    
%     vr.checkFunctionTestList("traffic_light", "../docs/source/Objects/road_signage.rst", "actor")
    

    fprintf('\n\n-------------------------------- Spline Line ----------------------------------\n\n');

    hCameraSplines = qlabs_free_camera(qlabs);
    x = hCameraSplines.spawn([-3.097, 2.579, 11.849], [0, 0.912, 1.141]);
    hCameraSplines.possess();

    hSpline2 = qlabs_spline_line(qlabs);

    lineWidth = 0.125;
    splineZ = 0.015;
    points = [-6.184, 9.595, splineZ,lineWidth
              -4.081, 9.856, splineZ, lineWidth
              -1.998, 10.178, splineZ, lineWidth
              -0.461, 11.024, splineZ, lineWidth
              0.168, 11.721, splineZ, lineWidth
              0.742, 13.048, splineZ, lineWidth
              0.991, 14.059, splineZ, lineWidth
              1.276, 15.72, splineZ, lineWidth
              1.363, 17.125, splineZ, lineWidth];

    color_selection = [0.5, 0.0, 0.0
                       0.5, 0.0, 0.5
                       0.0, 0.5, 0.0
                       0.0, 0.0, 0.5];

    for counter = 1:4
        x = hSpline2.spawn([0,0-counter*0.75,0+counter*0.001], [0,0,0], [1,1,1], counter, true);
        eval(x, true, 'Spawn configuration {}: {}".format(counter, x')

        x = hSpline2.set_points(color_selection(counter, :), points, false, true);
        eval(x, true, 'Set points {}: {}".format(counter, x')
        
    end
        
    pause(0.5);
    x = hSpline2.destroy_all_actors_of_class();
    eval(x, 4, 'Destroy all actors of class (expect 4): {}".format(x)')

    hSpline2.spawn_id(0, [0,0,0], [0,0,0], [1,1,1], counter, true);
    hSpline2.set_points(color_selection(1), points, false, true);
    pause(0.5);

    x = hSpline2.destroy();
    eval(x, 1, 'Destroy actor (expect 1): {}".format(x)')

    hSpline2.spawn_id_degrees(1, [0,0,0], [0,0,0], [1,1,1], counter, true);
    hSpline2.set_points(color_selection(1), points, false, true);
    x = hSpline2.ping();
    eval(x, true, 'Ping (expect True): {}".format(x)');

    hSpline2.destroy();
    hSpline2.actorNumber = 1;
    x = hSpline2.ping();
    eval(x, false, 'Ping actor that doesn"t exist (expect False): {}".format(x)');


    hSpline3 = qlabs_spline_line(qlabs);
    hSpline3.spawn([1.741, 8.757, 0.005], [0,0,0],[1,1,1],1);
    x = hSpline3.circle_from_center(1, 0.1, [1,0,1], 8);
    eval(x, true, 'Circle from center (expect True): {}".format(x)');


    hSpline4 = qlabs_spline_line(qlabs);
    hSpline4.spawn([4.467, 10.579, 0.005], [0,0,0],[1,1,1],1);
    hSpline4.arc_from_center(1, 0, pi/2, 0.1, [1,0,0], 8);
    eval(x, true, 'Arc from center (expect True): {}".format(x)');

    hSpline5 = qlabs_spline_line(qlabs);
    hSpline5.spawn([5.045, 11.205, 0.005], [0,0,0],[1,1,1],1);
    hSpline5.arc_from_center_degrees(1, 0, 90, 0.1, [1,0,0], 8);
    eval(x, true, 'Arc from center degrees (expect True): {}".format(x)');

    hSpline6 = qlabs_spline_line(qlabs);
    hSpline6.spawn([3.178, 10.713, 0.01], [0,0,0],[1,1,1],hSpline6.CURVE)
    hSpline6.rounded_rectangle_from_center(0.5, 2, 4, 0.1, [1,1,0]);
    eval(x, true, 'Rounded rectangle (expect True): {}".format(x)');
    

%     vr.checkFunctionTestList("spline_line", "../docs/source/Objects/splines.rst", "actor")
%
    fprintf('\n\n-------------------------------- Animals ----------------------------------\n\n');

    hCameraAnimals = qlabs_free_camera(qlabs);
    x = hCameraAnimals.spawn([25.802, 47.9, 0.484], [-0, -0.195, 1.009]);
    hCameraAnimals.possess();

    hGoat = qlabs_animal(qlabs);
    hGoat.spawn([26.206, 57, 1], [0,0,0], [1,1,1], hGoat.GOAT, true);
    hGoat.move_to([27.214, 49.286, 0], hGoat.GOAT_RUN, true);

    pause(3);
    hGoat.move_to([28.338, 47.826, 0], hGoat.GOAT_WALK, true);
    pause(6);
    hGoat.destroy();


    hSheep = qlabs_animal(qlabs);
    hSheep.spawn([26.206, 57, 1], [0,0,0], [1,1,1], hSheep.SHEEP, true);
    hSheep.move_to([27.214, 49.286, 0], hSheep.SHEEP_RUN, true);
    pause(3);
    hSheep.move_to([28.338, 47.826, 0], hSheep.SHEEP_WALK, true);
    pause(6);
    hSheep.destroy();


    hCow = qlabs_animal(qlabs);
    hCow.spawn([26.206, 57, 1], [0,0,0], [1,1,1], hCow.COW, true);
    hCow.move_to([27.214, 49.286, 0], hCow.COW_RUN, true);
    pause(3);
    hCow.move_to([28.338, 47.826, 0], hCow.COW_WALK, true);
    pause(6);

    end

%     vr.checkFunctionTestList("animal", "../docs/source/Objects/animal_library.rst", "character", "actor")

    fprintf('\n\n-------------------------------- Outdoor Environment ----------------------------------\n\n');
    
    hEnvironmentOutdoors2 = qlabs_environment_outdoors(qlabs);
    hEnvironmentOutdoors2.set_outdoor_lighting(0);

    hCameraWeather = qlabs_free_camera(qlabs);
    x = hCameraWeather.spawn([0.075, -8.696, 1.576], [0, -0.141, 1.908]);
    hCameraWeather.possess();

    pause(2.5);
%    hSystem = qlabs_system(qlabs);

     hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.CLEAR_SKIES);
%     hSystem.set_title_string('Clear skies')
     pause(2.5);

    hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.PARTLY_CLOUDY);
%     hSystem.set_title_string('Partly cloudy')
    pause(2.5);

    hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.CLOUDY);
%     hSystem.set_title_string('Cloudy')
    pause(2.5);

    hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.OVERCAST);
    hEnvironmentOutdoors2.set_outdoor_lighting(1);
%     hSystem.set_title_string('Overcast')
    pause(2.5);

    hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.FOGGY);
%     hSystem.set_title_string('Foggy')
    pause(2.5);

    hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.LIGHT_RAIN);
    hEnvironmentOutdoors2.set_outdoor_lighting(0)
%     hSystem.set_title_string('Light rain')
    pause(2.5);
% 
    hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.RAIN);
    hEnvironmentOutdoors2.set_outdoor_lighting(1);
%     hSystem.set_title_string('Rain')
    pause(2.5);

    hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.THUNDERSTORM);
%     hSystem.set_title_string('Thunderstorm')
    pause(2.5);

    hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.LIGHT_SNOW);
    hEnvironmentOutdoors2.set_outdoor_lighting(0);
%     hSystem.set_title_string('Light snow')
    pause(2.5);

    hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.SNOW);
    hEnvironmentOutdoors2.set_outdoor_lighting(1);
%     hSystem.set_title_string('Snow')
    pause(2.5);

    hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.BLIZZARD);
%     hSystem.set_title_string('Blizzard')
    pause(2.5);

    hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.PARTLY_CLOUDY);
    hEnvironmentOutdoors2.set_outdoor_lighting(0);
%     hSystem.set_title_string('QLABS VERIFICATION SCRIPT')

%     ### Real-Time
%     vr.PrintWSHeader("Real-Time")
%     print("\n\n---Real-Time---")
% 
%     vr.checkFunctionTestList("real_time", "../docs/source/System/real_time_library.rst")
% 
% 


    fprintf('\n\n------------------------------ Communications --------------------------------\n');
    
    qlabs.close();
    disp('All done!');

end

function eval(return_value, expected_value, message)

    if (return_value == expected_value)
        fprintf('Good: %s (expected %d): %d\n', message, expected_value, return_value)
    else
        fprintf('*** ERROR: %s (expected %d): %d\n', message, expected_value, return_value)
    end
end