import numpy as np
import vector


def add_vectors(list_1, list_2):
    vector_1 = np.array(list_1)
    vector_2 = np.array(list_2)
    vector_sum = vector_1 + vector_2
    return str(vector_sum)

def sub_vectors(list_1, list_2):
    vector_1 = np.array(list_1)
    vector_2 = np.array(list_2)
    vector_sum = vector_1 - vector_2
    return str(vector_sum)

def multiply_vectors(list_1, mult):
    vector_1 = np.array(list_1)
    vector_prod = vector_1 * mult
    return str(vector_prod)


q1a = [8.218, -9.341]
q1b = [-1.129, 2.111]
vector_1 = vector.Vector(q1a, q1b)
answer_1_cls = vector_1.add_vectors()
print('Dimension: ' + str(vector_1.dimension))
print('Q1 Class:' + answer_1_cls)
answer_1_fn = add_vectors(q1a, q1b)
print('Q1 Function:' + answer_1_fn)


q2a = [7.119, 8.215]
q2b = [-8.223, 0.878]
vector_2 = vector.Vector(q2a, q2b)
answer_2_fn = sub_vectors(q2a, q2b)
print('Q2 Function answer: ' + str(answer_2_fn))

answer_2_cls = vector_2.subtract_vectors()
print('Q2 Class answer: ' + answer_2_cls)

q3a = [1.671, -1.012, -0.318]
answer_3_fn = multiply_vectors(q3a, 7.41)

vector_3 = vector.Vector(q3a, [])
answer_3_cls = vector_3.multiply_vectors(7.41)
print("Q3 Function: " + answer_3_fn)
print("Q3 class: " + answer_3_cls)

print(answer_1_fn == answer_1_cls)
print(answer_2_fn == answer_2_cls)
print(answer_3_fn == answer_3_cls)