class heap:
    def __init__(self) -> None:
        self.heap = []
        
    def get_right_child(self, idx):
        if 2 * idx + 2 >= len(self.heap):
            raise None
        
        return 2 * idx + 2
    
    def get_left_child(self, idx):
        if 2 * idx + 1 >= len(self.heap):
            raise None
                
        return 2 * idx + 1
    
    def get_parent(self, idx):
        if idx == 0:
            raise None
        
        return (idx - 1 ) // 2
    
    def heap_up(self, idx):
        
        parent_idx = self.get_parent(idx)
        while idx and self.heap[self.get_parent(idx)] > self.heap[idx]:
            self.heap[self.get_parent(idx)], self.heap[idx] = self.heap[idx], self.heap[self.get_parent(idx)]
            idx = self.get_parent(idx)
            
    def heap_down(self, idx):
        
        while self.get_left_child(idx) < len(self.heap):
            left_child = self.get_left_child(idx)
            right_child = self.get_right_child(idx) if self.get_right_child(idx) < len(self.heap) else idx           
            min_child = min(left_child, right_child, key=lambda a: self.heap[a])
            
            if self.heap[idx] <= self.heap[min_child]:
                break
            
            self.heap[idx], self.heap[min_child] = self.heap[min_child], self.heap[idx]
            idx = min_child
            
    
        

    
    