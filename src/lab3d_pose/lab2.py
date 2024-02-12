import numpy as np

def quaternion_multiply(q0, q1):
    """
    Multiplies two quaternions.

    Input
    :param q0: A 4 element array containing the first quaternion (q01, q11, q21, q31)
    :param q1: A 4 element array containing the second quaternion (q02, q12, q22, q32)

    Output
    :return: A 4 element array containing the final quaternion (q03,q13,q23,q33)

    """
    # Extract the values from q0
    w0 = q0[0]
    x0 = q0[1]
    y0 = q0[2]
    z0 = q0[3]

    # Extract the values from q1
    w1 = q1[0]
    x1 = q1[1]
    y1 = q1[2]
    z1 = q1[3]

    # Computer the product of the two quaternions, term by term
    q0q1_w = w0 * w1 - x0 * x1 - y0 * y1 - z0 * z1
    q0q1_x = w0 * x1 + x0 * w1 + y0 * z1 - z0 * y1
    q0q1_y = w0 * y1 - x0 * z1 + y0 * w1 + z0 * x1
    q0q1_z = w0 * z1 + x0 * y1 - y0 * x1 + z0 * w1

    # Create a 4 element array containing the final quaternion
    final_quaternion = np.array([q0q1_w, q0q1_x, q0q1_y, q0q1_z])

    # Return a 4 element array containing the final quaternion (q02,q12,q22,q32)
    return final_quaternion

def quaternion_inverse(q):
    q_inv = np.zeros(4)
    q_len = q[0]**2 + q[1]**2 + q[2]**2 + q[3]**2

    #say q = s + v1.i + v2.j + v3.k
    #get the inverse of q1 which is equal to conjugate devided by length
    #so q_inv = (s - v1.i - v2.j - v3.k) / length
    q_inv[0] =  q[0] / q_len #s/length
    q_inv[1] = -q[1] / q_len #-v1/length
    q_inv[2] = -q[2] / q_len #-v2/length
    q_inv[3] = -q[3] / q_len #-v3/length
    return q_inv

#q_1 and q_2
q1 = [np.array([1,2,3,4]), np.array([3,4,-5,6]), np.array([4,-5,6,-7]), np.array([7,8,-9,10]), np.array([8,-9,10,-11]), np.array([10,-11,12,-13])]
q2 = [np.array([5,6,7,8]), np.array([7,-8,9,-10]), np.array([8,9,-10,11]), np.array([11,-12,13,-14]), np.array([12,13,-14,15]), np.array([14,15,-16,17])]

for i in range(0,6):

    print("Exercise %d:" % (i+1))
    print("q_1 = " + np.array2string(q1[i][0]) + " + " + np.array2string(q1[i][1]) + "i + " + np.array2string(q1[i][2]) + "j + " + np.array2string(q1[i][3]) + "k")
    print("q_2 = " + np.array2string(q2[i][0]) + " + " + np.array2string(q2[i][1]) + "i + " + np.array2string(q2[i][2]) + "j + " + np.array2string(q2[i][3]) + "k")

    #inverse of q_1
    q1_inv = quaternion_inverse(q1[i])

    #calculate q_r 
    #q_r = q_2 x q_1_inv
    qr = quaternion_multiply(q2[i], q1_inv)
    print("q_r = " + np.array2string(qr[0]) + " + " + np.array2string(qr[1]) + "i + " + np.array2string(qr[2]) + "j + " + np.array2string(qr[3]) + "k")
    print("")

