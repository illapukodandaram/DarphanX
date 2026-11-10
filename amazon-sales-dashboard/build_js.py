import csv, json
rows = list(csv.DictReader(open("data/sales.csv")))
for r in rows:
    for k in ("Sales","Quantity","Profit","ShippingCost"): r[k] = float(r[k])
open("data/data.js","w").write("const DATA = " + json.dumps(rows) + ";")
print("data/data.js written")
