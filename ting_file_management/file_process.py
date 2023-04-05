from ting_file_management.file_management import txt_importer
import sys


def process(path_file: str, instance):
    file_name = path_file.split("/")[-1]

    for item in instance._items:
        if item["nome_do_arquivo"].split("/")[-1] == file_name:
            print(f"Arquivo {path_file} já processado")
            return

    lines = txt_importer(path_file)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }
    instance.enqueue(data)
    print(data, file=sys.stdout)


def remove(instance):
    if instance.is_empty():
        print("Não há elementos", file=sys.stdout)
        return

    item = instance.dequeue()
    path_file = item["nome_do_arquivo"]
    print(f"Arquivo {path_file} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    try:
        file_data = instance.search(position)
        print(file_data, file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
