#join() 메서드
#join() 메서드는 merge() 메서드와 비슷하지만
#join() 메서드는 두 데이터 프레임의 행 인덱스를 기준으로 데이터를 결합한다.

import pandas as pd

left=pd.DataFrame({
    "A" : ["A0", "A1", "A2", "A3"],
    "B" : ["B0", "B1", "B2", "B3"]},
                  index=["K0", "K1", "K2", "K3"]
                  )

right=pd.DataFrame({
    "C" : ["C0", "C1", "C3", "C4"],
    "D" : ["D0", "D1", "D3", "D4"]},
                   index=["K0", "K1", "K3", "K4"]
                   )

#join() 메소드는 left join 방법을 사용한다.
#merge() 함수는 키를 기준으로 결합을,
#join() 메서드는 행 인덱스를 기준으로 결합을 한다는 점을 제외하고 거의 비슷하다.
result=left.join(right)

print(result)
