from cmath import log
from distutils.sysconfig import PREFIX
import discord
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()


def get_data(problem):
    url = "https://solved.ac/api/v3/problem/show?problemId=" + str(problem)
    requestData = requests.get(url)
    return json.loads(requestData.content)


def get_icon(level):
    icons = [
        "https://user-images.githubusercontent.com/97784561/210267171-d7b7de5f-a68a-4ff9-ada4-494d49df8ada.png",
        "https://user-images.githubusercontent.com/97784561/210267173-050d1ae9-a17b-4a7f-a2cf-be0a4c3794be.png",
        "https://user-images.githubusercontent.com/97784561/210267175-31d16c69-3b1b-4c59-9648-0e6222f1189e.png",
        "https://user-images.githubusercontent.com/97784561/210267177-c3352b7b-a028-47ef-bf1f-6c1f601934d8.png",
        "https://user-images.githubusercontent.com/97784561/210267178-ecb687ac-83b9-4754-905e-daadf6042eea.png",
        "https://user-images.githubusercontent.com/97784561/210267180-4aec3248-d91c-4566-8027-220ede31a199.png",
        "https://user-images.githubusercontent.com/97784561/210267181-c99dd3ad-d3d4-41c9-a65e-6158b36e2f4e.png",
        "https://user-images.githubusercontent.com/97784561/210267182-a9e62d9c-648c-41d3-a80a-a36227a69583.png",
        "https://user-images.githubusercontent.com/97784561/210385925-6a901eb1-f650-4b10-b864-e39c2e342e47.png",
        "https://user-images.githubusercontent.com/97784561/210267183-afc94124-07ee-4554-903e-7cfef5f769ab.png",
        "https://user-images.githubusercontent.com/97784561/210267184-2faa7096-0748-4cd2-8e7a-8804b79d1dd2.png",
        "https://user-images.githubusercontent.com/97784561/210267185-9f93420d-aeeb-48bd-a687-7b33fb1d7b48.png",
        "https://user-images.githubusercontent.com/97784561/210267186-92a7a422-a907-4bad-aa0c-2c339034942a.png",
        "https://user-images.githubusercontent.com/97784561/210267190-a3fb0ae7-d575-44b2-a35b-2eff9b6e2cda.png",
        "https://user-images.githubusercontent.com/97784561/210267191-8919b300-9918-453e-9590-0b9a4bfec25d.png",
        "https://user-images.githubusercontent.com/97784561/210267193-4b493b79-dbc4-4b0c-b924-da7779b8e597.png",
        "https://user-images.githubusercontent.com/97784561/210267196-b8ef2574-03df-420a-b8a1-df79a44fbe39.png",
        "https://user-images.githubusercontent.com/97784561/210267198-60dbb9e5-8bf4-433c-9565-1d9f72530ac0.png",
        "https://user-images.githubusercontent.com/97784561/210267200-a646b82b-d7a3-41d1-a195-96b9995266dd.png",
        "https://user-images.githubusercontent.com/97784561/210267201-ca0b5435-a654-44ea-a036-4d6f7869a859.png",
        "https://user-images.githubusercontent.com/97784561/210267204-28917812-529d-44b5-ab18-97d55ad1a880.png",
        "https://user-images.githubusercontent.com/97784561/210267206-980ed030-5b16-44c3-bb49-9dad4bd7c7a6.png",
        "https://user-images.githubusercontent.com/97784561/210267207-d37e6c80-7082-4bf7-87bc-5279a7a2fe16.png",
        "https://user-images.githubusercontent.com/97784561/210267209-60558608-82c2-40b3-a28e-7fe596a3f3ef.png",
        "https://user-images.githubusercontent.com/97784561/210267211-68ba02d5-2a56-4117-8812-05d32dd7a927.png",
        "https://user-images.githubusercontent.com/97784561/210267212-bd1f3385-dea6-4746-a875-770edafc8941.png",
        "https://user-images.githubusercontent.com/97784561/210267213-44ee961e-d0b3-4a12-84a6-47a9b3bbcc61.png",
        "https://user-images.githubusercontent.com/97784561/210267215-d07c4fc8-2074-4c80-b945-ca4a73113b3e.png",
        "https://user-images.githubusercontent.com/97784561/210267216-cd07fcec-4250-4b4e-8a86-1f2d43f5c905.png",
        "https://user-images.githubusercontent.com/97784561/210267220-6ce41883-4148-4933-a65f-11a93d37fc57.png",
        "https://user-images.githubusercontent.com/97784561/210267221-53ce6ecb-e190-489f-b2b0-1c01f45c53c2.png",
    ]
    return icons[level]


def get_level(level):
    levels = [
        "Unrated",
        "Bronze V",
        "Bronze IV",
        "Bronze III",
        "Bronze II",
        "Bronze I",
        "Silver V",
        "Silver IV",
        "Silver III",
        "Silver II",
        "Silver I",
        "Gold V",
        "Gold IV",
        "Gold III",
        "Gold II",
        "Gold I",
        "Platinum V",
        "Platinum IV",
        "Platinum III",
        "Platinum II",
        "Platinum I",
        "Diamond V",
        "Diamond IV",
        "Diamond III",
        "Diamond II",
        "Diamond I",
        "Ruby V",
        "Ruby IV",
        "Ruby III",
        "Ruby II",
        "Ruby I",
    ]
    return levels[int(level)]


PREFIX = os.environ["PREFIX"]
TOKEN = os.environ["TOKEN"]

# intents = discord.Intents.default()
# intents.message_content = True
# client = discord.Client(intents=intents)
client = discord.Client()


async def get_problem(text):
    name = text.split('\n')[0]
    url = "https://solved.ac/api/v3/search/problem"
    querystring = {"query": name}
    headers = {"Content-Type": "application/json"}
    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    for item in json.loads(response.content)['items']:
        if item['titleKo'] == name.strip():
            problem = int(item['problemId'])
            return int(problem)
    try:
        problem = int(text.split()[0].split()[0])
    except:
        problem = int(text.split("https://www.acmicpc.net/problem/")[1].split()[0])
    return int(problem)


async def get_code(text, problem):
    try:
        code = text.split(str(problem), maxsplit=1)[1].strip()
    except:
        name = text.split('\n')[0]
        code = text.split(str(name), maxsplit=1)[1].strip()
    return code


async def message_baekjooon(message, split_str):
    try:
        text = str(message.content).split(split_str, maxsplit=1)[1]
        problem = await get_problem(text)
        await message.delete()
    except:
        await message.channel.send('잘못된 입력입니다.')
        return

    try:
        data = get_data(problem)
    except:
        await message.channel.send('데이터를 가져오지 못했습니다.')
        return

    try:
        data = get_data(problem)
        tags = []
        for t in data["tags"]:
            tags.append(t["displayNames"][0]["name"])
        tags = ", ".join(tags)
        level = data["level"]
    except:
        await message.channel.send('데이터를 가져오지 못했습니다.')
        return

    try:
        embed = discord.Embed(
            color=0x3E76C0,
            title="문제 링크",
            url="https://www.acmicpc.net/problem/" + str(problem),
        )
        embed.set_author(
            name=data["titleKo"],
            url="https://www.acmicpc.net/problem/" + str(problem),
            icon_url=get_icon(level),
        )
        embed.add_field(name="문제 번호", value=data["problemId"], inline=True)
        embed.add_field(name="난이도", value=get_level(level), inline=True)
        embed.add_field(name="유형", value=tags, inline=False)
        await message.channel.send(embed=embed)
    except:
        await message.channel.send('메세지 전송이 실패했습니다.')


async def message_code(message, split_str):
    try:
        text = str(message.content).split(split_str, maxsplit=1)[1]
        problem = await get_problem(text)
        code = await get_code(text, problem)
        await message.delete()
    except:
        await message.channel.send('잘못된 입력입니다.')
        return

    try:
        data = get_data(problem)
        tags = []
        for t in data["tags"]:
            tags.append(t["displayNames"][0]["name"])
        tags = ", ".join(tags)
        level = data["level"]
        author = str(message.author).split('#')[0] + "님의 소스코드"
    except:
        await message.channel.send('데이터를 가져오지 못했습니다.')
        return

    try:
        embed = discord.Embed(
            color=0x3E76C0,
            title="문제 링크",
            url="https://www.acmicpc.net/problem/"+str(problem),
        )
        embed.set_author(
            name=data["titleKo"],
            url="https://www.acmicpc.net/problem/"+str(problem),
            icon_url=get_icon(level),
        )
        embed.add_field(name="문제 번호", value=data["problemId"], inline=True)
        embed.add_field(name="난이도", value=get_level(level), inline=True)
        embed.add_field(name="유형", value=tags, inline=True)
        embed.add_field(name=author, value=code, inline=False)
        await message.channel.send(embed=embed)
    except:
        try:
            embed = discord.Embed(
                color=0x3E76C0,
                title="문제 링크",
                url="https://www.acmicpc.net/problem/"+str(problem),
            )
            embed.set_author(
                name=data["titleKo"],
                url="https://www.acmicpc.net/problem/"+str(problem),
                icon_url=get_icon(level),
            )
            embed.add_field(name="문제 번호", value=data["problemId"], inline=True)
            embed.add_field(name="난이도", value=get_level(level), inline=True)
            embed.add_field(name="유형", value=tags, inline=True)
            await message.channel.send(embed=embed)
            await message.channel.send(author + '\n' + code)
        except:
            await message.channel.send('메세지 전송이 실패했습니다.')


async def message_long_code(message, split_str):
    try:
        text = str(message.content).split(split_str, maxsplit=1)[1]
        problem = await get_problem(text)
        code = await get_code(text, problem)
        await message.delete()
    except:
        await message.channel.send('잘못된 입력입니다.')
        return

    try:
        data = get_data(problem)
        tags = []
        for t in data["tags"]:
            tags.append(t["displayNames"][0]["name"])
        tags = ", ".join(tags)
        level = data["level"]
        author = str(message.author).split('#')[0] + "님의 소스코드 입니다."
    except:
        await message.channel.send('데이터를 가져오지 못했습니다.')
        return

    try:
        embed = discord.Embed(
            color=0x3E76C0,
            title="문제 링크",
            url="https://www.acmicpc.net/problem/"+str(problem),
        )
        embed.set_author(
            name=data["titleKo"],
            url="https://www.acmicpc.net/problem/"+str(problem),
            icon_url=get_icon(level),
        )
        embed.add_field(name="문제 번호", value=data["problemId"], inline=True)
        embed.add_field(name="난이도", value=get_level(level), inline=True)
        embed.add_field(name="유형", value=tags, inline=True)
        await message.channel.send(embed=embed)
        await message.channel.send(author + '\n' + code)
    except:
        await message.channel.send('메세지 전송이 실패했습니다.')


@client.event
async def on_ready():
    print(f"Logged in as {client.user}.")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(f"{PREFIX}백준"):
        await message_baekjooon(message, '/백준 ')
    elif message.content.startswith(f"{PREFIX}코드 "):
        await message_code(message, '/코드')
    elif message.content.startswith(f"{PREFIX}긴코드"):
        await message_long_code(message, '/긴코드 ')


try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
