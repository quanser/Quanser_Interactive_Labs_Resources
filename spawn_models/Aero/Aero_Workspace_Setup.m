%% Initialize workspace
% clear workspace
clear;
% Set Path
%addpath(pwd)
%addpath([pwd '\Export'])
% addpath([pwd '\Scripts'])
%addpath([pwd '\Images'])
% 
%% Load AERO parameters 
Aero_Workspace_Parameters; % model parameters
Aero_x00_AeroDynamicModelMainAssembly_DataFile; % SimScape data file from SolidWorks import
Pitch_deg_range = 62; % +/- degrees pitch can move before hitting hardstop 
% 