첫셀은 소리파형의 envelope 만드는 셀입니다.<br>
Eenvelope()로 찍어내고 예시)piano.result(변수)에 변수 넣어서 envelope 반환해 줍니다.<br>
변수는 순서대로 fs, attack time, decay time, sustain time, release time, slevel 입니다. fs는 샘플링 주파수이고
<br>![캡처](https://user-images.githubusercontent.com/74674780/127775246-459f89f8-3cb6-4278-a1fd-81a992082efb.PNG)<br>
위의 그래프를 예시로 보자면 (fs, 0.01, 0.2, 0.4, 3, 0.5) 입니다. (slevel은 sustain이 유지되는 값 입니다)<br>
<hr/><br>
2번째 셀부터 이미지를 사운드로 바꾸는 알고리즘 입니다.
![산11](https://user-images.githubusercontent.com/74674780/127775788-1378bcb0-8bf8-43f7-b150-0662434c7812.png)

