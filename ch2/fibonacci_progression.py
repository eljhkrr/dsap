from progression import Progression

class FibonacciProgression(Progression):
    """Iterator producing a generalized Fibonacci progression."""

    def __init__(self, first=0, second=1):
        """Create a new Fibonacci progression.

        start   first item of the progression (default 0)
        second  second item of the progression (default 1)
        """
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        """Update current value by taking sum of previous two."""
        self._prev, self._current = self._current, self._current + self._prev

if __name__ == '__main__':
     r = FibonacciProgression(2, 2)
     r.print_progression(8)
