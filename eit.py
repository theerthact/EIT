#!/usr/bin/python3

import numpy as np
import streamlit as st

from matplotlib import pyplot as plt

st.header("Absorption and Dispersion spectrum for a 3 level ladder system")
st.text("It plots the absorption and dispersion spectrum against probe detuning for a simple 3 level ladder system. Here we can change the values of all the variables")

A = st.sidebar.number_input('γ_21', value=1.0, min_value=0.0, max_value=10000.0)
B = st.sidebar.number_input('γ_31', value=1.0, min_value=0.0, max_value=10000.0)
D = st.sidebar.number_input('Ω_c', value=1.0, min_value=0.0, max_value=10000.0)
c_min = st.sidebar.number_input('Δ1 Minimum', value=1, min_value=-10000, max_value=10000)
c_max = st.sidebar.number_input('Δ1 Maximum', value=1, min_value=-10000, max_value=10000)
c_step = st.sidebar.number_input('Δ1 Step', value=1.0, min_value=0.0, max_value=10000.0)
C = np.arange(c_min, c_max, c_step)
re = (C*(D**2 - 4*C**2 - 4*B**2)) / ((4*(B*A-C**2)+D**2)**2 + 16*C*C*(A+B)**2)
im = (4*A*(B**2+C**2)+D*D*B) / ((4*(B*A-C**2)+D**2)**2 + 16*C*C*(A+B)**2)

fig, ax = plt.subplots()
ax.plot(C, im, label='Imaginary')
ax.plot(C, re, label='Real')
ax.set_title(f"Absorption and Despersion Curves(Rabi Frequency, $\Omega_c = {D}$)")
ax.set_xlabel("Detuning $\Delta_1$ (arbitrary units)")
ax.set_ylabel("Susceptibility $\chi$ (arbitrary units)")
ax.legend()
st.pyplot(fig)

fn = "eit.png"
plt.savefig(fn)
with open(fn, "rb") as img:
    btn = st.download_button(
        label="Download Graph",
        data=img,
        file_name=fn,
        mime="image/png"
    )
