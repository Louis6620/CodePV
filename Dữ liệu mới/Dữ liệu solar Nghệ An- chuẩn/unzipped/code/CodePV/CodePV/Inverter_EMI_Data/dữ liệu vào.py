import matplotlib.pyplot as plt

# Tạo ra danh sách các điểm trên đường thẳng đầu tiên
x1 = [0, 1, 2, 3, 4, 5]
y1 = [1, 3, 5, 7, 9, 11]

# Tạo ra danh sách các điểm trên đường thẳng thứ hai
x2 = [0, 1, 2, 3, 4, 5]
y2 = [0, 2, 4, 6, 8, 10]

# Vẽ đường thẳng đầu tiên
plt.plot(x1, y1)

# Vẽ đường thẳng thứ hai
plt.plot(x2, y2)

# Hiển thị biểu đồ
plt.show()