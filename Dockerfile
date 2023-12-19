FROM debian
COPY . /root
WORKDIR /root
RUN sed -i 's/deb.debian.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list.d/debian.sources && apt update \
&& DEBIAN_FRONTEND="noninteractive" apt install python3 python3-pip chromium python3-selenium -y
RUN grep -v 'selenium' requirements.txt > tmp.txt && pip3 install --break-system-packages -r tmp.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
ENTRYPOINT ["/usr/bin/python3","/root/main.py"]
