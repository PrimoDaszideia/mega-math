line = "================="

while True:
    print (line, 'SEJA BEM-VINDO AO MEGA-MATH', line)
    service = int(input('Qual tipo dos nossos serviços deseja usar (Digite o numero referente o serviço): \n1- Tabuada\n2- Conversor de Temperatura\n3- Área de Figuras Geometricas\n4- Juros Simples\n5- Juros Compostos\n6- Calculadora Basica\n0- Sair do Programa\n\nDigite a opção desejada: '))
    print ('\n')

    #tabuada
    if service == 1:
        while True:

            print (line, 'TABUADA', line)
            num_tabuada = int(input('Deseja ver a tabuada de qual número?\n'))
            print('\n')
            print (line, 'SEGUE O RESULTADO ABAIXO', line)
            i = 0

            while i < 10:
                i += 1
                result = num_tabuada * i
                print (f'{num_tabuada} X {i} = {result}')
            print('\n')
            escolha1 = int(input('1- Reiniciar Tabuada\n2- Voltar ao Menu Inicial \n'))
            
            print('\n')

            if escolha1 == 2:
                 break
                 
            

            
    #conversor de temperatura
    if service == 2:
      while True:
            print (line, 'CONVERSOR DE TEMPERATURA', line)
            temp_tipe = float(input('Digite qual tipo de temperatura deseja fazer a conversão (Digite um número referente a opção desejada):\n1- Kelvin => Celsius\n2- Kelvin => Fahrenheit\n3- Celsius => Kelvin\n4- Celsius => Fahrenheit\n5- Fahrenheit => Celsius\n6- Fahrenheit => Kelvin \n\nDigite a opção desejada: '))
            print('\n')

            #kelvin para celsius
            if temp_tipe == 1:
                 k = float(input('Digite a temperatura em Kelvin que deseja fazer a conversão para Celsius: '))
                 c = k - 273
                 print(f'{k}K na escala de graus Celsius é igual {c}°C')

            #kelvin para fahrenheit
            if temp_tipe == 2:
                 k = float(input('Digite a temperatura em Kelvin que deseja fazer a conversão para Fahrenheit: '))
                 f = ((k - 273) * 1.8 + 32)
                 print(f'{k}K na escala de graus Fahrenheit é igual {f}°F')

          #celsius para kelvin
            if temp_tipe == 3:    
                 c = float(input('Digite a temperatura em Celsius que deseja fazer a conversão para Kelvin: '))
                 k = c + 273
                 print(f'{c}°C na escala de graus Kelvin é igual {k}K')
     
            #celsius para fahrenheit
            if temp_tipe == 4:    
                 c = float(input('Digite a temperatura em Celsius que deseja fazer a conversão para Fahrenheit: '))
                 f = ((c * 1.8) + 32)
                 print(f'{c}°C na escala de graus Fahrenheit é igual {f}°F')
      
            #Fahrenheit para celsius
            if temp_tipe == 5:   
                 f = float(input('Digite a temperatura em Fahrenheit que deseja fazer a conversão para Celsius: '))
                 c = ((f - 32) / 1.8)
                 print(f'{f}°F na escala de graus Fahrenheit é igual {c}°C')
       
            #Fahrenheit para kelvin
            if temp_tipe == 6:
                 f = float(input('Digite a temperatura em Fahrenheit que deseja fazer a conversão para Kelvin: '))
                 k = ((f - 32) * 5/9 + 273)
                 print(f'{f}°F na escala de graus Fahrenheit é igual {k}K')
            
            escolha = int(input('1- Reiniciar Conversor De Temperatura\n2- Voltar ao Menu Inicial \n'))

            if escolha == 2:
                  break 
 

    #areas de figuras geometricas
    if service == 3:
      while True:      
            print (line, 'ÁREAS DE FIGURAS GEOMÉTRICAS', line)
            figure = int(input('De qual figura geométrica pretende descobrir a área (Digite um número referente a opção desejada):\n1- Quadrado\n2- Triangulo\n3- Trapezio\n4- Retangulo\n5- Circulo\n\nDigite a opção desejada: '))
            print ('\n')

            #quadrado
            if figure == 1:
            
                  Q1 = float(input('Digite o valor de um dos lados do quadrado: '))
                  calc_square = Q1 ** 2
                  print ('O valor da área desse quadrado é: ',calc_square)

            #triangulo
            elif figure == 2:
                 
                  base_tri = float(input('Digite o valor da base do triangulo: '))
                  alt_tri = float(input('Digite o valor da altura do triangulo: '))
                  calc_tri = base_tri * alt_tri / 2
                  print ('O valor da área desse triângulo é: ',calc_tri)

            #trapezio
            elif figure == 3:
                  
                  base1 = float(input('Digite o valor da base maior do trapezio: '))
                  base2 = float(input('Digite o valor da base menor do trapezio: '))
                  alt_trap = float(input('Digite o valor da altura do trapezio: '))
                  calc_trap = ((base1 + base2) * alt_trap) / 2
                  print ('O valor da área desse trapezio é: ',calc_trap)

            #retangulo
            elif figure == 4:
                 base_ret = float(input('Digite o valor da base do retangulo: '))
                 alt_ret = float(input('Digite o valor da altura do retangulo: '))
                 calc_ret = base_ret * alt_ret
                 print ('O valor da área desse triângulo é: ',calc_ret)

           

            #circulo
            elif figure == 5:
                 raio = float(input('Digite o valor do raio do circulo: '))
                 pi = 3.14
                 calc_circle = (pi * (raio**2))
                 print ('O valor da área desse cirulo é: ',calc_circle)
            escolha = int(input('1- Reiniciar Áreas De Figuras Geometricas\n2- Voltar ao Menu Inicial \n'))

            if escolha == 2:
                  break

    #juros simples
    if service == 4:
      while True:
            print (line, 'JUROS SIMPLES', line)
            c = float(input('Digite o valor de capital (Utilize ponto "." para números com vírgula): '))
            i = float(input('Digite o valor da taxa de juros (Utilize ponto "." para números com vírgula): '))
            t = float(input('Digite o tempo em anos (Utilize ponto "." para números com vírgula): '))
            j = (c * i * t) / 100
            m = c + j

            m = round(m,2)
            j = round(m,2)
      
            print(f'O valor do juros é R${j}. Totalizando um valor montante de R${m}')
            escolha = int(input('1- Reiniciar Calculadora De Juros Simples\n2- Voltar ao Menu Inicial \n'))

            if escolha == 2:
                  break


    #juros compostos
    if service == 5:
      while True:
          print (line, 'JUROS COMPOSTOS', line)
          c = float(input('Digite a capital inicial (Utilize ponto "." para números com vírgula): '))
          i = float(input('Digite o valor da taxa de juros (Utilize ponto "." para números com vírgula): '))
          t = float(input('Digite o tempo de aplicação em anos (Utilize ponto "." para números com vírgula): '))
          m = (c * (1 + i/100) ** t)
          j = m - c

          m = round(m,2)
          j = round(m,2)

          print(f'Total de juros fica R${j}. Totalizando um valor montante de R${m}')
          escolha = int(input('1- Reiniciar Calculadora De Juros Simples\n2- Voltar ao Menu Inicial \n'))

          if escolha == 2:
            break
          


    #calculadora basica
    if service == 6:
      while True:
            print (line, 'CALCULADORA BÁSICA', line)
            num1 = float(input('Digite o primeiro número para realizar a operação: '))
            operation = int(input('Qual tipo de operação deseja realizar (Digite um número referente a opção desejada):\n1- Adição\n2- Subtração\n3- Divisão\n4- Multiplicação\n5- Potenciação\n\nDigite a opção desejada:  '))
            num2 = float(input('Digite o segundo número para realizar o cálculo da operação: '))

            #adiçao
            if operation == 1:
                 print('O valor da operação é: ',num1 + num2)
            #subtraçao
            if operation == 2:
                  print('O valor da operação é: ',num1 - num2)
            #divisao
            if operation == 3:
                 print('O valor da operação é: ',num1 / num2)
            #multiplicacao
            if operation == 4:
                 print('O valor da operação é: ',num1 * num2)
            #potenciacao
            if operation == 5:
                 print('O valor da operação é: ',num1 ** num2)
            
            escolha = int(input('1- Reiniciar Calculadora Básica\n2- Voltar ao Menu Inicial \n'))

            if escolha == 2:
                  break
      
    if service == 0:
        print('Saindo do programa. Até logo!')
        break
    
    if service >= 7:
        print('Opção Inválida! Tente novamente.')
        print ('\n')

