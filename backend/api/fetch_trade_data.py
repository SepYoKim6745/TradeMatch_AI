import requests
import json

# 산업통상자원부_거래업체정보서비스 API 키
API_KEY = "9Ea5pzS6BpObO94XPLPn3Xe1dJdCRIf6q2tpX3cBXlo9dusEs4LeDFSdgr%2FguQRlAO0jrF1trwrLEEj%2BpbTJkA%3D%3D"

# 산업통상자원부_거래업체정보서비스 API URL (엔드 포인트)
API_URL = "https://apis.data.go.kr/1450000/infoSrvcGuidanceService"

# 요청 파라미터 설정
params = {
    "serviceKey": API_KEY,
    "year": "2023",
    # 실제 API 파라미터에 맞게 수정 필요
    "exportItem": "전자부품",
    "page": 1,
    "perPage": 10
}

response = requests.get(API_URL, params=params)

try:
    data = response.json()
    print(json.dumps(data, ensure_ascii=False, indent=2))
    # 샘플 데이터 저장
    with open("../../data/sample_input.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("샘플 데이터를 data/sample_input.json에 저장했습니다.")
except Exception as e:
    print("API 응답 파싱 오류:", e)
