from flask import Flask, render_template, request, jsonify
import main

# 赞助链接：https://img.picui.cn/free/2024/06/29/667fd377e13fe.png
# 赞助链接：https://img.picui.cn/free/2024/06/29/667fd377e13fe.png
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_invite', methods=['POST'])
def start_invite():
    data = request.get_json()
    invite_code = data.get('invite_code')
    output = []
    async def async_main(invite_code, output):
        try:
            output.append(f"Processing invite code: {invite_code}")
            # Simulate long-running task
            output.append("作者：1930520970")
            output.append("赞赏链接：https://img.picui.cn/free/2024/06/29/667fd377e13fe.png")
            output.append('代理IP：' + main.main())   #调用main里面的main函数并返回值
            output.append("Invite process completed.")

        except Exception as e:
            output.append('请重新运行')
            output.append(f"Error occurred: {str(e)}\n赞赏链接：https://img.picui.cn/free/2024/06/29/667fd377e13fe.png")
    return jsonify({'output': output})


@app.route('/get_free_node', methods=['GET'])
def get_free_node():
    print('正在获取免费节点')
    # 获取免费节点的逻辑
    output = []
    output.append('抱歉，此项目暂时关闭')
    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=12345)