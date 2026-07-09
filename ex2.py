class Song:
    def __init__(self, data):
        self.data = data
        self.next = None


class Playlist:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_song = Song(data)

        if self.head is None:
            self.head = new_song
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_song

    def prepend(self, data):
        new_song = Song(data)
        new_song.next = self.head
        self.head = new_song

    def insert(self, data, prev):
        new_song = Song(data)

        current = self.head
        while current:
            if current.data == prev:
                new_song.next = current.next
                current.next = new_song
                return
            current = current.next

        print("Previous song not found")

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

        print("Song not found")

    def search(self, data):
        current = self.head

        while current:
            if current.data == data:
                return True
            current = current.next

        return False

    def display(self):
        if self.head is None:
            print("Playlist is empty")
            return

        current = self.head
        while current:
            print(current.data)
            current = current.next


# Driver Code
print("Playlist")

ob = Playlist()

print(ob.is_empty())

ob.append("vennilave")
ob.append("oh shala")
ob.append("kandange kandange")

print("\nAfter Append:")
ob.display()

ob.prepend("vaaya moodi")
ob.append("en kadhal solla")

print("\nAfter Prepend and Append:")
ob.display()

flag = ob.search("kandange kandange")
print("\nSearch Result:", flag)

ob.delete("oh shala")

print("\nAfter Delete:")
ob.display()