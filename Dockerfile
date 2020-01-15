FROM python3

ADD bot.py /

RUN pip install discord
RUN pip install asyncio
RUN pip install json
RUN pip install requests
RUN pip install itertools
RUN pip install traceback
RUN pip install youtube_dl
RUN pip install async_tiemout
RUN pip install selenium
RUN pip install giphy_client

CMD [ "python", "./bot.py" ]