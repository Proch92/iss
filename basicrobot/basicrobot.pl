%====================================================================================
% basicrobot description   
%====================================================================================
context(ctxbasicrobot, "10.201.116.57",  "TCP", "8018").
 qactor( robotadapter, ctxbasicrobot, "itunibo.robot.robotAdapterQa").
  qactor( basicrobot, ctxbasicrobot, "it.unibo.basicrobot.Basicrobot").
  qactor( sentinel, ctxbasicrobot, "it.unibo.sentinel.Sentinel").
