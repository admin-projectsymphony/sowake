
def handle_command(command):
    import os
    try:
        return os.popen(command).read()
    except Exception as e:
        return str(e)
