import axios from 'axios';

export function sendQuestionToAPI(prompt, apiKey) {
    var data = JSON.stringify({
        "model": "gpt-3.5-turbo",
        "messages": [
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
