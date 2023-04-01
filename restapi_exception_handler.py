class RESTAPIException(Exception):
  def __init__(self, error: str, status_code: int | None):
    self.error = error
    self.status_code = status_code if status_code is not None else 401
