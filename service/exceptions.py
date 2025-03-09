from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError


def handle_db_exceptions(error: Exception):
    if isinstance(error, IntegrityError):
        error_message = str(error.orig)
        if "foreign key constraint" in error_message:
            raise HTTPException(
                status_code=400,
                detail="Invalid foreign key value. Please check the referenced table."
            )
        else:
            raise HTTPException(
                status_code=400,
                detail="Database integrity error. Please check your input data."
            )
    elif isinstance(error, ValueError):
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )
    elif isinstance(error, HTTPException):
        raise error
    else:
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred."
        )