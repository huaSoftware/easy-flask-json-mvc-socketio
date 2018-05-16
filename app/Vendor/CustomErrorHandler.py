import cerberus


class CustomErrorHandlers(cerberus.errors.BasicErrorHandler):
    def __init__(self, tree=None, custom_messages=None):
        super(CustomErrorHandlers, self).__init__(tree)
        self.custom_messages = custom_messages or {}

    def _format_message(self, field, error):
        tmp = self.custom_messages
        for x in error.schema_path:
            try:
                tmp = tmp[x]
            except KeyError:
                return super(CustomErrorHandlers, self)._format_message(
                    field, error)
        if isinstance(tmp, dict):
            return super(CustomErrorHandlers, self)._format_message(field, error)
        else:
            return tmp
