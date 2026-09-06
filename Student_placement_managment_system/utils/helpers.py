def format_output(data):
    """Helper function to format query results nicely"""
    return [dict(zip(["id", "name", "email"], row)) for row in data]
