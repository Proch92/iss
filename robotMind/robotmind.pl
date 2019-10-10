%====================================================================================
% robotmind description   
%====================================================================================
context(ctxmind, "localhost",  "TCP", "8023").
context(ctxbasicrobot, "10.201.116.57",  "TCP", "8020" ).
 qactor( basicrobot, ctxbasicrobot, "external").
  qactor( robotmind, ctxmind, "it.unibo.robotmind.Robotmind").
