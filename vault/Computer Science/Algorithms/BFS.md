```c
BFS()
    bfsCount = 1;
    finCount = 1;
    
    // 1. Initialize all vertices
    foreach s ∈ V {
        s->state = initial;
        s->parent = NULL;
    }
    
    // 2. Start a BFS visit for every disconnected component
    foreach s ∈ V {
        if (s->state == initial) {
            BFSvisit(s);
        }
    }

BFSvisit(s)
    Queue Q;
    
    // 1. Properly initialize and enqueue the starting node
    s->state = active;
    s->bfsNum = bfsCount++;
    Q.enqueue(s);
    
    // 2. Standard single-pass queue loop
    while (!Q.empty()) {
        v = Q.dequeue(); // Dequeue immediately!
        
        // 3. Process all neighbors of the current node
        foreach x ∈ N(v) {
            
            // 4. Only touch undiscovered nodes
            if (x->state == initial) {
                x->parent = v;           // Parent is safely assigned here
                x->state = active;       // Immediately mark as active
                x->bfsNum = bfsCount++;
                Q.enqueue(x);            // Enqueue exactly once
            }
        }
        
        // 5. Mark the current node as completely finished
        v->state = finished;
        v->finNum = finCount++;
    }
```