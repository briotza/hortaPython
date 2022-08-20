## Horta Comunitária

### Introdução
Esse código foi desenvolvido pela equipe Briotza destinado ao
desafio "Horta Comunitária" após conclusão do curso de férias "Fundamentos de Python"
desenvolvido pelo Centro Universitário FACENS.

### Objetivo
Criar uma plataforma de cadastros e controle de funções e produtos para uma Horta Comunitária, 
onde a ferramenta armazenará dados e informações de usuários e, a partir disso, auxiliará na administração do 
funcionamento da horta e distribuição de produtos à população.

### Funcionalidades da Aplicação
* Cadastro de moradores (colaboradores e/ou consumidores);
* Login para cadastrados;
* Portais de navegação, de acordo com a função definida no cadastro;
* Alteração de dados e exclusão de perfil;
* Contadores para cada produto produzido na horta;
* Definição de cronogramas para determinadas funções;
* Agendamento para retirada de produtos.

### IDE
A IDE utilizada para desenvolvimento dessa aplicação foi PyCharm.

### Guia das Funções
#### Plantação
O usuário escolhe duas datas de cada mês (não havendo necessidade de ser sempre
as mesmas) para realizar a plantação de novos produtos na horta. Após efetuar a plantação, o 
usuário deve acessar o portal e registrar quais e quantos produtos foram plantados em 
determinada data.

#### Irrigação
O usuário escolhe um dia da semana e um período (manhã ou tarde) para comparecer toda semana 
na horta e realizar a irrigação dos produtos plantados. Ele pode alterar o cronograma, porém 
apenas se nenhum outro usuário estiver utilizando esse dia/período.

#### Colheita
O usuário define um dia de cada mês para ir até a horta e realizar a colheita dos produtos, caso 
estejam prontos para serem colhidos. Após realizar a colheita, ele deve acessar o portal e 
registrar quais e quantos produtos foram colhidos em determinada data. O usuário pode alterar as 
datas porém é notificado quando alguém já agendou na data escolhida, podendo continuar ou não.

#### Distribuição
O usuário define um dia da semana e um horário (08h ou 17h) para realizar a distribuição dos produtos. 
Porém esse usuário só deve ir até a horta para cumprir sua função caso algum consumidor tenha agendado 
retirada de produto na sua data de distribuição. Para visualizar se possui reservas na sua próxima data 
o usuário deve acessar o portal na aba "Retirada".
