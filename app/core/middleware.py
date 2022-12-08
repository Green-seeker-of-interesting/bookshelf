import os


def clearing_temporary_files_middleware(get_response):
    def middleware(request):
        response = get_response(request)
        target = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        if response.headers['Content-Type'] == target:
            for file in os.listdir('temporary_files'):
                os.remove(os.path.join('temporary_files', file))
        return response
    return middleware
