### Bubble Sort

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

