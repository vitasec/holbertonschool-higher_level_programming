#!/usr/bin/python3
"""Bu modul Singly Linked List (Əlaqəli siyahı) və onun Node-unu təyin edir."""


class Node:
    """Əlaqəli siyahının bir düyününü (Node) təmsil edir."""

    def __init__(self, data, next_node=None):
        """Yeni bir Node instansiyası yaradır.

        Args:
            data (int): Düyündə saxlanılan məlumat.
            next_node (Node, optional): Siyahıdakı növbəti düyün.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Node-un data atributunu qaytarır."""
        return self.__data

    @data.setter
    def data(self, value):
        """Data atributunu təyin edir və növünü yoxlayır."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Node-un next_node atributunu qaytarır."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next_node atributunu təyin edir və növünü yoxlayır."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Təkyönlü əlaqəli siyahını təmsil edən sinif."""

    def __init__(self):
        """Boş bir SinglyLinkedList yaradır."""
        self.__head = None

    def __str__(self):
        """Siyahını ekranda çap etmək üçün sətrə (string) çevirir."""
        values = []
        current = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return '\n'.join(values)

    def sorted_insert(self, value):
        """Yeni bir Node-u siyahıda düzgün (artan) sıraya əlavə edir.

        Args:
            value (int): Əlavə ediləcək yeni məlumat (Node data).
        """
        new_node = Node(value)

        # 1-ci hal: Siyahı boşdur və ya yeni rəqəm ilk rəqəmdən kiçikdir
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        # 2-ci hal: Düzgün yeri tapana qədər siyahını gəzirik (traverse)
        current = self.__head
        while (current.next_node is not None and
               current.next_node.data < value):
            current = current.next_node

        # Yeni düyünü araya daxil edirik
        new_node.next_node = current.next_node
        current.next_node = new_node
