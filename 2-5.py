#https://wikidocs.net/2843

#월, 화, 수 3일연속 하한가.
#-30% -30% -30%


#월요일 100에서 -30%한 가격 a를 출력
#화요일 a에서 -30%한 가격 b를 출력
#수요일 b에서 -30%한 가격 c를 출력

naver = 1000000


for i in range(1,4):
    naver = naver - (naver*0.3)
    
    print(naver)
    
