# 06. 컴퓨터비전에서 쓴 파이썬

> 컴퓨터비전 수업에서 OpenCV, scikit-image 실습을 파이썬으로 진행했습니다. (C++ 실습은 이 레포에 포함하지 않았습니다)

| 파일 | 내용 |
|---|---|
| `0320_opencv_gray_resize.py` | 이미지를 읽고(파일이 없으면 안전하게 종료), dtype과 shape 확인 → 흑백 변환 → 50% 축소 → 텍스트 삽입 |
| `4-6_skimage_segmentation.py` | SLIC 슈퍼픽셀 + RAG + Normalized Cut으로 영역 분할, 걸린 시간 측정 |
| `city.jpg` | 0320 실습용 이미지 |

수업 필기에서 정리한 개념:

- **에지 검출**: 윤곽선을 찾는 것. **영역 분할**: 중심 픽셀 근처에서 비슷한 픽셀을 찾아 묶는 것
- **비최대 억제(NMS)**: 지역적으로 가장 큰 값만 남기고 나머지를 제거
- 학습은 정답과 예측 사이의 오차가 줄어드는 방향으로 값을 바꾸는 것 (미분 정의 복습)
- 새 패키지 설치: Anaconda Prompt → `conda activate vision_ai` → `pip install tensorflow`

```bash
pip install opencv-python scikit-image
python 06_computer_vision/0320_opencv_gray_resize.py   # 이 폴더에서 실행 (city.jpg 경로)
```
