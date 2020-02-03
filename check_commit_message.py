#!/bin/sh
import re
import sys

commitMessageFile = open(sys.argv[1])
commitMessage = commitMessageFile.read().strip()

if len(commitMessage) < 10:
    print("Commit message is less than the required 15 characters.")
    sys.exit(1)

if len(commitMessage.split(' ')) < 2:
    print("Commit message is less than 2 words.")
    sys.exit(1)

if bool(re.search('[а-яА-Я]', commitMessage)):
    print("Commit message has russian symbols.")
    sys.exit(1)

print("Commit message is validated")
sys.exit(0)
