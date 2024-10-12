import json
import requests
import time
import random


def process_json(uid, end):
    end_time = end
    data = json.loads(
        """{
    "uuid": "1",
    "experimentId": 473,
    "courseId": 2000077162,
    "startTime": 1651341660460,
    "endTime": 1651342288245,
    "timeUsed": 627,
    "status": 1,
    "score": 31.0,
    "appid": "",
    "secret": "",
    "steps": [
        {
            "seq": 1,
            "title": "一展厅一节学习",
            "startTime": 1651341792141,
            "endTime": 1651341809306,
            "timeUsed": 17,
            "expectTime": 120,
            "score": 0,
            "maxScore": 4,
            "repeatCount": 1,
            "evaluation": "优",
            "scoringModel": "赋分模型",
            "remarks": "备注"
        },
        {
            "seq": 2,
            "title": "围炉夜话体验",
            "startTime": 1651341831464,
            "endTime": 1651341950729,
            "timeUsed": 119,
            "expectTime": 180,
            "score": 0,
            "maxScore": 3,
            "repeatCount": 1,
            "evaluation": "优",
            "scoringModel": "赋分模型",
            "remarks": "备注"
        },
        {
            "seq": 3,
            "title": "一展厅二、三、四节学习",
            "startTime": 1651341951729,
            "endTime": 1651341966292,
            "timeUsed": 14,
            "expectTime": 660,
            "score": 0,
            "maxScore": 7,
            "repeatCount": 1,
            "evaluation": "优",
            "scoringModel": "赋分模型",
            "remarks": "备注"
        },
        {
            "seq": 4,
            "title": "一厅答题闯关",
            "startTime": 1651341967295,
            "endTime": 1651341978606,
            "timeUsed": 11,
            "expectTime": 120,
            "score": 3,
            "maxScore": 3,
            "repeatCount": 1,
            "evaluation": "优",
            "scoringModel": "赋分模型",
            "remarks": "备注"
        },
        {
            "seq": 5,
            "title": "二展厅学习",
            "startTime": 1651341996309,
            "endTime": 1651341999696,
            "timeUsed": 3,
            "expectTime": 780,
            "score": 0,
            "maxScore": 9,
            "repeatCount": 1,
            "evaluation": "优",
            "scoringModel": "赋分模型",
            "remarks": "备注"
        },
        {
            "seq": 6,
            "title": "二厅答题闯关",
            "startTime": 1651342000697,
            "endTime": 1651342013518,
            "timeUsed": 12,
            "expectTime": 120,
            "score": 3,
            "maxScore": 3,
            "repeatCount": 1,
            "evaluation": "优",
            "scoringModel": "赋分模型",
            "remarks": "备注"
        },
        {
            "seq": 7,
            "title": "三展厅学习",
            "startTime": 1651342022174,
            "endTime": 1651342024497,
            "timeUsed": 2,
            "expectTime": 780,
            "score": 0,
            "maxScore": 10,
            "repeatCount": 1,
            "evaluation": "优",
            "scoringModel": "赋分模型",
            "remarks": "备注"
        },
        {
            "seq": 8,
            "title": "三厅答题闯关",
            "startTime": 1651342025498,
            "endTime": 1651342052904,
            "timeUsed": 27,
            "expectTime": 120,
            "score": 3,
            "maxScore": 3,
            "repeatCount": 1,
            "evaluation": "优",
            "scoringModel": "赋分模型",
            "remarks": "备注"
        },
        {
            "seq": 9,
            "title": "四展厅学习",
            "startTime": 1651342068364,
            "endTime": 1651342070259,
            "timeUsed": 1,
            "expectTime": 780,
            "score": 0,
            "maxScore": 13,
            "repeatCount": 1,
            "evaluation": "优",
            "scoringModel": "赋分模型",
            "remarks": "备注"
        },
        {
            "seq": 10,
            "title": "四厅答题闯关",
            "startTime": 1651342071260,
            "endTime": 1651342081700,
            "timeUsed": 10,
            "expectTime": 120,
            "score": 3,
            "maxScore": 3,
            "repeatCount": 1,
            "evaluation": "优",
            "scoringModel": "赋分模型",
            "remarks": "备注"
        },
        {
            "seq": 11,
            "title": "五展厅一、二节学习",
            "startTime": 1651342091651,
            "endTime": 1651342092556,
            "timeUsed": 0,
            "expectTime": 420,
            "score": 0,
            "maxScore": 6,
            "repeatCount": 1,
            "evaluation": "优",
            "scoringModel": "赋分模型",
            "remarks": "备注"
        },
        {
            "seq": 12,
            "title": "毛泽东游学之路",
            "startTime": 1651342093556,
            "endTime": 1651342147838,
            "timeUsed": 54,
            "expectTime": 300,
            "score": 10,
            "maxScore": 10,
            "repeatCount": 1,
            "evaluation": "优",
            "scoringModel": "赋分模型",
            "remarks": "备注"
        },
        {
            "seq": 13,
            "title": "五展厅三、四节学习",
            "startTime": 1651342148839,
            "endTime": 1651342156405,
            "timeUsed": 7,
            "expectTime": 360,
            "score": 0,
            "maxScore": 4,
            "repeatCount": 1,
            "evaluation": "优",
            "scoringModel": "赋分模型",
            "remarks": "备注"
        },
        {
            "seq": 14,
            "title": "五厅答题闯关",
            "startTime": 1651342157406,
            "endTime": 1651342183563,
            "timeUsed": 26,
            "expectTime": 120,
            "score": 3,
            "maxScore": 3,
            "repeatCount": 1,
            "evaluation": "优",
            "scoringModel": "赋分模型",
            "remarks": "备注"
        },
        {
            "seq": 15,
            "title": "六展厅学习",
            "startTime": 1651342192629,
            "endTime": 1651342197278,
            "timeUsed": 4,
            "expectTime": 780,
            "score": 0,
            "maxScore": 13,
            "repeatCount": 1,
            "evaluation": "优",
            "scoringModel": "赋分模型",
            "remarks": "备注"
        },
        {
            "seq": 16,
            "title": "六厅答题闯关",
            "startTime": 1651342198279,
            "endTime": 1651342209758,
            "timeUsed": 11,
            "expectTime": 120,
            "score": 3,
            "maxScore": 3,
            "repeatCount": 1,
            "evaluation": "优",
            "scoringModel": "赋分模型",
            "remarks": "备注"
        },
        { 
            "seq": 17,
            "title": "宣誓学习",
            "startTime": 1651342275856,
            "endTime": 1651342302135,
            "timeUsed": 26,
            "expectTime": 120,
            "score": 3,
            "maxScore": 3,
            "repeatCount": 1,
            "evaluation": "优",
            "scoringModel": "赋分模型",
            "remarks": "备注"
        }
    ],
    "ReportSummary": "试验报告总结",
    "reportModels": [
        {
            "name": "试验步骤1",
            "reportContents": [
                {
                    "name": "一展厅一节学习",
                    "images": [],
                    "imageType": "none",
                    "type": "script",
                    "inputs": {},
                    "script": "4",
                    "datas": []
                }
            ]
        },
        {
            "name": "试验步骤2",
            "reportContents": [
                {
                    "name": "围炉夜话体验",
                    "images": [],
                    "imageType": "none",
                    "type": "script",
                    "inputs": {},
                    "script": "3",
                    "datas": []
                }
            ]
        },
        {
            "name": "试验步骤3",
            "reportContents": [
                {
                    "name": "一展厅二、三、四节学习",
                    "images": [],
                    "imageType": "none",
                    "type": "script",
                    "inputs": {},
                    "script": "7",
                    "datas": []
                }
            ]
        },
        {
            "name": "试验步骤4",
            "reportContents": [
                {
                    "name": "一厅答题闯关",
                    "images": [],
                    "imageType": "none",
                    "type": "script",
                    "inputs": {},
                    "script": "3",
                    "datas": []
                }
            ]
        },
        {
            "name": "试验步骤5",
            "reportContents": [
                {
                    "name": "二展厅学习",
                    "images": [],
                    "imageType": "none",
                    "type": "script",
                    "inputs": {},
                    "script": "9",
                    "datas": []
                }
            ]
        },
        {
            "name": "试验步骤6",
            "reportContents": [
                {
                    "name": "二厅答题闯关",
                    "images": [],
                    "imageType": "none",
                    "type": "script",
                    "inputs": {},
                    "script": "3",
                    "datas": []
                }
            ]
        },
        {
            "name": "试验步骤7",
            "reportContents": [
                {
                    "name": "三展厅学习",
                    "images": [],
                    "imageType": "none",
                    "type": "script",
                    "inputs": {},
                    "script": "10",
                    "datas": []
                }
            ]
        },
        {
            "name": "试验步骤8",
            "reportContents": [
                {
                    "name": "三厅答题闯关",
                    "images": [],
                    "imageType": "none",
                    "type": "script",
                    "inputs": {},
                    "script": "3",
                    "datas": []
                }
            ]
        },
        {
            "name": "试验步骤9",
            "reportContents": [
                {
                    "name": "四展厅学习",
                    "images": [],
                    "imageType": "none",
                    "type": "script",
                    "inputs": {},
                    "script": "13",
                    "datas": []
                }
            ]
        {
            "name": "试验步骤10",
            "reportContents": [
                {
                    "name": "四厅答题闯关",
                    "images": [],
                    "imageType": "none",
                    "type": "script",
                    "inputs": {},
                    "script": "3",
                    "datas": []
                }
            ]
        },
        {
            "name": "试验步骤11",
            "reportContents": [
                {
                    "name": "五展厅一、二节学习",
                    "images": [],
                    "imageType": "none",
                    "type": "script",
                    "inputs": {},
                    "script": "6",
                    "datas": []
                }
            ]
        },
        {
            "name": "试验步骤12",
            "reportContents": [
                {
                    "name": "毛泽东游学之路",
                    "images": [],
                    "imageType": "none",
                    "type": "script",
                    "inputs": {},
                    "script": "10",
                    "datas": []
                }
            ]
        },
        {
            "name": "试验步骤13",
            "reportContents": [
                {
                    "name": "五展厅三、四节学习",
                    "images": [],
                    "imageType": "none",
                    "type": "script",
                    "inputs": {},
                    "script": "4",
                    "datas": []
                }
            ]
        },
        {
            "name": "试验步骤14",
            "reportContents": [
                {
                    "name": "五厅答题闯关",
                    "images": [],
                    "imageType": "none",
                    "type": "script",
                    "inputs": {},
                    "script": "3",
                    "datas": []
                }
            ]
        },
        {
            "name": "试验步骤15",
            "reportContents": [
                {
                    "name": "六展厅学习",
                    "images": [],
                    "imageType": "none",
                    "type": "script",
                    "inputs": {},
                    "script": "13",
                    "datas": []
                }
            ]
        },
        {
            "name": "试验步骤16",
            "reportContents": [
                {
                    "name": "六厅答题闯关",
                    "images": [],
                    "imageType": "none",
                    "type": "script",
                    "inputs": {},
                    "script": "3",
                    "datas": []
                }
            ]
        },
        {
            "name": "试验步骤17",
            "reportContents": [
                {
                    "name": "宣誓学习",
                    "images": [],
                    "imageType": "none",
                    "type": "script",
                    "inputs": {},
                    "script": "3",
                    "datas": []
                }
            ]
        }
    ]
}"""
    )
    data["uuid"] = uid
    data["endTime"] = end
    data["score"] = 59
    all_time_use = 0
    k = end_time
    l = len(data["steps"])
    for i in range(l):
        step = data["steps"][l - 1 - i]
        t = random.randint(4, 50)  # 未在17个模块中花费的时间
        all_time_use += t
        k = k - t * 1000
        step["endTime"] = k

        t = step["expectTime"] + random.randint(4, 50)
        all_time_use += t
        step["timeUsed"] = t
        step["score"] = step["maxScore"]
        k = k - t * 1000
        step["startTime"] = k

    data["timeUsed"] = all_time_use
    start_time = data["endTime"] - all_time_use * 1000
    data["startTime"] = start_time
    return json.dumps(data)


def get_headers():
    headers = {
        "Host": "virtualcourse.zhihuishu.com",
        "Connection": "keep-alive",
        "Content-Length": "23341",
        "sec-ch-ua": """" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100" """,
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
        "sec-ch-ua-platform": "Windows",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Origin": "https://ar.zhihuishu.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https//ar.zhihuishu.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9 ",
    }
    return headers


def first(uid):
    url = (
        "https://virtualcourse.zhihuishu.com/report/queryUserName?uuid="
        + uid
        + "&courseId=2000077162&"
    )
    headers = {
        "Host": "virtualcourse.zhihuishu.com",
        "Connection": "keep-alive",
        "sec-ch-ua": """" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100" """,
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
        "sec-ch-ua-platform": "Windows",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Origin": "https://ar.zhihuishu.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https//ar.zhihuishu.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9 ",
    }
    res = requests.get(url, headers=headers)
    print(res.text)


def second():
    url = "https://studyservice.zhihuishu.com/api/stuExperiment/systemTime"
    headers = {
        "Host": "studyservice.zhihuishu.com",
        "Connection": "keep-alive",
        "sec-ch-ua": """" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100" """,
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
        "sec-ch-ua-platform": "Windows",
        "Accept": "*/*",
        "Origin": "https://ar.zhihuishu.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https//ar.zhihuishu.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9 ",
    }
    resp = requests.get(url, headers=headers)
    data = resp.text
    print(data)
    data = json.loads(data)
    return data["data"]


def third(uid, end):
    url = "https://virtualcourse.zhihuishu.com/report/saveReport"
    data = process_json(uid, end)
    data = {"jsonStr": data, "ticket": None}
    headers = get_headers()
    response = requests.post(url, data=data, headers=headers)
    print(response.status_code)
    print(response.text)


if __name__ == "__main__":
    uid = "         "  # 输入你的uuid运行即可
    # 打开恰同学少年网页F12输入 getUUID()获得UUid替换上面再执行文件即可
    # 如需帮助,请联系微信: NULL0001000
    end = second()
    third(uid, end)
