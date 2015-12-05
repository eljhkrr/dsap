import collections

class Range(collections.Sequence):
    """A class that mimics the built-in range class."""

    def __init__(self, start, stop=None, step=1):
        """Initialize a Range instance.

        Parameters are similar to the built-in range class.
        """

        if step == 0:
            raise ValueError("Step cannot be zero.")

        if stop is None:
            start, stop = 0, start

        self._length = max(0, (stop - start + step -1)//step)

        #Needed for __getitem__
        self._start = start
        self._step = step

    def __len__(self):
        """Return number of entries in the range."""
        return self._length

    def __getitem__(self, k):
        """Return entry at index k."""
        if k < 0:
            k += len(self)

        if not 0 <= k < self._length:
            raise IndexError("Index out of range.")

        return self._start + k*self._step
