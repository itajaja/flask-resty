import flask
import traceback

# -----------------------------------------------------------------------------


class ApiError(Exception):
    def __init__(self, status_code, *errors):
        self.status_code = status_code
        self.body = {
            'errors': errors
        }

        if flask.current_app.debug:
            self.body['debug'] = traceback.format_exc()

    def update(self, additional):
        for error in self.body['errors']:
            error.update(additional)

        # Allow e.g. `raise e.update(additional)`.
        return self
