#integer appolonian packing

import matplotlib.pyplot as plt
import numpy as np
import math
from math import isqrt

def issquare(num):
    sqrt_num = math.sqrt(num)
    return sqrt_num.is_integer()

def find_gcd(x, y):
    if(y>x):
        x,y=y,x
    while(y):
        x, y = y, x % y
    return x
        


def coherence_general_gcd(a, b):
    # Step 1: Calculate gcd of a and b
    g = find_gcd(a, b)
    
    # Step 2: Find the largest l such that l^2 divides g
    max_l = 0
    for l in range(1, int(g**0.5) + 1):  
        if g % (l * l) == 0: 
            max_l = l
    
    return max_l


k=[2255434430544645120, 5994079928069873664, 425496337031168, 895277554791945216]
kgcd=coherence_general_gcd(abs(k[0]),abs(k[1]))
print("kth coherence gcd is",kgcd)
kgcd = coherence_general_gcd(kgcd, abs(k[2]))
print("kth coherence gcd is",kgcd)
kgcd=coherence_general_gcd(kgcd,abs(k[3]))
if(kgcd!=1 and kgcd!=0):

    print("quadruple",k)
    print("kth coherence gcd is",kgcd)



# l = set()
# for a in range(2, 50):
#     for b in range(2, 50):
#         for c in range(2, 50):
#             sq = a*b + b*c + c*a
#             if issquare(sq):
#                 d = a + b + c + 2 * math.sqrt(sq)
#                 temp=tuple(sorted([a, b, c, d]))  # Convert to tuple
#                 l.add(temp)


# #till now we got integral appolonian packings
# non_primitive_list=[]

# for k in l:
#     gcd=find_gcd(k[0],k[1])
#     gcd = find_gcd(gcd, k[2])
#     gcd=find_gcd(gcd,k[3])
#     if(gcd!=1):
#         non_primitive_list.append(k)
        


# coherence_list=[]

# for k in non_primitive_list:
#     kgcd=coherence_general_gcd(k[0],k[1])
#     kgcd = coherence_general_gcd(kgcd, k[2])
#     kgcd=coherence_general_gcd(kgcd,k[3])
#     if(kgcd==1):
#         coherence_list.append(k)



# # Function to calculate the new curvature using Descartes' Circle Theorem
# def new_curvature_inner(k1, k2, k3):
#     return (int)(k1 + k2 + k3 + 2 * np.sqrt(float(k1 * k2 + k2 * k3 + k3 * k1)))

# def new_curvature_outer(k1, k2, k3):
#     return (int)(k1 + k2 + k3 - 2 * np.sqrt(float(k1 * k2 + k2 * k3 + k3 * k1)))
   
# def add_quadruple(quad, indices, curvature_function, quadruples):
#     d1 = curvature_function(*[quad[i] for i in indices])
#     temp =[quad[i] for i in indices] + [d1]
#     if tuple(sorted(temp)) not in quadruples:
#         quadruples.add(tuple(temp))


# # lis=[tuple([25, 40, 40, 225.0])]
# for l in coherence_list:

#     quadruples=set()
#     quadruples.add(l)
#     quadruples.add(tuple([l[0],l[1],l[2],new_curvature_outer(l[0],l[1],l[2])]))

#     processed = set()  # To track already processed quadruples

#     while len(quadruples) < 1000:
#         for quad in list(quadruples):  # Iterate over a snapshot
#             if quad in processed:
#                 continue  # Skip already processed quadruples

#             # Mark this quadruple as processed
#             processed.add(quad)

#             # Inner curvatures
#             add_quadruple(quad, [0, 1, 3], new_curvature_inner, quadruples)
#             add_quadruple(quad, [0, 2, 3], new_curvature_inner, quadruples)
#             add_quadruple(quad, [1, 2, 3], new_curvature_inner, quadruples)


#             # # Outer curvatures
#             add_quadruple(quad, [0, 1, 3], new_curvature_outer, quadruples)
#             add_quadruple(quad, [0, 2, 3], new_curvature_outer, quadruples)
#             add_quadruple(quad, [1, 2, 3], new_curvature_outer, quadruples)

#             # Break if we reach the limit
#             if len(quadruples) >= 10:
#                 break


#     for k in quadruples:
#         kgcd=coherence_general_gcd(abs(k[0]),abs(k[1]))
#         kgcd = coherence_general_gcd(kgcd, abs(k[2]))
#         kgcd=coherence_general_gcd(kgcd,abs(k[3]))
#         if(kgcd!=1 and kgcd!=0):
#             print("false for root quadruple", l)
#             print("quadruple for which it came false",k)
#             print("coherence gcd for that quadruple",kgcd)
#             print()
#             break


