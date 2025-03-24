import streamlit as st

import plotly.express as pex
from plotly.subplots import make_subplots
import plotly.graph_objects as pgo
import matplotlib.pyplot as plt


st.title("LET'S VISUALIZE!")
st.markdown('Our Interactive Dashboard aims to visualize three chaotic equations: The Logistic Map, The Henon Map, and The Lorenz System. Users can select their desired chaotic equation from the sidebar and adjust the parameters associated with each equation!!!')
st.markdown("LET'S GET STARTED!")
st.sidebar.title("SELECT YOUR CHAOS!")
st.sidebar.markdown("Select the desired chaotic equation: ")

def logistic_map(r, initial_population, num_iterations):
    population = [initial_population]

    for i in range(num_iterations):
        new_population = r * population[-1] * (1 - population[-1])
        population.append(new_population)

    return population

def henon_map(a, b, x0, y0, num_iterations):
    x = [x0]
    y = [y0]
    
    for i in range(num_iterations):
        xn = y[-1] + 1 - a * x[-1]**2
        yn = b * x[-1]
        x.append(xn)
        y.append(yn)
    
    return x, y

def lorenzone(x1, y1, z1, s, r, b):
    x_dot1 = s * (y1 - x1)
    y_dot1 = r * x1 - y1 - x1 * z1
    z_dot1 = x1 * y1 - b * z1
   
    return x_dot1, y_dot1, z_dot1

def lorenztwo(x1, y1, z1, x2, y2, z2, s, r, b):
    x_dot1 = s * (y1 - x1)
    y_dot1 = r * x1 - y1 - x1 * z1
    z_dot1 = x1 * y1 - b * z1
    x_dot2 = s * (y2 - x2)
    y_dot2 = r * x2 - y2 - x2 * z2
    z_dot2 = x2 * y2 - b * z2
    return x_dot1, y_dot1, z_dot1, x_dot2, y_dot2, z_dot2

# Set up the sliders for each chaotic equation
if st.sidebar.checkbox("Logistic Map", key="logistic"):
    st.sidebar.subheader("Logistic Map Parameters")
    st.subheader("Logistic Map")
    r = st.sidebar.slider("Growth rate(r)", min_value=0.0, max_value=4.0, value=0.0, step=0.01)
    initial_population = st.sidebar.slider("Initial Population", min_value=0.0, max_value=1.0, value=0.2, step=0.01)
    num_iterations = st.sidebar.slider("Number of Iterations", min_value=0, max_value=150, value=1, step=1)
    population = logistic_map(r, initial_population, num_iterations)
    fig = make_subplots(rows=1, cols=1)
    fig.add_trace(pgo.Scatter(x=list(range(num_iterations+1)), y=population, mode="lines", name="Population VS Iteration"),row=1, col=1)
    fig.update_layout(height=500, width=1000)
    st.plotly_chart(fig)

if st.sidebar.checkbox("Henon Map: 1 Point", key="henon_1"):
    st.sidebar.subheader("Henon Map Parameters")
    st.subheader("Henon Map for a single point: (x,y)=(0.1,0.1)")
    a = 1.4
    b = 0.3
    x0 = st.sidebar.slider("x0", min_value=-2.00, max_value=2.00, value=0.63, step=0.001)
    y0 = st.sidebar.slider("y0", min_value=-2.00, max_value=2.00, value=0.19, step=0.001)
    
    num_iterations = st.sidebar.slider("Number of Iterations", min_value=0, max_value=50000, value=1, step=1)
    
    x0_val, y0_val = henon_map(a, b, x0, y0, num_iterations)
    
    fig = make_subplots(rows=1, cols=1)
    
    fig.add_trace(pgo.Scatter(x=x0_val, y=y0_val, mode="markers", name="First Point"),row=1, col=1)
    fig.update_layout(height=800, width=800)
    st.plotly_chart(fig)

if st.sidebar.checkbox("Henon Map: 2 Points", key="henon_2"):
    st.sidebar.subheader("Henon Map Parameters")
    st.subheader("Henon Map for 2 points: (0.1,0.2),(0.11,0.21)")
    a = 1.4
    b = 0.3
    x0 = st.sidebar.slider("x0", min_value=-2.0, max_value=2.0, value=0.1, step=0.1)
    y0 = st.sidebar.slider("y0", min_value=-2.0, max_value=2.0, value=0.2, step=0.1)
    x1 = st.sidebar.slider("x1", min_value=-2.0, max_value=2.0, value=0.11, step=0.1)
    y1 = st.sidebar.slider("y1", min_value=-2.0, max_value=2.0, value=0.21, step=0.1)
    num_iterations = st.sidebar.slider("Number of Iterations", min_value=0, max_value=50000, value=1, step=1)
    
    x0_val, y0_val = henon_map(a, b, x0, y0, num_iterations)
    x1_val, y1_val = henon_map(a, b, x1, y1, num_iterations)
    fig = make_subplots(rows=1, cols=1)
    

    fig.add_trace(pgo.Scatter(x=x0_val, y=y0_val, mode="lines", name="First Point"),row=1, col=1)
    fig.add_trace(pgo.Scatter(x=x1_val, y=y1_val, mode="lines", name="Second Point"),  row=1, col=1)
    
    fig.update_layout(height=800, width=800)
    st.plotly_chart(fig)
dt = 0.01

if st.sidebar.checkbox("Lorenz System: 1 point", key="lorenz_1"):
    st.sidebar.subheader("Lorenz System Parameters")
    st.subheader("Lorenz System for a single point")
    x1 = st.sidebar.slider("x1", min_value=-20.0, max_value=30.0, value=0.01, step=0.1)
    y1 = st.sidebar.slider("y1", min_value=-20.0, max_value=30.0, value=0.01, step=0.1)
    z1 = st.sidebar.slider("z1", min_value=-20.0, max_value=30.0, value=0.01, step=0.1)
    #x2 = st.sidebar.slider("x2", min_value=-20.0, max_value=30.0, value=10.1, step=0.1)
    #y2 = st.sidebar.slider("y2", min_value=-20.0, max_value=30.0, value=28.1, step=0.1)
    #z2 = st.sidebar.slider("z2", min_value=-20.0, max_value=30.0, value=2.668, step=0.1)
    s = st.sidebar.slider("Sigma", min_value=0.0, max_value=30.0, value=10.0, step=0.1)
    r = st.sidebar.slider("Rho", min_value=0.0, max_value=50.0, value=28.0, step=0.1)
    b = st.sidebar.slider("Beta", min_value=0.0, max_value=10.0, value=2.667, step=0.1)

    x1s, y1s, z1s = [], [], []
    #x2s, y2s, z2s = [], [], []

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    for i in range(2000):
        # Calculate the next state of the system 1
        x_dot1, y_dot1, z_dot1 = lorenzone(x1, y1, z1, s, r, b)
        x1 += x_dot1 * dt
        y1 += y_dot1 * dt
        z1 += z_dot1 * dt
        x1s.append(x1)
        y1s.append(y1)
        z1s.append(z1)

        # Calculate the next state of the system for system 2
       # x2 += x_dot2 * dt
        #y2 += y_dot2 * dt
       # z2 += z_dot2 * dt
        #x2s.append(x2)
        #y2s.append(y2)
        #z2s.append(z2)

    ax.clear()
    ax.set_xlim(-25, 25)
    ax.set_ylim(-35, 35)
    ax.set_zlim(5, 55)
    ax.plot(x1s, y1s, z1s, label="Lorenz System ", lw=1)
    #ax.plot(x2s, y2s, z2s, label="Lorenz System 2", lw=1)
    ax.scatter(x1, y1, z1, color="blue", label="Current Position 1", lw=1.5)
    #ax.scatter(x2, y2, z2, color="orange", label="Current Position 2", lw=1.5)
    # Set the axis labels and legend
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.legend()
    # Display the figure using Streamlit
    st.pyplot(fig)

if st.sidebar.checkbox("Lorenz System: 2 points", key="lorenz_2"):
    st.sidebar.subheader("Lorenz System Parameters")
    st.subheader("Lorenz System for points $(x_1,y_1,z_1)$=(0, 1, 1.05) & $(x_2, y_2, z_2)$=(0.001, 1.001, 1.051)")
    x1 = 0
    y1 = 1
    z1 = 1.05
    x2 = 0.001
    y2 = 1.001
    z2 = 1.051
    s = st.sidebar.slider("Sigma", min_value=0.0, max_value=30.0, value=10.0, step=0.1)
    r = st.sidebar.slider("Rho", min_value=0.0, max_value=50.0, value=28.0, step=0.1)
    b = st.sidebar.slider("Beta", min_value=0.0, max_value=10.0, value=2.667, step=0.1)

    x1s, y1s, z1s = [], [], []
    x2s, y2s, z2s = [], [], []

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    for i in range(2000):
        # Calculate the next state of the system 1
        x_dot1, y_dot1, z_dot1, x_dot2, y_dot2, z_dot2 = lorenztwo(x1, y1, z1, x2, y2, z2, s, r, b)
        x1 += x_dot1 * dt
        y1 += y_dot1 * dt
        z1 += z_dot1 * dt
        x1s.append(x1)
        y1s.append(y1)
        z1s.append(z1)

        # Calculate the next state of the system for system 2
        x2 += x_dot2 * dt
        y2 += y_dot2 * dt
        z2 += z_dot2 * dt
        x2s.append(x2)
        y2s.append(y2)
        z2s.append(z2)

    ax.clear()
    ax.set_xlim(-25, 25)
    ax.set_ylim(-35, 35)
    ax.set_zlim(5, 55)
    ax.plot(x1s, y1s, z1s, label="Lorenz System 1", lw=1)
    ax.plot(x2s, y2s, z2s, label="Lorenz System 2", lw=1)
    ax.scatter(x1, y1, z1, color="blue", label="Current Position 1", lw=1.5)
    ax.scatter(x2, y2, z2, color="orange", label="Current Position 2", lw=1.5)
    # Set the axis labels and legend
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.legend()
    # Display the figure using Streamlit
    st.pyplot(fig)