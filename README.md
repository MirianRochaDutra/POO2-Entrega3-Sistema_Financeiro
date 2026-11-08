# POO2-Entrega3-Sistema_Financeiro
Terceira entrega da disciplina de POO2, atividades referentes aos capitulos 12,13,14 e 15 do Módulo 4.


# Projeto Financeiro - Terceira Parte

## Módulo 4

Nesta etapa foram aplicados os conceitos de Simple Factory, Factory Method e Injeção de Dependências.

## Leitores

Foi utilizada uma Simple Factory para criar os leitores.

A classe `CriadorLeitor` recebe a extensão do arquivo e cria o leitor correspondente.

Foram implementados:

- `LeitorCSV`
- `LeitorJSON`

A Simple Factory foi escolhida porque a decisão depende de um dado simples: a extensão do arquivo.

Não é necessário criar uma hierarquia de classes para decidir qual leitor será utilizado.

## Exportadores

Para os exportadores foi utilizado Factory Method.

Foram implementados:

- `ExportadorCSV`
- `ExportadorHTML`

A classe `ExportadorRelatorio` possui o fluxo comum da exportação e possui o método `criar_documento()` como Factory Method.

Cada subclasse decide qual documento deve ser criado.

A escolha pelo Factory Method ocorreu porque cada formato pode ter sua própria forma de criar o documento.

## Importadores

Para os importadores foi utilizada uma Simple Factory.

Foram implementados:

- `ImportadorBancoX`
- `ImportadorBancoY`

A classe `CriadorImportador` recebe o banco de origem e cria o importador correspondente.

A escolha foi feita porque o banco de origem é um dado simples utilizado para escolher o objeto.

## Injeção de Dependências

O `ServicoImportacao` recebe suas dependências pelo construtor:

- `CriadorLeitor`
- `CriadorImportador`
- `ExportadorRelatorio`

O serviço não cria essas classes internamente.

Isso facilita os testes porque podemos substituir os colaboradores reais por dublês.

## O que ainda é criado internamente

As classes concretas de leitores e importadores são criadas pelas respectivas factories.

Isso faz parte da responsabilidade das factories.

O `ServicoImportacao` não cria diretamente esses objetos.

## Raiz de composição

A raiz de composição está na função:

`montar_aplicacao()`

no arquivo:

`financeiro/aplicacao.py`

É nesse local que os colaboradores são montados e entregues ao serviço.

## Substituição por dublê

Atualmente é possível substituir o leitor, o criador de importador e o exportador por dublês sem modificar o `ServicoImportacao`.

Isso foi demonstrado no teste:

`test_substituir_colaboradores_por_dubles`

O teste cria versões falsas dos colaboradores e as entrega ao serviço pelo construtor.