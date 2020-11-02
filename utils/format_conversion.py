import yaml


def json_to_yaml(filepath, req=None):
    with open(filepath, "r+", encoding='utf-8') as f:
        yaml.safe_dump(req, stream=f, default_flow_style=False)


if __name__ == '__main__':
    json_to_yaml('../data/login_template.yaml', req={
        "headers": {
            "Content-Type": "application/json"
        },
        "method": "post",
        "url": "https://gateway.dev.m3.innowealth.cn/recv",
        "json": {
                "service": "login",
                "qdata": "18516126760",
                "unionid": "o1jaVwTeT8fN-WlrHJK6cZkUXAvY",
                "invitationCode": "null",
                "signType": "MD5",
                "pid": "1",
                "requestTime": 1596527403197,
                "symbol": "158fec90597c4fbbb255587e58006535",
                "uticket": "A08ADeolNo1Pq9dMfTzyFZfmoDgPrB/TEWNB8eM+p/0=",
                "sign": "b01255d9de8329065af4ebcabf0c7beb"
            }})
