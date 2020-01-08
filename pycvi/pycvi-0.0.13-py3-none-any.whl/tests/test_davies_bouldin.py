from pycvi.internal import davies_bouldin

X0 = [1, 2, 3, 4, 5]
X1 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
y0 = [0, 0, 0, 1, 1]
y1 = [1, 0, 0, 1, 1]

a = davies_bouldin.DB(X0, y0)
print(a.db)

b = davies_bouldin.DB(X0, y1)
print(b.db)

c = davies_bouldin.DB(X1, y0)
print(c.db)