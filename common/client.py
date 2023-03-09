import jsonpath
import requests

session = requests.session()

class RequestsClient():
    def send(self,url,method,**kwargs):
        try:
            self.resp = session.request(url=url,method=method,**kwargs)
        except BaseException as e:
            raise BaseException(f'接口发起异常:{e}')
        return self.resp
    # 针对jsonpath的提取封装一个方法
    # 第一个参数指的是你要匹配的数据的jsonpath表达式
    # 第二个指的是你想返回匹配的第几个，默认是0返回第一个
    def extract_resp(self, json_path, index=0):
    # 注意有的接口是没有返回信息的，返回信息是空的
        text = self.resp.text  # 获取返回信息的字符串形式
        if text != '':
            resp_json = self.resp.json()  # 获取响应信息的json格式
            # 如果能匹配到值，那么res就是个列表
            # 如果匹配不到res就是个False
            res = jsonpath.jsonpath(resp_json, json_path)
            if res:
                if index < 0:
                    # 如果index小于0 ，我认为你要匹配到的所有结果
                    print("index < 0")
                    return res
                else:
                    return res[index]

            else:
                print('没有匹配到任何东西')
        else:
            raise BaseException('接口返回信息为空，无法提取')
if __name__ == '__main__':
    client=RequestsClient()
    client.send(url= 'http://apis.juhe.cn/fapig/nba/rank', method='post', data={'key':'8035d49e4ce6fc2a63e40d8e436e937e'})
    print(client.extract_resp('$.result.ranking[*]',))