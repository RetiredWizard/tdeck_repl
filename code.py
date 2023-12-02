from tdeck_repl import input

while True:
    __cmd = input("=>> ")
    __result = None
    try:
        exec('__result='+__cmd)
    except:
        try:
            exec(__cmd)
        except Exception as err:
            print("*ERROR* Exception:",str(err))

    if __result != None and __cmd.find('=') == -1:
        print(__result)
