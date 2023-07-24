function change_hil_read_timebase_settings(folder)
%CHANGE_HIL_READ_TIMEBASE_SETTINGS Changes HIL Read Timebase blocks to use
% the Synchronize option on the Advanced tab. Note that the samples in
% buffer does not need to change as it is ignored for tnis option.
%
%   CHANGE_HIL_READ_TIMEBASE_SETTINGS(folder)
%
% For example:
%   CHANGE_HIL_READ_TIMEBASE_SETTINGS('C:\Examples')

qc_check_arguments(0, 1, nargin);

if nargin < 1
    folder = pwd;
end

old_folder = pwd;
try
    cd(folder);
    d = dir('**\*.slx');

    for i=1:numel(d)
        cd(d(i).folder);
        [~, model, ext] = fileparts(d(i).name);
        if strcmp(ext, '.slx')
            load_system(d(i).name);

            blocks = find_system(model, 'FollowLinks', 'off', 'MaskType', 'HIL Read Timebase');
            if ~isempty(blocks)
                for j=1:numel(blocks)
                    block_handle = blocks{j};
                    set_param(block_handle, 'overflow_mode', 'Synchronize (for simulated cards only)');
                end
            end

            save_system(model);
            close_system(model);
            cd(folder);
        end
    end
catch me
    cd(old_folder);
    me.rethrow;
end

end
