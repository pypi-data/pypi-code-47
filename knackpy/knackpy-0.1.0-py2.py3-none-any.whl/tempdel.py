import pdb
from pprint import pprint as print

from knackpy import Knack

app_id = '5815f29f7f7252cc2ca91c4f'
api_key = '01b0fadd-b352-4126-9da2-9b3534cb7019'
obj = "object_185"

kn = Knack(
  obj=obj,
  app_id=app_id,
  api_key=api_key,
  page_limit=1,
  rows_per_page=9999999,
  tzinfo="US/Eastern"
)

pdb.set_trace()
kn.download(
    destination="_downloads",
    overwrite=True,
)


res = knackpy.record(
  payload,
  obj_key='object_185',
  app_id=app_id,
  api_key=api_key,
  method='delete'
)
pdb.set_trace()