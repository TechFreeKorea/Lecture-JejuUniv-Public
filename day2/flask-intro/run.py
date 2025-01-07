from flask import Flask

# Flask 애플리케이션 생성
app = Flask(__name__)

# 기본 라우트 설정
@app.route("/")
def home():
    return "<h1>안녕하세요! Flask 기본 서버입니다. 🌟</h1><p>여기에서 새로운 프로젝트를 시작해 보세요!</p>"

# 추가 라우트 예제
@app.route("/about")
def about():
    return "<h1>Flask 소개</h1><p>이 서버는 Flask 프레임워크를 사용하여 만들어졌습니다. 🚀</p>"

# 서버 실행
if __name__ == "__main__":
    print("서버를 시작합니다... http://127.0.0.1:5000 에서 확인하세요!")
    app.run(debug=True)
