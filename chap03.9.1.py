#데이터 프레임 합치기
#pandas 에서 데이터프레임을 합치는 함수에는
#concat(), merge(), join() 이 있다.

import pandas as pd

df1=pd.DataFrame({
    "A" : ["A0", "A1", "A2", "A3"],
    "B" : ["B0", "B1", "B2", "B3"],
    "C" : ["C0", "C1", "C2", "C3"],
    "D" : ["D0", "D1", "D2", "D3"]
    },
                 index=[0, 1, 2, 3],
                 )

df2=pd.DataFrame({
    "A" : ["A4", "A5", "A6", "A7"],
    "B" : ["B4", "B5", "B6", "B7"],
    "C" : ["C4", "C5", "C6", "C7"],
    "D" : ["D4", "D5", "D6", "D7"]
    },
                 index=[4, 5, 6, 7],
                 )

df3=pd.DataFrame({
    "A" : ["A8", "A9", "A10", "A11"],
    "B" : ["B8", "B9", "B10", "B11"],
    "C" : ["C8", "C9", "C10", "C11"],
    "D" : ["D8", "D9", "D10", "D11"]
    },
                 index=[8, 9, 10, 11],
                 )

#열 이름이 같은 경우
result=pd.concat([df1, df2, df3])

print(result)
print()
print()


df4=pd.DataFrame({
    "B" : ["B2", "B3", "B6", "B7"],
    "D" : ["D2", "D3", "D6", "D7"],
    "F" : ["F2", "F3", "F6", "F7"]
    },
                 index=[2, 3, 6, 7],
                 )

#열 이름이 다른 경우
result=pd.concat([df1, df4])

print(result)
print()
print()

#행 인덱스를 초기화하고 싶은 경우
#ignore_index=True 를 입력

result=pd.concat([df1, df4], ignore_index=True)

print(result)
print()
print()


#행이 아닌 열 기준으로 데이터를 합치는 경우
#axis=1 인자를 입력하면 열방향으로 데이터가 합쳐짐

result=pd.concat([df1, df4], axis=1)

print(result)
print()
print()


#합집합이 아닌 교집합을 기준으로 사용하고 싶을 경우
#"join = inner" 인자를 추가로 입력한다.

result=pd.concat([df1, df4], axis=1, join="inner")

print(result)
print()
print()


#데이터프레임에 시리즈를 합치는 경우

s1=pd.Series(["X0", "X1", "X2", "X3"], name="X")
result=pd.concat([df1, s1], axis=1)

print(result)
print()
print()
