import axios from 'axios';

var role = "你是一个中英翻译机器人。\n";
var scene = "场景是将输入的文本翻译成中文或者英文，如果输入的是中文则翻译成英文，如果输入的是英文则翻译成中文。不要回答其他无关信息直接输出翻译内容，下面是输入的文本：\n";

export function sendQuestionToAPI(prompt, apiKey, difficulty) {
    var data = JSON.stringify({
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": role + scene
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
    });

    var config = {
        method: 'post',
        url: 'https://api.chatanywhere.tech/v1/chat/completions',
        headers: { 
            'Authorization': `Bearer ${apiKey}`, 
            // 'User-Agent': 'Apifox/1.0.0 (https://apifox.com)', 
            'Content-Type': 'application/json'
        },
        data: data
    };

    return axios(config)
        .then(function (response) {
            const answer = response.data.choices[0].message.content;
            console.log(answer)
            return answer;
        })
        .catch(function (error) {
            console.error(error);
            throw error;
        });
}
