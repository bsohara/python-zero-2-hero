from array import array

'''
- Arrays (Matriz) => utilizar quando a lista estiver maior
    - melhora a performance da lista
    - não se deve criar um array e informar o tipo não compatível

'''
letras = ['a', 'b', 'c', 'd']
int_nums = [1, 2, 3, 4]
float_nums = [1.1, 2.2, 3.3, 4.4]

print(letras)
print(int_nums)
print(float_nums)

letras2 = array('u', ['a', 'b', 'c', 'd']) # 'u' => unicode
int_nums2 = array('i', [1, 2, 3, 4])
float_nums2 = array('f', [1.1, 2.2, 3.3, 4.4])

print()
print(letras2)
print(int_nums2)
print(float_nums2)

