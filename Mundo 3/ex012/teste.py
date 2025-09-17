from utilidadesCeV import moeda
from utilidadesCeV import dado

preço = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(preço, 20, 12)