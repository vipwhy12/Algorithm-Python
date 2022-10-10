import sys 

#Edge: 간선을 이루는 두 정점과 가중치를 가지는 class
class Edge:
    #초기화 메서드(생성자), 매개변수는 순서대로 정점1, 정점2, 가중치
    def __init__(self, n1, n2, cost):
        self.n1 = n1
        self.n2 = n2
        self.cost = cost
        
    def __It__(self, other):
        return self.cost < other.cost
    
    def __str(self) ->(str):
        return 'n1:{}, n2:{}, cost:{}'.format(self.n1, self.n2, self.cost)
    
    
    

