첫셀은 소리파형의 envelope 만드는 셀입니다.<br>
Eenvelope()로 찍어내고 예시)piano.result(변수)에 변수 넣어서 envelope 반환해 줍니다.<br>
변수는 순서대로 fs, attack time, decay time, sustain time, release time, slevel 입니다. fs는 샘플링 주파수이고
<br>![캡처](https://user-images.githubusercontent.com/74674780/127775246-459f89f8-3cb6-4278-a1fd-81a992082efb.PNG)<br>
위의 그래프를 예시로 보자면 (fs, 0.01, 0.2, 0.4, 3, 0.5) 입니다. (slevel은 sustain이 유지되는 값 입니다)<br>

*****
<br>2번째 셀부터 이미지를 사운드로 바꾸는 알고리즘 입니다.<br>

![1414](https://user-images.githubusercontent.com/74674780/127775832-02f1af86-767c-430b-99ed-81446e0c02f7.PNG)  
first_f0 = 전체사진에서 sec,third,four_f0는 2,3,4 영역에서 추출합니다  
우선 전체사진에서 rgb --> hsv 후 v의 히스토그램은 옥타브, s의 히스토그램은 그 옥타브의 12건반 중 하나를 선택합니다.  
그렇게 first_f0를 구한 후 2영역의 s의 히스토그램으로부터 그 first_f0건반부터 위로 13개의 건반 중 하나를 선택합니다.(=sec_f0)  
2영역의 h(앞으로 언급없으면 히스토그램)는 2개의 주법 중 하나를 선택하고 v는 메이저와 마이너코드 중 하나를 선택하는 변수입니다.    
<br>third_f0는 first_f0건반부터 쌓은 13개의 건반에서 sec_f0를 제외한 12개 중에 하나를 선택합니다. 3영역의 s가 그 변수입니다.  
3영역의 h와 v는 2영역 처럼 주법과 코드를 선택하는 변수입니다.  
<br>four_f0는 5도권으로 알아서 선택되며 4영역의 v를 통해 상행 5도인지, 하행 5도인지를 선택합니다.  
4영역의 h는 똑같이 주법을 선택하는 변수입니다. (4영역의 코드는 major로 마무리하였습니다.)  
******  
envelope의 release를 3s로 했다면 소리는 0s에서 first_f0를 발생시키고 그 소리는 3s에서 끝납니다.  
소리 발생을 시간으로 보자면  
0s~3s: first_f0  <br>

0.5s ~ 3.5s: sec_f0(chordtone1)  
1.5s ~ 4.5s: sec_f0(chordtone2)  
주법에 따라  
0.5s ~ 3.5s: sec_f0(아르페지오)  
1s ~ 4s: sec_f0(아르페지오)  
1.5s ~ 4.5s: sec_f0(아르페지오) #아르페지오는 이렇게 3번의 소리가 발생합니다
<br>
0.5s ~ 3.5s: sec_f0(원파이브) #원파이브는 한번의 소리가 발생합니다  
<br>
2.5s ~ 5.5s: third_f0(chordtone1)  
3.5s ~ 6.5s: third_f0(chordtone2)  +주법에따라  
<br>
4.5s ~ 7.5s: four_f0(chordtone1)  
5.5s ~ 8.5s: four_f0(chordtone2)  +주법에 따라  
<br>first_f0 0s발생 후 0.5s부터 sec_f0가 들어왔는데 조절할 수 있는 변수입니다.  
final_time = 8.5 과 sta_time = 0.5을 조절하면 됩니다.  
<br>chordtone1,2는 같은 chordtone을 1s의 간격으로 2번누른 것 입니다.  
모든 소리파형은 삼각파를 사용했습니다.  
*****
현재 최종으로 나오는 sound에 대한 판단은 사진이 어두울수록 낮은 옥타브에서 시작할 것이고  
2,3,4 각 영역에서 어둡다면 minor(우울한) 밝다면 major(활기찬) 코드톤을  
색깔에 대해서는 (빨강, 노랑, 초록, 하늘)이 주를 이룬다면 아르페지오 주법을  
(파랑, 보라, 자주, 빨강)이 주를 이룬다면 원파이브 주법을  
채도에 대해서는 채도가 높을 수록 더 높은 주파수의 건반을 근음으로하는 코드톤을 들려줄 것 입니다.  
외곽에서 부터 영역을 좁혔기에 판단의 범위는 외곽에서 부터 중앙으로 생각할 수 있습니다.  
