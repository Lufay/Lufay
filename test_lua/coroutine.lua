#!/usr/bin/env lua

--[[
function foo(str)
    if type(str) ~= "string" then
        error("not string")
    end
    print("End")
end

pcall(foo({}))
--]]

function myyield()
    print("in myyield before")
    coroutine.yield()
    print("in myyield after")
end

co = coroutine.create(function()
    print("hello", coroutine.yield())
end)
co2 = coroutine.create(function() print("hello2") print(coroutine.status(co2)) end)
co3 = coroutine.create(function()
    print("before")
    coroutine.yield()
    print("before myyield")
    myyield();
    print("after")
end)


coroutine.resume(co, 1)
coroutine.resume(co2)
coroutine.resume(co3)
print(coroutine.status(co))
print(coroutine.status(co2))
print(coroutine.status(co3))

print("yielding1")

coroutine.resume(co, 2)
coroutine.resume(co3)

print("yielding2")

print(coroutine.status(co))
print(coroutine.status(co3))
print(coroutine.resume(co3))
print(coroutine.status(co3))
