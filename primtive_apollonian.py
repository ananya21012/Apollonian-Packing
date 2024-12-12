#integer apollonian packing

import matplotlib.pyplot as plt
import numpy as np
import math


def issquare(num):
    sqrt_num = math.sqrt(num)
    return sqrt_num.is_integer()

def find_gcd(x, y):
    if(y>x):
        x,y=y,x
    while(y):
        x, y = y, x % y
    return x
  


integral_list = set()
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            sq = a*b + b*c + c*a
            if issquare(sq):
                d = a + b + c + 2 * math.sqrt(sq)
                temp=tuple(sorted([a, b, c, d]))  # Convert to tuple
                integral_list.add(temp)



#till now we got integral appolonian packings
primitive_list=[]

for k in integral_list:
    gcd=find_gcd(k[0],k[1])
    gcd = find_gcd(gcd, k[2])
    gcd=find_gcd(gcd,k[3])
    if(gcd==1):
        primitive_list.append(k)
        


# Function to calculate the new curvature using Descartes' Circle Theorem
def new_curvature_inner(k1, k2, k3):
    return (int)(k1 + k2 + k3 + 2 * np.sqrt(float(k1 * k2 + k2 * k3 + k3 * k1)))

def new_curvature_outer(k1, k2, k3):
    return (int)(k1 + k2 + k3 - 2 * np.sqrt(float(k1 * k2 + k2 * k3 + k3 * k1)))
   
def add_quadruple(quad, indices, curvature_function, quadruples):
    d1 = curvature_function(*[quad[i] for i in indices])
    temp =[quad[i] for i in indices] + [d1]
    if tuple(sorted(temp)) not in quadruples:
        quadruples.add(tuple(temp))


print("the following are primitive packings:")
print()
# lis=[tuple([25, 40, 40, 225.0])]
for l in primitive_list:

    quadruples=set()
    quadruples.add(l)
    quadruples.add(tuple([l[0],l[1],l[2],new_curvature_outer(l[0],l[1],l[2])]))

    processed = set()  # To track already processed quadruples

    while len(quadruples) < 10:
        for quad in list(quadruples):  # Iterate over a snapshot
            if quad in processed:
                continue  # Skip already processed quadruples

            # Mark this quadruple as processed
            processed.add(quad)

            # Inner curvatures
            add_quadruple(quad, [0, 1, 3], new_curvature_inner, quadruples)
            add_quadruple(quad, [0, 2, 3], new_curvature_inner, quadruples)
            add_quadruple(quad, [1, 2, 3], new_curvature_inner, quadruples)


            # Outer curvatures
            add_quadruple(quad, [0, 1, 3], new_curvature_outer, quadruples)
            add_quadruple(quad, [0, 2, 3], new_curvature_outer, quadruples)
            add_quadruple(quad, [1, 2, 3], new_curvature_outer, quadruples)

            # Break if we reach the limit
            if len(quadruples) >= 10:
                break

    print(quadruples)
    print()


