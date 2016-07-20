from wsgiref.simple_server import make_server
from cgi import parse_qs

from app.battle_field import Battlefield


def battle(num_armies):
    """
    Function that starts the war.

    :param int num_armies: the number of armies on the battlefield.
    :return:The return value is used to show log on the screen.
    :rtype: str
    """
    num_armies = int(num_armies)
    b = Battlefield(num_armies)
    return b.start()


def open_f(file, mode='r', parameter=''):
    """
    Open file function.

    :param str file: path to file or file name
    :param str mode:
        'r'   Open text file for reading.  The stream is positioned at the
         beginning of the file.

        'r+'  Open for reading and writing.  The stream is positioned at the
         beginning of the file.

        `w'   Truncate file to zero length or create text file for writing.
         The stream is positioned at the beginning of the file.

        'w+'  Open for reading and writing.  The file is created if it does not
         exist, otherwise it is truncated.  The stream is positioned at
         the beginning of the file.

        'a'   Open for writing.  The file is created if it does not exist.  The
         stream is positioned at the end of the file.  Subsequent writes
         to the file will always end up at the then current end of file,
         irrespective of any intervening fseek(3) or similar.

        'a+'  Open for reading and writing.  The file is created if it does not
         exist.  The stream is positioned at the end of the file.  Subse-
         quent writes to the file will always end up at the then current
         end of file, irrespective of any intervening fseek(3) or similar.

    :param str parameter: used if it is needed to change the text in file.
    :return: file's content.
    :rtype: str.
    """
    with open(file, mode) as f:
        return f.read().format(parameter).encode('UTF-8')


def app(env, resp_start):
    """
    WSGI application.

    :param env: dictionary of environment variables.
    :param resp_start: executable object of response start
    :return: array of strings
    """
    route = {'battle': battle}

    resp_start('200 OK', [('content-type','text/html')])

    path = env.get('PATH_INFO')[1:]
    parts = path.split('/')
    for part in parts:
        if part == 'favicon.ico':
            parts.remove(part)
    if len(parts)>0 and parts[0]!='':
        content_length = int(env.get('CONTENT_LENGTH'))
        post_data = env['wsgi.input'].read(content_length)
        post_data = parse_qs(post_data)
        fn = route.get(parts[0])
        if post_data[b'num_armies'][0].decode('UTF-8') > '0':
            log = fn(post_data[b'num_armies'][0].decode('UTF-8'))
            html = open_f('html/battle.html', 'r', log)
        else:
            html = open_f('html/index.html', 'r')
    else:
        html = open_f('html/index.html','r')

    return [html]


if __name__ == '__main__':
    serv = make_server('', 8080, app)
    serv.serve_forever()
