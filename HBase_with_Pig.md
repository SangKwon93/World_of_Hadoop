## HBase를 Pig 와 함께 사용하여 대규모 데이터 가져오기
- 빅데이터일 경우
    - 로컬 파일 시스템을 읽는python 스크립트를 활용했던 ``hadoop_NoSQL.md``와 ``HBaseExamples.py`` => **``불가``**
    - ``Pig``는 **``가능``**
    (HDFS클러스터에서 정보를 뽑아내 HBase 테이블에 작성가능)

**``빅데이터의 경우 HBase 보다 Pig가 더 유용!!!``**

#### Pig 작동 방식
- Pig에서 HBase로 무언가를 작성하려면 ``HBase 테이블이 사전에 만들어 있어야함``
- 사전작업으로 HBase 셸에 가서 그 테이블을 먼저 구성하고 ``첫째 열에는 고유한 키를 가져``와야만 한다.
- 각 관계성은 고유한 키를 갖고 ``HBase 테이블에 저장할 열과 매핑할 열을
갖도록 한다.``

#### 예제 실습
1. HDFS에 파일이 있어 데이터를 Pig로 가져와서 HBase에 저장!
    [root]``hbase shell``
2. HBase 인스턴스 존재하는 테이블의 목록 확인
    [hbase(main):001:0>] ``list``
3. 열 패밀리를 포함하는 ``users`` , ``userinfo``만들기
    ``create 'users','userinfo'``
4. HBase shell 종료
    ``exit``
5. 스크립트 다운
    [root]``wget http://media.sundog-soft.com/hadoop/hbase.pig``
6. 다운받은 파일 내용 확인하기
    [root]``less hbase.pig``
    - 직전에 HDFS로 업로드한 'user/maria_dev/ml-100k/u.user' 파일을 가져와 ``ratings``라는 관계성을 만듬.
    => 순서대로 필요한 정보를 추출한 관계성이 생겼으니 HBase 테이블에 매핑 가능!
7. 실행
    [root]``pig hbase.pig``
    - MapReduce부터 작업을 분산하는 등의 필요한 작업 진행
8. hbase shell 접속
    [root]``hbase shell``
9. 'user' 데이터 보기
    [hbase(main):001:0>] ``scan 'users'``
10. 비활성화
    [hbase(main):001:0>]``disable 'users'``
11. 삭제 
    [hbase(main):001:0>]``drop 'user'``
12. HBase shell 종료
    [hbase(main):001:0>]``exit``



 