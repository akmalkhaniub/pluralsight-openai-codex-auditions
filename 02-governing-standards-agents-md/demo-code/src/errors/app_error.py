class AppError(Exception):
    """Base exception for all application-level errors."""
    def __init__(self, message: str, status_code: int = 500, details: dict = None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.details = details or {}

class NotificationDeliveryError(AppError):
    """Raised when an external notification webhook fails delivery."""
    def __init__(self, message: str, status_code: int = 502, details: dict = None):
        super().__init__(f"Webhook delivery failed: {message}", status_code=status_code, details=details)
