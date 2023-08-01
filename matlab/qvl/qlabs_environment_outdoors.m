classdef qlabs_environment_outdoors < handle
    properties
        c = [];
        
%         This class modifies QLabs open worlds with outdoor environments.

        ID_ENVIRONMENT_OUTDOORS = 1100
%         Class ID
    
        FCN_SET_TIME_OF_DAY = 10
        FCN_SET_TIME_OF_DAY_ACK = 11
        FCN_OVERRIDE_OUTDOOR_LIGHTING = 12
        FCN_OVERRIDE_OUTDOOR_LIGHTING_ACK = 13
        FCN_SET_WEATHER_PRESET = 14
        FCN_SET_WEATHER_PRESET_ACK = 15
    
        CLEAR_SKIES = 0
        PARTLY_CLOUDY = 1
        CLOUDY = 2
        OVERCAST = 3
        FOGGY = 4
        LIGHT_RAIN = 5
        RAIN = 6
        THUNDERSTORM = 7
        LIGHT_SNOW = 8
        SNOW = 9
        BLIZZARD = 10
        
        qlabs = [];
        verbose = false;
        classID = 0;
    end

    methods
        function obj = qlabs_environment_outdoors(qlabs, verbose)

            arguments
                qlabs quanser_interactive_labs
                verbose logical = false
            end            

            obj = obj@handle();

            obj.qlabs = qlabs;
            obj.verbose = verbose;
            obj.c = qlabs_comm_modular_container();
        end

        function success = set_time_of_day(obj, time)
            arguments
                obj qlabs_environment_outdoors
                time single = 12
            end
            success = false;

%             Set the time of day for an outdoor environment.
% 
%             :param time: A value from 0 to 24. Midnight is a value 0 or 24. Noon is a value of 12.
%             :type time: float
%             :return: `True` if setting the time was successful, `False` otherwise
%             :rtype: boolean

            obj.c.classID = self.ID_ENVIRONMENT_OUTDOORS;
            obj.c.actorNumber = 0;
            obj.c.actorFunction = self.FCN_SET_TIME_OF_DAY;
            obj.c.payload = [flip(typecast(single(time), 'uint8'))];
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);

            obj.qlabs.flush_receive();

           if (obj.qlabs.send_container(obj.c))
                if waitForConfirmation
                    rc = obj.qlabs.wait_for_container(obj.ID_SPLINE_LINE, obj.actorNumber, obj.FCN_SET_TIME_OF_DAY_ACK);
                    if isempty(rc)
                        if (obj.verbose == true)
                            fprintf('Timeout waiting for response.\n')
                        end
                        return
                    end
                end
                success = true;
                return
            end
        end

        function success = set_outdoor_lighting(obj, state)
            arguments
                obj qlabs_environment_outdoors
                state single
            end
            success = false;

%             Overrides the outdoor lighting set by other environment functions
% 
%             :param state: 0 force lights off, 1 force lights on
%             :type time: int32
%             :return: `True` if setting the time was successful, `False` otherwise
%             :rtype: boolean

            obj.c.classID = obj.ID_ENVIRONMENT_OUTDOORS;
            obj.c.actorNumber = 0;
            obj.c.actorFunction = obj.FCN_OVERRIDE_OUTDOOR_LIGHTING;
            obj.c.payload = [flip(typecast(int32(state), 'uint8'))];
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);

            obj.qlabs.flush_receive();

            if (obj.qlabs.send_container(obj.c))
                rc = obj.qlabs.wait_for_container(obj.ID_ENVIRONMENT_OUTDOORS, 0, obj.FCN_OVERRIDE_OUTDOOR_LIGHTING_ACK);
                if isempty(rc)
                    if (obj.verbose == true)
                        fprintf('Timeout waiting for response.\n')
                    end
                    return
                end
            end
            success = true;
            return
        end

        function success = set_weather_preset(obj, weather_preset)
            arguments
                obj qlabs_environment_outdoors
                weather_preset single
            end
            success = false;

%             Set the weather conditions for an outdoor environment with a preset value
% 
%             :param time: A preset index (see defined constants for weather types)
%             :type time: int32
%             :return: `True` if setting the time was successful, `False` otherwise
%             :rtype: boolean
            
            obj.c.classID = obj.ID_ENVIRONMENT_OUTDOORS;
            obj.c.actorNumber = 0;
            obj.c.actorFunction = obj.FCN_SET_WEATHER_PRESET;
            obj.c.payload = [flip(typecast(int32(weather_preset), 'uint8'))];
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);

            obj.qlabs.flush_receive();

            if (obj.qlabs.send_container(obj.c))
                rc = obj.qlabs.wait_for_container(obj.ID_ENVIRONMENT_OUTDOORS, 0, obj.FCN_OVERRIDE_OUTDOOR_LIGHTING_ACK);
                if isempty(rc)
                    if (obj.verbose == true)
                        fprintf('Timeout waiting for response.\n')
                    end
                    return
                end
                success = true;
                return
            end
        end
    end
end