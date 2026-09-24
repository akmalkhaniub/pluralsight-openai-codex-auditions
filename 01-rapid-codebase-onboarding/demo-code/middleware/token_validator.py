from fastapi import Request, HTTPException, status

async def verify_client_identity(request: Request) -> dict:
    """
    Middleware: Inspects request headers for valid Client App Key.
    Extracts origin metadata for audit logging.
    """
    client_app_id = request.headers.get("X-Client-App-Id")
    if not client_app_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing required X-Client-App-Id header."
        )
    
    return {
        "client_app_id": client_app_id,
        "ip": request.client.host if request.client else "127.0.0.1",
        "user_agent": request.headers.get("User-Agent", "Unknown")
    }
