import time
import jwt

# payload
token_dict = {
    'iat': time.time(),
    'name': 'lowman'
# 自定义的参数
}
"""payload 中一些固定参数名称的意义, 同时可以在payload中自定义参数"""
# iss  【issuer】发布者的url地址
# sub 【subject】该JWT所面向的用户，用于处理特定应用，不是常用的字段
# aud 【audience】接受者的url地址
# exp 【expiration】 该jwt销毁的时间；unix时间戳
# nbf  【not before】 该jwt的使用时间不能早于该时间；unix时间戳
# iat   【issued at】 该jwt的发布时间；unix 时间戳
# jti    【JWT ID】 该jwt的唯一ID编号

# headers
headers = {
    'alg': "HS256",  # 声明所使用的算法
}

"""headers 中一些固定参数名称的意义"""
# jku: 发送JWK的地址；最好用HTTPS来传输
# jwk: 就是之前说的JWK
# kid: jwk的ID编号
# x5u: 指向一组X509公共证书的URL
# x5c: X509证书链
# x5t：X509证书的SHA-1指纹
# x5t#S256: X509证书的SHA-256指纹
# typ: 在原本未加密的JWT的基础上增加了 JOSE 和 JOSE+ JSON。JOSE序列化后文会说及。适用于JOSE标头的对象与此JWT混合的情况。
# crit: 字符串数组，包含声明的名称，用作实现定义的扩展，必须由 this->JWT的解析器处理。不常见。

# 调用jwt库,生成json web token
jwt_token = jwt.encode(token_dict,"zhananbudanchou1234678",algorithm="HS256",headers=headers)

# print(jwt_token)
print(jwt_token)
# jwt_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6Ijk1MjcifQ.eyJpYXQiOjE1NTkyNzY5NDEuNDIwODgzNywibmFtZSI6Imxvd21hbiJ9.GyQhOJK8FKD_Gd-ggSEDPPP1Avmz3M5NDVnmfOfrEIY"

data = jwt.decode(jwt_token, "zhananbudanchou1234678", algorithms=['HS256'])



print(data)