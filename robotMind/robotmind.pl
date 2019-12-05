%====================================================================================
% robotmind description   
%====================================================================================
context(ctxmind, "localhost",  "TCP", "8020").
context(ctxbasicrobot, "10.201.116.57",  "TCP", "8018").
 qactor( basicrobot, ctxbasicrobot, "external").
  qactor( robotmind, ctxmind, "it.unibo.robotmind.Robotmind").
