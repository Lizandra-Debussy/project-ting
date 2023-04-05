from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._items = []

    def __len__(self):
        return len(self._items)

    def enqueue(self, value):
        self._items.append(value)

    def dequeue(self):
        if len(self._items) == 0:
            raise IndexError("Fila Vazia")
        return self._items.pop(0)

    def search(self, index):
        if index < 0 or index >= len(self._items):
            raise IndexError("Índice Inválido ou Inexistente")
        return self._items[index]

    def is_empty(self):
        return not bool(self._items)
