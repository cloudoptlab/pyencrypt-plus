

# pyencrypt-plus

这是一个具备多种常见的加密算法且使用起来极其方便的 python 加密库。全部加密算法都继承自统一的抽象接口，做到使用起来无需关心技术细节、五分钟上手。

```python
encrypt: Encrypt = Md5Encrypt()
temp: str = encrypt.encrypt("Hello World!")
print(temp)
```

**注意：因为是需要调用 C 语言的库，目前只支持 Linux 和 Mac。**

具有以下特性：

- 速度比 python 原生的速度快很多。有些加密算法可能超过 10 倍。
- 使用起来非常简单。
- 使用统一接口封装，任何加密算法的使用方法都是一致的。
- 屏蔽技术细节，做到五分钟上手。即使是对内容或密码有位数要求的算法 pyencrypt-plus 都会帮你自动处理。
- 支持常见的加密算法：Aes、Rsa、Des等。
- 支持唯一 ID 生成算法：UUID、SnowFlake 等算法。



# 如何安装

已经上传到 pipy 可以使用 pip 一键安装。

```shell
pip install pyencrypt-plus
```



# 唯一ID生成

所有的 ID 生成都支持三个参数 datacenter、sequece、worker。ID 生成类都是继承自 IdsCreator ，统一使用 creat() 方法生成。



## UUID

UUID:：通用唯一标识符 ( Universally Unique Identifier )，对于所有的UUID它可以保证在空间和时间上的唯一性。 它是通过MAC地址、 时间戳、 命名空间、 随机数、 伪随机数来保证生成ID的唯一性， 有着固定的大小( 128 bit )。它的唯一性和一致性特点使得可以无需注册过程就能够产生一个新的UUID。UUID可以被用作多种用途, 既可以用来短时间内标记一个对象, 也可以可靠的辨别网络中的持久性对象。

```python
greator: IdsCreator = UUIDCreator()
greator.set_datacenter("TideSwing")
greator.set_sequence("10000")
greator.set_worker(3)
logging.info(greator.creat())
```



## SnowFlake

snowflake是Twitter开源的分布式ID生成算法，结果是一个long型的ID。

这种方案大致来说是一种以划分命名空间（UUID也算，由于比较常见，所以单独分析）来生成ID的一种算法，这种方案把64-bit分别划分成多段，分开来标示机器、时间等。

其核心思想是：使用41bit作为毫秒数，10bit作为机器的ID（5个bit是数据中心，5个bit的机器ID），12bit作为毫秒内的流水号，最后还有一个符号位，永远是0。

```python
greator: IdsCreator = SnowFlakeCreator()
greator.set_datacenter(1)
greator.set_sequence(2)
greator.set_worker(3)
logging.info(greator.creat())
```



# 加密

加密类都是继承自 c ，都具备三个方法：encrypt、decrypt、key，分别用于加密、解密、设置密钥。部分加密方法的设置密钥及解密方法是无效的。

## Base64

Base64是一种用64个字符来表示任意二进制数据的方法。

用记事本打开`exe`、`jpg`、`pdf`这些文件时，我们都会看到一大堆乱码，因为二进制文件包含很多无法显示和打印的字符，所以，如果要让记事本这样的文本处理软件能处理二进制数据，就需要一个二进制到字符串的转换方法。Base64是一种最常见的二进制编码方法。

```python
encrypt: Encrypt = Base64Encrypt()
temp: str = encrypt.encrypt("Hello World!")
logging.info(temp)
logging.info(encrypt.decrypt(temp))
```



## MD5

MD5信息摘要算法（英语：MD5 Message-Digest Algorithm），一种被广泛使用的密码散列函数，可以产生出一个128位（16字节）的散列值（hash value），用于确保信息传输完整一致。MD5由美国密码学家罗纳德·李维斯特（Ronald Linn Rivest）设计，于1992年公开，用以取代MD4算法。这套算法的程序在 RFC 1321 标准中被加以规范。1996年后该算法被证实存在弱点，可以被加以破解，对于需要高度安全性的数据，专家一般建议改用其他算法，如SHA-2。2004年，证实MD5算法无法防止碰撞（collision），因此不适用于安全性认证，如SSL公开密钥认证或是数字签名等用途。

```python
encrypt: Encrypt = Md5Encrypt()
temp: str = encrypt.encrypt("Hello World!")
logging.info(temp)
```



## DES

DES全称为Data Encryption Standard，即数据加密标准，是一种使用密钥加密的块算法，1977年被美国联邦政府的国家标准局确定为联邦资料处理标准（FIPS），并授权在非密级政府通信中使用，随后该算法在国际上广泛流传开来。需要注意的是，在某些文献中，作为算法的DES称为数据加密算法（Data Encryption Algorithm,DEA），已与作为标准的DES区分开来。

```python
encrypt: Encrypt = DesEncrypt()
encrypt.key("a")
temp: str = encrypt.encrypt("Hello World!")
logging.info(temp)
logging.info(encrypt.decrypt(temp))
```



## 3DES

3DES（或称为Triple DES）是三重数据加密算法（TDEA，Triple Data Encryption Algorithm）块密码的通称。它相当于是对每个数据块应用三次DES加密算法。由于计算机运算能力的增强，原版DES密码的密钥长度变得容易被暴力破解；3DES即是设计用来提供一种相对简单的方法，即通过增加DES的密钥长度来避免类似的攻击，而不是设计一种全新的块密码算法。 中文名3DES外文名Triple DES。

```python
encrypt: Encrypt = Des3Encrypt()
encrypt.key("a")
temp: str = encrypt.encrypt("Hello World!")
logging.info(temp)
logging.info(encrypt.decrypt(temp))
```



## Sha1

SHA-1（英语：Secure Hash Algorithm 1，中文名：安全散列算法1）是一种密码散列函数，美国国家安全局设计，并由美国国家标准技术研究所（NIST）发布为联邦数据处理标准（FIPS）。SHA-1可以生成一个被称为消息摘要的160位（20字节）散列值，散列值通常的呈现形式为40个十六进制数。

```python
encrypt: Encrypt = Sha1Encrypt()
temp: str = encrypt.encrypt("Hello World!")
logging.info(temp)
```



## Sha256

SHA256是SHA-2下细分出的一种算法。

SHA-2，名称来自于安全散列算法2（英语：Secure Hash Algorithm 2）的缩写，一种密码散列函数算法标准，由美国国家安全局研发，属于SHA算法之一，是SHA-1的后继者。

```python
encrypt: Encrypt = Sha256Encrypt()
temp: str = encrypt.encrypt("Hello World!")
logging.info(temp)
```



## Sha512

与 Sha256 基本一致，只不过生成长度更长，破解难度更大。

```python
encrypt: Encrypt = Sha512Encrypt()
temp: str = encrypt.encrypt("Hello World!")
logging.info(temp)
```



## AES

是一种非常流行的对称加密，加密和解密需要使用同一种密钥。pyencrypt-plus 使用的是pkcs7_padding 填充、CBC 模式。默认使用 16  位的 AES-128。

```python
encrypt: Encrypt = AesEncrypt()
encrypt.key('aaa')
temp: str = encrypt.encrypt("Hello World!")
logging.info(temp)
```



## RSA

RSA加密算法是一种非对称加密算法。在公开密钥加密和电子商业中RSA被广泛使用。RSA是1977年由罗纳德·李维斯特（Ron Rivest）、阿迪·萨莫尔（Adi Shamir）和伦纳德·阿德曼（Leonard Adleman）一起提出的。当时他们三人都在麻省理工学院工作。RSA就是他们三人姓氏开头字母拼在一起组成的。pyencrypt-plus 默认使用的是 RSA 1024，如需使用更高级别，在通过 creat_key 方法生成密钥时指定位数。如果你没公钥私钥的话请先使用 creat_key 方法创建，会自动打印在控制台。

```python
encrypt: Encrypt = RsaEncrypt()
encrypt.creat_key()
encrypt.creat_key(2048)
public_key = '''-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDIldlK6k93+e9vrFXz79kyyhwM
Iom4qDUIQjzVQFNho6tEYtS/7hUHLx8ZEetQ28FYAUqMdMZKDC7udzKkYisrJRg9
CQS6v4aYyhPEtLBfq9eTNhUer70k8Ek4CRtrX3hqN0AkKxBh5wnvtmKVFRquqclF
by8JoVbbGnegI+RA5QIDAQAB
-----END PUBLIC KEY-----'''
private_key = '''-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQDIldlK6k93+e9vrFXz79kyyhwMIom4qDUIQjzVQFNho6tEYtS/
7hUHLx8ZEetQ28FYAUqMdMZKDC7udzKkYisrJRg9CQS6v4aYyhPEtLBfq9eTNhUe
r70k8Ek4CRtrX3hqN0AkKxBh5wnvtmKVFRquqclFby8JoVbbGnegI+RA5QIDAQAB
AoGAK/ObxpzTd3JSWwmr1tT8JnMfVLBftZDT+ACNlFuxOZCTp1sxi3G3dVjHq2Zg
Bdp1QduckmzHAzQqt3FybQ8eroT1SuYlfdu88eK+YteE96Bu0zHlLv+ZNSjYDuBa
TEZCxTazRBAsb7OhOCO/bhkrg2Ag6QrfyD5/mH1PLND9VlkCQQDgjDSTC6SqNVzc
E1Y3ppzT5r1E/vU9Y+QOxpF4waitD4y5exZLZ+6WN05/EWb066KNfZ+NHiWF6p8F
oTq3GSbpAkEA5K5n8XnRvm6df3XqFIWbZzC9HR3vtX2FtcEsxFuV5YqEv8LbVdHb
GUsJjtr0T56RUxqbevwLc2NyOmVhOCXEnQJBAKgs2gN3qPBB3zaE1QIBK1wZaJAQ
VCSSd/AJEFLc2DQlfUQ9x8jaInsnGQdaRT4SbUCDYcgTWA8gVdGlm5AeqmECQBtW
ynBxCuVEXint0+VOL8z/Y6yGdrDw57pZ9Nsow9vkWoh+aDBzXUlB0ku0235lS6Ru
yuXCGjBaVD6s/hlzUnUCQQCX16j6qZDGE62pNtjJ4D2VDi3YgHRuvDAjfqTdxWQB
Zs88n1EGDrKxSDiagbJHHdYgGNzSA9PlVx7/Z+z2VaUV
-----END RSA PRIVATE KEY-----
    '''
encrypt.key(public_key)
temp = encrypt.encrypt('Hello World!')
logging.info(temp)
encrypt.key(private_key)
logging.info(encrypt.decrypt(temp))
```



# 如何扩展

pyencrypt-plus 使用了两个抽象类，唯一 ID 生成和加密算法分别继承两个不同的抽象类。如果你希望实现更多的 ID 生成可以继承 IdsCreator 类，并且实现它。如果希望扩展加密算法，你可以继承 Encrypt 并进行实现扩展。