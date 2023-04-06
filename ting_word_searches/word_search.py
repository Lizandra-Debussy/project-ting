def exists_word(word, instance):
    results = []
    for file_index in range(len(instance)):
        file = instance.search(file_index)
        file_occurrences = [
            {"linha": line_index + 1}
            for line_index, line in enumerate(file["linhas_do_arquivo"])
            if word.lower() in line.lower()
        ]
        if file_occurrences:
            results.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": file_occurrences
            })
    return results


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
