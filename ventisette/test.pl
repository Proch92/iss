%====================================================================================
% test description   
%====================================================================================
context(ctxtest, "localhost",  "TCP", "8020").
context(ctxpython, "127.0.0.1",  "TCP", "8019").
 qactor( robot, ctxpython, "external").
  qactor( source, ctxtest, "it.unibo.source.Source").
