from math import sin, cos, tan, radians 

angulo_graus = float(input('Informe o ângulo deste triângulo => '))
angulo_radios = radians(angulo_graus)

seno = sin(angulo_radios)
cosseno = cos(angulo_radios)
tangente = tan(angulo_radios)

print(f'O Seno será {seno:.2f}\n O cosseno será {cosseno:.2f}\n O tangente será {tangente:.2f}')