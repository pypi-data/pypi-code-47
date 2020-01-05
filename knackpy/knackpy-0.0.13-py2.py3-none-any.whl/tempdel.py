import pdb
from pprint import pprint as print

from knackpy import Knack

app_id = '5815f29f7f7252cc2ca91c4f'
api_key = '01b0fadd-b352-4126-9da2-9b3534cb7019'
obj = "object_12"

kn = Knack(
  obj=obj,
  app_id=app_id,
  api_key=api_key,
  rows_per_page=5,
  page_limit=1
)

kn.to_csv("try.csv")
pdb.set_trace()