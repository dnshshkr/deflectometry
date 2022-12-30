import numpy as np       

imlist = [(1,1),(2,2)]
print("IMLIST: ",imlist)

num = len(imlist)
print("num:",num)

n = np.arange(0, num)
print("n:",n)


#MERGE
R = np.dstack(imlist)
print("R:",R)

M = np.array([np.ones_like(n), np.cos(2*np.pi*n/num), -np.sin(2*np.pi*n/num)]).T #(num, 3)

print("M:",M)
print("M_size:",M.shape)

# M_pinv = np.linalg.inv(M.T @ M) @ M.T #(3, num)
# print("M_pinv:",M_pinv)

# U = np.tensordot(M_pinv, R, axes=(1,2)).transpose(1, 2, 0) #(height, width, 3)
# print("U:",U)