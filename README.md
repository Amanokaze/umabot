## umabot 업데이트 적용사항
- 스킬 적용 완료
- 캐릭터 Main 적용 완료
- 캐릭터 Detail 적용 완료


## umabot 업데이트 예정사항

### 캐릭터
- 1차 결과 캐러셀, 2차 결과 Detail
- Detail - ListCard
  - 기본 능력치: 0/0/0/0/0 (3성 기준)
    - 링크 누르면 1,2,3,4,5성 능력치 SimpleText 출력
  - 고유기: 스킬로 바로 이동
    - card_rarity_data - skill_set / skill_set - skill_id1 Join
  - 초기 스킬: 아래 쿼리
    - card_data - available_skill_set_id / available_skill_set Table Join Need Rank = 0
  - 보유 스킬: 아래 쿼리
    - card_data - available_skill_set_id / available_skill_set Table Join Need Rank > 0
  - 이벤트: 버튼만 만들고 Action은 보류할 것
    - 이벤트쪽 다 만든 다음에 진행하는게 맞을 것
  - Bottom Button
    - 다른 캐릭터, 초기화면
- Detail List Click Result
  - 캐릭터 메인을 바텀버튼으로 바꾸고, 나머지는 QuickReply로 유지하는게 낫겠다..
  - Bottom Button
    - 캐릭터 메인
  - QuickReply
    - 다른 캐릭터, 초기화면
- Todo 
  - QuickReply 부분 Template 이동 함수 수정
  - message를 QuickReply의 Parameter가 아니라 Button Parameter로 수정

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

### 링크
- 유용한 링크 모음 정보 구성 필요