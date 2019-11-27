%====================================================================================
% ventisette description   
%====================================================================================
context(ctxrobot, "192.168.43.229",  "TCP", "8020").
context(ctxconsole, "192.168.43.184",  "TCP", "8030").
 qactor( robot, ctxrobot, "it.unibo.robot.Robot").
  qactor( console, ctxconsole, "it.unibo.console.Console").
