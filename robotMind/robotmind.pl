%====================================================================================
% robotmind description   
%====================================================================================
mqttBroker("localhost", "1884").
context(ctxmind, "192.168.1.128",  "MQTT", "8020").
context(ctxbasicrobot, "127.0.0.1",  "MQTT", "8030").
 qactor( robot, ctxbasicrobot, "external").
  qactor( robotmind, ctxmind, "it.unibo.robotmind.Robotmind").
  qactor( detector, ctxmind, "it.unibo.detector.Detector").
  qactor( tvocsentinel, ctxmind, "it.unibo.tvocsentinel.Tvocsentinel").
  qactor( plasticbox, ctxmind, "it.unibo.plasticbox.Plasticbox").
