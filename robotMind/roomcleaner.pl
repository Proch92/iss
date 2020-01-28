%====================================================================================
% roomcleaner description   
%====================================================================================
context(ctx, "localhost",  "TCP", "8020").
 qactor( plasticbox, ctx, "it.unibo.plasticbox.Plasticbox").
  qactor( tvocsentinel, ctx, "it.unibo.tvocsentinel.Tvocsentinel").
  qactor( detector, ctx, "it.unibo.detector.Detector").
