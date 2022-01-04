import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# criando antecedentes
qualidade = ctrl.Antecedent(np.arange(0, 11, 1), 'qualidade')  # valores de 0 a 10 
servico = ctrl.Antecedent(np.arange(0, 11, 1), 'servico') # valores de 0 a 10

# criando consequente
gorjeta = ctrl.Consequent(np.arange(0, 21, 1), 'gorjeta') # valores de 0 a 20

# Funções de associação
qualidade.automf(number=3, names=['ruim', 'boa', 'saborosa'])
servico.automf(number=3, names=['ruim', 'aceitável', 'ótimo'])

# utilizando técnica triangular
gorjeta['baixa'] = fuzz.trimf(gorjeta.universe, [0, 3, 6])
gorjeta['media'] = fuzz.trimf(gorjeta.universe, [5, 10, 13])
gorjeta['alta'] = fuzz.trimf(gorjeta.universe, [14, 20, 20])

# criando as regras
regra1 = ctrl.Rule(qualidade['ruim'] | servico['ruim'], gorjeta['baixa'])
regra2 = ctrl.Rule(servico['aceitável'], gorjeta['media'])
regra3 = ctrl.Rule(servico['ótimo'] | qualidade['saborosa'], gorjeta['alta'])

sistema_controle = ctrl.ControlSystem([regra1, regra2, regra3])
sistema = ctrl.ControlSystemSimulation(sistema_controle)


qualidade = input("Classifique a qualidade da comida [0-10]")
servico = input("Classifique o serviço [0-10]")

sistema.input['qualidade'] = int(qualidade)
sistema.input['servico'] = int(servico)
sistema.compute()

print("\nPorcentagem da Gorjeta: ", round(sistema.output['gorjeta'], 2), "%")

