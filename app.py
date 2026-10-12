from flask import Flask, jsonify, request

app = Flask(__name__) # __name__代表目前執行的模組

@app.route('/') # 函式的裝飾 (decorator) 以函示為基礎，提供附加的功能， 例如用來定義路由
def index():
    return jsonify({"message": "Hello, World!"})

if __name__ == '__main__': # 如果以主程式執行此模組，則啟動 Flask 應用程式
    # app.run(debug=True) # 立刻啟動伺服器
    # 讀取 Render 分配的 Port，預設為 10000
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)