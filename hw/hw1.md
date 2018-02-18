## EP476: Introduction to Scientific Computing for Engineering Physics

# Homework #1

**Due: Tuesday, February, 6, 1:00 PM**

Most of these questions are based on a common directory structure found at
`~wilsonp/ep476-hw1`.

Prepare a standard text file with the answers to these questions, as
appropriate.  Send the text file to me by email.

1. What is the command that will tell you the full path of this directory?
   What is that full path?

1. Describe the contents of this subdirectory in a way that shows the
   hierarchy and indicates which are files, which are directories and which
   are symbolic links.

1. Write a script with the commands that would accomplish the following in
   precisely this order:

   * make a new copy of the entire directory structure from its original
     location (`~wilsonp/ep476-hw1`) to the current directory, and in
     that new copy:
   * create an environment variable called `NUCLEAR_DIR` that refers to the
     absolute path of the top-level directory of this copy, i.e. the
     directory that was created by making the copy
   * Create an alias that will show you a long listing of the `fission`
     directory that you copied above.
   * change to the `fusion` directory
   * rename the `tokamak.rst` file to be `tokamak.txt`
   * make two directories: `magnetic` and `inertial`
   * move the `tokamak.txt` and `stellarator.txt` files to the `magnetic` directory
   * move the `iec.txt` and `laser.txt` files to the `inertial` directory
   * list the contents of the `thermal` subdirectory of the `fission` directory
   * create a symbolic link in your current directory (`fusion`) to the
     `hybrid.txt` file that is in the `fission` directory
   * Change the permissions of the directory referenced in `NUCLEAR_DIR`, and
     all of the directories and files below it, so that others can view it.
     You may also have to change the permissions of some directories above it
     to ensure that it is accessible. It is advisable to give the minimum
     possible permissions to the directories above this one.  I will check
     these permissions by accessing the directory indicated by `NUCLEAR_DIR`
     above.
   * change your prompt to remove only the username and hostname portion

   Attach your script as a separate file to your email.

1. Repeat question #2 with the new directory structure.

1. In what ways does tab completion improve both accuracy and efficiency when
   working with the command-line?

1. What did you learn about the command-line that might affect the way that
   you work?
