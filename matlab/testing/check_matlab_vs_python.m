
function check_matlab_vs_python()
    close all;
    clear all;
    clc;
    
    matlab_qvl = "../qvl/*.m";
    python_qvl = "../../python/qvl/*.py";

    python_file_list = get_python_list(python_qvl);
    matlab_file_list = get_matlab_list(matlab_qvl);
    
    compare_class_list(python_file_list, matlab_file_list, true);

    
    compare_function_list(python_file_list, matlab_file_list, "../../python/qvl/", "../qvl/");
    
    


end

%%
function compare_function_list(python_list, matlab_list, python_path, matlab_path)
    python_match = compare_class_list(python_list, matlab_list, false);

    fprintf("=======================\n")
    fprintf("Class method comparison\n");
    fprintf("=======================\n")

    for index = 1:length(python_match)
        if (python_match(index) == 1)
            python_function_list = "";
            python_function_list_count = 0;
            matlab_function_list = "";
            matlab_function_list_count = 0;            

            fprintf("\n\n%s\n", python_list(index));
            fprintf("-----------------\n")

            % get python functions

            text = readlines(sprintf("%s%s.py", python_path, python_list(index)));
            for line = 1:length(text)
                current_line = char(strtrim(text(line)));
                
                if length(current_line) > 6
                    if (current_line(1:4) == "def ")
                        if (current_line(5:6) == "__")

                        else
                            python_function_list_count = python_function_list_count + 1;
                            python_function_list(python_function_list_count) = get_python_function_name(current_line);
                            %fprintf("(p) %s\n", python_function_list(python_function_list_count))
                            
                        end
                    end

                end

            end

            % get matlab functions

            text = readlines(sprintf("%sqlabs_%s.m", matlab_path, python_list(index)));
            for line = 1:length(text)
                current_line = char(strtrim(text(line)));
                
                if length(current_line) > 11
                    if (current_line(1:9) == "function ")
                        if (current_line(1:14) ~= "function obj =")
                            matlab_function_list_count = matlab_function_list_count + 1;
                            matlab_function_list(matlab_function_list_count) = get_matlab_function_name(current_line);
                            
                            %fprintf("(m) %s\n", matlab_function_list(matlab_function_list_count))
                        end    
                    end

                end

            end  

            % compare lists
            all_functions_match = true;

            for i = 1:python_function_list_count
                found = false;
                for j = 1:matlab_function_list_count
                    if python_function_list(i) == matlab_function_list(j)
                        found = true;
                    end
                end
                if (found == false)
                    fprintf("(Matlab) %s\n", python_function_list(i))
                    all_functions_match = false;
                end                
            end

            for i = 1:matlab_function_list_count
                found = false;
                for j = 1:python_function_list_count
                    if python_function_list(j) == matlab_function_list(i)
                        found = true;
                    end
                end
                if (found == false)
                    fprintf("(Python) %s\n", matlab_function_list(i))
                    all_functions_match = false;
                end                
            end


            if (all_functions_match)
                fprintf("All functions match.\n")
            end

        end
    end

end

%%
function name = get_python_function_name(raw_text)
    name = raw_text(5:end);

    if (name(1) == "_")
        name = name(2:end);
    end

    name = name(1:strfind(name, "(")-1);
end

%%
function name = get_matlab_function_name(raw_text)
    name = raw_text;

    index = strfind(name, "=");
    if isempty(index)
        name = name(10:end);
    else
        name = name(index+2:end);
    end
    name = name(1:strfind(name, "(")-1);

end

%%
function file_list = get_python_list(python_qvl)

    py_files = dir(python_qvl);
    
    count = 1;
    
    while (count < length(py_files) )
        if (strfind(py_files(count).name, "__"))
            py_files(count) = [];
        else
            count = count + 1;
        end
    end
    
    
    file_list = "";
    
    for (count = 1:length(py_files))
        file_list(count) = extractBefore(py_files(count).name, length(py_files(count).name)-2);
    end
    
end

%%
function file_list = get_matlab_list(matlab_qvl)

    m_files = dir(matlab_qvl);
    
    file_list = "";
    
    for (count = 1:length(m_files))
        file_list(count) = extractBefore(m_files(count).name, length(m_files(count).name)-1);
        
        index = strfind(file_list(count), "qlabs_");
        if index > 0
            file_list(count) = extractAfter(file_list(count), index+5);
        end
    end
    
end

%%
function python_match = compare_class_list(python_list, matlab_list, display_missing)

    found_all = true;
    python_match = zeros(length(python_list),1);

    if (display_missing)
        fprintf("Matlab Class List\n")
        fprintf("-----------------\n")
    end

    for i = 1:length(python_list)
        found = false;

        if not(strcmp(python_list(i), "qlabs"))
            for j = 1:length(matlab_list)
                if (strcmp(python_list(i), matlab_list(j)))
                    found = true;
                    python_match(i) = 1;
                end
            end
    
            if (found == false)
                found_all = false;
                if (display_missing)
                    fprintf("Missing " + python_list(i) + "\n");
                end
                
            end
        end
    end

    if (found_all == true && display_missing)
        fprintf("All classes matched.\n")
    end

    if (display_missing)
        fprintf("\n\n")


        fprintf("Python Class List\n")
        fprintf("-----------------\n")
    end

    for i = 1:length(matlab_list)
        found = false;

        if not(strcmp(matlab_list(i), "comm_modular_container") || strcmp(matlab_list(i), "quanser_interactive_labs"))
            for j = 1:length(python_list)
                if (strcmp(matlab_list(i), python_list(j)))
                    found = true;
                end
            end
    
            if (found == false)
                found_all = false;
                if (display_missing)
                    fprintf("Missing " + matlab_list(i) + "\n")
                end                
                
            end    
        end

        
    end

    if (found_all == true)
        fprintf("All classes matched.\n")
    end

    fprintf("\n\n")    


end