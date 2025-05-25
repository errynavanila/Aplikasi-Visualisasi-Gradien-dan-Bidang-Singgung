import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

st.title("📈 Aplikasi Turunan Parsial - Fungsi Keuntungan Produksi")

st.markdown("""
Fungsi keuntungan produksi yang digunakan adalah:

\\[
f(x, y) = 50x + 40y - x^2 - y^2 - xy
\\]

di mana:
- \\( x \\): jumlah produk A
- \\( y \\): jumlah produk B
""")

# Input titik evaluasi
x0 = st.number_input("Masukkan nilai x₀", value=2.0)
y0 = st.number_input("Masukkan nilai y₀", value=2.0)

# Fungsi keuntungan
def f(x, y):
    return 50*x + 40*y - x**2 - y**2 - x*y

# Turunan parsial
def dfdx(x, y):
    return 50 - 2*x - y

def dfdy(x, y):
    return 40 - 2*y - x

# Evaluasi fungsi dan gradien
z0 = f(x0, y0)
grad_x = dfdx(x0, y0)
grad_y = dfdy(x0, y0)

st.write(f"🔹 Nilai fungsi f(x, y) di ({x0}, {y0}) adalah **{z0}**")
st.write(f"🔸 Turunan parsial ∂f/∂x di ({x0}, {y0}) = **{grad_x}**")
st.write(f"🔸 Turunan parsial ∂f/∂y di ({x0}, {y0}) = **{grad_y}**")

# Grid untuk grafik 3D
x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 50)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Bidang singgung
Z_tangent = z0 + grad_x * (X - x0) + grad_y * (Y - y0)

# Plot grafik
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7)
ax.plot_surface(X, Y, Z_tangent, color='red', alpha=0.5)

ax.set_xlabel("x (produk A)")
ax.set_ylabel("y (produk B)")
ax.set_zlabel("f(x, y) = Keuntungan")
ax.set_title("📊 Permukaan Fungsi Keuntungan dan Bidang Singgung")

st.pyplot(fig)
