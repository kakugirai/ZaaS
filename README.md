# ZaaS
残留 as a Service. Fill in zanryu card? NO MORE!

## Introduction

By using ZaaS, the only thing you need to do when you want to 残留 in Delta is to:

```
ssh cpu
zanryu
```

That's all!

Wait a minute? What happened?

You just post a zanryu request to ZaaS server, which is actually also running on CPU (no external traffic, it's secure!). The server will handle all the dirty jobs for you and finally print out all the zanryu card at around 1:00 am!

By default, `zanryu` command will search for a `.zanryu.json` file in your `$HOME`, which should look like this:

```
{
    "student-id": "716123123",
    "gakubu": "環",
    "gakunen": "1",
    "student-name": "慶応　太郎",
    "class-name": "研究会",
    "teacher-name": "村井　純",
    "location": "デルタ館 N205",
    "parent-name": "慶応　花子",
    "relation": "母",
    "tele": "080 5666 6666"
}
```

so just simply create your own `.zanryu.json` in your `$HOME`, or you can also specify which file you would like to use if you prefer.

```
zanryu new_zanryu.json
```

run`zanryu --help`for more information.

## Installation
This repo contains both ZaaS client and server.

### Install ZaaS client on CPU

```
git clone https://github.com/kakugirai/ZaaS.git
cd ZaaS/ZaaS-client
python setup.py install
```

### Install ZaaS server
Please note that I've already deployed a ZaaS server on CPU, so run it on your own machine if you want to have a try!

First, install the PDF generator

```
brew install wkhtmltopdf
```

then

```
git clone https://github.com/kakugirai/ZaaS.git
cd ZaaS/ZaaS-server
pip install -r requirements.txt
```

start the server

```
python app.py
```

## TODOs
- [ ] <STRIKE>Rewrite HTML with a model engine(EJS? Pug?)</STRIKE>
- [ ] Decrease dependencies
- [ ] Python2 support on ZaaS server
