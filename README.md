### Bubble Sort

---

- O Bubble Sort é um algoritmo de ordenação simples que organiza os elementos de uma lista comparando valores que estão lado a lado. Quando estão na ordem errada, eles são trocados. Esse processo continua até que toda a lista esteja organizada. A cada passagem, o maior elemento que ainda não está na posição correta vai sendo levado para o final da lista.
- **Complexidade:**
  - Melhor caso: O(n) — acontece quando os elementos já estão ordenados;
  - Caso médio: O(n²) — ocorre quando os elementos estão misturados, exigindo várias comparações e trocas;
  - Pior caso: O(n²) — acontece quando a lista está completamente invertida.
- **Vantagens:**
  - Fácil de compreender e programar;
  - Mantém a ordem dos elementos iguais, sendo um algoritmo estável;
  - Não precisa de espaço adicional significativo para funcionar.
- **Limitações:**
  - Apresenta baixo desempenho em listas maiores;
  - Pode realizar muitas comparações e trocas desnecessárias.
- **Situações de uso:**
  - Adequado: Para aprendizado, exemplos didáticos ou listas muito pequenas que já estejam quase ordenadas.
  - Não recomendado: Para aplicações reais que trabalham com grandes quantidades de dados.

### Quick Sort

- O Quick Sort é um algoritmo de ordenação baseado na ideia de “dividir e conquistar”. Primeiro, ele escolhe um elemento da lista como pivô e reorganiza os demais elementos, deixando os menores de um lado e os maiores do outro. Depois, o mesmo processo é realizado nas partes menores até que toda a lista esteja ordenada.
- **Complexidade:**
  - Melhor caso: O(n log n) — acontece quando o pivô consegue dividir os elementos em partes próximas de tamanho igual;
  - Caso médio: O(n log n) — normalmente ocorre quando as divisões são razoavelmente equilibradas;
  - Pior caso: O(n²) — acontece quando o pivô escolhido gera divisões muito desequilibradas, como quando ele é sempre o menor ou o maior elemento.
- **Vantagens:**
  - Possui um bom desempenho na maioria das situações;
  - Utiliza pouca memória adicional;
  - Costuma apresentar um bom desempenho por aproveitar bem a memória cache do processador.
- **Limitações:**
  - Não mantém necessariamente a ordem dos elementos iguais;
  - Pode apresentar desempenho O(n²) quando o pivô é escolhido de forma inadequada;
  - Sua implementação pode ser mais difícil por utilizar recursividade.
- **Situações de uso:**
  - Adequado: Para trabalhar com grandes quantidades de dados, principalmente quando é necessário obter um bom desempenho médio.
  - Não recomendado: Quando é obrigatório manter a estabilidade da ordenação, em situações de tempo real que não toleram o pior caso ou quando os dados estão armazenados em listas encadeadas.
### Tabela Comparativa

| Característica | Bubble Sort | Quick Sort |
| :--- | :--- | :--- 
| **Princípio de funcionamento** | Compara elementos vizinhos e troca quando estão fora de ordem | Escolhe um pivô e divide o array em partes menores 
| **Melhor caso** | O(n) | O(n log n) 
| **Caso médio** | O(n²) | O(n log n) 
| **Pior caso** | O(n²)| O(n²) 
| **Uso de memória** | O(1)  | O(log n) 
| **Vantagem principal** | Simples de entender e implementar | Muito mais eficiente para grandes quantidades de dados 
| **Limitação principal** | Fica muito lento com muitos elementos |Pode chegar a O(n²) dependendo da escolha do pivô
| **Aplicação recomendada** | Arrays pequenos e estudos didáticos | Arrays grandes e situações em que é necessário desempenho

---

### Experimento de Ordenação

---

a) Qual algoritmo realizou menos operações para 10 elementos?
* O Quick Sort realizou menos operações. Foram 25 comparações e 10 movimentações

b) O comportamento permaneceu igual para 20 elementos?
* O Quick Sort normalmente continua realizando menos operações, enquanto o número de operações do Bubble Sort aumenta mais rapidamente

c) O que aconteceu quando o tamanho aumentou para 1.000 elementos?
* Com 1.000 elementos, a diferença ficou muito maior. O Bubble Sort precisou realizar uma quantidade muito maior de comparações e trocas, enquanto o Quick Sort apresentou um crescimento menor na quantidade de operações

d) Qual algoritmo apresentou maior crescimento da quantidade de operações?
* O Bubble Sort apresentou o maior crescimento na quantidade de operações. Isso acontece porque sua complexidade média é O(n²)

e) Os resultados experimentais são coerentes com as complexidades teóricas estudadas?
* Sim. O Bubble Sort possui complexidade média O(n²), enquanto o Quick Sort possui complexidade média O(n log n). Por isso, conforme o tamanho do array aumenta, o Bubble Sort tende a realizar muito mais operações

f) Em qual situação você escolheria Bubble Sort?
Em listas pequenas e situações em que a simplicidade do algoritmo é mais importante. Ele também é útil para estudar e entender conceitos básicos de ordenação

g) Em qual situação você escolheria Quick Sort?
* Para listas maiores, pois ele geralmente apresenta um número menor de operações e melhor desempenho médio em comparação com o Bubble Sort
  
---

## Investigação de busca em matrizes

---

a) Por que encontrar um elemento no início exige menos operações?

* Porque a busca sequencial começa pela primeira posição da matriz. Se o valor estiver no início, ele será encontrado logo na primeira comparação.

b) O que acontece quando o elemento procurado não existe?

* O algoritmo percorre todos os elementos da matriz, fazendo uma comparação com cada um. Ao chegar ao final, informa que o valor não foi encontrado.

c) Qual é o pior caso da busca sequencial?

* O pior caso acontece quando o elemento está na última posição ou quando o elemento não existe. Nesse caso, são necessárias m × n comparações

d) Como o aumento das dimensões da matriz influencia a quantidade de operações?

* Quanto maior a matriz, mais elementos precisam ser analisados, então se você multiplicar a quantidade de células por 100, no pior caso de comparações também sera multiplicado por 100.
* 
e) Qual a complexidade da busca sequencial em uma matriz com m linhas e n colunas?

* A complexidade de tempo é O(m × n), é a quantidade de colunas ,pois o algoritmo percorre todas as linhas e colunas. 
