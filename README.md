### umabot 업데이트 적용사항
- 나중에 따로 정리
  
### umabot 업데이트 예정사항

#### 스킬
- condition 부분 정보 획득해서 변경해야 함
- ability type 정보 획득해서 변경해야 함

### 캐릭터
- 캐릭터 정보 받아오는 쿼리 필요
- 해당 정보에 따른 아이콘 구성 필요
- 1차 결과 캐러셀, 2차 결과 Detail
- 캐릭터 별 기본 표시 항목
  - 이름, 사진
  - 기본스탯
  - 기본적성
  - 기본스킬
  - 이벤트스킬
  - 캐릭터별 이벤트 리스트 및 목록 결과
  - 그런데, output이 여러개로 구성 가능한 것 같은데.. 그렇게 해야 할 듯

### 서포트 카드
- 카드 정보 쿼리 필요
- 1차 결과 캐러셀, 2차 결과 Detail
- 공통 표시 항목
  - 카드명, 아이콘
    - 등급, 유형 필요없음 아이콘에 다 있음
- 1차 표시 항목
  - 고유 보너스
  - 퀵메뉴 구성
    - 효과
    - 트레이닝 상승치
    - 스킬
    - 이벤트
- 2차 표시 항목
  - 위와 같이 이미 4개로 구분되었음
  - 캐러셀이 아닌 그냥 itemList로 표시
  - 효과, 트레이닝 상승치는 보여주는 것에서 종료
  - 스킬은 itemList 표시, 클릭 시 스킬 이동
  - 이벤트는 itemList 표시, 클릭 시 이벤트 이동

### 마장
- 키워드는 마장, 경기장
- 마장 별 사진 및 기타 정보 표시

### 이벤트
- 이벤트 키워드 검색 후 검색 결과 나타내는 형태
- 캐릭터, 서폿카, 시나리오 모든 이벤트에 적용해야 함
- 1차 결과 캐러셀, 2차 결과 Detail
- 기본 표시 항목
  - 이벤트 내용
  - 선택지 및 결과
  - 해당 조건 포함된 캐릭터 및 서포트 리스트
  - 캐릭터 누르면 해당 캐릭터, 서포트 누르면 해당 서포트로 이동

#### 링크
- 유용한 링크 모음 정보 구성 필요

#### 공통 적용 사항
- 이전으로 가기, 처음으로 가기 구성이 있어야 함
- 퀵메뉴 클릭에 따라 데이터를 전달해서 이전 값이 무엇인지를 가지고 있어야 함