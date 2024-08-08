
# 홈 페이지
@app.route('/')
def index():
    return render_template('index.html')

# 검색 요청 처리
@app.route('/search', methods=['POST'])