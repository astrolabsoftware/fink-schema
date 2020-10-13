
from avro.datafile import DataFileReader
from avro.io import DatumReader
import json
import avro


candidate = dict()

def printfields(fields, fname, level = 0):
    global candidate

    prefix = "  "*level
    for field in fields:
        # print('--------------------------')
        name = field.name
        ftype = field.type
        if fname == "candidate":
            candidate[name] = ftype

        cand = ""
        if fname == "prv_candidates":
            if name not in candidate:
                cand = "bad"
            else:
                cand = "(condidate)"

        if isinstance(ftype, avro.schema.UnionSchema):
            ftype = ftype.schemas[0]
        if isinstance(ftype, avro.schema.ArraySchema):
            ftype = ftype.items
        ztf = ""
        if fname == "" and name in ztf_fields: ztf = "ztf"
        if name == "prv_candidates":
            pass
        if isinstance(ftype, avro.schema.RecordSchema):
            print(prefix, name, "=>", ztf)
            printfields(ftype.fields, name, level = level + 1)
        else:
            print(prefix, name, "=> ", ftype, ztf)


filename = "template_schema_ZTF_3p3.avro"
file = open(filename, 'rb')
datum_reader = DatumReader()
file_reader = DataFileReader(file, datum_reader)

# print(file_reader.meta)
# print(file_reader.schema)


print('==========', filename)

ztf_fields = []
meta = file_reader.meta['avro.schema']
schema = json.loads(meta)
print("ZTF schema:")
print("{")
for k in schema:
    if k == "fields": continue
    print('  "{}": "{}",'.format(k, schema[k]))

print('  "fields": [')
fields = schema["fields"]
for field in fields:
    # print('--------------------------')
    name = field['name']
    ftype = field['type']
    print('    {}"name": "{}", "type": ["{}", "null"]{},'.format(r'{', name, ftype, r'}'))
    if name == "candidate":
        candidate_fields = sorted([f['name'] for f in ftype['fields']])
    ztf_fields.append(name)
print('  ]')
print("}")


print(json.dumps(schema["fields"]))

"""
filename = "distribution_schema_0p2.avsc"
print('==========', filename)

file = open(filename, 'rb')

schema = avro.schema.parse(open(filename, "rb").read())

printfields(schema.fields, "")
"""

print("-".join(candidate_fields))
print("-".join(sorted(candidate.keys())))

