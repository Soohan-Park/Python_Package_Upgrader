"""
<Python 모든 패키지 한번에 업그레이드>

제작자 : SoohanPark
제작일 : 2019-06-16
"""

import os


def main():
    try:
        os.system("clear")
        print("<<< Start upgrade Packages >>>")

        pkgs = os.popen("pip freeze")
        fileName = "pipList.txt"
        f = open("{}".format(fileName), "w")

        for pkg in pkgs:
            temp = pkg.replace('==', '>=')
            f.write(temp)

        f.close()

        os.system("pip install -r {} --upgrade".format(fileName))

        print("\n<<< All packages are upgraded >>>\n")
        os.system("rm {}".format(fileName))
        os.system("Pause")

    except Exception as err:
        print('ERROR OCCURED >> {}'.format(err))


if __name__ == '__main__':
    main()