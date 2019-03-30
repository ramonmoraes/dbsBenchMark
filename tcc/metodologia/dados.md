# Como os dados foram feitos

## Nomes

Para conseguir uma lista de nomes eu baixei um csv desse [link](https://brasil.io/dataset/genero-nomes/nomes);
Nesse csv haviam diversos campos desnecessarios para meu projeto, assim limpei com o script, `cleanNamesCsv` os dados e gerei uma lista apenas de nomes;

Com essa lista de nomes dividi em 3 partes, 0,01% do total de nomes para a quantidade de juizes, 0,5% para advogados e o restante para partes do processo;

A lista de tribunais eu peguei de um outro projeto, com 52 tribunais diferentes.
