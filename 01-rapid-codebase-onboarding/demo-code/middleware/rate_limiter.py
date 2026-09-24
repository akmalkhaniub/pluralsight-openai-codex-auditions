from fastapi import Request, HTTPException, status
import time

# Simple in-memory tracker simulating Redis rate limiting
_request_history = {}

async def apply_rate_limit(request: Request):
    """
    Middleware: Ensures incoming requests from a given IP 
    do not exceed 5 registration attempts per 60 seconds.
    """
    client_ip = request.client.host if request.client else "127.0.0.1"
    current_time = time.time()
    
    attempts = _request_history.get(client_ip, [])
    # Filter attempts within the last 60 seconds
    recent_attempts = [t for t in attempts if current_time - t < 60]
    
    if len(recent_attempts) >= 5:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Registration rate limit exceeded. Please wait 60 seconds."
        )
    
    recent_attempts.append(current_time)
    _request_history[client_ip] = recent_attempts
    return True
