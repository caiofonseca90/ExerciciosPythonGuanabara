'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e
 mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER
'''
from datetime import date

nasc = int(input('Em que ano você nasceu?: '))

ano = date.today().year
mes = date.today().month

idade = ano - nasc

if idade <= 9:
    print('Você é um(a) atleta de {} anos, e se enquadra na categoria MIRIM !'.format(idade))
elif idade > 9 and idade <=14:
    print('Você é um(a) atleta de {} anos, e se enquadra na categoria INFANTIL !'.format(idade))
elif idade > 14 and idade <=19:    
    print('Você é um(a) atleta de {} anos, e se enquadra na categoria JÚNIOR !'.format(idade))
elif idade > 19 and idade <=25:    
    print('Você é um(a) atleta de {} anos, e se enquadra na categoria SÊNIOR !'.format(idade))
else:    
    print('Você é um(a) atleta de {} anos, e se enquadra na categoria MASTER !'.format(idade))