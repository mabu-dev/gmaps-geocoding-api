def get_api_keys():
    try:
        with open('/Users/mabu/dev/tutorials/maps-api/configs/key.txt') as f:
            return f.readlines()[0]
    except Exception as ex:
        return ex
