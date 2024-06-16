# -*- coding: utf-8 -*-
from flask import request
from flask_restful import Resource

from LogServer.LogClient import initlog

logger = initlog(__name__)

SAVE_PATH = "D:/code/jzhPractice/UploadStorage/"


class TestUpload(Resource):
    def post(self):
        try:
            file = request.files.get('file')
            # file.save(SAVE_PATH + file.filename)
            logger.info(f"接收文件上传成功,存储路径: {SAVE_PATH + file.filename}")
            logger.info("alskaslas")
            logger.warn("asas")
            logger.error("qewd")
            return f"已接收: {file.filename}"
        except Exception as ex:
            logger.error(f"TestUpload error: {ex}")
            return None
