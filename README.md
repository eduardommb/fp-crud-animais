# **Manual do usuario**

## **MENU**

- Ao iniciar o sistema você verá esta mesagem:

```
   === Sistema Adoção+ ===
1. Adicionar Animal
2. Ver Animais
3. Editar Animal
4. Excluir Animal
5. Adicionar Cuidado/Atividade
6. Ver Cuidados/Atividades
7. Ver Datas
8. Sugestões Personalizadas
9. Adicionar Adotante
10. Ver Adotantes
11. Editar Adotantes
12. Deletar Adotantes
0. Sair
Escolha uma opção:
```

- Para começar a mexer neste menu, digite o número para qual a função desejada. No caso começe com o numero 1 para adicionar um animal.

- **Atenção**: Digitar o número como inteiro e não como uma palavra.

### Ao digitar o número 1, você será levado à uma lista de informações necessárias nesta ordem:

1. **Nome**: (Digite o nome do animal)
2. **Espécie**: (Digite a espécie do animal, *ex: gato, cachorro, ave, etc...*)
3. **Raça**: (Digite a raça do animal, *ex: vira-lata, chihuahua, siamês, etc...* )
4. **Idade**: (Digite a idade do animal novamente como um numero inteiro e não por exemplo:"nove anos")
5. **Saúde**: (Digite o estado de saúde do animal)
6. **Data de chegada**: (Digite a que o animal chegou a clínica neste formato *dd/mm/aaaa*)
7. **Comportamento**: (Digite o comportamento característico do animal, *ex:calmo, arisco, agitado, etc...* )
8. **Nome do arquivo**: (Digite o nome do arquivo que deseja salvar a foto do animal)

### Depois desses passos, o primeiro arquivo .csv vai ser criado e você poderá proseguir.

- Ao digitar o número 2, você poderá visualizar as informações de cada animal que foi digitado.\
ex:

```
Nome           Espécie        Raça           Idade   Saúde               Chegada        Comportamento
------------------------------------------------------------------------------------------------------------
bebe           cachorro       chihuahua      6       normal              21/11/2025     carente
tyler          gato           gato de rua    5       doente              20/11/2025     agressivo

```

### Editar animal

- Ao adicionar o número 3, será perguntado qual o nome do animal que deseja editar.Digite conforme sua vontade.
- O terminal irá passar pela mesma lista do numero 1 e pedirá para alterar as informações desejadas, **caso não queira alterar deixe em branco**.\
ex:

```
Nova espécie (gato):
Nova idade (5): 7
```

- No caso do exemplo acima a espécie não será alterada, mas a idade do gato será alterada de 5 para 7 anos.

### Excluir animal

- Basta digitar o nome do animal que deseja excluir.\
ex:

```

Digite o nome do animal que deseja editar: tyler
```

## Cuidados

### Adicionar Cuidados

- Para adicionar cuidados digite 5. 

- Ao digitar 5, você será perguntado qual o nome do animal que deseja adicionar o cuidado e será apresentado a seguinte lista de informações:

1. **Nome do cuidado/atividade: **: Digite aqui qual será a atividade do animal, *ex: banho, tosa, consulta, etc...*
1. **Descrição do cuidado/atividade**: Digite uma descrição sobre o que é/ o que se trata esse cuidado. 
2. **Data prevista (dd-mm-aaaa)**: Digite a data desejada que a atividade precisa ser feita (no formato indicado).
3. **Responsável**: Digite o nome do responsável pela a atividade.\
4. **Anotações adicionais**: Digite alguma anotação extra *ex: recomendações, tipo do remédio, etc. (opcional)*
ex:

```
=== Adicionar Cuidado/Atividade ===
Nome do cuidado/atividade: banho
Descrição do cuidado/atividade: banho completo 
Data prevista (dd/mm/aaaa): 01/12/2025
Responsável: nininho
Anotações adicionais: usar shampoo e condicionador
```


### Ver Cuidados/Atividades

- Digite 6 para ver as atividades do animal.
- Digite o nome do animal desejado para ver atividades.

## Ver Datas

- Para ver quantos dias faltam para a atividade de um animal, digite 7 em ver datas.
- Digite o nome do animal que deseja ver as datas conforme a tabela.
- Será exibido o tipo de atividade seguido pela data marcada e depois a quantidade de dias restantes.\
ex:

```
-------Cuidados de tyler:--------

- consulta (13/12/2025): faltam 21 dias

Pressione ENTER para continuar...

```

## Sugestões Personalizadas

- Digite 8 para ver as principais sugestões para o animal.
- Digite o nome do animal que deseja ver as sugestões.
- As sugestões são divididas em:

1. Perfil ideal de adotante: o melhor cenário de adotante conforme as caracteristicas do animal.\
    ex:  `Indicado para adotante experiente`
2. Compatibilidade: para ver qual os melhores tipos de ambiente e interação do animal.\
    ex: `Compatível com outros cães ativos`
3. Cuidados especiais: caso o animal possua certas características será exibido cuidados especiais necessários.\
    ex: `Processo de socialização gradual`
4. Atividades recomendadas: Principais atividades que serão recomendadas ao animal.\
    ex: `Passeios frequentes, brincadeiras ao ar livre e treinamento básico`

## Sistema de Adotante

- Separamos um sistema para que cadastre uma lista de possiveis adotantes.

### Para adicionar um adotador

Ao digitar 9 para adicionar um adotador, você deverá preencher:

1. **Nome Completo**: Digite o nome completo da pessoa;
2. **Idade**: Digite a idade da pessoa;
3. **Genero**: Digite o genero;
4. **Status**: Digite o Status social que se encontra;
5. **Animal Querido**: Digite o tipo de animal que prefere adotar;
6. **Comportamento Animal**: Digite o comportamento desejado.\
ex:

```
=========CADASTRO DE ADOÇÃO========
Nome Completo: Pedro Henrique Fonseca da Silva
Idade: 30 
Genero: masculino
Status: casado
Animal querido: cachorro
Comportamento Animal: calmo
```

### Ver adotantes

- Para ver os adotantes cadastrados, digite 10.
- Estará separada pelas informações do item anterior.\
ex:

```
Nome                               Idade          Genero         Status         Animal Preferido    Comportamento Preferido
========================================================================================================================   
Elian Gabriel Andrade Cunha        22             Masculino      solteiro       gato                tranquilo
Pedro Henrique Fonseca da Silva    30             masculino      casado         cachorro            calmo
```

### Deletar Adotantes

- Para deletar um adotante, digite 12.
- Depois digite o nome completo do adotador que deseja deletar.


` Caso deseje encerrar as atividades, basta digitar 0`

# Interface gráfica
- Ao entrar no site da nossa interface grafica, você verá duas opções:
<br>
<img width="1919" height="916" alt="Image" src="https://github.com/user-attachments/assets/37b5dab0-114c-47d3-9990-2c97b5b17fbc" />

## Dados dos Animais
### CRUD
- Ao clicar em conferir os dados dos animais, você verá uma tabela com todos os animais cadastrados:
<br>
<img width="1919" height="914" alt="Image" src="https://github.com/user-attachments/assets/ab38c0b8-c34f-4223-80d2-702568cfe109" />
<br>
<br>
- No canto superior esquerdo, você verá três opções: *adicionar, editar e excluir nesta ordem*:\
1. **Adicionar** lhe levará a uma tela pedindo todas as informações previamente discutidas:
<br>
<img width="1917" height="912" alt="Image" src="https://github.com/user-attachments/assets/de14c6b9-7fef-4fb8-b8b7-d1840c21cb2f" />
<br>
2. **Editar** lhe pedirá um nome dentro da tabela para editar e depois lhe levará para a mesma tela de adicionar mas com as informações já postas.
<br>
<img width="448" height="204" alt="Image" src="https://github.com/user-attachments/assets/dad0ddc3-5643-417c-a4c6-ef7b9e7c0d4f" />
<br>
<img width="1762" height="574" alt="Image" src="https://github.com/user-attachments/assets/1128273b-eb50-429b-a333-4cf84cfd8195" />
<br>
3. **Excluir** irá pedir novamente o nome do animal que deseja exluir e depois é so apagar.

### Interface do Animal
- Ao clicar no animal desejado na lista, você poderá ver todas as informações cadastradas do animal, bem como sugestões personalizadas e os dias restantes para as tarefas registradas(Proximo ponto a ser mostrado).
<br>
<img width="1666" height="890" alt="Image" src="https://github.com/user-attachments/assets/13f44789-d8f4-4a6e-b2eb-453c3e50522f" />
<br>

### Tarefas
- Ao clicar no botão **Tarefas** no canto superior direito, você será levado a um cadastro que deverá conter as informações previamente discutidas sobre Cuidados/Atividades como o tipo de tarefa e o responsavel.
<br>
<img width="524" height="405" alt="Image" src="https://github.com/user-attachments/assets/fe9c71ed-7118-480a-a0eb-10f238f63b14" />
<br>
<br>
<br>
- Você pode acessar as tarefas cadastradas ao clicar em **Tarefas** na página do animal(imagem acima).
<br>
<img width="1885" height="895" alt="Image" src="https://github.com/user-attachments/assets/85dede61-8dae-4525-b4ec-4b62ce2bbc12" />
