%====================================================================================
% basicrobot description   
%====================================================================================
context(ctxbasicrobot, "172.0.0.1",  "TCP", "8030").
 qactor( robotadapter, ctxbasicrobot, "itunibo.robot.robotAdapterQaStream").
  qactor( robot, ctxbasicrobot, "it.unibo.robot.Robot").
