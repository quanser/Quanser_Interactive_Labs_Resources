
function check_matlab_vs_python()
    close all;
    clear all;
    clc;
    
    matlab_qvl = "../qvl/*.m";
    python_qvl = "../../python/qvl/*.py";

    python_file_list = get_python_list(python_qvl);
    matlab_file_list = get_matlab_list(matlab_qvl);
    
    compare_class_list(python_file_list, matlab_file_list);
    


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
function compare_class_list(python_list, matlab_list)

    found_all = true;


    fprintf("Matlab Class List\n")
    fprintf("-----------------\n")

    for i = 1:length(python_list)
        found = false;

        if not(strcmp(python_list(i), "qlabs"))
            for j = 1:length(matlab_list)
                if (strcmp(python_list(i), matlab_list(j)))
                    found = true;
                end
            end
    
            if (found == false)
                found_all = false;
                fprintf("Missing " + python_list(i) + "\n");
            end
        end
    end

    if (found_all == true)
        fprintf("All classes matched.\n")
    end

    fprintf("\n\n")


    fprintf("Python Class List\n")
    fprintf("-----------------\n")

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
                fprintf("Missing " + matlab_list(i) + "\n")
            end    
        end

        
    end

    if (found_all == true)
        fprintf("All classes matched.\n")
    end

    fprintf("\n\n")    


end