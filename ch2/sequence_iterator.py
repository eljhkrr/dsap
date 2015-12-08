class SequenceIterator:
    """An iterator of Python's sequence types."""

    def __init__(self, sequence):
        """Create an iterator for the given sequence."""
        self._seq = sequence
        self._k = -1            #increments to 0 on first call to next

    def __next__(self):
        """Return the next element, or raise StopIteration Exception."""
        self._k += 1    #advance index
        if self._k < len(self._seq):
            return self._seq[self._k]
        else:
            raise StopIteration()

    def __eq__(self, other):
        if len(self._seq) != len(other):
            return False
        else:
            for i in range(len(self._seq)):
                if self._seq[i] != other[i]:
                    return False
            return True
        
    def __len__(self):
        return len(self._seq)

    def __getitem__(self, j):
        return self._seq[j]

    def __iter__(self):
        """By convention, an iterator returns itself as an iterator."""
        return self
