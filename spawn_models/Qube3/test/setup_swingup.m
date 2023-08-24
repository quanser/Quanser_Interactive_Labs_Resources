% Load model parameters
qube2_rotpen_param;
% Moment of inertia of pendulum about center of mass (kg-m^2)
Jp_cm = mp*Lp^2/12; % used to calculate pendulum energy in swing-up control
% 
%% Swing-Up Control
% Reference Energy (J)
Er = 2*mp*g*l;
% Maximum torque for 10 V
tau_max = kt*10/Rm;
% Maximum acceleration of pivot (m/s^2)
a_max = tau_max / (mr*r);