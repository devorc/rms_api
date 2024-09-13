import base64
import os
import uuid

from connectivity import py_connectivity, py_uploadS3
from dotenv import load_dotenv
from pathlib import Path

env_path = str(Path(__file__).absolute().parents[1] / "config.env")
load_dotenv(env_path)


def fn_purchase_list():
    purchases = []
    try:
        sql = (
            "select purchase_pk_id as id,name,description,qty,total_price,invoice_url,items,suppliers,DATE_FORMAT("
            "created_at,'%d %M %Y %r') as created_at,DATE_FORMAT(purchased_at,'%d %M %Y %r') as purchased_at from "
            "stc_purchase")
        result, key = py_connectivity.get_result(sql)
        if result and len(result) > 0:
            for row in result:
                json_data = dict(list(zip(key, row)))
                purchases.append(json_data)
        return {"purchases": purchases}
    except Exception as e:
        print("fn_purchase_list " + str(e))
        return {"purchases": purchases}


def fn_add_purchase(request):
    name = request.get("name")
    description = request.get("description")
    qty = request.get("qty")
    total_price = request.get("total_price")
    items = request.get("purchase_items")
    suppliers = request.get("suppliers")
    purchased_at = request.get("date")
    purchased_at = str(purchased_at).replace("T", " ")
    purchased_at = purchased_at.split(".")
    purchased_at = purchased_at[0]
    base_dir = os.getenv("FILE_PATH")
    file = request.get("file")
    file_type = request.get("file_type")
    try:
        if file:
            if not os.path.exists(base_dir):
                os.mkdir(base_dir)
            write_file, file_type = check_file_type(file, file_type)
            filename = str(uuid.uuid4().hex) + file_type
            with open(base_dir + filename, 'wb') as f:
                f.write(base64.b64decode(write_file))
            s3_path = os.getenv("AWS_S3_PATH") + "/" + filename
            if py_uploadS3.file_move(base_dir + filename, s3_path):
                invoice_url = "https://" + os.getenv("AWS_S3_BUCKET") + ".s3.ap-south-1.amazonaws.com/" + s3_path
                print(name, description, qty, total_price, invoice_url, items, suppliers,
                      str(purchased_at))
                result = py_connectivity.call_proc('sp_purchase_add', (
                    name, description, qty, total_price, invoice_url, items, suppliers,
                    str(purchased_at), None))
        return {"val": 1, "message": "Your response have been updated successfully"}
    except Exception as e:
        print("fn_add_purchase " + str(e))
        return {"val": 0, "message": "Something went wrong"}


def check_file_type(file, file_type):
    if len(file) > 0:
        file_data = file.replace('data:' + str(file_type) + ';base64,', '')
        file_type = "." + str(file_type.split("/")[1])
        return file_data, file_type
