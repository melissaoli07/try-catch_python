#melissa de oliveira pecoraro rm98698

import time

import random

b_sort5k = []
b_sort10k = []
b_sort100k = []
b_sort150k = []
b_sort200k = []
s_sort5k = []
s_sort10k = []
s_sort100k = []
s_sort150k = []
s_sort200k = []
i_sort5k = []
i_sort10k = []
i_sort100k = []
i_sort150k = []
i_sort200k = []
m_sort5k = []
m_sort10k = []
m_sort100k = []
m_sort150k = []
m_sort200k = []

#complexidade: O(n*2)
#bubble Sort (ordenação por flutuação)
def bubble_sort(lista):
    # obtém o tamanho da lista
    tam = len(lista)
    # variável para rastrear se houve alguma troca durante a iteração
    troca = False
    # loop externo para percorrer toda a lista
    for i in range(tam-1):
        # loop interno para comparar elementos adjacentes e fazer trocas se necessário
        for j in range(0, tam-i-1):
            # compara o elemento atual com o próximo e troca se estiverem na ordem errada
            if lista[j] > lista[j+1]:
                troca = True
                # realiza a troca de elementos
                lista[j], lista[j+1] = lista[j+1], lista[j]
        # verifica se houve trocas durante esta iteração
        if not troca:
            # se não houve trocas, a lista está ordenada e podems interromper
            return



#complexidade: O(n*2)
#selection Sort (ordenação por seleção)
def selection_sort(lista):
    # percorre a lista
    for i in range(len(lista)):
        # assume que o índice do menor elemento é o índice atual
        min_index = i
        
        # encontra o índice do menor elemento a partir do índice atual até o final da lista
        for j in range(i+1, len(lista)):
            #seleciona o menor elemento a cada iteração
            if lista[j] < lista[min_index]:
                min_index = j
        # troca o elemento atual com o menor elemento encontrado    
        lista[i], lista[min_index] = lista[min_index], lista[i]


 
#complexidade: O(n*2)
#insertion Sort (ordenação por inserção)
def insertion_sort(lista):
    # percorre a lista começando do segundo elemento - índice 1    
    for i in range (1, len(lista)):
        # pega o elemento atual para comparar - pivo
        pivo = lista[i]
        # define o índice anterior ao elemento atual
        j = i-1
        # move os elementos maiores que o pivo para uma posição a frente
        # até encontrar a posição correta para o pivo
        while j>=0 and pivo<lista[j]:
            # move o elemento para frente
            lista[j+1] = lista[j]
            # move para o próximo elemento a esquerda
            j-=1
        # insere o pivo na posição correta    
        lista[j+1] = pivo     



#complexidade: O(nlog2n)
#merge Sort (ordenação por mistura)
def merge_sort(lista):
    if len(lista)>1:
        #encontrando o meio da lista
        meio = len(lista) // 2 #parte inteira

        #fatiamento de listas
        L = lista[:meio]
        R = lista[meio:]

        #chamada recursiva 
        merge_sort(L)
        merge_sort(R)

        #variaveis de controle
        # i - faz o controle da lista L
        # J - faz o controle da lista R
        # k - faz o controle da lista (anterior a chamada recursiva)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                lista[k] = L[i]
                i += 1
            else:
                lista[k] = R[j]
                j+=1
            k += 1

        #verficacao dos elementos da lista L
        while i < len(L):
            lista[k] = L[i]
            i += 1
            k += 1

        #verificacao dos elementos da lista R
        while j < len(R):
            lista[k] = R[j]
            j += 1
            k += 1   


# função para obter a escolha do usuário
def obter_escolha():
    while True:
        escolha = input("Escolha um algoritmo de ordenação:\n (1) Bubble Sort\n (2) Selection Sort\n (3) Insertion Sort\n (4) Merge Sort\n")
        if escolha in ['1', '2', '3', '4']:
            return int(escolha)
        else:
            print("Opção inválida. Por favor, escolha 1, 2, 3 ou 4.")



# função para deixar números dentro da lista aleatórios, para depois serem ordenados pelo algoritmo
def lista_aleatoria(tam):
    return [random.randint(0, tam) for _ in range(tam)]



# principal
while True:
    escolha = obter_escolha()
    #escolha = int(input("Escolha um algoritmo de ordenação:\n (1) Bubble Sort\n (2) Selection Sort\n (3) Insertion Sort\n (4) Merge Sort\n"))
    if (escolha == 1):
        tam = int(input("Escolha um tamanho da lista:\n 1 - 5000\n 2 - 10000\n 3 - 100000\n 4 - 150000\n 5 - 200000\n"))
        tam_sizes = [5000, 10000, 100000, 150000, 200000]
        tamanho = lista_aleatoria(tam_sizes[tam - 1])
        #tam = int(input("Escolha um tamanho da lista:\n 10000\n 100000\n 250000\n 500000\n 1000000\n"))
        #tamanho = lista_aleatoria(tam)
        inicio = time.time()
        bubble_sort(tamanho)
        fim = time.time()
        print('Bubble Sort')
        tempo = round(fim-inicio, 3)
        print(f'Tempo:{tempo}')
        print(f'Tamanho da lista: {tam_sizes[tam - 1]}')
        if tam  == 1:
            b_sort5k.append(tempo)
        elif tam  == 2:
            b_sort10k.append(tempo)
        elif tam  == 3:
            b_sort100k.append(tempo)
        elif tam  == 4:
            b_sort150k.append(tempo)
        else: 
            b_sort200k.append(tempo)
    elif (escolha == 2):
        tam = int(input("Escolha um tamanho da lista:\n 1 - 5000\n 2 - 10000\n 3 - 100000\n 4 - 150000\n 5 - 200000\n"))
        tam_sizes = [5000, 10000, 100000, 150000, 200000]
        tamanho = lista_aleatoria(tam_sizes[tam - 1])
        inicio = time.time()
        selection_sort(tamanho)
        fim = time.time()
        print('Selection Sort')
        tempo = round(fim-inicio,3)
        print(f'Tempo:{tempo}')
        print(f'Tamanho da lista: {tam_sizes[tam - 1]}')
        if  tam == 1:
            s_sort5k.append(tempo)
        elif tam == 2:
            s_sort10k.append(tempo)
        elif tam == 3:
            s_sort100k.append(tempo)
        elif tam == 4:
            s_sort150k.append(tempo)
        else: 
            s_sort200k.append(tempo)
    elif (escolha == 3):
        tam = int(input("Escolha um tamanho da lista:\n 1 - 5000\n 2 - 10000\n 3 - 100000\n 4 - 150000\n 5 - 200000\n"))
        tam_sizes = [5000, 10000, 100000, 150000, 200000]
        tamanho = lista_aleatoria(tam_sizes[tam - 1])
        inicio = time.time()
        insertion_sort(tamanho)
        fim = time.time()
        print('Insertion Sort')
        tempo = round(fim-inicio, 3)
        print(f'Tempo:{tempo}')
        print(f'Tamanho da lista: {tam_sizes[tam - 1]}')
        if tam == 1:
            i_sort5k.append(tempo)
        elif tam == 2:
            i_sort10k.append(tempo)
        elif tam == 3:
            i_sort100k.append(tempo)
        elif tam == 4:
            i_sort150k.append(tempo)
        else: 
            i_sort200k.append(tempo)
    else:
        tam = int(input("Escolha um tamanho da lista:\n 1 - 5000\n 2 - 10000\n 3 - 100000\n 4 - 150000\n 5 - 200000\n"))
        tam_sizes = [5000, 10000, 100000, 150000, 200000]
        tamanho = lista_aleatoria(tam_sizes[tam - 1])
        inicio = time.time()
        merge_sort(tamanho)
        fim = time.time()
        print('Merge Sort')
        tempo = round(fim-inicio, 3)
        print(f'Tempo:{tempo}')
        print(f'Tamanho da lista: {tam_sizes[tam - 1]}')
        if tam == 1:
            m_sort5k.append(tempo)
        elif tam == 2:
            m_sort10k.append(tempo)
        elif tam == 3:
            m_sort100k.append(tempo)
        elif tam == 4:
            m_sort150k.append(tempo)
        else: 
            m_sort200k.append(tempo)

    continuar = input("Deseja continuar? (s/n): ").lower()
    if continuar != 's':
            break

print(f'Lista de Tempos Bubble Sort 5k: {b_sort5k}')
mediab5 = (sum(b_sort5k) / len(b_sort5k))
print(f'Média dos Tempos Bubble Sort 5k: {mediab5}')
print(f'Lista de Tempos Bubble Sort 10k: {b_sort10k}')
mediab10 = (sum(b_sort10k) / len(b_sort10k))  
print(f'Média dos Tempos Bubble Sort 10k: {mediab10}')
print(f'Lista de Tempos Bubble Sort 100k: {b_sort100k}')
mediab100 = (sum(b_sort100k) / len(b_sort100k))  
print(f'Média dos Tempos Bubble Sort 100k: {mediab100}')
print(f'Lista de Tempos Bubble Sort 150k:  {b_sort150k}')
mediab150 = (sum(b_sort150k) / len(b_sort150k))  
print(f'Média dos Tempos Bubble Sort 150k: {mediab150}')
print(f'Lista de Tempos Bubble Sort 200k: {b_sort200k}')
mediab200 = (sum(b_sort200k) / len(b_sort200k))  
print(f'Média dos Tempos Bubble Sort 200k: {mediab200}')
print(f'Lista de Tempos Selection Sort 5k: {s_sort5k}')
medias5 = (sum(s_sort5k) / len(s_sort5k))  
print(f'Média dos Tempos Selection Sort 5k: {medias5}')
print(f'Lista de Tempos Selection Sort 10k: {s_sort10k}')
medias10 = (sum(s_sort10k) / len(s_sort10k))  
print(f'Média dos Tempos Selection Sort 10k: {medias10}')
print(f'Lista de Tempos Selection Sort 100k: {s_sort100k}')
medias100 = (sum(s_sort100k) / len(s_sort100k))  
print(f'Média dos Tempos Selection Sort 100k: {medias100}')
print(f'Lista de Tempos Selection Sort 150k: {s_sort150k}')
medias150 = (sum(s_sort150k) / len(s_sort150k))  
print(f'Média dos Tempos Selection Sort 150k: {medias150}')
print(f'Lista de Tempos Selection Sort 200k: {s_sort200k}')
medias200 = (sum(s_sort200k) / len(s_sort200k))  
print(f'Média dos Tempos Selection Sort 200k: {medias200}')
print(f'Lista de Tempos Insertion Sort 5k: {i_sort5k}')
mediai5 = (sum(i_sort5k) / len(i_sort5k))  
print(f'Média dos Tempos Insertion Sort 5k: {mediai5}')
print(f'Lista de Tempos Insertion Sort 10k: {i_sort10k}')
mediai10 = (sum(i_sort10k) / len(i_sort10k))  
print(f'Média dos Tempos Insertion Sort 10k: {mediai10}')
print(f'Lista de Tempos Insertion Sort 100k: {i_sort100k}')
mediai100 = (sum(i_sort100k) / len(i_sort100k))  
print(f'Média dos Tempos Insertion Sort 100k: {mediai100}')
print(f'Lista de Tempos Insertion Sort 150k:: {i_sort150k}')
mediai150 = (sum(i_sort150k) / len(i_sort150k))  
print(f'Média dos Tempos Insertion Sort 150k: {mediai150}')
print(f'Lista de Tempos Insertion Sort 200k: {i_sort200k}')
mediai200 = (sum(i_sort200k) / len(i_sort200k))  
print(f'Média dos Tempos Insertion Sort 200k: {mediai200}')
print(f'Lista de Tempos Merge Sort 5k: {m_sort5k}')
mediam5 = (sum(m_sort5k) / len(m_sort5k))  
print(f'Média dos Tempos Merge Sort 5k: {mediam5}')
print(f'Lista de Tempos Merge Sort 10k: {m_sort10k}')
mediam10 = (sum(m_sort10k) / len(m_sort10k))  
print(f'Média dos Tempos Merge Sort 10k: {mediam10}')
print(f'Lista de Tempos Merge Sort 100k: {m_sort100k}')
mediam100 = (sum(m_sort100k) / len(m_sort100k))  
print(f'Média dos Tempos Merge Sort 100k: {mediam100}')
print(f'Lista de Tempos Merge Sort 150k: {m_sort150k}')
mediam150 = (sum(m_sort150k) / len(m_sort150k))  
print(f'Média dos Tempos Merge Sort 150k: {mediam150}')
print(f'Lista de Tempos Merge Sort 200k: {m_sort200k}')
mediam200 = (sum(m_sort200k) / len(m_sort200k))  
print(f'Média dos Tempos Merge Sort 200k: {mediam200}')

