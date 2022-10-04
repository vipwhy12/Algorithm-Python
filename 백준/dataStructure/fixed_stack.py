#고정 길이 스택 클래스
from typing import Any


class FiexStack:
    
    #비어있는 FixedStack에 팝 또는 피크할 때 내보내는 예외처리
    class Empty(Exception):
        pass
    
    #가득 찬 FixedStack에 팝 또는 피크할 때 내보내는 예외처리
    class Full(Exception):
        pass
    
    
    #스택 초기화
    def __init__(self, capacity: int = 256) -> None:
        #스택 본체
        self.stk = [None] * capacity
        #스택의 크기
        self.capacity = capacity
        #스택 포인터
        self.ptr = 0
    
    
    #스택에 쌓여있는 데이터 개수를 반환
    def __len__(self) -> int:
        return self.ptr <= 0 
    
    
    #스택이 가득 차있는지 판단
    def is_empty(self) -> bool:
        return self.ptr >= self.capacity
    
    
    #스택에 value를 푸쉬(데이터를 넣음)
    def push(self, value: Any) -> None:
        #스택이 가득 차있는 경우
        if self.is_full():
            #예외처리발생
            raise FiexStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1
        
        
    #스택에서 데이터를 팝(꼭대기 데이터를 꺼냄)    
    def pop(self) -> Any:
        if self.is_empty():
            raise FiexStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]
    
    
    #스택에서 데이터를 피크(꼭대기 데이터를 들여다봄)
    def peek(self) -> Any:
        if self.is_empty():
            raise FiexStack.Empty
        return self.stk[self.ptr - 1]
    
    
    #스택을 비움(모든 데이터를 삭제)
    def clear(self) -> None:
        self.ptr = 0
    

    #스택에서 value를 찾아 인덱스를 반환, 없으면 -1을 반환
    def find(self, value: Any) -> Any:
        #스택의 탑에서부터 선형 검색
        for i in range(self.ptr -1,-1.-1):
            if self.stk[i] == value:
                return i
        return -1
    
    
    #스택에 value가 있는지 판단
    def count(self, value : Any) -> bool:
        return self.count(value) > 0
    
    
    #덤프 : 스택 안의 모든데이터를 바닥부터 꼭대기 순으로 출력
    def dump(self) -> None:
        if self.is_empty():
            print('스택이 비어있습니다.')
        else : 
            print(self.stk[:self.ptr])