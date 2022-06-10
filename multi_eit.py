#!/usr/bin/python3

import numpy as np
import streamlit as st

from matplotlib import pyplot as plt

st.header("Absorption and Dispersion spectrum for a multi level (Y type) ladder system")
st.text("It plots the absorption and dispersion spectrum against probe detuning for a multi level (Y type) ladder system. Here we can change the values of all the variables")

A = 0.01
B = st.sidebar.number_input('Ω_c', value=1.0, min_value=-10000.0, max_value=10000.0)
C = st.sidebar.number_input('Ω_s', value=1.0, min_value=-10000.0, max_value=10000.0)
d_min = st.sidebar.number_input('Δp Minimum', value=1, min_value=-10000, max_value=10000)
d_max = st.sidebar.number_input('Δp Maximum', value=1, min_value=-10000, max_value=10000)
d_step = st.sidebar.number_input('Δp Step', value=1.0, min_value=0.0, max_value=10000.0)
D = np.arange(d_min, d_max, d_step)
E = st.sidebar.number_input('Γ_21', value=1.0, min_value=-10000.0, max_value=10000.0)
F = st.sidebar.number_input('Γ_31', value=1.0, min_value=-10000.0, max_value=10000.0)
G = st.sidebar.number_input('Γ_41', value=1.0, min_value=-10000.0, max_value=10000.0)

denom = (((F**2+D**2)*(G**2*E+D**2*E+C**2*G/4)+(G**2+D**2)*((B**2*F)/4))**2) + (D**2*((F**2+D**2)*(G**2+D**2-(C**2)/4)-(G**2+D**2)*(B**2*F/4))**2)
im = ((A/2)*((F**2+D*D)*(G**2+D*D))*((F**2+D*D)*(G**2+D*D)*E+(G**2+D*D)*((B**2)/4)*F+(F**2+D*D)*(C**2)*G/4)) / denom
re = (D*A/2)*(((F**2+D**2)*(G**2+D**2-(C**2)/4))-((G**2+D**2)*(B**2)/4))*((F**2+D**2)*(G**2+D**2)) / denom

fig, ax = plt.subplots()
ax.plot(D, im, label='Imaginary')
ax.plot(D, re, label='Real')
ax.set_title(f"Absorption and Despersion Curves(Rabi Frequency, $\Omega_c = {B} and \Omega_c = {B}$)")
ax.set_xlabel("Detuning $\Delta_p$ (arbitrary units)")
ax.set_ylabel("Susceptibility $\chi$ (arbitrary units)")
ax.legend()
st.pyplot(fig)

fn = "multi_eit.png"
plt.savefig(fn)
with open(fn, "rb") as img:
    btn = st.download_button(
        label="Download Graph",
        data=img,
        file_name=fn,
        mime="image/png"
    )
