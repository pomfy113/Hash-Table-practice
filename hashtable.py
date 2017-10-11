#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        self.buckets = [LinkedList() for i in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{}: {}'.format(repr(k), repr(v)) for k, v in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({})'.format(repr(self.items()))

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table."""
        # Collect all keys in each of the buckets
        # O(n)? You're grabbing every bucket, but also every
        # item within the bucket. In terms of REAL time, it's n where
        # n is the amount of total items which you spread out across buckets
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table."""
        # O(n). See def keys(self) for thoughts.
        all_values = []
        for pail in self.buckets:
            for key, value in pail.items():
                all_values.append(value)
        return all_values
        pass

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table."""
        # O(n). See above again. Just about the same really.
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the length of this hash table by traversing its buckets"""
        # O(n^2). Length is O(n), and we're looping through.
        # TECHNICALLY it shouldn't change in terms of real time running;
        # When all spread out in buckets vs in the same linked list is same.
        count = 0
        for pail in self.buckets:
            count += pail.length()
        return count

    def contains(self, key):
        """Return True if this hash table contains the given key, or False"""
        # Check bucket O(1), then do a find O(n). It's O(n)
        # Worst case scenario is if it's at the end of a bucket.
        if (self.buckets[self._bucket_index(key)].find(lambda item: item[0] == key)):
            return True
        else:
            return False
        pass

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError"""
        # See above. O(n) again.
        if self.contains(key):
            data = self.buckets[self._bucket_index(key)].find(lambda item: item[0] == key)
            return data[1]
        else:
            raise KeyError

        pass

    def set(self, key, value):
        """Insert or update the given key with its associated value"""
        # Insert or update the given key-value entry into a bucket
        # Constant + append which is constant.
        if self.contains(key):
            self.delete(key)
        self.buckets[self._bucket_index(key)].append((key, value))
        pass

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError"""
        # See "delete" function of linked list;
        # Can range from a few (if front or empty list) to O(n) (middle/end)
        if self.contains(key):
            self.buckets[self._bucket_index(key)].delete((key, self.get(key)))
            return
        else:
            raise KeyError
        pass


def test_hash_table():
    ht = HashTable()
    print(ht)

    print('Setting entries:')
    ht.set('I', 1)
    print(ht)
    ht.set('V', 5)
    print(ht)
    ht.set('X', 10)
    print(ht)
    ht.set('X', 20)
    print(ht, "\n\n")
    print('contains(X): ' + str(ht.contains('X')))
    print('get(I): ' + str(ht.get('I')))
    print('get(V): ' + str(ht.get('V')))
    print('get(X): ' + str(ht.get('X')))
    print('length: ' + str(ht.length()))
    print(ht.values())

    # Enable this after implementing delete:
    print('Deleting entries:')
    ht.delete('I')
    print(ht)
    ht.delete('V')
    print(ht)
    ht.delete('X')
    print(ht)
    print('contains(X): ' + str(ht.contains('X')))
    print('length: ' + str(ht.length()))


if __name__ == '__main__':
    test_hash_table()
