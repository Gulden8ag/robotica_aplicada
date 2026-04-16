import numpy as np, matplotlib.pyplot as plt
dt = 0.02; T = 12.0; t = np.arange(0, T, dt)

# inputs: forward speed v(t), yaw rate w(t)
v = 0.25*np.ones_like(t)
w = 0.6*np.sin(0.4*t)  # gentle weave

x = np.zeros_like(t); y = np.zeros_like(t); th = np.zeros_like(t)
for k in range(1, len(t)):
    th[k] = th[k-1] + w[k-1]*dt
    x[k]  = x[k-1]  + v[k-1]*np.cos(th[k-1])*dt
    y[k]  = y[k-1]  + v[k-1]*np.sin(th[k-1])*dt

# "impossible" lateral test (violates Pfaffian): try pure y-translation at th=0
vy_illegal = 0.2
viol = -np.sin(0)*0 + np.cos(0)*vy_illegal  # != 0 -> violates no-slip

plt.figure(); plt.plot(x, y, label='unicycle path'); plt.axis('equal'); plt.legend(); plt.title('Unicycle (Pfaffian respected)')
plt.figure(); plt.plot(t, -np.sin(th)*np.gradient(x,dt) + np.cos(th)*np.gradient(y,dt))
plt.title('A(q) qdot (should be ~0)'); plt.xlabel('t'); plt.ylabel('constraint residual');
plt.show()


L = 0.26  # wheelbase (m), adjust to your kit
delta = 0.35*np.sin(0.3*t)   # steering (rad)
v = 0.3*np.ones_like(t)      # forward speed

x=y=th=0.0
X=[]; Y=[]
for k in range(len(t)):
    th_dot = v*np.tan(delta[k])/L
    x += v*np.cos(th)*dt
    y += v*np.sin(th)*dt
    th += th_dot*dt
    X.append(x); Y.append(y)

plt.figure(); plt.plot(X, Y); plt.axis('equal'); plt.title('Ackermann bicycle (no lateral slip instantaneously)')
plt.show()