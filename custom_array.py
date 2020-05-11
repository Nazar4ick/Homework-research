import ctypes


class Array:
    """
    Class for representing arrays
    """
    def __init__(self, size):
        """
        Initializes a new array
        :param size: int
        """
        assert size > 0
        self._size = size
        py_array = ctypes.py_object * size
        self._elements = py_array()
        self.clear(None)

    def __len__(self):
        """
        returns the length of the array
        :return: int
        """
        return self._size

    def __getitem__(self, index):
        """
        returns the value with the specified index
        """
        assert 0 <= index < len(self), "Array subscript out of range"
        return self._elements[index]

    def __setitem__(self, index, value):
        """
        sets the item with the specified index to the value
        """
        assert 0 <= index < len(self)
        self._elements[index] = value

    def clear(self, value):
        """
        sets all items to the specified value
        """
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        return _ArrayIterator(self._elements)

    def __str__(self):
        """
        represents the array
        :return: str
        """
        string = ''
        for i in range(len(self)):
            string += ', ' + str(self._elements[i])
        return string[2::]


class _ArrayIterator:
    """
    Class for representing array iterators
    """
    def __init__(self, array):
        """
        Initializes a new array iterator
        :param array:
        """
        self._array_ref = array
        self._cur_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur_index < len(self._array_ref):
            item = self._array_ref[self._cur_index]
            self._cur_index += 1
            return item
        else:
            raise StopIteration
