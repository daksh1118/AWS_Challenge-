from typing import Any, Dict, Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

# Security scheme to extract Bearer token from HTTP Authorization header
security_scheme = HTTPBearer(auto_error=False)


async def get_current_user(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security_scheme),
) -> Dict[str, Any]:
    """
    FastAPI dependency for Firebase JWT authentication.
    Currently mocks token verification and returns a dummy user.
    """
    # NOTE: Firebase Admin SDK authentication verification will be integrated here:
    # try:
    #     token = credentials.credentials
    #     decoded_token = auth.verify_id_token(token)
    #     return decoded_token
    # except Exception:
    #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    return {"uid": "123", "role": "teacher"}
