---
tags:
    - data-structures
    - computer-science
---

# Single-Ended Singly Linked List

```cpp
class ListNode {
public:
    Data data;
    Node* next;
    Node(Data data)
    {
        this->data = data;
        next = nullptr;
    }
    Node(Data data, Node* next)
    {
        this->data = data;
        this->next = nullptr;
    }
}
```

```cpp
class LinkedList
{
    ListNode* head;
    
    LinkedList()
    {
        head = nullptr;
    }
}
```

## PushBack

Non-recursive:

- Only `head`, $O(n)$:

```cpp
class LinkedList
{
public:
    void pushBack(Data data)
    {
        if (this->head == nullptr)
        {
            this->head = new ListNode(data);
            return;
        }

        ListNode* currentNode = this->head;
        
        while(currentNode->next != nullptr)
            currentNode = currentNode->next;

        currentNode->next = new ListNode(data);
    }
};
```

Recursive:

```cpp
class LinkedList
{
public:
    void pushBack(Data data)
    {
        pushBackRecursive(data, this->head);
    }

private:
    void pushBackRecursive(Data data, ListNode* &currentNode)
    {
        if (currentNode == nullptr)
        {
            currentNode = new ListNode(data);
        }
        else{
            pushBackRecursive(data, currentNode->next);
        }
    }
};
```

## PopBack

Non-recursive:

```cpp

```

Recursive:

```cpp

```