# AI-Project-Structure-Generator
一个简单的基于大语言模型的项目文件结构生成器  
idea来自与和gpt讨论大作业，他直接吧项目的文件结构生成出来了，但是我依然需要手动一个个创建
### 使用方法
安装python3并执行以下命令  
```pip install -r requirements.txt```  
```python main.py```  
在第一次运行后会生成.env文件，你需要填入自己的openai apikey或者中转url及apikey  
后会要求输入生成路径
最后输入项目需求后即可  
**注意 目前提示词无法确保输出的内容一定能被识别，可能失败，重试即可**  
也希望有能力的大佬能一起改进这个项目