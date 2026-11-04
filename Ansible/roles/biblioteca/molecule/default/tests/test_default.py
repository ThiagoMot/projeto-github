def test_diretorio_aplicacao_existe(host):
    assert host.file("/tmp/sistema-biblioteca").exists


def test_aplicacao_e_um_diretorio(host):
    assert host.file("/tmp/sistema-biblioteca").is_directory


def test_ambiente_virtual_criado(host):
    assert host.file("/tmp/sistema-biblioteca/venv").is_directory


def test_python_do_venv_existe(host):
    assert host.file("/tmp/sistema-biblioteca/venv/bin/python").exists


def test_requirements_copiado(host):
    assert host.file("/tmp/sistema-biblioteca/requirements.txt").is_file


def test_pasta_tests_copiada(host):
    assert host.file("/tmp/sistema-biblioteca/tests").is_directory