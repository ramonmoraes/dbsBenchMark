# Introdução

Com o aumento da quantidade de informações e o grande cresimento em inteligencia artificial, é comun ter bancos de diversos giga byte de tamanho.
Para fazer predições matematicas, encontrar data que relacione o seu modelo ou buscar informações para outros motivos, fazer buscas com dados relacionados em tempo habil é de suma importancia.

Os bancos SQL, são os ensinados em faculdades e os mais utilizados na industria<sup>1</sup> de acordo com a pesquisa do stack-overflow<sup>2</sup>. Assim é comun quando criamos em um novo projeto, ou fazemos uma migração de dados, seja escolhido tais bancos como ferramenta de armazenamento. Mas a depender da modelagem outro banco possa ser mais perfomatico. Nesse projeto, testo a hipótese de que para dados altamente relacionados um banco de dados em grafo é mais performatico do que um SQL.

O teste é feito atravez da comparação da velocidade de busca entre os bancos, utilizando dados relacionados em ambos os casos.
