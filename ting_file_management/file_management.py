import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith(".txt"):
            raise ValueError("Formato inválido")
        with open(path_file, "r") as f:
            lines = f.read().split("\n")
        return lines
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    except ValueError:
        print("Formato inválido", file=sys.stderr)
