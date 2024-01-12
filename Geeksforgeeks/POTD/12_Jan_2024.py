# method2

    def modifyQueue(self, q, k):
        # Create a temporary queue to store the first k elements
        temp_queue = Queue()
        
        # Dequeue the first k elements from the main queue and enqueue them into the temporary queue
        for _ in range(k):
            temp_queue.put(q.get())
        
        # Reverse the first k elements using a list
        reversed_elements = list(temp_queue.queue)[::-1]
        
        # Enqueue the reversed elements back into the main queue
        for element in reversed_elements:
            q.put(element)
        
        # Enqueue the remaining elements back into the main queue
        for _ in range(q.qsize() - k):
            q.put(q.get())
        
        # Convert the queue to a list for returning
        modified_queue = list(q.queue)
        
        return modified_queue