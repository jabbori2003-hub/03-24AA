#Eng Kotta Elementni Topish
def eng_kotta_element(A):
    if not A:
        return None
    max_element = A[0]
    for element in A:
        if element > max_element:
            max_element = element
    return max_element
#Eng Kotta Elementni Topish
def eng_kichik_element(A):
    if not A:
        return None
    min_element = A[0]
    for element in A:
        if element < min_element:
            min_element = element
    return min_element
#Foydalanish
massiv = [3,7,2,9,1,11,12,23]
print("Eng Kattasi",eng_kotta_element  (massiv))
print("Egn Kichigi",eng_kichik_element (massiv))