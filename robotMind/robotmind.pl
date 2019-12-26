%====================================================================================
% robotmind description   
%====================================================================================
context(ctxmind, "192.168.1.92",  "TCP", "8020").
context(ctxbasicrobot, "127.0.0.1",  "TCP", "8030").
 qactor( robot, ctxbasicrobot, "external").
  qactor( robotmind, ctxmind, "it.unibo.robotmind.Robotmind").
  qactor( detector, ctxmind, "it.unibo.detector.Detector").
