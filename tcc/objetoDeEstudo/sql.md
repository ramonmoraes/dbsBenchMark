# Bancos SQL
Bancos de dados são ferramentas para armazenar dados de forma persistente e de facil consulta. Um banco de dados SQL (_Structured Query Language_) pode ser representado por um sistema de armazenamento onde cada registro é armazenado em uma pasta relativa ao assunto do registro, a qual a pasta é armazenada dentro de um arquivo. Seguindo esse exemplo, caso haja a necessidade encontrar um arquivo de um assunto especifico, basta procurar na pasta relacionada ao assunto no arquivo.

Assim também são feitos os bancos de dados SQL, cada registro deve seguir um padrão (_schema_), e deve ser inserido na sua tabela (_table_) relativa, que são armazenadas no banco de dados. É comun dividir um banco em diversas tabelas, uma para cada tipo de registro.

Como as informações são dispersas em diversas tabelas separadas por tipos, as informações de uma tabela completam informações de outra. Um registro de uma tabela referencia outro registro de outra tabela, assim informando que aqueles registros apesar de estarem separados por tabelas, pertecem a mesma informação original.

Para conseguir essa informação completa requere o uso de cruzamento de informações entre tabelas(_join_), onde é dito quais tabelas se co-relacionam, assim onde há registro referenciando outro registro, após o uso do join havera a união dos registros resultado na informação completa.
