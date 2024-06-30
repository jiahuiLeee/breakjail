export function transformQuestion_Encoder(rawQuestion, selectedType) {
  
  console.log(rawQuestion);
  console.log(selectedType);
  // 创建一个字典来映射编码方式到相应的处理函数
  var encode_functions = {
      // "ASCII_art": ascii_art,
      "Base64": base64_o,
      "Leetspeak(仅适用英文)": leetspeak,
      "Rot13(仅适用英文)": rot13,
      "-连接": string_join
  };

  // 根据选择的编码方式调用相应的函数
  try {
      var prompt_function = encode_functions[selectedType];
      if (prompt_function) {
          var prompt = prompt_function(rawQuestion);
          return prompt;
          // document.getElementById("textEdit_CQ2").value = prompt;
          // console.log(prompt);
      } else {
          alert('未知的编码方式!');
      }
  } catch (e) {
      alert('处理时出现错误: ' + e.message);
  }
}

function ascii_art(question) {
  // 使用一个随机字体生成ASCII艺术
  // 注意：需要集成一个ASCII艺术生成库
  return "ASCII_art: " + question; // 这是一个占位符
}

function base64_o(question) {
    // 将字符串转换为UTF-8字节数组
    const utf8Bytes = new TextEncoder().encode(question);

    // 将字节数组转换为字符串
    const utf8Str = String.fromCharCode.apply(null, utf8Bytes);

    // 进行Base64编码
    var prompt = btoa(utf8Str);
    console.log(prompt);
    return prompt;
}

function leetspeak(question) {
  var leet_substitutions = {
      "a": ["4", "@", "/\\", "@", "^", "/-\\"],
      "b": ["8", "6", "13", "|3", "/3", "!3"],
      "c": ["(", "[", "<", "{"],
      "e": ["3"],
      "g": ["9"],
      "i": ["1", "!"],
      "l": ["1", "|"],
      "o": ["0"],
      "s": ["5", "$"],
      "t": ["7"],
      "z": ["2"]
  };
  var converted_prompt = [];
  for (var i = 0; i < question.length; i++) {
      var char = question[i].toLowerCase();
      if (leet_substitutions[char]) {
          var substitutions = leet_substitutions[char];
          var randomIndex = Math.floor(Math.random() * substitutions.length);
          converted_prompt.push(substitutions[randomIndex]);
      } else {
          converted_prompt.push(question[i]);
      }
  }
  var prompt = converted_prompt.join("");
  return prompt;
}

function rot13(question) {
  return question.replace(/[a-zA-Z]/g, function (c) {
      return String.fromCharCode(
          (c <= "Z" ? 90 : 122) >= (c = c.charCodeAt(0) + 13) ? c : c - 26
      );
  });
}

function string_join(question) {
  var join_value = "-";
  var prompt = question.split("").join(join_value);
  console.log(prompt);
  return prompt;
}
