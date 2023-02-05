import multiprocessing
import sys, os
import time


def run_api():
    sys.path.pop(0)
    sys.path.pop(1)
    sys.path.insert(0, os.getcwd() + '/enginetribe')
    print(sys.path)
    os.environ['CONFIG_PATH'] = os.getcwd() + '/enginetribe/config.yml'
    import enginetribe
    enginetribe.run()


def run_bot_discord():
    sys.path.pop(0)
    sys.path.pop(1)
    sys.path.insert(0, os.getcwd() + '/enginebot_discord')
    print(sys.path)
    os.environ['CONFIG_PATH'] = os.getcwd() + '/enginebot_discord/config.yml'
    os.environ['LOCALES_PATH'] = os.getcwd() + '/enginebot_discord/locales'
    import enginebot_discord
    enginebot_discord.run()


if __name__ == '__main__':
    p_api = multiprocessing.Process(target=run_api)
    p_api.start()
    time.sleep(0.3)
    p_bot_discord = multiprocessing.Process(target=run_bot_discord)
    p_bot_discord.start()
