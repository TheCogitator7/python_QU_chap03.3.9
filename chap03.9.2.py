#merge() 함수
#merge() 함수는 기준이 되는 열이나 인덱스, 즉 키(key)를 기준으로 두 데이터 프레임을 합친다.
#데이터프레임을 병합하는 방법은 inner join, left join, right join, outer join으로 구분된다.

#inner join : pd.merge(left, right, on="inner") (on="inner" 는 생략가능)
#left join : pd.merge(left, right, on="left")
#right join : pd.merge(left, right, on="right")
#outer join : pd.merge(left, right, on="outer")

import pandas as pd

left=pd.DataFrame({
    "key" : ["K0", "K1", "K2", "K3"],
    "A" : ["A0", "A1", "A2", "A3"],
    "B" : ["B0", "B1", "B2", "B3"]
    })

right=pd.DataFrame({
    "key" : ["K0", "K1", "K3", "K4"],
    "C" : ["C0", "C1", "C3", "C4"],
    "D" : ["D0", "D1", "D3", "D4"]
    })

#inner join 은 양쪽 데이터프레임에서 기준이 되는 열의 데이터가
#모두 있는 교집합 부분만 반환한다.

result=pd.merge(left, right, on="key") #기준이 되는 열을 on 뒤에 입력한다.

#merge() 함수는 기본적으로 inner join 으로 데이터를 합친다.

print(result)
print()
print()


#left join 은 왼쪽 데이터프레임은 유지되며,
#오른쪽 데이터프레임이 키를 기준으로 합쳐진다.

result=pd.merge(left, right, on="key", how='left')

print(result)
print()
print()

#right join은 오른쪽 데이터프레임은 유지되며
#왼쪽 데이터프레임이 키를 기준으로 합쳐진다.

result=pd.merge(left, right, on="key", how="right")

print(result)
print()
print()

#outer join 은 데이터프레임 중 어느 한쪽에만 속하더라도
#상관없이 합집합 부분을 반환한다.

result=pd.merge(left, right, on="key", how="outer")

print(result)
print()
print()



#기준이 되는 열의 이름이 서로 다른 경우는 left_on과 right_on을 통해 키를 직접 선언한다.
left=pd.DataFrame({
    "key_left" : ["K0", "K1", "K2", "K3"],
    "A" : ["A0", "A1", "A2", "A3"],
    "B" : ["B0", "B1", "B2", "B3"]
    })

right=pd.DataFrame({
    "key_right" : ["K0", "K1", "K3", "K4"],
    "C" : ["C0", "C1", "C3", "C4"],
    "D" : ["D0", "D1", "D3", "D4"]
    })

result=pd.merge(left, right, left_on="key_left", right_on="key_right", how="inner")

print(result)
print()
print()


#merge(left, right)가 아닌 left.merge(right) 형태로 함수를 작성할 수도 있다.
#해당 방법으로 코드를 작성할 경우
#왼쪽 데이터프레임에 오른쪽 데이터프레임을 붙인다는 점이 더욱 직관적이다.

result=left.merge(right, left_on="key_left", right_on="key_right", how="inner")

print(result)


