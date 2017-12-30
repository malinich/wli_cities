import traceback

import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    def write_error(self, status_code, **kwargs):
        self.set_header("Content-Type", 'application/json')

        if self.settings.get("serve_traceback") and "exc_info" in kwargs:
            # in debug mode, try to send a traceback
            self.set_header('Content-Type', 'text/plain')
            for line in traceback.format_exception(*kwargs["exc_info"]):
                self.write(line)
            self.finish()
        else:
            self.finish({
                "code": status_code,
                "message": self._reason
            })

    @property
    def payload(self) -> dict:
        return tornado.escape.json_decode(self.request.body)

    def get_current_user(self):
        return self.payload['user']

    def dumps(self, obj, many=False):
        sh = self.schema(many=many, strict=True)
        res = sh.dumps(obj, True)
        return res.data
