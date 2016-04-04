import math
from math import exp, floor

def takacs(nr_layers, A, V, Q_f, X_f, Q_u, params, X, delta_X):
	J = [0] * nr_layers
	v_s = [0] * nr_layers
	
	layer_f = 5
	
	for i in range(nr_layers):
		v_s[i] = max(0.0, min(params[0], params[1]*(exp(-params[2]*(X[i] - params[4]*X_f)) - exp(-params[3]*(X[i] - params[4]*X_f)))))

	for i in range(layer_f-1):
		if X[i+1] > params[5]:
			J[i] = min(v_s[i]*X[i], v_s[i + 1]*X[i + 1])
		else:
			J[i] = v_s[i]*X[i]

	for i in range(layer_f-1,nr_layers-1):
		J[i] = min(v_s[i]*X[i], v_s[i + 1]*X[i + 1])

	J[nr_layers-1] = min(v_s[nr_layers-2]*X[nr_layers-2], v_s[nr_layers-1]*X[nr_layers-1])
		
	delta_X[0] = ((Q_f - Q_u)*(X[1] - X[0]) - J[0]*A)*nr_layers/V

	for i in range(1,layer_f-1):
		delta_X[i] = ((Q_f-Q_u)*(X[i + 1] - X[i]) + (J[i - 1] - J[i])*A)*nr_layers/V

	delta_X[layer_f - 1] = (Q_f*(X_f - X[layer_f - 1]) + (J[layer_f - 2] - J[layer_f - 1])*A)*nr_layers/V

	for i in range(layer_f,nr_layers-1):
		delta_X[i] = (Q_u*(X[i-1] - X[i]) + (J[i-1] - J[i])*A)*nr_layers/V
	
	delta_X[nr_layers - 1] = (Q_u*(X[nr_layers - 2] - X[nr_layers - 1]) + J[nr_layers - 2]*A)*nr_layers/V
	
def clarification(C_f, C_e, X_f, X_e):
	C_e.s_o = C_f.s_o
	C_e.s_no = C_f.s_no
	C_e.s_nd = C_f.s_nd
	C_e.s_nh = C_f.s_nh
	C_e.s_s = C_f.s_s
	C_e.s_i = C_f.s_i

	C_e.x_h = C_f.x_h*X_e/X_f
	C_e.x_a = C_f.x_a*X_e/X_f
	C_e.x_s = C_f.x_s*X_e/X_f
	C_e.x_nd = C_f.x_nd*X_e/X_f
	C_e.x_p = C_f.x_p*X_e/X_f
	C_e.x_i = C_f.x_i*X_e/X_f

def sedimentation(C_f, C_u, X_f, X_u):
        C_u.s_o = C_f.s_o
        C_u.s_no = C_f.s_no
        C_u.s_nd = C_f.s_nd
        C_u.s_nh = C_f.s_nh
        C_u.s_s = C_f.s_s
        C_u.s_i = C_f.s_i

        C_u.x_h = C_f.x_h*X_u/X_f
        C_u.x_a = C_f.x_a*X_u/X_f
        C_u.x_s = C_f.x_s*X_u/X_f
        C_u.x_nd = C_f.x_nd*X_u/X_f
        C_u.x_p = C_f.x_p*X_u/X_f
        C_u.x_i = C_f.x_i*X_u/X_f
