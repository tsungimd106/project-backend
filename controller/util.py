from flask import Response
import json
from coder import MyEncoder


def checkParm(cond, content):
    res = ""
    for i in cond:
        if(i not in content.keys()):
            res += "缺少必要參數 %s\n" % i
    return res


def ret(result):
    return Response(json.dumps(result, cls=MyEncoder), mimetype='application/json')

def normalize_query_param(value):
    """
    Given a non-flattened query parameter value,
    and if the value is a list only containing 1 item,
    then the value is flattened.

    :param value: a value from a query parameter
    :return: a normalized query parameter value
    """
    return value if len(value) > 1 else value[0]

def normalize_query(params):
    """
    Converts query parameters from only containing one value for each parameter,
    to include parameters with multiple values as lists.

    :param params: a flask query parameters data structure
    :return: a dict of normalized query parameters
    """
    params_non_flat = params.to_dict(flat=False)
    return {k: normalize_query_param(v) for k, v in params_non_flat.items()}