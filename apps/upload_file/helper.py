from blogv2.settings import QINIU_AK, QINIU_SK
import qiniu


class QiniuOSS:
    """
    七牛oss
    """
    def __init__(self, bucket_name):
        self.auth = qiniu.Auth(QINIU_AK, QINIU_SK)
        self.bucket = bucket_name

    def upload_file(self, file):
        """
        上传文件到七牛oss
        """
        # print("filename: {}".format(file.name))
        qiniu_key = "upload/{}".format(file.name).strip()

        policy = {
            'callbackUrl':"http://ebgdky.natappfree.cc/upload_file/qiniu_callback/",
            'callbackBody': "filename={}&filesize=$(fsize)&qiniu_key={}".format(file.name, qiniu_key),
        }
        token = self.auth.upload_token(self.bucket, qiniu_key, 60*60, policy)

        # print("token: {}, qiniu_key: {}".format(token, qiniu_key))
        ret = qiniu.put_data(token, qiniu_key, file.read())

        # print("ret：{}".format(ret))
        return ret

    def get_file(self, prefix=None, limit=10, delimiter=None, marker=None):
        """
        获取文件
        """
        bucket = qiniu.BucketManager(self.auth)
        
        result, *_ = bucket.list(self.bucket, prefix, marker, limit, delimiter)

        return result.get('items', [])    

    def download_file(self):
        """
        下载文件
        """
        pass

