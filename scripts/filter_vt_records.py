import ijson, csv
with open(r"output.csv", "w") as o:
    dataWriter = csv.writer(o,delimiter=',', quoting=csv.QUOTE_MINIMAL)
    dataWriter.writerow(['NAME','URL'])
    with open("../../index_2011.json") as f:
        parser = ijson.parse(f)
        obj = {}
        for prefix, event, value in parser:
            if prefix == 'Filings2011.item.URL' and len(value)>0:
                obj = {'url':value}
            if prefix == 'Filings2011.item.OrganizationName':
                if "VERMONT" in value or "VT " in value or " VT " in value:
                    obj['name'] = value
                    #print(obj)
                    dataWriter.writerow([obj['name'].strip(),obj['url'].replace("\\n","")])
