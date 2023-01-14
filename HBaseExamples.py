# starbase - HBase의 REST 클라이언트를 가진 python 래퍼 패키지 활용!
from starbase import Connection

# 연결
c=Connection('127.0.0.1','8000')

# ratings 테이블 만들기
ratings=c.table('ratings')

if ratings.exists():
    print('기존 평점 테이블 삭제 \n')
    ratings.drop()

# ratings 테이블 안에 rating 열 패밀리 생성
ratings.create('rating')

print("ml-100k 등급 데이터를 분석하면...... \n")

# PC 내 파일 절대주소로 불러오기
ratingFile=open('C:/Users/apfhd/ml-100k/u.data',"r")

# ratings 테이블에 batch 객체 생성
batch=ratings.batch()

for line in ratingFile:
    (userID, movieID, rating, timestamp) = line.split()
    batch.update(userID, {"rating":{movieID:rating}})

ratingFile.close()

# batch를 서비스에 commit해서 HBase에 실제로 작성되고 이 시점부터 데이터를 쿼리 가능!

print("REST 서비스를 통해 HBase에 등급 데이터 제공 \n")
batch.commit(finalize=True)

# 1번 사용자의 모든 평점 보기
print("유저 아이디 1인 사람 평점: \n")
print(ratings.fetch("1"))

# python HBaseExamples.py로 실행하면 유저 아이디 1,33인 사람에 movieID가 기록된다.