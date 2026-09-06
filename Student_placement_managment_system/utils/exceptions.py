class PlacementSystemError(Exception):
    """Base class for custom exceptions"""
    pass

class DatabaseError(PlacementSystemError):
    """Raised when database operations fail"""
    pass

class ValidationError(PlacementSystemError):
    """Raised when input validation fails"""
    pass
