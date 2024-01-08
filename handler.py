import json
import io
import cgi

def converter(event, context):
    print(event)
    # file = io.BytesIO(event['body'].encode('utf-8'))
    # pdict = cgi.parse_header(event['headers']['content-type'])[1]
    # print('pdict', pdict)
    # if 'boundary' in pdict:
    #     pdict['boundary'] = pdict['boundary'].encode('utf-8')
    # pdict['CONTENT-LENGTH'] = event['headers']['content-length']
    # form_data = cgi.parse_multipart(file, pdict)
    # print(str(form_data['file']))
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
    }
    # body = {
    #     "message": "Go Serverless v3.0! Your function executed successfully!",
    #     "input": str(form_data['file']),
    # }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
