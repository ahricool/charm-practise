response=[{u'date': u'2014-01-01', u'country': u'US', u'revenue': 1.1, u'refund_revenue': 1.1}, {u'date': u'2014-01-02', u'country': u'US', u'revenue': 1.1, u'refund_revenue': 1.1}, {u'date': u'2014-01-03', u'country': u'US', u'revenue': 1.1, u'refund_revenue': 1.1}]



def _format_response( adapted_response, adapted_query):
    """
    Because the aa-conn-sales-go-services didn't format the data, but aa-sales-service can do it.
    So we will handle the format there.
    :return: None
    """
    # import ipdb;ipdb.set_trace()
    deprecated_dict = {'metrics': [{'expression': 'revenue', 'name': 'revenue'}, {'expression': 'refund_revenue', 'name': 'refund_revenue'}], 'meta': {'format': 'cascade'}, 'dimensions': [{'name': 'date'}, {'name': 'country'}], 'filters': [{'values': [1, 2], 'name': 'user_product_id'}, {'start': '2014-01-01', 'end': '2014-01-03', 'name': 'date'}, {'values': ['US'], 'name': 'country'}, {'values': [1], 'name': 'ipp_id'}]}
    meta_info = deprecated_dict.get("meta", {})
    if meta_info.get("format") == "cascade":
        dimensions = deprecated_dict.get("dimensions", [])
        dimensions = [d["name"] for d in dimensions]
        return _format_cascade(adapted_response, dimensions)
    else:
        return adapted_response


def _format_cascade(response, dimensions):
    formatted_response = {}
    for row in response:
        values = formatted_response
        for dimension in dimensions:
            dv = row[dimension]
            values = values.setdefault(dv, {})
        for k, v in row.items():
            if k not in dimensions and k not in values:
                values.update({k:v})
    return formatted_response
res=_format_response(response,1)
print(res)
