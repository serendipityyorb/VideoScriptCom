import streamlit as st
from VideoScript import GetVideoScript

st.title("💯 视频脚本生成器")

with st.sidebar:
    api_key = st.text_input("请输入你的API密钥:",type="password")
    base_url = st.text_input("请输入你的API服务端点:")
    st.markdown("[从该网站学习获取教程](https://ai.nengyongai.cn/register?aff=PEeJ)")
    st.markdown("<br>"*10, unsafe_allow_html=True)  # 生成30个空行
    st.markdown("&nbsp;"*20+"**作者署名**  *Serendipity*",unsafe_allow_html=True)
st.info("""
🤖 我是一个视频脚本生成大师(很厉害的那种喵！！),
来都来了，快提供给我你要生成的视频标题、时长、创造力吧！
分享乐事一条：装垃圾的叫垃圾袋，装脑子的叫脑袋~~~""")

st.divider()
st.markdown("### 🌋 请输入视频的标题:")
title = st.text_input("")
st.divider()
st.markdown("### 🗻 请选择视频的时长:")
length = st.number_input("",value=1.0,min_value=0.1,max_value=10.0,step=0.1)
st.divider()
st.markdown("### 🪵 请确定视频的创造力:")
temperature = st.slider("",value=0.2,min_value=0.0,max_value=1.0,step=0.1)

submit = st.button("提交")
if submit and not api_key:
    st.info("请输入API密钥")
    st.stop()
if submit and not base_url:
    st.info("请输入API服务端口")
    st.stop()
if submit and not title:
    st.info("请输入视频标题")
    st.stop()
if submit and not length:
    st.info("请输入视频时长")
    st.stop()
if submit and not temperature:
    st.info("请输入视频创造力")
    st.stop()
if submit:
    with st.spinner("让我聪明的小脑袋瓜仔细想想……"):
        title,script = GetVideoScript("gpt-4o",api_key,base_url,temperature,length,title)
    st.write(title)
    st.write(script)
    st.info("呼…消耗脑力100000,不用谢我(顺手的事)")

