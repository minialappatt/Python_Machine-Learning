class ListNode:

    def __init__(self, val='', next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class TextEditor:

    def __init__(self):
        self.head = ListNode(val='HEAD')  # dummy head node
        self.cursor = self.head

    def AddText(self, text: str) :
        node = self.cursor.next
        for ch in text:
            new_node = ListNode(val=ch)
            self.cursor.next = new_node
            new_node.prev = self.cursor
            self.cursor = self.cursor.next
        if node:
            self.cursor.next = node
            node.prev = self.cursor

    def DeleteText(self, k: int) :
        node = self.cursor.next
        i = 0
        while self.cursor.prev and i < k:
            self.cursor = self.cursor.prev
            i += 1
        self.cursor.next = node
        if node:
            node.prev = self.cursor

    def MoveLeft(self, k: int) :
        i = 0
        while self.cursor.prev and i < k:
            self.cursor = self.cursor.prev
            i += 1

    def MoveRight(self, k: int) :
        i = 0
        while self.cursor.next and i < k:
            self.cursor = self.cursor.next
            i += 1

    def PrintText(self) :
        node = self.head.next

        while node :
            file2.write(node.val)
            print(node.val, end="")
            node = node.next
        file2.write('\n')
        print()
        print(self.cursor.val)

#main control
editor = TextEditor()
file1 = open('inputPS03.txt', 'r')
file2 = open('outputPS03.txt', 'w')

Lines = file1.readlines()

# Strips the newline character
for line in Lines:
    text = line.strip()

    if "PrintText" in text :
        editor.PrintText()
    else :
        command, param = text.split(" ",1)

        if "AddText" in command :
            editor.AddText(param)
        if "DeleteText" in command :
            editor.DeleteText(int(param))
        if "MoveLeft" in command :
            editor.MoveLeft(int(param))
        if "MoveRight" in command :
            editor.MoveRight(int(param))

file1.close()
file2.close()