# На координатной прямой отмечены три различные точки с координатами x1, x2, x3 соответственно. 
# Улитка проползла из первой точки во вторую, затем из второй точки в третью и затем из третьей точки вернулась в первую. 
# Выведите суммарную длину пути улитки.

x1 = int(input())
x2 = int(input())
x3 = int(input())
print(abs(x2 - x1) + abs(x3 - x2) + abs(x1 - x3))
