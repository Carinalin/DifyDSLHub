from fastapi import FastAPI, Request, HTTPException
import random

app = FastAPI()

@app.post('/fortune')
async def get_fortune(request: Request):
    auth_header = request.headers.get('Authorization')
    if auth_header != 'Bearer carina':
        raise HTTPException(status_code=403, detail="Invalid Authorization header")
    request_data = await request.json()
    username = request_data.get('username', None)
    if username is None:
        return {
            'status': 'error',
            'errorInfo': 'No username provided',
            'data': None
        }

    # 运势或励志名言列表
    fortunes = [
        "踏上新的冒险之旅，将收获意想不到的友谊。",
        "在今日的小胜利中找到力量，迈向更大的成功。",
        "发现隐藏的天赋，点燃快乐与创造力。",
        "拥抱变化，它将指引你走向新的机遇。",
        "光芒四射，用你的善良与决心激励他人。"
    ]
    # 随机选择运势和语气
    selected_fortune = random.choice(fortunes)
    tone = random.choice(['神秘的', '振奋人心的', '命中注定的'])
    
    # 返回对LLM友好的字符串格式响应
    return f"{username}，星辰为你指引{tone}道路：你将{selected_fortune}"

import uvicorn

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8082)