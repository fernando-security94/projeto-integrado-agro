# Resolução situação problema para
# facilitar a criação e manipulação de 
# pronturários médicos

class Prontuario:
    def __init__(self, paciente, diagnostico, tratamento, proximo=None):
        self.paciente = paciente
        self.diagnostico = diagnostico
        self.tratamento = tratamento
        self.proximo = proximo

    def __repr__(self):
        return(f'Paciente: {self.paciente}\n'
               f'Diagnóstico: {self.diagnostico}\n'
               f'Tratamento: {self.tratamento}')

class ProntuariosEncadeados:
    def __init__(self):
        self.cabecalho = None
    
    def adicionar_prontuario(self, paciente, diagnostico, tratamento):
        novo_prontuario = Prontuario(paciente, diagnostico, tratamento, self.cabecalho)
        self.cabecalho = novo_prontuario

    def buscar_prontuario(self, nome_paciente):
        atual = self.cabecalho

        while atual:
            if atual.paciente == nome_paciente:
                return atual
            atual = atual.proximo
        return None
    
# Uso da lista encadeada para gerenciar prontuarios
sistema_prontuarios = ProntuariosEncadeados()

sistema_prontuarios.adicionar_prontuario("Alice Santos", "Diabetes tipo II", "Metformina")
sistema_prontuarios.adicionar_prontuario("João Silva", "Hipertensão", "Losartana")
sistema_prontuarios.adicionar_prontuario("Fernando Ribeiro", "Lesão LCA", "Reconstrução de Ligamentos")

# Buscando prontuario
p1 = sistema_prontuarios.buscar_prontuario("Fernando Ribeiro")
print(p1)
print()
p2 = sistema_prontuarios.buscar_prontuario("Alice Santos")
print(p2)