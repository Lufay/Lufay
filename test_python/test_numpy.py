import numpy as np

print(np.sctypeDict.keys())
print(set(x.__name__ for x in np.sctypeDict.values()))

a = np.arange(20).reshape((4, 5))
print(np.atleast_3d(a))
# a = np.arange(60).reshape((3, 4, 5))
# print(a, a[:, 1:3, 2:5])
# a.ravel()

# a[:, 1:3, 2:5] = np.random.randint(np.zeros((3,2,3)),[100, 200, 300])
# print(a)
# print(a.T)
# print(list(a.flat))

# it = np.nditer(a, flags=['c_index'])
# while not it.finished:
#     print(it[0], it.index)
#     it.iternext()

b = np.arange(120).reshape((2,3,4,5))
print(b, b.shape)
for i in range(0,4):
    print(np.rollaxis(b, i).shape)
for i in range(0, 4):
    for j in range(3,i,-1):
        print(i, j, np.swapaxes(b, i, j).shape)
print(np.broadcast_to(np.arange(3), (5,4,3)))

import numpy as np
a = np.arange(2*3*4*5*6).reshape((2,3,4,5,6))
b = np.arange(100, 100+2*3*4*5*6).reshape((2,3,4,5,6))
s0 = np.stack([a,b],axis=0)
print(s0)
s1 = np.stack([a,b],axis=1)
print(s1)
s2 = np.stack([a,b],axis=2)
print(s2)
s3 = np.stack([a,b],axis=3)
print(s3)
c0 = np.concatenate((a,b),axis=0)
print(c0)
c1 = np.concatenate((a,b),axis=1)
print(c1)
c2 = np.concatenate((a,b),axis=2)
print(c2)
v = np.vstack((a,b)) # 1->s0, 2->c0, 3->c0
print(np.all(v==c0))
h = np.hstack((a,b)) # 1->c0, 2->c1, 3->c1
print(np.all(h==c1))
d = np.dstack((a,b)) # 1->s1, 2->s2, 3->c2
print(np.all(d==c2))

a = np.arange(4)
b = np.arange(4,8)
c = np.concatenate((np.atleast_2d(a), np.atleast_2d(b)), axis=0)
d = np.vstack((a,b))
print(c, d)
c = np.concatenate((np.atleast_3d(a), np.atleast_3d(b)), axis=2)
d = np.dstack((a,b))
print(c,d)

a = np.arange(6).reshape((2,3))
b = np.arange(10, 16).reshape((2,3))
c = np.concatenate((np.atleast_3d(a), np.atleast_3d(b)), axis=2)
d = np.dstack((a,b))
print(c,d)

a = np.arange(8).reshape((2,-1))
# a.resize(2,5)
b = np.resize(a, (2,5))
print(a, b)

a = np.arange(3)
a = np.atleast_2d(a).swapaxes(0,1)
b = np.arange(3,6)
b = np.atleast_2d(b)
print(a, b)
bc = np.broadcast(a, b)
c = np.empty(bc.shape)
c.flat = [u+v for u,v in bc]
print(c)

a = np.empty((1, 1, 3, 1)).squeeze()
print(a.shape)


# x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])  
# print ('我们的数组是：')
# print (x)
# print ('\n')
# # 现在我们会打印出大于 5 的元素  
# print  ('大于 5 的元素是：')
# print(x>=4)
# print (x[x >= 4])

# x=np.arange(32).reshape((8,4))
# print(x)
# # 二维数组读取指定下标对应的行
# print("-------读取下标对应的行-------")
# print (x[[4,2,1,7], None])
# print(np.ix_([1,5,7,2],[0,3,1,2]))