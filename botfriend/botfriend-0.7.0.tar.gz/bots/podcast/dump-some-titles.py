from pdb import set_trace
import json
from olipy.ia import Audio
out = "details.201705-06.ndjson"
out = open(out, "w")
a = 0
for f in "201705", "201706":
    i = "data/podcasts.%s.ndjson" % f
    for j in open(i):
        raw = json.loads(j)
        item = Audio(raw)
        json.dump(item.item.item_metadata, out)
        out.write("\n")
        a += 1
        if not a % 100:
            print(item.item.item_metadata)
