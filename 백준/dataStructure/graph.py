from msilib.schema import Class


# 지하철 역 노드를 나타내는 클래스
Class StationNode:
    def __init__(self, name, num_exits):
        self.name = name
        self.exits = num_exits