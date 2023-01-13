## [Sandbox HDP 2.6.5] Hadoop으로 관계형 데이터 저장소 사용하기 명령어
#### MySQL과 Hadoop 통합하기 
    mysql -u root -p
</br>    
    오류 발생 시</br>

    su root
    systemctl stop mysqld
    systemctl set-environment MYSQLD_OPTS='--skip-grant-tables --skip-networking'
    systemctl start mysqld
    mysql -uroot
</br>
    mysql shell 에서 작성</br>

    FLUSH PRIVILEGES;
    ALTER USER 'root'@'localhost' IDENTIFIED BY 'hadoop';
    FLUSH PRIVILEGES;
    QUIT;

</br> 
    터미널 창에서 작성 </br>

    systemctl unset-environment MYSQLD_OPTS
    systemctl restart mysqld
    exit

<br> 
    터미널 창에서 MySQL 접속하기</br>

    mysql -uroot -phadoop
    password : hadoop

==>  **최초 세팅 후 mysql -u root -p로 접속** 

===================여기서 부터 mysql창에서=====================
#### 파일 내에 정보 확인
    less movielens.sql;


#### movielens databases 저장해둔 코드 불러오기 (여기는 mysql 창 x)
    wget http://media.sundog-soft.com/hadoop/movielens.sql

#### 데이터 UTF-8양식으로 셋팅하기
    SET NAMES 'utf8';
    SET CHARACTER SET utf8;

#### movielens db 활용하기
    use movieLens;

#### 스크립트를 활용해 데이터 불러오기
    source movielens.sql;


## Sqoop을 사용하여 MySQL에서 있는 데이터를 가상 클러스터 HFDS/Hive로 데이터 불러오기(가져오기)

</br>

#### 로컬 호스트의 movielens 데이터베이스에 접근할 떄 필요한 모든 권한 부여하기
    GRANT ALL PRIVILEGES ON movieLens. * to ''@'localhost' indentified by 'hadoop';
    >quit (mysql 서버 종료)
#### HDFS에 데이터 저장하기(sqoop 활용)
    sqoop import --connect jdbc:mysql://localhost/movielens --driver com.mysql.jdbc.Driver --table movies -m 1

    {sqoop import} - HDFS로 import

    {--connect jdbc:mysql://localhost/movielens} - JDBC를 통해 로컬 호스트의 MySQL 데이터베이스에 있는 'movielens'에 접속

    {--driver com.mysql.jdbc.Driver} - 데이터베이스와 소통할 때 사용할 드라이버 명시

    {--table movies} - movies 테이블에서만 데이터를 가져온다.

    {-m 1} - 을 마지막으로 입력해 하나의 매퍼만 사용(HDP에서는 하나의 호스트만 있기에 그 이상으로 매퍼 만드는 것은 의미없어서 1개만 생성) 

</br>

## Sqoop을 사용하여 Hadoop에서 MySQL로 데이터 내보내기

</br>

#### 데이터를 MySQL 데이터베이스에서 (sqoop이 파일을 만들지 않고) Hive 바로 데이터 넣기
    sqoop import --connect jdbc:mysql://localhost/movielens --driver com.mysql.jdbc.Driver --table movies -m 1 --hive-import 

    + --hive-import 만 붙여주면 된다.

</br>

#### 참고) 터미널은 마스터 노드 or 클라이언트 노드에 로그인해 명령어를 사용해 HDFS 파일 시스템 조작! 
--> 그러기 위해서는 ``인스턴스에 연결할 터미널``이 필요하다.
--> 로컬 머신에서 SSH세선을 열어 실행중인 이 가상머신과 연결한다.
    putty.exe 열어서 maria_dev@127.0.0.1 port : 2222로 접속
-> HDFS를 명령어로 조작하려면 hadoop fs -
-> Sqoop를 조작하려면 sqoop ~ 