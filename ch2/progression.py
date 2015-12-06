class Progression:
    """Iterator producing a generic progression.

    Default iterator produces the whole numbers 0, 1, 2...
    """

    def __init__(self, start=0):
        """Initialize current to the first value of the progression."""
        self._current = start

    def _advance(self):
        """Update self._current to a new value.

        This should be overriden by a subclass to customize progression.

        By convention, if current is set to None, this designates the end of a finite progression.
        """
        self._current += 1

    def __next__(self):
        """Return the next element or raise a StopIteration error."""
        if self._current is None:       #by convention
            raise StopIteration
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        """By convention, an iterator returns itself."""
        return self

    def print_progression(self, n):
        """Print the next n values of the progression."""
        print(' '.join(str(next(self)) for i in range(n)))
