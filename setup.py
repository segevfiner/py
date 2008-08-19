"""
    setup file for 'py' package based on:

        https://codespeak.net/svn/py/trunk, revision=57462

    autogenerated by gensetup.py
"""
import os, sys
        
if 1: # set to zero if you want plain distutils
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, Extension
else:
    from distutils.core import setup, Extension
        
def main():
    setup(cmdclass=cmdclass,
        name='py',
        description='pylib and py.test: agile development and test support library',
        version='1.0.0a1', 
        url='http://pylib.org', 
        license='MIT license',
        platforms=['unix', 'linux', 'osx', 'cygwin', 'win32'], 
        author='holger krekel, Guido Wesdorp, Carl Friedrich Bolz, Armin Rigo, Maciej Fijalkowski & others',
        author_email='holger at merlinux.eu, py-dev at codespeak.net',
        ext_modules = [Extension("py.c-extension.greenlet.greenlet", 
            ["py/c-extension/greenlet/greenlet.c"]),],
        
        py_modules=['_findpy'],
        long_description='the py lib is a development support library featuring py.test, ad-hoc distributed execution, micro-threads and svn abstractions.',
        classifiers=['Development Status :: 3 - Alpha',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved :: MIT License',
                     'Operating System :: POSIX',
                     'Operating System :: Microsoft :: Windows',
                     'Operating System :: MacOS :: MacOS X',
                     'Topic :: Software Development :: Testing',
                     'Topic :: Software Development :: Libraries',
                     'Topic :: System :: Distributed Computing',
                     'Topic :: Utilities',
                     'Programming Language :: Python'],
        scripts=['py/bin/py.cleanup',
                 'py/bin/py.countloc',
                 'py/bin/py.lookup',
                 'py/bin/py.rest',
                 'py/bin/py.test',
                 'py/bin/py.which'],
        packages=['py',
                  'py.apigen',
                  'py.apigen.rest',
                  'py.apigen.rest.testing',
                  'py.apigen.source',
                  'py.apigen.source.testing',
                  'py.apigen.testing',
                  'py.apigen.tracer',
                  'py.apigen.tracer.testing',
                  'py.apigen.tracer.testing.package',
                  'py.apigen.tracer.testing.package.submodule',
                  'py.apigen.tracer.testing.package.submodule.pak',
                  'py.builtin',
                  'py.builtin.testing',
                  'py.c-extension',
                  'py.code',
                  'py.code.testing',
                  'py.compat',
                  'py.compat.testing',
                  'py.doc',
                  'py.execnet',
                  'py.execnet.script',
                  'py.execnet.testing',
                  'py.green',
                  'py.green.pipe',
                  'py.green.server',
                  'py.green.test',
                  'py.io',
                  'py.io.testing',
                  'py.log',
                  'py.log.testing',
                  'py.magic',
                  'py.magic.testing',
                  'py.misc',
                  'py.misc.cmdline',
                  'py.misc.testing',
                  'py.path',
                  'py.path.gateway',
                  'py.path.local',
                  'py.path.local.testing',
                  'py.path.svn',
                  'py.path.svn.testing',
                  'py.path.testing',
                  'py.process',
                  'py.process.testing',
                  'py.rest',
                  'py.rest.testing',
                  'py.test',
                  'py.test.dsession',
                  'py.test.dsession.testing',
                  'py.test.looponfail',
                  'py.test.looponfail.testing',
                  'py.test.report',
                  'py.test.report.testing',
                  'py.test.report.webdata',
                  'py.test.testing',
                  'py.test.testing.import_test.package',
                  'py.test.web',
                  'py.thread',
                  'py.thread.testing',
                  'py.tool',
                  'py.tool.testing',
                  'py.xmlobj',
                  'py.xmlobj.testing'],
        package_data={'py': ['LICENSE',
                             'apigen/api.js',
                             'apigen/apigen.js',
                             'apigen/source/index.cgi',
                             'apigen/style.css',
                             'apigen/todo-apigen.txt',
                             'apigen/todo.txt',
                             'bin/_findpy.py',
                             'bin/py.cleanup',
                             'bin/py.countloc',
                             'bin/py.lookup',
                             'bin/py.rest',
                             'bin/py.test',
                             'bin/py.which',
                             'c-extension/greenlet/README.txt',
                             'c-extension/greenlet/dummy_greenlet.py',
                             'c-extension/greenlet/greenlet.c',
                             'c-extension/greenlet/greenlet.h',
                             'c-extension/greenlet/setup.py',
                             'c-extension/greenlet/slp_platformselect.h',
                             'c-extension/greenlet/switch_amd64_unix.h',
                             'c-extension/greenlet/switch_mips_unix.h',
                             'c-extension/greenlet/switch_ppc_macosx.h',
                             'c-extension/greenlet/switch_ppc_unix.h',
                             'c-extension/greenlet/switch_s390_unix.h',
                             'c-extension/greenlet/switch_sparc_sun_gcc.h',
                             'c-extension/greenlet/switch_x86_msvc.h',
                             'c-extension/greenlet/switch_x86_unix.h',
                             'c-extension/greenlet/test_generator.py',
                             'c-extension/greenlet/test_generator_nested.py',
                             'c-extension/greenlet/test_greenlet.py',
                             'c-extension/greenlet/test_remote.py',
                             'c-extension/greenlet/test_throw.py',
                             'compat/LICENSE',
                             'compat/testing/test_doctest.txt',
                             'compat/testing/test_doctest2.txt',
                             'doc/TODO.txt',
                             'doc/apigen.txt',
                             'doc/apigen_refactorings.txt',
                             'doc/bin.txt',
                             'doc/code.txt',
                             'doc/coding-style.txt',
                             'doc/contact.txt',
                             'doc/download.txt',
                             'doc/example/genhtml.py',
                             'doc/example/genhtmlcss.py',
                             'doc/example/genxml.py',
                             'doc/example/pytest/failure_demo.py',
                             'doc/example/pytest/test_failures.py',
                             'doc/example/pytest/test_setup_flow_example.py',
                             'doc/execnet.txt',
                             'doc/future.txt',
                             'doc/future/code_template.txt',
                             'doc/future/planning.txt',
                             'doc/future/planning2.txt',
                             'doc/future/pylib_pypy.txt',
                             'doc/future/rsession_todo.txt',
                             'doc/greenlet.txt',
                             'doc/impl-test.txt',
                             'doc/index.txt',
                             'doc/io.txt',
                             'doc/links.txt',
                             'doc/log.txt',
                             'doc/misc.txt',
                             'doc/path.txt',
                             'doc/release-0.9.0.txt',
                             'doc/release-0.9.2.txt',
                             'doc/style.css',
                             'doc/test.txt',
                             'doc/why_py.txt',
                             'doc/xml.txt',
                             'env.cmd',
                             'execnet/NOTES',
                             'misc/testing/data/svnlookrepo.dump',
                             'path/gateway/TODO.txt',
                             'path/svn/quoting.txt',
                             'path/svn/testing/repotest.dump',
                             'rest/rest.sty.template',
                             'rest/testing/data/example.rst2pdfconfig',
                             'rest/testing/data/example1.dot',
                             'rest/testing/data/formula.txt',
                             'rest/testing/data/formula1.txt',
                             'rest/testing/data/graphviz.txt',
                             'rest/testing/data/part1.txt',
                             'rest/testing/data/part2.txt',
                             'rest/testing/data/tocdepth.rst2pdfconfig',
                             'test/report/webdata/index.html',
                             'test/report/webdata/source.js']},
        zip_safe=False,
    )

class Win32PathHandling:
    """ a helper to remove things added to system PATHs in previous installations. """
    _winreg = None
    def __init__(self):
        if sys.platform == 'win32':
            try:
                import _winreg  
            except ImportError:
                print sys.stderr, "huh could not import _winreg on windows, ignoring"
            else:
                self._winreg = _winreg

    def remove_pylib_path(self):
        reg = self._winreg.ConnectRegistry(
		  None, self._winreg.HKEY_LOCAL_MACHINE)
        key = r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment"
        path = self.get_registry_value(reg, key, "Path")
        newpath = self.prunepath(path)
        if newpath != path:
            print "PATH contains old py/bin/win32 scripts:", path
            print "pruning and setting a new PATH:", newpath
            self.set_registry_value(reg, key, "Path", newpath)
        # Propagate changes to current command prompt
        os.system("set PATH=%s" % path)
        self.try_propagate_system()

    def prunepath(self, path):
        basename = os.path.basename
        dirname = os.path.dirname
        l = []
        for p in path.split(';'):
            if basename(p) == "win32" and basename(dirname(p)) == "bin" \
               and basename(dirname(dirname(p))) == "py":
               continue # prune this path 
            l.append(p)
        return ";".join(l)

    def try_propagate_system(self):
        try:
            import win32gui, win32con
        except ImportError:
            return
        # Propagate changes throughout the system
        win32gui.SendMessageTimeout(win32con.HWND_BROADCAST,
            win32con.WM_SETTINGCHANGE, 0, "Environment",
            win32con.SMTO_ABORTIFHUNG, 5000)
    
    def get_registry_value(self, reg, key, value_name):
        k = self._winreg.OpenKey(reg, key)
        value = self._winreg.QueryValueEx(k, value_name)[0]
        self._winreg.CloseKey(k)
        return value
      
    def set_registry_value(self, reg, key, value_name, value):
        k = self._winreg.OpenKey(reg, key, 0, self._winreg.KEY_WRITE)
        value_type = self._winreg.REG_SZ
        # if we handle the Path value, then set its type to REG_EXPAND_SZ
        # so that things like %SystemRoot% get automatically expanded by the
        # command prompt
        if value_name == "Path":
            value_type = self._winreg.REG_EXPAND_SZ
        self._winreg.SetValueEx(k, value_name, 0, value_type, value)
        self._winreg.CloseKey(k)

# on windows we need to hack up the to-be-installed scripts
from distutils.command.install_scripts import install_scripts
class my_install_scripts(install_scripts):
    def run(self):
        install_scripts.run(self)
        #print self.outfiles
        for fn in self.outfiles:
            basename = os.path.basename(fn)
            if "." in basename:
                #print "tackling", fn
                newbasename = basename.replace(".", "_")
                newfn = os.path.join(os.path.dirname(fn), newbasename)
                if os.path.exists(newfn):
                    os.remove(newfn)
                os.rename(fn, newfn)
                newname = fn + ".cmd"
                if os.path.exists(newname):
                   os.remove(newname)
                f = open(newname, 'w')
                f.write("@echo off\n")
                f.write('python "%%~dp0\py_command_trampolin" %s %%*\n' % basename)
                f.close()
        w32path = Win32PathHandling()
        w32path.remove_pylib_path()
                
if sys.platform == "win32":
    cmdclass = {'install_scripts': my_install_scripts}
else:
    cmdclass = {}
        
if __name__ == '__main__':
    main()
        