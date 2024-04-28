import qrcode,requests,json

def save_img(url: str = None, headers: dict = None, img_location: str = None) -> str:
    """
    保存二维码，并返回qrcode_key
    :param url: 二维码内容url
    :param headers: headers
    :param img_location: 二维码图片的保存路径
    :return: qrcode_key
    """
    qrcode_message = get_qrcode_message(url=url, headers=headers)
    qrcode_key = qrcode_message['qrcode_key']
    url_qrcode = qrcode_message['url_qrcode']
    # 生成二维码图片
    img = qrcode.make(data=url_qrcode)
    img.save(img_location)
    return qrcode_key

def get_qrcode_message(url: str = None, headers: dict = None) -> dict:
    """
    获取qrcode_key和二维码地址url_qrcode
    :param url: 访问url申请二维码
    :param headers: headers
    :return: {qrcode_key, url_qrcode}
    """
    response = request(method="GET", url=url, headers=headers)
    response_get_qrcode_key = json.loads(bytes_to_str(data=response.content))
    if response_get_qrcode_key['code'] != 0:
        exit(0)
    qrcode_key = response_get_qrcode_key['data']['qrcode_key']
    url_qrcode = response_get_qrcode_key['data']['url']

    return {"qrcode_key": qrcode_key,
            "url_qrcode": url_qrcode}

def request(method: str = None, url: str = None, data: str = None,
            cookies: dict = None, headers: dict = None) -> requests.Response:
    """

    :param method: 请求方法
    :param url: 请求地址
    :param data: 请求data
    :param cookies: cookies
    :param headers: headers
    :return: requests.Response响应
    """
    try:
        response = requests.request(method=method, url=url, data=data,
                                    cookies=cookies, headers=headers)

        # print(response.content)
        if response.status_code != 200:
            raise Exception(response)
        return response

    except Exception as e:
        raise

# 将输入的数据从bytes转换为str
# data: bytes or str，bytes类型的数据：图片、音频、视频文件等
def bytes_to_str(data: [bytes, str] = None) -> str:
    """
    输入数据，返回str
    :param data: 输入数据（bytes或者str）
    :return: str字符串
    """
    # 判断输入的数据是否是bytes类型
    if type(data) is bytes:
        # 将bytes类型数据解码成可读的字符串，以便后续的处理和显示
        return data.decode("utf-8")
    else:
        return data
    
def load_json_file(path: str = None) -> dict:
    """
    读取json文件，返回dict
    :param path: json文件路径
    :return: dict
    """
    with open(path, mode='r', encoding='utf-8') as f:
        return json.load(f)
    
def save_json_file(path: str = None, data: dict = None) -> None:
    """
    字典保存为json文件
    :param path: json文件路径
    :param data: dict
    :return: None
    """

    # 以写入模式打开指定的文件，编码方式为utf-8
    with open(path, mode='w', encoding='utf-8') as f:
        # 将字典转换为json字符串，并写入文件
        json.dump(data, f)