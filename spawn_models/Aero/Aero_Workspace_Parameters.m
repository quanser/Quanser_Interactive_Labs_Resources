% 
%% Quanser Aero Parameters
% 
% Moment of Inertia of helicopter body (kg-m^2)
L_body = 6.5*0.0254; % length of horizontal body (metal tube)
m_body = 0.094; % mass of horizontal body (metal tube) 
J_body = m_body * L_body^2 / 12; % horizontal cylinder rotating about CM
% 
% Moment of Inertia of yoke fork that rotates about yaw axis (kg-m^2)
m_yoke = 0.526; % mass of entire yoke assembly (kg)
% h_yoke = 9*0.0254; % height of yoke assembly (m)
r_fork = 0.04/2; % radius of each fork (approximated as cylinder)
J_yoke = 0.5*m_yoke*r_fork^2;
% 
% Moment of Inertia from motor + guard assembly about pivot (kg-m^2)
m_prop = 0.43; % mass of dc motor + shield + propeller shield
% m_motor = 0.203; % mass of dc motor
r_prop = 6.25*0.0254; % distance from CM to center of pitch axis
J_prop = m_prop * r_prop^2; % using parallel axis theorem
% 
% total aero body mass (kg)
Mb = 1.15; 
% distance from aero body plane to center of mass below (m)
Dm = 7.1e-3; 
% Gravity
g = 9.81;
% 
% Thrust force constant (N/V) [found experimentally] 
Kpp = 0.6*0.0154; % 0.85*0.0154; % low-efficiency
Kyy = 0.0129; % 0.65*0.0129; % low-efficiency
Kpy = 2*0.00329; % 2*0.00329; % low-efficiency
Kyp = -2.5*0.00167; % -2.5*0.00167; % low-efficiency
% 
% Stiffness (N-m/rad)
% Ksp = 0.0405; % 0.037463; % found experimentally
Ksp = 0.45*Mb*g*Dm; % Based on first-principles
% 
% Viscous damping (N-m-s/rad) [found experimentally]
% Dp = 0.0071116; % pitch axis (pre-production unit: Dp = 0.0226) 
% Dy = 0.0220; % yaw axis (pre-production unit: Dy = 0.0211) 
% Identified values (Aug 2021)
% Dp = 1.3*0.0189; % low-efficiency
Dp = 0.65*0.0124; % 0.65*0.0124 0.33*0.0275; 0.0275/4 high-efficiency
% Dy = 0.01798;
% old spawn model: Dp = 0.01 Dy = 0.02;
% Dp = 0.8*0.0189;
Dy = 0.65*0.01798;
% 
%% Fans - Allied Motion CL40 Series 7W Coreless DC Motors, 16705
% Force_per_V = 1; % N/V value to represent axial thrust
% J_motor = 4e-6; % kg-m^2
% R_term = 8.4; % Ohm, terminal resistance
% L_motor = 1.16; % mH, inductance of rotor
% K_motor = 0.042; % constant of proportionality, V/rad/s, or Nm/A
D_motor = 6e-5; % 2e-5; % 3e-4; %0.0002; % m*s*N/rad
% Rotor Moment of Inertia from CAD
% smiData.Solid(168).MoI
% 0.0295    0.0584    0.0295    kg-in^2
% 1.904e-5  3.770e-5    1.904e-5 kg-m^2
% smiData.Solid(168).mass
% 0.0234 kg
% Black propeller = 24 g. Gray propeller = 10 g.
% 