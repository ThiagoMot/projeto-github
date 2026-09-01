# Documento de Baseline - Versão 1.0.0

## Identificação
- **Nome do Sistema:** Sistema de Biblioteca
- **Identificação da Baseline:** BASELINE-LIB-1.0.0
- **Versão:** 1.0.0
- **Data:** 17/08/2026
- **Integrantes Responsáveis:** Thiago, Emanuella, Matheus e Guilherme
- **Status da Baseline:** Aprovada

---

## Itens de Configuração (ICs)

| Nome | Tipo | Estado/Versão | Justificativa |
| :--- | :--- | :--- | :--- |
| **Código Fonte (`atv.py`)** | Código | v1.0.0 | Contém a lógica de negócio e regras do sistema. |
| **Documentação da Baseline (`baseline-v1.0.0.md`)** | Documentação | v1.0.0 | Registra formalmente o estado aprovado dos ICs. |
| **Instruções de Uso (`README.md`)** | Documentação | v1.0.0 | Permite a reprodução e execução do projeto. |
| **Configuração Git (`.gitignore`)** | Configuração | v1.0.0 | Impede versionamento de arquivos temporários. |

---

## Funcionalidades Incluídas
1. Cadastro de usuários
2. Cadastro de livros
3. Empréstimo de livros (com validação de disponibilidade)
4. Devolução de livros

---

## Ambiente
- **Python:** 3.10 ou superior
- **Sistema Operacional:** Windows
- **Dependências Externas:** Nenhuma

---

## Limitações Conhecidas
- Armazenamento volátil em memória (os dados são perdidos ao reiniciar o programa).