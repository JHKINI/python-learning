import cv2
import sys

# 1. 사진 읽어오기 (예외 처리 포함)
img_path = 'city.jpg' # 본인의 사진 파일명으로 바꾸세요!
src = cv2.imread(img_path)

if src is None:
    print("이미지를 불러올 수 없습니다. 파일 경로를 확인하세요.")
    sys.exit() # 프로그램 안전하게 종료

# 2. 데이터 타입 및 배열 형태(가로, 세로, 채널) 출력
print(f"데이터 타입: {src.dtype}")
print(f"이미지 형태 (세로, 가로, 채널): {src.shape}")

# 3. 원본 컬러 영상을 명암(Gray) 영상으로 변환
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 4. 변환된 영상을 가로세로 50% 비율로 축소
# dsize=(0, 0)으로 두고 fx, fy를 0.5로 설정하면 반으로 줄어듭니다.
dst = cv2.resize(gray, dsize=(0, 0), fx=0.5, fy=0.5)



# 날짜 삽입: cv2.putText(이미지, 내용, 위치, 폰트, 크기, 색상, 두께)
text = "2036.03.20"
cv2.putText(dst, text, (20, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.8, 255, 2)

# 6. 최종 결과 영상 화면 표시
cv2.imshow('Final Result', dst)

# 아무 키나 누르면 창이 닫히도록 설정
cv2.waitKey(0)
cv2.destroyAllWindows()