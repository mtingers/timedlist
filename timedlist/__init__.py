__version__ = '1.0.2'
VERSION = __version__


class TimedList:
    """A timed list is similar to a normal list but adds a timestamp
    associated with each item. This can be useful for building sliding
    windows automatically without having to do the tracking yourself.
    """
    def __init__(self, maxtime=None, filled_percent=3.0):
        self.times = []
        self.items = []
        self.maxtime = maxtime
        self.filled_percent = filled_percent/100.0
        self._filled_max = maxtime + (self.filled_percent * maxtime)
        self._filled_min = maxtime - (self.filled_percent * maxtime)
        if self.maxtime < 1:
            raise Exception('maxtime must be >= 1')

    def prune(self, maxtime=None):
        """If maxtime is set, prune the list to fit within
        filled_percent. If maxtime is specified, this will
        override the maxtime for this call set on __init__().
        """
        if not maxtime and not self.maxtime:
            return
        if not maxtime:
            maxtime = self.maxtime
            filled_max = self._filled_max
        else:
            filled_max = maxtime + (self.filled_percent * maxtime)
        while self.times:
            total_time = self.times[-1] - self.times[0]
            if total_time <= filled_max:
                return
            del(self.times[0])
            del(self.items[0])

    @property
    def elapsed(self):
        """Get the total time from the last to first item in list"""
        if not self.times:
            return 0.0
        return self.times[-1] - self.times[0]

    @property
    def is_filled(self):
        """Check if the list is filled within filled_percent"""
        if not self.maxtime:
           return True
        if not self.times:
            return False
        total_time = self.times[-1] - self.times[0]
        if not total_time:
            return False
        if total_time < self._filled_min:
            return False
        return True

    def append(self, epoch, item):
        """Append an item to the list"""
        self.times.append(float(epoch))
        self.items.append(item)
        self.prune()

    def clear(self):
        """Reset the list"""
        self.items = []
        self.times = []

    def count(self, search):
        """Count items in list matching search"""
        return self.items.count(search)

    def count_time(self, search):
        """Count items in time list matching search"""
        return self.times.count(search)

    def index(self, search):
        """Find index of search in list"""
        return self.times.index(search)

    def insert(self, index, epoch, item):
        """Same as list insert"""
        self.times.insert(index, epoch)
        self.items.insert(index, item)

    def pop(self):
        """Sam as list pop but returns time and item"""
        return (self.times.pop(), self.items.pop())

    def remove(self, value):
        """Remove first occurrence of value."""
        index = self.items.index(value)
        del(self.items[index])
        del(self.times[index])

    def reverse(self):
        """Reverse *IN PLACE*."""
        self.times.reverse()
        self.items.reverse()

    def sort(self):
        """Stable sort *IN PLACE*."""
        raise Exception('Not implemented. Sorting a timelist/window probably does not make sense.')

    def __str__(self):
        out = 'TimedList(['
        for i in range(len(self.items)):
            out += '({}, {}), '.format(self.times[i], self.items[i])
        out += '])'
        return out

    def __repr__(self):
        out = 'TimedList(['
        for i in range(len(self.items)):
            out += '({}, {})'.format(self.times[i], self.items[i])
        return out

    def __contains__(self, value):
        return value in self.items

    def __add__(self, other):
        new_list = TimedList(maxtime=self.maxtime, filled_percent=self.filled_percent)
        new_list.items = self.items
        new_list.times = self.times
        try:
            if new_list.times[-1] < other.times[0]:
                raise Exception('Can only add TimedList if the right hand start time is > left hand end time.')
            new_list.items += other.items
            new_list.times = other.times
        except:
            raise Exception('TimedList can only be added to another TimedList object')
        return new_list

    def __radd__(self, other):
        return self.__add__(other)

    def __reversed__(self):
        return (reversed(self.times), reversed(self.items))


    def __delitem__(self, index):
        del(self.items[index])
        del(self.times[index])

    def __setitem__(self, key, epoch, item):
        self.times[key] = epoch
        self.items[key] = item

    def __getitem__(self, key):
        return (self.times[key], self.items[key])

    def get_item(self, key):
        return self.items[key]

    def get_time(self, key):
        return self.times[key]

    def __len__(self):
        return len(self.times)

    def __lt__(self, other):
        raise Exception('Not implemented.')

    def __le__(self, other):
        return __lt__(other)

    def __gt__(self, other):
        return __lt__(other)

    def __ge__(self, other):
        return __lt__(other)

    def __eq__(self, other):
        try:
            return self.items == other.items and self.times == other.times
        except:
            raise Exception('TimedList can only be compared to another TimedList object')

    def __ne__(self, other):
        return not self.__eq__(other)
