%====================================================================================
% basicrobot description   
%====================================================================================
context(ctxrobot, "localhost",  "TCP", "8018").
 qactor( robot, ctxrobot, "it.unibo.robot.Robot").
  qactor( robotcallersimulator, ctxrobot, "it.unibo.robotcallersimulator.Robotcallersimulator").
