import sys
from typing import Dict, Literal
input = sys.stdin.readline

# 1. 프로세스 클래스 생성
class Processor:
    # 1-1. initialize 함수 생성
    def __init__(self, N):
        self.N = N
        # 1-1-1. 전화번호 딕셔너리 생성
        self.call_numbers:Dict[str, bool] = self._get_call_numbers()

    # 1-2. 전화번호 딕셔너리 생성 함수 정의
    def _get_call_numbers(self) -> Dict[str, bool]:
        call_numbers = dict()

        # 1-2-1.
        for _ in range(self.N):
            # 전화번호 입력 및 딕셔너리 내 추가
            call_numbers[input().strip()] = True

        return call_numbers

    # 1-3. 일관성 체크 함수 정의
    def _validate(self, call_number:str) -> bool:
        # 1-3-1. 비교 문자열 초기화
        target = ""
        # 1-3-2.
        for idx, char in enumerate(call_number):
            if idx != len(call_number) -1 :
                # 비교 문자열 업데이트
                target += char
                # 비교 문자열로 구성된 전화번호가 딕셔너리에 있는 경우 False 반환
                if target in self.call_numbers:
                    return False
        # 1-3-3. 일관성이 유지되므로 True 반환
        return True

    # 1-4. 실행 함수 정의
    def execute(self) -> Literal["YES", "NO"]:
        # 1-4-1. 전화 번호 리스트 생성
        call_number_list = self.call_numbers.keys()
        # 1-4-2.
        for call_number in call_number_list:
            # 해당 전화번호를 대상으로 일관성이 깨진 경우 NO 반환
            if not self._validate(call_number):
                return "NO"
        # 1-4-3. 일관성이 있는 목록이므로 YES 반환
        return "YES"

T = int(input())
# 2.
for _ in range(T):
    N = int(input())
    # 2-1. 프로세스 실행
    print(Processor(N).execute())