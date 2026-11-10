import functools

from prometheus_client import Counter, start_http_server

OPERACOES = Counter(
    "biblioteca_operacoes_total",
    "Total de operações realizadas no sistema",
    ["operacao", "resultado"],
)


def iniciar_monitoramento(porta=8000):
    """Abre o endereço /metrics para o Prometheus coletar."""
    start_http_server(porta)


def registrar_operacao(operacao, sucesso):
    resultado = "sucesso" if sucesso else "falha"
    OPERACOES.labels(operacao=operacao, resultado=resultado).inc()


def monitorar(operacao):
    """Decorador: conta o resultado de uma função que retorna (bool, mensagem)."""
    def decorador(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            resultado = func(*args, **kwargs)
            sucesso = resultado[0] if isinstance(resultado, tuple) else bool(resultado)
            registrar_operacao(operacao, sucesso)
            return resultado
        return wrapper
    return decorador