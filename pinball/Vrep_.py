threadFunction=function()
 
sim.setThreadSwitchTiming(2) -- Default timing for automatic thread switching
 
-- Here we execute the regular thread code:
res,err=xpcall(threadFunction,function(err) return debug.traceback(err) end)
    if not res then
    sim.addStatusbarMessage('Lua runtime error: '..err)
    end
 
-- Put some clean-up code here:
simRemoteApi.start(19997)
end