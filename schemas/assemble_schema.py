
from avro.datafile import DataFileReader
from avro.io import DatumReader
import json
import avro

header = '''{
  "type": "record",
  "name": "topLevelRecord",
  "fields": ['''

trailer = '''  ]
}'''

conf_file = "Fink_0.2.conf"
with open(conf_file, 'r') as f:
    all_names = [line.strip() for line in f.readlines()]


print(header)
for name in all_names:
    if name.startswith("telescope"):
        filename = name.split(" ")[1]
        file = open(filename, 'rb')
        datum_reader = DatumReader()
        file_reader = DataFileReader(file, datum_reader)
        meta = file_reader.meta['avro.schema']
        schema = json.loads(meta)
        ztf = json.dumps(schema["fields"])

        print(ztf[1:-1], ',')
    else:
        with open("source/{}.avsc".format(name)) as f:
            for line in f.readlines():
                print(line.strip('\n'))
print(trailer)
