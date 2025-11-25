from fastapi import FastAPI

from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(router_v1)


# if __name__ == "__main__":
#     import uvicorn
#
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, workers=1)

from core.db.models import Operator, Source, OperatorsToSources, Appeal
from sqlalchemy import select, func


# print(select(Operator)
#         .join(OperatorsToSources)
#         .join(Source)
#         .where(Source.id == 1, )
#       )

appeal_count = (
    select(func.count(Appeal.id))
    .where(Appeal.operator_id == Operator.id)
    .scalar_subquery()
)

stmt = (
    select(Operator)
    .join(OperatorsToSources)
    .join(Source)
    .where(
        Source.id == 1,
        Operator.is_active == True,
        Operator.req_limit < appeal_count
    )
)
