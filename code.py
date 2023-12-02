from tdeck_repl import input

while True:
    cmd = input("=>> ")
    result = None
    try:
        exec('result='+cmd)
    except:
        try:
            exec(cmd)
        except Exception as err:
            print("*ERROR* Exception:",str(err))

    if result != None and cmd.find('=') == -1:
        print(result)
