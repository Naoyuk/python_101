# -*- coding: utf-8 -*-
import sys

def py2_or_py3():
    """
    実行中のPyhotnが2系か3系かを判定する

    この関数はPython 1.xでの実行は想定しない
    """
    major = sys.version_info.major
    if major < 3:
        print('Your python version is 2.x.')
    else:
        print('お使いのPythonのバージョンは3系です。')

py2_or_py3()
