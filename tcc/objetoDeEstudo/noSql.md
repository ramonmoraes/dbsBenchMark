# NoSQL
Onde no SQL o agrupamento de data era feito por tabelas nos bancos NoSQL é feito por uma coleção, e os registros são referenciados como documentos.
Uma coleção não define o tipo do documento que vai ser inserida nela, assim os documentos não precisam de um padrão(_schema_) definido, é possivel inserir diversos dados diferentes;

Caso haja a necessidade de adicionar um novo atributo em um registro, no SQL seria necessario atualizar o schema da tabela, e depois modificar todos registros daquela tabela com um valor padrão para esse novo atributo; No NoSQL, basteria inserir o registro do jeito que veio, sem nenhuma modificação aos outros documentos;

No NoSQL não há a necessidade de relacionar os arquivos com chaves, assim também não garante a mesma integridade de dados que o SQL;
