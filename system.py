line = "================="

while True:
    service = int(input('Qual tipo dos nossos serviços deseja usar (Digite o numero referente o serviço): \n1- Tabuada\n2- Conversor de Temperatura\n3- Área de Figuras Geometricas\n4- Juros Simples\n5- Juros Compostos\n6- Calculadora Basica\n0- Sair do Programa\n'))

    #tabuada
    if service == 1:

        print (line, 'TABUADA', line)
        num_tabuada = int(input('Deseja ver a tabuada de qual número?\n'))
        print('\n')
        print (line, 'SEGUE O RESULTADO ABAIXO', line)
        i = 0

        

        
        while i < 10:
            i += 1
            result = num_tabuada * i
            print (f'{num_tabuada} X {i} = {result}')
      

            
    #conversor de temperatura
    if service == 2:
          print (line, 'CONVERSOR DE TEMPERATURA', line)


    #areas de figuras geoetricas
    if service == 3:
          print (line, 'ÁREAS DE FIGURAS GEOMÉTRICAS', line)

    #juros simples
    if service == 4:
          print (line, 'JUROS SIMPLES', line)

    #juros compostos
    if service == 5:
          print (line, 'JUROS COMPOSTOS', line)

    #calculadora basica
    if service == 2:
          print (line, 'CALCULADORA BÁSICA', line)

    if service == 0:
        print('Saindo do programa. Até logo!')
        break

    else:
        print('Função ainda não implementada ou opção inválida. Tente novamente.')