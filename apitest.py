import urllib.request
import json

API_URL = ""
API_KEY = ""
API_MODEL = ""

def set_config(url, key, model):
    global API_URL, API_KEY, API_MODEL
    API_URL = url
    API_KEY = key
    API_MODEL = model

def apitest(filenamee):
    prompt_for_ai = "你现在的作用是一个文件分类机器人，你需要根据文件名来分类不同学科的文件。你只能回答以下内容之一：语文、数学、英语、物理、历史、化学、生物、政治、地理、无法识别。以下是你需要辨别的文件名："+filenamee

    headers = {
        "Authorization": "Bearer " + API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "model": API_MODEL,
        "messages": [{"role": "user", "content": prompt_for_ai}]
    }

    json_data = json.dumps(data).encode('utf-8')

    req = urllib.request.Request(API_URL, data=json_data, headers=headers, method='POST')

    try:
        with urllib.request.urlopen(req) as response:
            response_data = response.read().decode('utf-8')
            result = json.loads(response_data)
            
            ai_response = result['choices'][0]['message']['content'].strip()
            print(ai_response)
            return ai_response
            
    except urllib.error.URLError as e:
        print(f"请求错误: {e}")
        return "无法识别"
    except KeyError as e:
        print(f"解析响应出错: {e}")
        print("原始响应:", response_data if 'response_data' in locals() else "无响应")
        return "无法识别"

def apiretry(witfile):
    prompt_for_ai = "你现在的作用是一个文件分类机器人，你需要根据内容来分类不同学科的文件。你只能回答以下内容之一：语文、数学、英语、物理、历史、化学、生物、政治、地理、无法识别。以下是你需要辨别的文件内容："+witfile

    headers = {
        "Authorization": "Bearer " + API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "model": API_MODEL,
        "messages": [{"role": "user", "content": prompt_for_ai}]
    }

    json_data = json.dumps(data).encode('utf-8')

    req = urllib.request.Request(API_URL, data=json_data, headers=headers, method='POST')

    try:
        with urllib.request.urlopen(req) as response:
            response_data = response.read().decode('utf-8')
            result = json.loads(response_data)
            
            ai_response = result['choices'][0]['message']['content'].strip()
            print(ai_response)
            return ai_response
            
    except urllib.error.URLError as e:
        print(f"请求错误: {e}")
        return "无法识别"
    except KeyError as e:
        print(f"解析响应出错: {e}")
        print("原始响应:", response_data if 'response_data' in locals() else "无响应")
        return "无法识别"
