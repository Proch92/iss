%====================================================================================
% sprint1req description   
%====================================================================================
context(ctxbasicrobot, "192.168.43.171",  "TCP", "8018").
context(ctxrobotappl0, "localhost",  "TCP", "8033").
 qactor( basicrobot, ctxbasicrobot, "external").
  qactor( robotappl0, ctxrobotappl0, "it.unibo.robotappl0.Robotappl0").
