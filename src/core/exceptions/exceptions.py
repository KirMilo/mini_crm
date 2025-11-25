from fastapi import HTTPException, status


class AllOperatorsAreBusy(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="All operators are busy, try later...",
        )


class SourceNotFound(HTTPException):
    def __init__(self, source_id: int):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Source {source_id} not found",
        )


class OperatorNotFound(HTTPException):
    def __init__(self, operator_id: int):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Operator {operator_id} not found",
        )


class LeadNotFound(HTTPException):
    def __init__(self, lead_id: int):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Lead {lead_id} not found",
        )