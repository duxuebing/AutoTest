import time

import requests

"""
https://www.autodl.com/console/elasticDeploy/list
list_deployment_uuid列表中存放的是目前需要关机的测试服务器的部署ID,下面是测试用可能使用的测试

9/9/2024 检查测试环境所有部署id
testEn#SwapHair_CQ：eb9b3a1a18
testEn#SwapInpaint：f3907b6c77
testEn#Creative_Filter_ChongQing：4db0816435
testEn#SwapInpaint：848c1af2b4
testEn#SwapStudio：2704d249be
testEn#DREAMBOOTHTRAIN：ba3428e6a2
testEn#SwapHair：3d26ffc9fd
testEn#xiaoda：56f414c47f
testEn#Creative_Filter：22faa947e0
testEn#MAGIC_INPAINTING：4fa825afb7
test Han2：0f55e25ee9
test han XL：fab8d2f365
testEn#App_Background：795e73a08c
testEn#STABLE_DIFFUSION_WEST：21be6c6c28
testEn#Retake_Two_Phase：e37b8abc34
testEn#ReTakePortrait：9ea5b43c67
testEn#PHOTOROOM_SHADOW：d69c7c9b75
testEn#SwapInpaint：d119bd291a
testEn#DREAMBOOTHINFERENCE：9fcaa93a59
testEn#MASK_VARIATION_FIN_PROD：cc57dad58d
testEn#PHOTOROOM：8a2de16aca
test Han：74e3f0818a
testEn#MASK_VARIATION_SEGMENT：724caccdef
testEn#DREAMBOOTHTRAIN：1e9c994099
testEn#SwapStudio：826db4c036
testEn#REF_IMG_WORD：e6ea84e29f9087f
testEn#CLOTH_PERSON：041c72d13603fe3
testEn#MAGIC_INPAINTING_XL：ed7155a8f390d51
"""

# list_deployment_uuid = ["eb9b3a1a18","f3907b6c77","4db0816435","848c1af2b4","2704d249be","ba3428e6a2","3d26ffc9fd","56f414c47f","22faa947e0","4fa825afb7","0f55e25ee9","fab8d2f365","795e73a08c","21be6c6c28","e37b8abc34","9ea5b43c67","d69c7c9b75","d119bd291a","9fcaa93a59","cc57dad58d","8a2de16aca","74e3f0818a","724caccdef","1e9c994099","826db4c036","e6ea84e29f9087f","041c72d13603fe3","ed7155a8f390d51"]
list_deployment_uuid = ["3d26ffc9fd"]

headers = {
    "Authorization": "eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjQ0NjA5LCJ1dWlkIjoiM2M1ODNlYzgtODY1Ny00MWYwLWIzNmMtMGUwNGZlNGIyZDk1IiwiaXNfYWRtaW4iOmZhbHNlLCJpc19zdXBlcl9hZG1pbiI6ZmFsc2UsInN1Yl9uYW1lIjoiIiwidGVuYW50IjoiYXV0b2RsIn0.2vMXRe3Z7tDuR0Z_pmVEli8WK8nlVXMRGjACT0gcfLyMoQZQs2_3yDV7yrjmT4iLiM-4MqCqJjxAHk709F5w4A",
    "Content-Type": "application/json"
}
url = "https://api.autodl.com/api/v1/dev/deployment/container/list"
list1 = []
for i in list_deployment_uuid:
    body = {
        "deployment_uuid": i,
        "container_uuid": "",
        "date_from": "",
        "date_to": "",
        "gpu_name": "",
        "cpu_num_from": 0,
        "cpu_num_to": 0,
        "memory_size_from": 0,
        "memory_size_to": 0,
        "price_from": 0,
        "price_to": 0,
        "released": False,

        "page_index": 1,
        "page_size": 100,
    }
    response = requests.post(url, json=body, headers=headers)
    time.sleep(3)
    print(response.content.decode())
    print(response.json()["data"]["list"])
    print(len(response.json()["data"]["list"]))
    uuid = response.json()["data"]["list"]
    if uuid is not None:
        for j in range(len(uuid)):
            list1.append(uuid[j]["uuid"])
time.sleep(3)
print(list1)
'''将开启的测试服务器的容器停止'''
headers = {
    "Authorization": "eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjQ0NjA5LCJ1dWlkIjoiM2M1ODNlYzgtODY1Ny00MWYwLWIzNmMtMGUwNGZlNGIyZDk1IiwiaXNfYWRtaW4iOmZhbHNlLCJpc19zdXBlcl9hZG1pbiI6ZmFsc2UsInN1Yl9uYW1lIjoiIiwidGVuYW50IjoiYXV0b2RsIn0.2vMXRe3Z7tDuR0Z_pmVEli8WK8nlVXMRGjACT0gcfLyMoQZQs2_3yDV7yrjmT4iLiM-4MqCqJjxAHk709F5w4A",
    "Content-Type": "application/json"
}
url1 = "https://api.autodl.com/api/v1/dev/deployment/container/stop"
for l in list1:
    body1 = {
        "deployment_container_uuid": l,
        "decrease_one_replica_num": True
    }
    print(body1)
    response = requests.put(url1, json=body1, headers=headers)
    print(response)
    print(response.content.decode())

