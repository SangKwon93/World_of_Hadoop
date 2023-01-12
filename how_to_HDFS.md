## HDFS 동작하기
1) http://localhost:8080/ 접속하여 Ambari UI를 활용
2) 인터페이스 활용(마스터 노드 또는 클라이언트 노드에 로그인해 명령어를 사용해 HDFS 조작)

### 1) 웹사이트에서 직접 조작함
### 2) 인터페이스 활용

1) 인스턴스에 연결할 터미널에 접속하기
- 원도우 : PuTTY 활용 / Mac OS : 내장 터미널 활용
- 원도우 www.putty.org에서 putty.exe 파일 다운
- 접속해서 Connection type : SSH로
- Host Name(or IP address) : maria_dev@127.0.0.1 Port: 2222
- Open
- 터미널 작동! 

2) 데이터를 Hadoop에 복사(로컬 파일시스템(리눅스 호스트) -> HDFS로 데이터 업로드)
- HDFS를 리눅스 호스트의 명령줄로 조작하려면 ``hadoop fs -`` + 명령어
- ex) hadoop fs -ls : HDFS 내 데이터 리스트 확인
- ex) ls : maria_dev 홈 디렉토리 데이터 리스트 확인
- 로컬에 있는 데이터를 HDFS로 복사하는 방법
    - hadoop fs -copyFromLocal {데이터 이름} {위치}
    - ex) ``hadoop fs -copyFromLocal u.data ml-l00k/u.data``
- 제거 방법
    - ``hadoop fs -rm ml-100k/u.data`` 
