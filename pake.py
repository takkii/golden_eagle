import gc
import sys

try:
    # It doesn't support python4 yet.
    py_mj = sys.version_info[0]
    py_mi = sys.version_info[1]

    # 3.5 and higher, 4.x or less,python version is required.
    if (py_mj == 3 and py_mi > 4) or (py_mj < 4):
        print('{}'.format('-----------------------------------------------------------------'))

        # Run, unit/facecompare.py
        with open('./unit/facecompare.py') as fa:
            cmd = fa.read()
            exec(cmd)

        print('\n')
        print('If no exceptions are raised, the process succeeded.')
        print('{}'.format('-----------------------------------------------------------------'))

        # Run, unit/timestamp.py
        with open('./unit/timestamp.py') as ti:
            cmd = ti.read()
            exec(cmd)

        print('{}'.format('-----------------------------------------------------------------'))

        # Run, unit/xunit.py
        with open('./unit/xunit.py') as xut:
            xcmd = xut.read()
            exec(xcmd)

        print('{}'.format('-----------------------------------------------------------------'))

        # Run, unit/unit.py
        with open('./unit/unit.py') as ut:
            cmd = ut.read()
            exec(cmd)

    # Python_VERSION: 3.5 or higher and 4.x or less.
    else:
        raise ValueError("VERSION: 3.5 or higher and 4.x or less")

# Custom Exception.
except ValueError as e:
    print(e)
    raise RuntimeError from None

finally:
    # GC collection.
    gc.collect()
