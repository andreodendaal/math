import numpy as np


def add_vectors(list_1, list_2):
    vector_1 = np.array(list_1)
    vector_2 = np.array(list_2)
    vector_sum = vector_1 + vector_2
    return vector_sum

def sub_vectors(list_1, list_2):
    vector_1 = np.array(list_1)
    vector_2 = np.array(list_2)
    vector_sum = vector_1 - vector_2
    return vector_sum

def multiply_vectors(list_1, mult):
    vector_1 = np.array(list_1)
    vector_prod = vector_1 * mult
    return vector_prod


q1a = [8.218, -9.341]
q1b = [-1.129, 2.111]

answer_1 = add_vectors(q1a, q1b)
print(answer_1)

q2a = [7.119, 8.215]
q2b = [-8.223, 0.878]

answer_2 = sub_vectors(q2a, q2b)
print(answer_2)

q3a = [1.671, -1.012, -0.318]
answer_3 = multiply_vectors(q3a, 7.41)
print(answer_3)