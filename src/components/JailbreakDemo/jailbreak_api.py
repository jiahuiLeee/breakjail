from openai import OpenAI
from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage
import requests
import json
from llamaapi import LlamaAPI
from zhipuai import ZhipuAI

# gpt_key = "sk-OXjzOIjK8vpZgpneWFVkAIg5CHVAUUbaJBFTrHPJETiiAvAQ"
# gpt_key = "sk-fC5uw6U7Km0yIdIjCgeuZFIYQeWdzwY1877vSFCAVW0xfWXz"
gpt_key = "sk-OXjzOIjK8vpZgpneWFVkAIg5CHVAUUbaJBFTrHPJETiiAvAQ"
gpt2_key = "SheugeI9qRquUWNNR63h7hz9Uz6ekG2j"
# sk-IkyMvUBTTltHa40zxmdolJxZzrMV5vpYhIes0Lt9s9TacsPM
llama_key = "LL-HVHBH57ewaOJRaEXBwUkNrpDpp2PO1HzpDV2K7XKCZqMCQbTYzNNHKnrcJ1gl0fZ"

baichuan_key = "sk-0a98492026ba0c2c50e2b06415f978e2"

zhipu_key = "7e658af90a28f32a946f1dd9eff061a9.bvnyezwKyxJ77VIQ"

#星火认知大模型调用秘钥信息，请前往讯飞开放平台控制台（https://console.xfyun.cn/services/bm35）查看
SPARKAI_APP_ID = 'f84624ca'
SPARKAI_API_SECRET = 'OWQwNTY2MTVhZTI3NGZhMDZhZmQyYjY2'
SPARKAI_API_KEY = '53f46273ec832b624ecc58cd40d2750f'

BAIDU_APPID = '76243299'
BAIDU_API_KEY = 'K89VisNv3C2DF9hEzAKrG1uH'
BAIDU_SECRET_KEY = '3lfawTP42uNcJERtNN0wqHhnzaX7M7Qw'


# 非流式响应
def gpt_35_api(prompt : str):
    """为提供的对话消息创建新的回答
    Args:
        messages (list): 完整的对话消息
    """
    client = OpenAI(
        # defaults to os.environ.get("OPENAI_API_KEY")
        api_key=gpt_key,  # https://github.com/chatanywhere/GPT_API_free 申请一个免费的api key
        base_url="https://api.chatanywhere.tech/v1"
    )
    message = [{'role': 'user', 'content': prompt}]
    completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=message)
    # print(completion.choices[0].message.content)
    return completion.choices[0].message.content

def gpt_4_api(prompt : str):
    """为提供的对话消息创建新的回答
    Args:
        messages (list): 完整的对话消息
    """
    client = OpenAI(
        # defaults to os.environ.get("OPENAI_API_KEY")
        api_key=gpt_key,  # https://github.com/chatanywhere/GPT_API_free 申请一个免费的api key
        base_url="https://api.chatanywhere.tech/v1"
    )
    messages = [{'role': 'user', 'content': prompt}]
    completion = client.chat.completions.create(model="gpt-4", messages=messages)
    # print(completion.choices[0].message.content)
    return completion.choices[0].message.content


def llama_api(prompt):
    client = OpenAI(
        api_key = llama_key,
        base_url = "https://api.llama-api.com"
        )
    response = client.chat.completions.create(
        model="llama-13b-chat",
        messages=[
            {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def baichuan2(prompt):
    url = "https://api.baichuan-ai.com/v1/chat/completions"
    api_key = baichuan_key

    data = {
        "model": "Baichuan2-Turbo",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False
    }
    json_data = json.dumps(data)
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + api_key
    }

    response = requests.post(url, data=json_data, headers=headers, timeout=60, stream=True)

    if response.status_code == 200:
        data = json.loads(response.text)
        return data['choices'][0]['message']['content']
    else:
        return None

def chatglm3(prompt):
    client = ZhipuAI(api_key=zhipu_key) # 请填写您自己的APIKey
    response = client.chat.completions.create(
        model="glm-3-turbo",  # 填写需要调用的模型名称
        messages=[
                {"role": "user", "content": prompt},
            ],
            stream=False,
    )
    # print(response.choices[0].message.content)
    return response.choices[0].message.content

def chatglm4(prompt):
    client = ZhipuAI(api_key=zhipu_key) # 请填写您自己的APIKey
    response = client.chat.completions.create(
        model="glm-4",  # 填写需要调用的模型名称
        messages=[
                {"role": "user", "content": prompt},
            ],
            stream=False,
    )
    # print(response.choices[0].message.content)
    return response.choices[0].message.content


def sparkai_lite_api(prompt: str):
    spark = ChatSparkLLM(
        spark_api_url='wss://spark-api.xf-yun.com/v1.1/chat', #星火认知大模型Spark3.5 Max的URL值，其他版本大模型URL值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
        spark_app_id=SPARKAI_APP_ID,
        spark_api_key=SPARKAI_API_KEY,
        spark_api_secret=SPARKAI_API_SECRET,
        spark_llm_domain='general',
        streaming=False,
    )
    messages = [ChatMessage(
        role="user",
        content=prompt
    )]
    handler = ChunkPrintHandler()
    a = spark.generate([messages], callbacks=[handler])
    # print(a.generations[0][0].text)
    # print(type(a.generations[0][0].text))
    return a.generations[0][0].text

def sparkai35_max_api(prompt: str):
    spark = ChatSparkLLM(
        spark_api_url='wss://spark-api.xf-yun.com/v3.5/chat',
        spark_app_id=SPARKAI_APP_ID,
        spark_api_key=SPARKAI_API_KEY,
        spark_api_secret=SPARKAI_API_SECRET,
        spark_llm_domain='generalv3.5',
        streaming=False,
    )
    messages = [ChatMessage(
        role="user",
        content=prompt
    )]
    handler = ChunkPrintHandler()
    a = spark.generate([messages], callbacks=[handler])
    # print(a.generations[0][0].text)
    # print(type(a.generations[0][0].text))
    return a.generations[0][0].text

def get_access_token():
    """
    使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
    """ 
    url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={BAIDU_API_KEY}&client_secret={BAIDU_SECRET_KEY}"
    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")

def baidu_ERNIE_4_8K(prompt):
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token=" + get_access_token()
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    data = json.loads(response.text)
    return data['result']

def baidu_ERNIE_35_8K(prompt):
    # url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie_speed?access_token=" + get_access_token()
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions?access_token=" + get_access_token()
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    data = json.loads(response.text)
    return data['result']

def baidu_ERNIE_Speed(prompt):
    # url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie_speed?access_token=" + get_access_token()
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie_speed?access_token=" + get_access_token()
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    data = json.loads(response.text)
    return data['result']

def baidu_ERNIE_Lite(prompt):
    # url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie_speed?access_token=" + get_access_token()
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token=" + get_access_token()
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    data = json.loads(response.text)
    return data['result']

def llama2_7B(prompt):
    # url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie_speed?access_token=" + get_access_token()
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/llama_2_7b?access_token=?access_token=" + get_access_token()
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    data = json.loads(response.text)
    return data['result']

from flask import Flask, request, jsonify
# from models_api import gpt_35_api, gpt_4_api, baidu_ERNIE_Lite, baidu_ERNIE_Speed, sparkai35_max_api, sparkai_lite_api, llama2_7B, baichuan2, chatglm3, chatglm4
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/ask', methods=['POST'])
def ask():
    data = request.json
    prompt = data.get('prompt')
    model = data.get('model')
    print(prompt)
    if not prompt or not model:
        return jsonify({'error': 'Invalid input'}), 400

    try:
        if model == 'option2-1':
            response = baidu_ERNIE_Lite(prompt)
        elif model == 'option2-2':
            response = baidu_ERNIE_Speed(prompt)
        elif model == 'option2-3':
            response = sparkai35_max_api(prompt)
        elif model == 'option2-4':
            response = sparkai_lite_api(prompt)
        elif model == 'option2-5':
            response = gpt_35_api(prompt)
        elif model == 'option2-6':
            response = gpt_4_api(prompt)
        elif model == 'option2-7':
            response = llama2_7B(prompt)
        elif model == 'option2-8':
            response = baichuan2(prompt)
        elif model == 'option2-9':
            response = chatglm3(prompt)
        elif model == 'option2-10':
            response = chatglm4(prompt)
        else:
            response = 'Invalid model'
        print(response)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
