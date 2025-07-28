from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
#from langchain_community.utilities import WikipediaAPIWrapper

def GetVideoScript(model,api_key,base_url,temperature,length,title):
    model = ChatOpenAI(model=model,api_key=api_key,base_url=base_url,temperature=temperature)
    title_prompt_template = ChatPromptTemplate.from_messages(
        [
            ("human","请为主题{title}想一个吸引人注意力的标题")
        ]
    )
    title_chain = (title_prompt_template | model)

    script_prompt_template = ChatPromptTemplate.from_messages(
        [
            ("human","""你是一个视频脚本书写者，需要根据视频的主题{title}和视频时长{length}分钟来书写视频脚本，语言生动活泼幽默，
            以【开头】【中间】【结尾】的markdown格式书写，除了脚本外不要输出其他格式的文本，""")
        ]
    )#我会提供Wiki百科对这个主题的介绍，你可以参考这个介绍，介绍内容将用三个#包围，###Wiki百科:{wiki_introduction}###
    script_chain = (script_prompt_template | model)
    #wiki = WikipediaAPIWrapper(lang="zh")
    #wiki_introduction = wiki.run(title)
    title = title_chain.invoke({"title":title}).content
    script = script_chain.invoke({"title":title,"length":length}).content
    return title,script
