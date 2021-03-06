**This is obsolete. Since when this was written, Python grew the subprocess
module. Use that instead. This repo exists just for my archival enjoyment.**

process.py is a (rather large) Python module to make process control easier and
more consistent on Windows, Linux, and Mac OS X (and other Un*ces). The current
mechanisms (os.popen*, os.system, os.exec*, os.spawn*) all have limitations.

A quick list of some reasons to use process.py:

1. You don't have to handle quoting the arguments of your command line. You can
   pass in a command string or an argv.
2. You can specify the current working directory (cwd) and the environment (env)
   for the started process.
3. On Windows you can spawn a process without a console window opening.
4. You can wait for process termination or kill the running process without
   having to worry about weird platform issues. (Killing on Windows should first
   give the process a chance to shutdown cleanly. Killing on Linux will not work
   from a different thread than the process that created it.)
5. The ProcessProxy class allows you to interact in a pseudo-event-based way
   with the spawned process. I.e., you can pass in file-like object for any of
   stdin, stdout, or stderr to handle interaction with the process. 

# Project Status

Since I originally developed process.py, Python has grown (in version 2.4) the
new subprocess module. I haven't done a feature comparison of process.py and
subprocess but the latter is definitely more capable than the older Python
process control mechanisms. If you are considering using process.py you should
definitely checkout subprocess as well.

It has been over 3 years since this module has been maintained. In its current
state it was used heavily in the commercial Komodo IDE project. However, since
2007 a significant overhaul of process.py used in Komodo was undertaken.
Komodo's process module is now a (rather heavily) tweaked wrapper around
Python's core subprocess module. See the process modules in the open source
Komodo Edit source tree here. The process modules are the same as those used in
Komodo IDE.

Despite this module not having been maintained, there are still somethings of
value in here. Esp. regarding the guts of some process control from Python on
Windows. Gross stuff. Mostly this project is here for reference. Python process
control links
